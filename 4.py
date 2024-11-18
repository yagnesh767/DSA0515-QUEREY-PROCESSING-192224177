import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

ticker = "GOOGL"
start_date = "2023-01-01"  
end_date = "2023-12-31"    
stock_data = yf.download(ticker, start=start_date, end=end_date)

print(stock_data.head())

plt.figure(figsize=(10, 6))
plt.plot(stock_data.index, stock_data["Close"], label="Closing Price", color="blue")

plt.title(f"Historical Stock Prices of {ticker} ({start_date} to {end_date})", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Closing Price (USD)", fontsize=12)
plt.legend()
plt.grid(alpha=0.5)
plt.show()
