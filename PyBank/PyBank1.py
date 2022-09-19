# import 
import csv
import os

# input and output file details
file_for_analysis = "Resources/budget_data.csv"
file_to_report = "Analysis/pybank_report.txt"

# Starting points for various variables 
total_months = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_profit = 0

# reading csv data file and to convert into a list of dictionaries
with open(file_for_analysis) as profit_data:
    reader = csv.DictReader(profit_data)

# Track the totals
    for row in reader:

        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit/Losses"])

# Track the Profit/Losses
        Profit_change = int(row["Profit/Losses"]) - prev_profit
        prev_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [Profit_change]
        month_of_change = month_of_change + [row["Date"]]

# Calculate greatest increase
        if (Profit_change) > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = Profit_change

# Calculate greatest decrease
        if (Profit_change) < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = Profit_change

# Calculate the average Profit/loss 
Profit_avg = sum(profit_change_list) / len(profit_change_list)

# Output Summary
Output = (
f"\Financial Analysis\n"
f"----------------------\n" 
f"Total months: {total_months}\n"
f"Total: ${total_profit}\n"
f"Average Change: ${Profit_avg}\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(Output)

with open(file_to_report, "w") as txt_file:
    txt_file.write(Output)
