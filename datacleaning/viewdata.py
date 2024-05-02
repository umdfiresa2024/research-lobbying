import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./data_with_price.csv")

# Calculate percentage difference
df["Percent_Diff"] = (df["Price_After"] - df["Price_Before"]
                      ) / df["Price_Before"] * 100

# Apply log transformation to both axes (handling zeros)
df["log_lobby"] = np.log10(df["lobby"] + 1)
df["log_Percent_Diff"] = np.log10(abs(df["Percent_Diff"]) + 1)

# Calculate the line of best fit
slope, intercept = np.polyfit(df["log_lobby"], df["log_Percent_Diff"], 1)
x_values = np.array([df["log_lobby"].min(), df["log_lobby"].max()])
y_values = slope * x_values + intercept

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df["log_lobby"], df["log_Percent_Diff"])

# Plot the line of best fit on top of the scatter plot
plt.plot(x_values, y_values, color='red', label='Line of Best Fit')

plt.xlabel("Log(Lobby + 1)")
plt.ylabel("Log(Abs(% Difference) + 1)")
plt.title("Scatter Plot with Log-Transformed Axes")
plt.grid(True)
plt.legend()  # Add a legend to display the line label
plt.show()
