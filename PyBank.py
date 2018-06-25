# dependencies
import os
import csv
# create variables
filepath = os.path.join("raw_data/budget_data_1.csv")
total_months = 0
total_revenue = 0
revenue_change_list = []
month_of_change = []
prev_revenue = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]
# code
with open (filepath, newline='') as revenue_data:
    csvreader = csv.reader(revenue_data, delimeter=',')
    for row in csvreader:
        # track months
        total_months = total_months + 1
        # total revenue
        current_revenue = int(row["Revenue"])
        total_revenue = total_revenue + current_revenue
        # track revenue change
        revenue_change = current_revenue - prev_revenue
        revenue_change_list = revenue_change_list.append(revenue_change)
        month_of_change = month_of_change.append()
        prev_revenue = current_revenue
        # find greatest revenue increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = month_of_change
            greatest_increase[1] = revenue_change
        # find greatest decrease increase
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = month_of_change
            greatest_decrease[1] = month_of_change

revenue_change_avg = sum(revenue_change_list) / len(revenue_change_list)
print(
    f""
)

