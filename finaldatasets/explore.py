import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("flight_crispr.csv")
print(df.describe())

df['Total GHG'].plot(kind="bar")
