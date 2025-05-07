from fetch_data import get_stock_data

def moving_averages(df, timeframes =[7,30]):
  df["MA7"] = df["Close"].rolling(window = 7).mean()
  df["MA30"] = df["Close"].rolling(window = 30).mean()
  return df