from fetch_data import get_stock_data
from visualize import plot_close_price
from indicators import moving_averages
company = input("enter a company").strip().upper()
start_date= input("enter the starting date").strip()
end_date = input("enter the ending date").strip()

if not start_date and not end_date:
  df = get_stock_data(company)
elif not start_date:
  df = get_stock_data(company, end=end_date)
elif not end_date:
  df = get_stock_data(company, start=start_date)
else:
  df = get_stock_data(company, start=start_date, end=end_date)
df = moving_averages(df)


plot_close_price(df, company)