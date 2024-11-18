import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
data = pd.read_csv('../4. merge with meng/merged_meng.csv')

# Select relevant columns
columns = ['Total GHG', 'NAICS', 'lobby_amount']
data = data[columns]

# Drop rows with missing values
data['lobby_amount'] = data['lobby_amount'].replace(0, np.nan)
data = data.dropna()

# Extract first 2 digits of NAICS code
data['NAICS'] = data['NAICS'].astype(str).str[:2].astype(int)

# Apply log transformation to Total GHG and lobby_amount
data['log_GHG'] = np.log(data['Total GHG'])
data['log_lobby_amount'] = np.log(data['lobby_amount'])

data.to_csv("training_data.csv", index=False)
