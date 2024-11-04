import pandas as pd
import numpy as np

summedGHG = pd.read_csv("../2. generate tickers/SummedGHGs.csv")
cleanedCRSP = pd.read_csv(
    "../1. generate datasets/flight and crsp/cleaned-crsp.csv")

# Create a mapping of TICKER to NAICS
naics_mapping = dict(zip(cleanedCRSP['TICKER'], cleanedCRSP['NAICS']))

# Use the mapping to efficiently assign NAICS values
summedGHG['NAICS'] = summedGHG['Ticker'].map(naics_mapping).fillna(np.nan)

summedGHG.to_csv("naics_ghgs.csv", index=False)
