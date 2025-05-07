import os
import matplotlib.pyplot as plt
from fetch_data import get_stock_data

def plot_close_price(df, company_name):
  xpoints = df.index
  ypoints = df["Close"]
  plt.xlabel("Date")
  plt.ylabel("Price (USD)")

  plt.plot(xpoints,ypoints)
  plt.title(f"{company_name} Closing Price Over Time")
  plt.show()
  plt.clf()


