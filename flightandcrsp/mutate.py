import pandas as pd

crsp = pd.read_csv('../cleaned-crsp.csv')
flight = pd.read_csv('../cleaned-flight.csv')
merged = pd.read_csv('merged_flight_data.csv')

print(len(merged))
print(len(merged.dropna()))
print(len(merged.dropna()) / len(merged))

# crsp.to_csv("../cleaned-crsp.csv", index=False)
# flight.to_csv("../cleaned-flight.csv", index=False)
