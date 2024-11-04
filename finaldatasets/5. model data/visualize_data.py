
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Load the dataset
data = pd.read_csv('training_data.csv')
data['NAICS'] = data['NAICS'].astype(str)

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Plot 1: Total GHG vs Lobbying Amount
ax1.scatter(data['log_GHG'], data['log_lobby_amount'], alpha=0.5)
ax1.set_xlabel('log_GHG')
ax1.set_ylabel('Lobbying Amount')
ax1.set_title('Total GHG vs Lobbying Amount')
ax1.grid(True)

# Plot 2: NAICS (first 2 digits) vs Lobbying Amount
# Extract first 2 digits of NAICS and calculate mean lobby amount for each
naics_mean = data[['NAICS', 'log_lobby_amount']].groupby('NAICS')[
    'log_lobby_amount'].mean()

print(naics_mean)

ax2.bar(naics_mean.index, naics_mean.values)
ax2.set_xlabel('NAICS (First 2 Digits)')
ax2.set_ylabel('Average Log Lobbying Amount')
ax2.set_title('Average Log Lobbying Amount by Industry Sector')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True)

plt.savefig('data_visualization.png')

plt.tight_layout()
plt.show()
