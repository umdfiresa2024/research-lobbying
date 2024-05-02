import pandas as pd
import yfinance as yf
import logging
logger = logging.getLogger('yfinance')
logger.disabled = True
logger.propagate = False


def load_tickers_from_file(filename):
    with open(filename, "r") as f:
        tickers = [line.strip() for line in f]
    return tickers


# Example usage
tickers = load_tickers_from_file("tickers.txt")
df = pd.read_csv("../main_data.csv")
df.insert(1, "Ticker", tickers, True)
df.insert(2, "Price_Before", [None for _ in range(len(df))], True)
df.insert(3, "Price_After", [None for _ in range(len(df))], True)

# Fetch and store stock prices
failed_tickers = []
for idx, row in df.iterrows():
    ticker_data = yf.Ticker(row["Ticker"])
    price = ticker_data.history(
        period="1y", start="2009-06-01", end="2010-06-01")["Close"]
    if len(price) >= 2 and price.iloc[0] > 0:
        df.at[idx, "Price_Before"] = round(price.iloc[0], 2)
        df.at[idx, "Price_After"] = round(price.iloc[-1], 2)
        print(row["Ticker"], df.at[idx, "Price_Before"],
              df.at[idx, "Price_After"])
    else:
        print(row["Ticker"], "failed")
        failed_tickers.append(row["Ticker"])

print("failed tickers:\n", failed_tickers)
# Save the updated DataFrame to a new CSV file
df.dropna(subset=["Price_Before"], inplace=True)
df.to_csv("data_with_price.csv", index=False)
