import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
from modeltrain import StockPricePredictor, parse_settings


def predict_with_model(model, lobbying_amount):
    # Prepare input tensor
    input_tensor = torch.tensor(
        [np.log(lobbying_amount)], dtype=torch.float32)

    # Get prediction
    with torch.no_grad():  # No need to track gradients during inference
        output = model(input_tensor)

    return output.item()  # Convert tensor to a Python number


df = pd.read_csv("../main_data.csv")
df = df[df["outlier"] == 0]
df["log_lobby"] = np.log(df["lobby"])
df["log_dValue"] = np.log(abs(df["dValue_CAPM"]))
print(len(df))


# Load trained model
settings = parse_settings("settings.cfg")
model_path = "stock_price_predictor.pth"
model = StockPricePredictor(
    settings["input_size"], settings["hidden_size"], settings["output_size"])
model.load_state_dict(torch.load(model_path))
model.eval()

# Get X and Y
predicted_prices = []
for index, row in df.iterrows():
    # Apply log to lobbying amount here
    predicted_price = predict_with_model(
        model, row["lobby"])
    predicted_prices.append(predicted_price)
df["pred_log_dValue"] = predicted_prices


# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df["log_lobby"], df["log_dValue"])

# Plot the line of best fit
plt.plot(df["log_lobby"], df["pred_log_dValue"],
         color='red', label='Line of Best Fit')

plt.xlabel("Log Lobby Amount")
plt.ylabel("Log Abs Stock Price Change")
plt.title(f"Lobby Amount vs Predicted Stock Value in 2009-2010, n={len(df)}")
plt.grid(True)
plt.legend()  # Add a legend to display the line label
plt.show()
