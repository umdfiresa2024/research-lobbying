import pandas as pd

crsp = pd.read_csv('../cleaned-crsp.csv')
flight = pd.read_csv('../cleaned-flight.csv')


crsp['Company'] = crsp['Company'].str.lower()
flight['Company'] = flight['Company'].str.lower()

# Create a set of company names from flight for faster checking
set_crsp = set(crsp['Company'])
set_flight = set(flight['Company'])

print(len(set_flight.intersection(set_crsp)))
