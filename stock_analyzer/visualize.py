import os
import matplotlib.pyplot as plt
from fetch_data import get_stock_data
from indicators import moving_averages

def plot_close_price(df, company_name):
  xpoints = df.index
  ypoints = df["Close"]
  plt.xlabel("Date")
  plt.ylabel("Price (USD)")

  plt.plot(xpoints,ypoints, label = "Close")
  plt.plot(xpoints,df["MA7"], label = "MA 7")
  plt.plot(xpoints,df["MA30"], label= "MA 30")
  plt.legend()
  plt.title(f"{company_name} Closing Price Over Time")
  plt.savefig(f"output/{company_name}_closing_price.png")
  plt.show()
  plt.clf()


