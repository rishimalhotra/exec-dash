# dashboard_generator.py

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

import os
csv_filepath = "/Users/Rishi/Documents/GitHub/exec-dash/sales-201710.csv"

import pandas
import numpy
#csv_filepath = "data/products.csv"
#csv_filepath = os.path.join(os.path.dirname(__file__), "..", "sales-201710.csv")
#sales = pandas.read_csv("data/monthly-sales/sales-201710.csv")

#totals = pandas.read_csv("/Users/Rishi/Documents/GitHub/exec-dash/sales-201710.csv")

#df = pandas.read_csv(csv_filepath) #df dataframe is the variable to put into pandas dataframe format

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

#def to_usd(my_price):
    #return f"${my_price:,.2f}"

df = pandas.read_csv(csv_filepath)
#print(df.head(0))

df["sales_total"] = df["units_sold"] * df["unit_price"]
print(df.head(6))
#print(totals.columns.tolist())
#saletotal = df["sales_total"].sum
my_saletotal = df.groupby(['product'])[['sales_total']].sum()
#print(saletotal)
print(my_saletotal)


#https://www.wintellect.com/using-pandas-to-analyze-sales-data/
#https://www.geeksforgeeks.org/create-a-new-column-in-pandas-dataframe-based-on-the-existing-columns/?ref=rp
#worked my_sale=totals.groupby(['product'])[['units_sold']].sum()
#not workmy_sales=totals.groupby(['sales_price'])[['units_sold']].prod()

#my_saletotal=totals.groupby(['product'])[['units_sold', 'sales_price']].prod()
#print(my_sales)

#not work my_saletotals=totals.groupby(['product'])([['units_sold'])([['sales_price']]).prod()
#print(my_saletotals)

#worked print(my_sale)

#print(df.sales_price.sum())
#https://stackoverflow.com/questions/28236305/how-do-i-sum-values-in-a-column-that-match-a-given-condition-using-pandas

#total_sales = to_usd(sales_price)
#print(total_sales)


import plotly
import plotly.graph_objs as go

#totals = pandas.read_csv("/Users/Rishi/Documents/GitHub/exec-dash/sales-201710.csv")

#df = pandas.read_csv(csv_filepath)


#fig = go.bar(df, x = 'sales_total', y = 'product', title='sales')
#fig.show()


#breakpoint()

#sales = []
#for sales_pricing in totals:
    #from pprint import pprint
    #pprint('sales_total')
    #sales.append(sales_pricing['units_sold'])

#product_category = []
#for product_cat in totals:
    #product_category.append(product_cat['product'])

#df.to_dict("sales_total")

#df.to_dict("product")

# productnames = []
# for namez in df:
#     productnames.append(namez["product"])

# numbersss = []
# for number in df:
#     numbersss.append(number["sales_total"])


# productnames = []
# for namez, row in df.iterrows(0):
#     productnames.append(namez["product"])

# numbersss = []
# for number, row in df.iterrows(0):
#     numbersss.append(number["sales_total"])


    #from pprint import pprint
    #pprint('sales_total')
    #sales.append(sales_pricing['units_sold'])

#product_category = []
#for product_cat in totals:
    #product_category.append(product_cat['product'])

plotly.offline.plot({
   "data" : [go.Bar(x=df['sales_total'], y=df['product'], orientation='h')]}, auto_open=True)

#https://plotly.com/python/v3/plot-data-from-csv/
# plotly.offline.plot({
#    "data" : [go.Bar(x=numbersss, y=productnames, orientation='h')]}, auto_open=True)




#workedish plotly.offline.plot([
    #workedish go.Bar(x=df['sales_total'], y=df['product'])])
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