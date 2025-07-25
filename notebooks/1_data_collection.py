import yfinance as yf
import os

# Create data folder if it doesn't exist
os.makedirs("../data", exist_ok=True)

# Download historical stock data (e.g., Apple Inc.)
ticker = "AAPL"
data = yf.download(ticker, start="2015-01-01", end="2024-12-31")

# Save to CSV
data.to_csv("../data/AAPL_stock.csv")
print(f"✅ Data saved to ../data/AAPL_stock.csv with {len(data)} rows.")