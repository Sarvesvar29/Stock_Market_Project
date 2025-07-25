import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import numpy as np
import yfinance as yf
import os

# Step 1: Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Step 2: Download AAPL stock data and save to CSV
df = yf.download("AAPL", start="2015-01-01", end="2024-01-01")
df.to_csv("data/AAPL_stock.csv")

# Step 3: Use only 'Close' column
df = df[['Close']]
df.dropna(inplace=True)

# Step 4: Train/test split
train_size = int(len(df) * 0.9)
train, test = df[:train_size], df[train_size:]

# Step 5: Fit ARIMA model
model = ARIMA(train['Close'], order=(5, 1, 0))
model_fit = model.fit()

# Step 6: Forecast
forecast = model_fit.forecast(steps=len(test))
forecast.index = test.index

# Step 7: Evaluate RMSE
rmse = np.sqrt(mean_squared_error(test['Close'], forecast))
print(f"📉 RMSE: {rmse:.2f}")

# Step 8: Plot
plt.figure(figsize=(14, 6))
plt.plot(train.index, train['Close'], label='Train', color='blue')
plt.plot(test.index, test['Close'], label='Actual', color='green')
plt.plot(forecast.index, forecast, label='Predicted (ARIMA)', color='red')
plt.title("ARIMA Forecast vs Actual", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Step 9: Save plot
os.makedirs("visuals", exist_ok=True)
plt.savefig("visuals/arima_forecast.png")
plt.show()