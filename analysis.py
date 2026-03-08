import csv

total_sales = 0
profit_list = []
product_list = []
sales_list = []

products_above_5000 = []

with open("retail_sales.csv","r") as f:
    reader = csv.DictReader(f)

    for row in reader:

        sales = int(row["sales"])
        profit = int(row["profit"])
        product = row["product"]

        total_sales += sales

        profit_list.append(profit)
        product_list.append(product)
        sales_list.append(sales)

        # products with sales > 5000
        if sales > 5000:
            products_above_5000.append(product)

# best profit product
max_profit = max(profit_list)
index = profit_list.index(max_profit)
best_product = product_list[index]

# average profit
average_profit = sum(profit_list) / len(profit_list)

print("Total Sales:", total_sales)
print("Average Profit:", average_profit)
print("Best Product:", best_product)

print("Products with Sales > 5000:", products_above_5000)

#OUTPUT
'''
Total Sales: 101000
Average Profit: 1779.0
Best Product: Laptop
Products with Sales > 5000: ['Laptop', 'Chair', 'Desk', 'Monitor', 'Table']
```
