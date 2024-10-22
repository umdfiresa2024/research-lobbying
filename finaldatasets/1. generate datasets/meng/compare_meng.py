import pandas as pd
import numpy as np

meng = pd.read_csv('meng_tickers_gemini.csv')
meng2 = pd.read_csv('meng_tickers_gpt.csv')

for i in range(len(meng)):
    if meng.iloc[i]["Company"] != meng2.iloc[i]["Company"]:
        print("Different name")
    elif meng.iloc[i]["Ticker"] != meng2.iloc[i]["Ticker"]:
        print(
            f"{meng.iloc[i]['Company']:<20} {meng.iloc[i]['Ticker']:<10} {meng2.iloc[i]['Ticker']}")
