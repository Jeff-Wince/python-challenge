import csv

import_file = "Resources/budget_data.csv"
output_file = "analysis/budget_analysis.txt"

total_months=0
prev_rev=0
month_rev=0
month_change=[]
revenue_list=[]
greatest_increase= ["",0]
greatest_decrease= ["",1000000000000]
total_rev=0

with open('import_file','r') as rev_data:
    reader= csv.DictReader(rev_data, delimiter=',')

    for row in reader:
        total_months = total_months + 1
        total_rev = total_rev + int(row["Revenue"])


        revenue_change = int(row["Revenue"]) - prev_rev
        prev_rev = int(row["Revenue"])
        revenue_list = revenue_list + [revenue_change]
        month_change = month_change + [row["Date"]]


        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        
        if (revenue_change > greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change


avg_revenue = sum(revenue_list) / len(revenue_list)


output = (
"Financial Analysis"
"------------------------"
f"Total Months:{len(month_change)}"
f"Total: ${sum(total_rev)}"
f"Average Change: ${(avg_revenue)} \n"
f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]}) \n"
f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]}) \n")

print(output)

with open(output_file,"w") as txt_file:
    txt_file.write(output)