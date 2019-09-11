# Unit 3 | Assignment - Py Me Up, Charlie (PyBank)
import os
import csv

# Set File path
csvpath = os.path.join("..", "resources", "budget_data.csv")

# Variables
TotalMonths = 0
NetAmount = 0
MonthlyChange = []
Mon_Count = [] 
Greatest_Increase = 0
Greatest_Increase_mon = 0
Greatest_Decrease = 0
Greatest_Decrease_mon = 0

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

row = next(csvreader)
    
  
previous_row = int(row[1])
TotalMonths += 1
NetAmount += int(row[1])
Greatest_Increase = int(row[1])
Greatest_Increase_mon = row[0]
    
    
for row in csvreader:
        
       
        TotalMonths += 1
        # Calculate net amount of "Profit/Losses" over time
        NetAmount += int(row[1])

        # Calculate change from current to previous month
        revenue_change = int(row[1]) - previous_row
        MonthlyChange.append(revenue_change)
        previous_row = int(row[1])
        Mon_Count.append(row[0])
        
        # Calculate Greatest_Increase
        if int(row[1]) > Greatest_Increase:
            Greatest_Increase = int(row[1])
            Greatest_Increase_mon = row[0]
            
        # Calculate The Greatest_Decrease
        if int(row[1]) < Greatest_Decrease:
            Greatest_Decrease = int(row[1])
            Greatest_Decrease_month = row[0]  
        
    
average_change = sum(MonthlyChange)/ len(MonthlyChange)
    
highest = max(MonthlyChange)
lowest = min(MonthlyChange)

# Print Analysis statement 
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${NetAmount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {Greatest_Increase_mon}, (${highest})")
print(f"Greatest Decrease in Profits:, {Greatest_Decrease_mon}, (${lowest})")

# Specify File To Write To
output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {TotalMonths}\n")
    txtfile.write(f"Total: ${NetAmount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {Greatest_Increase_mon}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {Greatest_Decrease_mon}, (${lowest})\n")