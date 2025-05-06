from fetch_data import get_stock_data
df = get_stock_data("AAPL", start="2025-03-05", end="2025-06-05")
print(df.head())
print(df.columns)
print(df.describe())
