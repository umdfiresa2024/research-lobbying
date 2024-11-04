
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Load the dataset
data = pd.read_csv('../4. merge with meng/merged_meng.csv')

# Select relevant columns
columns = ['Total GHG', 'NAICS', 'lobby_amount']
data = data[columns]

# Drop rows with missing values
data = data.dropna()

# One-hot encode the 'NAICS' column
# Handle unseen NAICS in test set
encoder = OneHotEncoder(handle_unknown='ignore')
encoded_naics = encoder.fit_transform(
    data[['NAICS']]).toarray()  # Convert to dense array

# Create a DataFrame with the encoded columns
encoded_naics_df = pd.DataFrame(
    encoded_naics, columns=encoder.get_feature_names_out(['NAICS']))

# Concatenate the encoded columns with the original DataFrame
data = pd.concat([data.drop('NAICS', axis=1), encoded_naics_df], axis=1)

# Apply log transformation to Total GHG and lobby_amount
data['Total GHG'] = np.log1p(data['Total GHG'])
data['lobby_amount'] = np.log1p(data['lobby_amount'])

# Define the independent variables (X) and the dependent variable (y)
X = data.drop('lobby_amount', axis=1)
y = data['lobby_amount']

print(X.head())
print(y.head())

# Create a figure with subplots
fig, axes = plt.subplots(1, len(columns) - 1, figsize=(15, 5))
axes = axes.ravel()  # Flatten axes array for easier iteration

# Plot each feature against lobby_amount
for idx, col in enumerate(columns[:-1]):  # Exclude lobby_amount
    if col == 'NAICS':
        continue
    axes[idx].scatter(data[col], y, alpha=0.5)
    axes[idx].set_xlabel(col)
    axes[idx].set_ylabel('Lobbying Amount')
    axes[idx].set_title(f'{col} vs Lobbying Amount')
    axes[idx].grid(True)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
