
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

data.to_csv("training_data.csv", index=False)
