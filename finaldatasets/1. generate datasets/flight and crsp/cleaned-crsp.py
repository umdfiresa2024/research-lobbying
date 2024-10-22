import pandas as pd

# Load the CRSP data
crsp = pd.read_csv('../../../200908-201012CRSP.csv')

# Filter companies whose ticker appears exactly 18 times
ticker_counts = crsp['TICKER'].value_counts()
tickers_18_times = ticker_counts[ticker_counts == 18].index

# Filter the crsp dataframe for these tickers
filtered_crsp = crsp[crsp['TICKER'].isin(tickers_18_times)]

# Sort the dataframe by ticker and date to ensure most recent entries are at the bottom for each ticker
filtered_crsp = filtered_crsp.sort_values(
    by=['TICKER', 'date'], ascending=[True, True])

# Get the most recent entry for each ticker
most_recent_companies = filtered_crsp.groupby('TICKER').last().reset_index()

# Select only the ticker and most recent company name
result_df = most_recent_companies[['TICKER', 'COMNAM']]

# Display the result
print(result_df)

result_df.to_csv("cleaned-crsp.csv", index=False)
