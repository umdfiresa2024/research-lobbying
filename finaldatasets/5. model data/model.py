import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Load the dataset
data = pd.read_csv('../4. merge with meng/merged_meng.csv')

# Select relevant columns
columns = ['Total GHG', 'NAICS', 'US_revenue_share',
           'carbon_intensity', 'lobby_amount']
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

# Define the independent variables (X) and the dependent variable (y)
X = data.drop('lobby_amount', axis=1)
y = data['lobby_amount']

print(X.head())
print(y.head())

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


# Fit the Ridge regression model using scikit-learn
regressor = Ridge()
regressor.fit(X_train, y_train)

# Make predictions
y_pred = regressor.predict(X_test)

# Calculate R^2 score
r2 = r2_score(y_test, y_pred)

print(f'R^2 score: {r2}')

# Plot the true vs predicted values
plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())],
         [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())], 'k--', lw=2)  # Improved line for visual comparison
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('True vs Predicted Lobby Amount')
plt.show()
