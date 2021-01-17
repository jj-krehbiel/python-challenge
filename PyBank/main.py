#import modules
import os
import csv

#declare variables
total_PnL = 0
row_count = 0
prev_profit = 0
max_change = 0
min_change = 0

#make path to csv file
csvpath = os.path.join('PyBank_Resources', 'budget_data.csv')

#open csv file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        #make a variable that will add row count
        row_count += 1

        #add profits for total_PnL
        total_PnL += int(row[1])

        #if on first row, change = 0
        if row_count == 1:
            change = 0
            prev_profit = int(row[1])

        # row_count > 1, change = row[1] - prev_profit then reset prev_profit to current row
        elif row_count > 1:
            change = (int(row[1]) - prev_profit)
            prev_profit = int(row[1])
        
            #if change > max_change then update max_change
            if change > max_change:
                max_change = change
                max_month = (row[0])
               

            if change < min_change:
                min_change = change
                min_month = (row[0])
                

#calculate avg_change
avg_change = int(change) / (int(row_count) - 1)

print("Total Month: " + str(row_count))
print("Total Profit: " + str(total_PnL))
print("Average Change: " + str(avg_change))
print("Greatest Profit: " + str(max_month) + " " + "$"+str(max_change))
print("Least Profit: " + str(min_month) + " " + "$"+str(min_change))

#Turn it into a text file
with open ("PyBank_Analysis/PnL_Report.txt", "w") as file:
    file.write("Total Month: " + str(row_count))
    file.write("\n")
    file.write("Total Profit: " + str(total_PnL))
    file.write("\n")
    file.write("Average Change: " + str(avg_change))
    file.write("\n")
    file.write("Greatest Profit: " + str(max_month) + " " + "$"+str(max_change))
    file.write("\n")
    file.write("Least Profit: " + str(min_month) + " " + "$"+str(min_change))


