import pandas as pd

crsp = pd.read_csv('../200908-201012CRSP.csv')
flight = pd.read_csv('../flight_2010.csv')
final = pd.read_csv('final.csv')


tick2naics = {k: v for k, v in zip(crsp['TICKER'], crsp['NAICS'])}
final['naics'] = [tick2naics.get(k) for k in final['Ticker']]
print(final)

# crsp.to_csv("../cleaned-crsp.csv", index=False)
# flight.to_csv("../cleaned-flight.csv", index=False)
final.to_csv("final.csv", index=True, index_label='Index')
