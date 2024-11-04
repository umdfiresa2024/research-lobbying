import pandas as pd
import numpy as np

# Load the datasets
naics_ghgs = pd.read_csv('../3. join naics with ghgs/naics_ghgs.csv')
meng_with_ticker_df = pd.read_csv('meng_with_tickers.csv')


# Merge the dataframes on the Ticker columns
merged_df = pd.merge(naics_ghgs, meng_with_ticker_df[['ticker.ticker', 'lobby', 'US_revenue_share', 'carbon_intensity']],
                     how='left', left_on='Ticker', right_on='ticker.ticker')

print(f"# overlapping tickers: {merged_df['ticker.ticker'].count()}")

# Fill NaN values in the lobby column with 0
merged_df = merged_df.fillna(np.nan)
merged_df['lobby'] = merged_df['lobby'].fillna(0)

merged_df['lobby_amount'] = merged_df['lobby']

merged_df = merged_df.drop(columns=['ticker.ticker', 'lobby'])

print(merged_df.describe())

merged_df.to_csv('merged_meng.csv', index=False)
