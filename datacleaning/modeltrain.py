import torch
import torch.nn as nn
import pandas as pd
import numpy as np


def parse_settings(path):
    with open(path, 'r') as f:
        return {entry[0]: int(entry[1]) for line in f.readlines() if (entry := line.strip().split(" = "))}


class StockPricePredictor(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(StockPricePredictor, self).__init__()
        self.linear1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        return out


if __name__ == "__main__":
    settings = parse_settings("settings.cfg")

    df = pd.read_csv("../main_data.csv")
    df = df[df["outlier"] == 0]
    df["log_lobby"] = np.log(df["lobby"])
    df["log_dValue"] = np.log(abs(df["dValue_CAPM"]))

    model = StockPricePredictor(
        settings["input_size"], settings["hidden_size"], settings["output_size"])

    # Define loss function and optimizer
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters())

    # Convert to tensors
    X = torch.tensor(df["log_lobby"].values, dtype=torch.float32)
    y = torch.tensor(df["log_dValue"].values, dtype=torch.float32)

    # Training loop
    print("training started")
    for epoch in range(settings["num_epochs"]):
        for i in range(len(X)):
            output = model(torch.tensor([X[i]]))
            loss = criterion(output, y[i])

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    print("training finished")

    # Save the trained model
    torch.save(model.state_dict(), "stock_price_predictor.pth")
