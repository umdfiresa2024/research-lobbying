import pandas as pd
import numpy as np

crsp = pd.read_csv('../200908-201012CRSP.csv')
flight = pd.read_csv('../flight_2010.csv')
final = pd.read_csv('final.csv')
test = pd.read_csv('../meng_tickers.csv')
test2 = pd.read_csv('../meng_tickers2.csv')

for i in range(len(test)):
    if test.iloc[i]["Company"] != test2.iloc[i]["Company"]:
        print("Different name")
    elif test.iloc[i]["Ticker"] != test2.iloc[i]["Ticker"]:
        print(
            f"{test.iloc[i]['Company']:<20} {test.iloc[i]['Ticker']:<10} {test2.iloc[i]['Ticker']}")

# crsp.to_csv("../cleaned-crsp.csv", index=False)
# flight.to_csv("../cleaned-flight.csv", index=False)
# final.to_csv("final.csv", index=True, index_label='Index')
