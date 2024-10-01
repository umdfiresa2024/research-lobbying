import pandas as pd
import yfinance as yf
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed

# Disable logging from yfinance to suppress warnings/errors in output
logger = logging.getLogger('yfinance')
logger.disabled = True
logger.propagate = False


def load_tickers_from_file(filename):
    """Load a list of tickers from a text file."""
    with open(filename, "r") as f:
        tickers = [line.strip() for line in f]
    return tickers


def check_ticker(ticker):
    """
    Check if the ticker had a stock price on a specific date.
    Returns (ticker, company_name) if valid, otherwise None.
    """
    ticker_data = yf.Ticker(ticker)
    try:
        # Fetch stock price data for the ticker on Dec 1, 2010
        price_data = ticker_data.history(
            interval="1d", start="2010-12-01", end="2010-12-02")["Close"]

        if not price_data.empty and price_data.iloc[0] > 0:
            # Get the ticker and company name
            print(f"{ticker} - Valid")
            company_name = ticker_data.info.get(
                'longName', 'N/A')  # Get company name, if available
            return ticker, company_name
        else:
            print(f"{ticker} - Failed")
            return None
    except Exception as e:
        print(f"Failed to fetch data for {ticker}: {str(e)}")
        return None


def save_progress(data_dict, file_name):
    """
    Save progress of valid tickers and company names to CSV.
    """
    df = pd.DataFrame(data_dict)
    df.to_csv(file_name, index=False)
    print(f"Progress saved with {len(df)} valid tickers.")


# Example usage
tickers = load_tickers_from_file("tickers.txt")

# Load any existing data from previous runs
try:
    existing_df = pd.read_csv("valid_tickers_with_names.csv")
    existing_tickers = set(existing_df['Ticker'].tolist())
    print(f"Loaded {len(existing_df)} tickers from previous runs.")
except FileNotFoundError:
    # If the file does not exist, initialize an empty set for existing tickers
    existing_df = pd.DataFrame(columns=["Ticker", "Company_Name"])
    existing_tickers = set()

# Compute the difference between all tickers and the tickers already processed
tickers_to_process = set(tickers) - existing_tickers
print(f"{len(tickers_to_process)} tickers to process out of {len(tickers)} total tickers.")

# Initialize the dictionary with the existing data
valid_tickers_dict = {
    'Ticker': existing_df['Ticker'].tolist(),
    'Company_Name': existing_df['Company_Name'].tolist()
}

# Initialize counters
save_interval = 50  # Change to 100 if you want
counter = 0
valid_counter = len(valid_tickers_dict['Ticker'])  # Start from existing data
total_tickers = len(tickers_to_process)

# Use ThreadPoolExecutor for parallel API calls
with ThreadPoolExecutor(max_workers=10) as executor:
    # Submit all the tasks to the executor
    futures = {executor.submit(check_ticker, ticker)
                               : ticker for ticker in tickers_to_process}

    # Process the results as they complete
    for future in as_completed(futures):
        result = future.result()
        counter += 1  # Increment total tickers processed

        if result is not None:
            ticker, company_name = result
            valid_tickers_dict['Ticker'].append(ticker)
            valid_tickers_dict['Company_Name'].append(company_name)
            valid_counter += 1  # Increment valid tickers count

            # Print valid/total status
            print(
                f"Processed {valid_counter}/{counter} valid tickers out of {total_tickers} new tickers to process")

            # Save every 'save_interval' valid tickers
            if valid_counter % save_interval == 0:
                save_progress(valid_tickers_dict,
                              "valid_tickers_with_names.csv")

# Final save after all futures are completed
save_progress(valid_tickers_dict, "valid_tickers_with_names.csv")

print("Process complete. Data saved to valid_tickers_with_names.csv")
