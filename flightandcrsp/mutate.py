import pandas as pd

crsp = pd.read_csv('../cleaned-crsp.csv')
flight = pd.read_csv('../cleaned-flight.csv')
merged = pd.read_csv('merged_flight_data.csv')
compared = pd.read_csv('compared.csv')


tickers = {key: value for key,
           value in zip(compared['Company'], compared['Ticker'])}

flight['Ticker'] = flight['Company'].apply(
    lambda c: tick if (tick := tickers.get(c)) is not None else "None")

# crsp.to_csv("../cleaned-crsp.csv", index=False)
flight.to_csv("../cleaned-flight.csv", index=False)
# compared.to_csv("compared.csv", index=False)
