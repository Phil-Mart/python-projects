# PyBankSolution.py
# import
import os
import csv
     
# set path to read file
csvpath = os.path.join("Resources", "budget_data.csv")

# set path for text file creation
output_path = os.path.join('analysis/budget_analysis.txt')
# open csv file 

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    print(csvreader)
    #remove header
    header = next(csvreader)

    # Variables
    month = 0 
    total_net = 0
    net_change_list = []
    january = next(csvreader)
    month = month + 1
    total_net = total_net + int(january[1])
    previous_net_profit = int(january[1])
    greatest_increase = 0
    greatest_decrease = 0
    greatest_change_dates = []
    best_month = ""
    worst_month = ""

    for rows in csvreader:
        print(rows)
    
        # capture string of the name of date
        month_date = str(rows[0])
        # capture the number of total months
        month = month + 1
        # capture the net profit
        total_net = total_net + int(rows[1])
        # capture the change between months
        net_change = int(rows[1]) - previous_net_profit
        # capture differrence between net change and previous net
        previous_net_profit = int(rows[1])
        # store the net change in a new list to find the greatest inc.& dec.
        net_change_list = net_change_list + [net_change]

        # compare the net list to the next month to determine largest deltas
        if net_change > greatest_increase:
            greatest_increase = net_change
            best_month = month_date
        elif net_change < greatest_decrease:
            greatest_decrease = net_change
            worst_month = month_date
        # update the average net before moving onto next row  
        average_net = sum(net_change_list)/len(net_change_list)

# Print!
    print("Total months:" + str(month))
    print("Net Profit:" + str(total_net))
    print("Average Monthly Profit:" + str(average_net))
    print(f"The best fiscal month was: {best_month} : {greatest_increase}")
    print(f"The worst fiscal month was: {worst_month} ={greatest_decrease}")

with open(output_path, 'w') as f:

    results=(
       f"\n\nFiscal Analysis\n"
        f"-------------------------\n"
        f"Total months: {month}\n"
        f"Net Protit: {total_net}\n"
        f"Average Montly Profit: {best_month}: {greatest_decrease}\n"
        f"The best fiscal month was: {best_month}: {greatest_increase}\n"
        f"The worst fiscal month was: {worst_month}: {greatest_decrease}\n"
        f"-------------------------\n")

    # Write the first row (column headers)
    f.write(results)