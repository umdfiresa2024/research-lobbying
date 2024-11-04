import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Load the dataset
data = pd.read_csv('training_data.csv')

# Define the independent variables (X) and the dependent variable (y)
X = data.drop('log_lobby_amount', axis=1)
y = data['log_lobby_amount']

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
