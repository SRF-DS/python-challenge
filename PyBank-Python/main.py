#!/usr/bin/env python
# coding: utf-8

import os
import csv

# File path

file_path = os.path.join('Resources','budget_data.csv')



# Initialize variables
total_months = 0
net_total_pnl = 0
previous_pnl = 0
changes = []
dates = []

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Count total months
        total_months += 1

        # Calculate net total Profit/Losses
        current_pnl = int(row[1])
        net_total_pnl += current_pnl

        # Calculate change in Profit/Losses
        if total_months > 1:
            change = current_pnl - previous_pnl
            changes.append(change)
            dates.append(row[0])

        previous_pnl = current_pnl

# Calculate average change
average_change = sum(changes) / len(changes)

# Find greatest increase and decrease
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]

greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Print the analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_pnl:,.0f}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,.0f})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,.0f})")

# Save the results to a text file
output_path = os.path.join('analysis', 'financial_analysis.txt')
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total_pnl:,.0f}\n")
    file.write(f"Average Change: ${average_change:,.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,.0f})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,.0f})\n")

print(f"\nResults have been saved to {output_path}")