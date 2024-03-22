# import the operating systems functionalities to access and manipulate directories and files
import os

# import the csv module functionalities to read and write csv file
import csv

filePath = os.path.join(".", "Resources", "budget_data.csv")

# print(f"File path: {filePath}")

# Define the integer variable to collect the count of the total number of Months
count = 0

# Define an empty list to collect the dates by appending the values in each row of the date column 
Dates_mo = []

# Define an empty list to collect the Profit/Losses by appending the values in each row of the Profit/Losses column 
Profit_Losses = []


#Define empty integer variable to calculate the Net total amount of Proft/Losses
Net_total = 0

#Define an empty list to collect the changes overtime
changes_overtime = []

#Define empty integer variable to calculate the greatest change increase in profit
greatest_profit_increase = 0


#Define empty integer variable to calculate the greatest change decrease in profit
greatest_profit_decrease = 0

# Define empty variables for greatest change increase and decrease in profit
greatest_increase_date = ""

greatest_decrease_date = ""

with open(filePath) as fileToOpen:

    fileToRead = csv.reader(fileToOpen, delimiter = ",")

    # print(f"File to read: {fileToRead}")

    # skip the header row
    csv_header = next(fileToRead)

    # print(f"show: csv_header")

    #for row in csv_header:
        # print(row)
 

    for row in fileToRead:

        Dates_mo.append(row[0])
        Profit_Losses.append(int(row[1])) # otherwise use list comprehension afterward to calculate the same of values for Net_Total

    # Convert the strings to integers using list comprehension
    # Profit_Losses_int = [int(value) for value in Profit_Losses]


    # count the number of rows in dataset for the date column:
    for row in Dates_mo:
        count = count + 1
  
    #print(f"Counts: {count}")

    # print(f"Months: {Dates_mo}")
    
        
    Net_total = sum(Profit_Losses)

    # print(f'Net_total: {Net_total}')

    # Loop through the list of Profit_Losses to calculate the changes over time

    for i in range(1, len(Profit_Losses)):

        change = Profit_Losses[i] - Profit_Losses[i-1]

        changes_overtime.append(change)
        
        # print(changes_overtime)

    # iterate the rows of the Profit_Losses list to generate the changes
        
    for row in range(len(Profit_Losses)-1):
        
        changes = Profit_Losses[row + 1] - Profit_Losses[row]

        # Check if there was a great change increase
        if changes > greatest_profit_increase:
            
            greatest_profit_increase = changes

            # Corresponding date
            greatest_increase_date = Dates_mo[row + 1] 


        # Check if there was a great change decrease
        if changes < greatest_profit_decrease:
            
            greatest_profit_decrease = changes

            # Corresponding date
            greatest_decrease_date = Dates_mo[row + 1] 

    

    # Calculate the mean of changes
    mean_change = round(sum(changes_overtime) / len(changes_overtime),2)

    # print(mean_change)
            
    # print(f'Greatest Increase in Profits: {greatest_increase_date} ({greatest_profit_increase})')

    # print(f'Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_profit_decrease})')

    # print("Financial Analysis")
    # print("----------------------------")
    # print(f"Total Months: {count}")
    # print(f'Total: {Net_total}')
    # print(f'Average Change: {mean_change}')
    # print(f'Greatest Increase in Profits: {greatest_increase_date} ({greatest_profit_increase})')
    # print(f'Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_profit_decrease})')

# Financial analysis output
financial_analysis = [
    "                            ",
    "Financial Analysis",
    "                            ",
    "----------------------------",
    "                            ",
    f"Total Months: {count}",
    "                            ",
    f"Total: ${Net_total}",
    "                            ",
    f"Average Change: ${mean_change}",
    "                            ",
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_profit_increase})",
    "                            ",
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_profit_decrease})",
    "                            ",
]

# Print the financial analysis to the terminal

for line in financial_analysis:

    print(line)

# Define the file path for the output file
    
results_folder = "analysis"

results_file = "financialanalysis.txt"

output_path = os.path.join(results_folder, results_file)

# Ensure the output folder exists

os.makedirs(results_folder, exist_ok=True)

# Write the analysis results to the output file

with open(output_path, 'w') as file:

    for line in financial_analysis:
        
        file.write(line + '\n')

print("Financial analysis has been saved to 'financial_analysis.txt'.")