import pandas as pd
import numpy as np

# Load the CSV files
flight_tickers = pd.read_csv('flight_tickers.csv')
cleaned_flight = pd.read_csv(
    '../1. generate datasets/flight and crsp/cleaned-flight.csv')


# Merge the ticker column from flight_tickers to the right of cleaned_flight.
# Keep only existing tickers
flight_tickers["Ticker"] = flight_tickers["Ticker"].replace("None", np.nan)

cleaned_flight = cleaned_flight.merge(flight_tickers, on='Company')

cleaned_flight['Ticker'] = cleaned_flight['Ticker'].fillna('N/A')

# Drop rows where Ticker is 'N/A'
cleaned_flight = cleaned_flight[cleaned_flight['Ticker'] != 'N/A']

cleaned_flight["Ticker"] = cleaned_flight["Ticker"].apply(
    lambda s: s.replace('"', ""))

cleaned_flight = cleaned_flight.groupby("Ticker")['Total GHG'].sum()

# Save the merged data to a new CSV file
cleaned_flight.to_csv('cleaned_flight_no_NA.csv', index=False)
