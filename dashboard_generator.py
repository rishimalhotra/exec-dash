# dashboard_generator.py

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

import os
import pandas
#csv_filepath = "data/products.csv"
#csv_filepath = os.path.join(os.path.dirname(__file__), "..", "sales-201710.csv")
csv_filepath = "sales-201710.csv"
sales = pandas.read_csv("data/monthly-sales/sales-201710.csv")

df = pandas.read_csv(csv_filepath)

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")


import plotly
import plotly.graph_objs as go

sales = []
for sales_price in "sales-201710.csv":
    sales.append(sales_price["sales price"]

product = []
for productcat in "sales-201710.csv"
    product.append(productcat["product"])

plotly.offline.plot([
    go.Bar(x=sales_price['sales'], y=product_category['product'])])
    #based on: #https://nbviewer.jupyter.org/github/SayaliSonawane/Plotly_Offline_Python/blob/master/Bar%20Chart/Bar_Chart%20%28Simple%2CGrouped%20and%20Stacked%29.ipynb 
    # https://stackoverflow.com/questions/53381074/plotting-a-grouped-bar-chart-using-plotly-from-a-pandas-dataframe 
    # https://stackoverflow.com/questions/35150580/how-to-draw-bar-chart-using-plotly-offline-mode-in-python

#plotly.offline.plot({
   # "data": [go.Bar(x=sales_price, y=product_category]}), auto_open=True)


print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")