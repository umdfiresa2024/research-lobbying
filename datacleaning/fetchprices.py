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
            company_name = ticker_data.info.get(
                'longName', 'N/A')  # Get company name, if available
            return ticker, company_name
        else:
            return None
    except Exception as e:
        print(f"Failed to fetch data for {ticker}: {str(e)}")
        return None


# Example usage
tickers = load_tickers_from_file("tickers.txt")

# Initialize a dictionary to store tickers and company names
valid_tickers_dict = {'firm_name': [], 'ticker': []}

# Initialize the counters
save_interval = 50  # Change to 100 if you want
counter = 0
valid_counter = 0
total_tickers = len(tickers)

# Function to save the DataFrame periodically


def save_progress(data_dict, file_name):
    df = pd.DataFrame(data_dict)
    df.to_csv(file_name, index=False)
    print(f"Progress saved with {len(df)} valid tickers.")


# Use ThreadPoolExecutor for parallel API calls
with ThreadPoolExecutor(max_workers=10) as executor:
    # Submit all the tasks to the executor
    futures = {executor.submit(check_ticker, ticker): ticker for ticker in tickers}

    # Process the results as they complete
    for future in as_completed(futures):
        result = future.result()
        counter += 1  # Increment total tickers processed

        if result is not None:
            ticker, company_name = result
            valid_tickers_dict['ticker'].append(ticker)
            valid_tickers_dict['firm_name'].append(company_name)
            valid_counter += 1  # Increment valid tickers count

            # Print valid/total status
            print(
                f"Processed {valid_counter}/{counter} valid tickers out of {total_tickers} total")

            # Save every 'save_interval' valid tickers
            if valid_counter % save_interval == 0:
                save_progress(valid_tickers_dict,
                              "valid_tickers_with_names.csv")

# Final save after all futures are completed
save_progress(valid_tickers_dict, "valid_tickers_with_names.csv")

print("Process complete. Data saved to valid_tickers_with_names.csv")
