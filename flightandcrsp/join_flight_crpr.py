import pandas as pd
import numpy as np


flight_crsp = pd.read_csv('../finaldatasets/ghg_flight_crispr.csv')
cleaned_crsp = pd.read_csv('../cleaned-crsp.csv')
original_crsp = pd.read_csv('../200908-201012CRSP.csv')


def naics(row):
    ticker = row['Ticker']
    naics_vals = original_crsp[ticker]
    if len(naics_vals) == 0:
        row['naics']
    return naics_vals['NAICS'][0]


# Perform the join based on the 'ticker' column. Using outer join to include tickers from both CSVs
merged_df = pd.concat([flight_crsp, cleaned_crsp], ignore_index=True)

# Drop duplicates based on the 'ticker' column, keeping the first occurrence
final_df = merged_df.drop_duplicates(subset='Ticker', keep='first')
final_df['Total GHG'].fillna(0, inplace=True)
final_df.apply(naics, axis=1)

# Save the result to a new CSV file
final_df.to_csv('../finaldatasets/full_flight_crspr.csv', index=False)

print("Merge completed and saved to merged_output.csv")
