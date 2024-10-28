import pandas as pd
import numpy as np

# Load the CSV files
company2ticker = pd.read_csv('company2ticker.csv')
cleaned_flight = pd.read_csv(
    '../1. generate datasets/flight and crsp/cleaned-flight.csv')


cleaned_flight['Company'] = cleaned_flight['Company'].apply(
    lambda s: str(s).upper())

cleaned_flight = cleaned_flight.merge(company2ticker, on='Company')

# Clean up any double quotes in Ticker
cleaned_flight["Ticker"] = cleaned_flight["Ticker"].apply(
    lambda s: s.replace('"', ""))

# Calculate grouped sums
grouped_sums = cleaned_flight.groupby("Ticker")['Total GHG'].sum()

# Get the first occurrence of each ticker
first_occurrences = cleaned_flight.groupby("Ticker", as_index=False).first()

# Merge the grouped sums into the first occurrences DataFrame
first_occurrences = first_occurrences.merge(
    grouped_sums, on='Ticker', suffixes=('', '_Sum'))

# Replace the original 'Total GHG' with the summed value
first_occurrences['Total GHG'] = first_occurrences['Total GHG_Sum']

# Drop the now redundant '_Sum' column
first_occurrences.drop(columns=['Total GHG_Sum'], inplace=True)

# Save the result
first_occurrences.to_csv('SummedGHGs.csv', index=False)

print(first_occurrences)
