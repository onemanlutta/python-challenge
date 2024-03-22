# import the operating systems functionalities to access and manipulate directories and files
import os

# import the csv module functionalities to read and write csv file
import csv

filePath = os.path.join(".", "Resources", "election_data.csv")


# Define an integer variable to collect the total number of votes cast
total_votes = 0

# create an empty dictionary in which we will append votes cast for each candidate
candidate_votes = {}

# create an empty dictionary in which we will append percentage of votes cast per candidates
percentPerCandidate = {}

# Read the CSV file and calculate total votes and votes per candidate

with open(filePath) as fileToOpen:

    fileToRead = csv.reader(fileToOpen, delimiter = ",")

    # print(f"File to read: {fileToRead}")

    # skip the header row
    
    csv_header = next(fileToRead)

    # print(f"show: csv_header")

    #for row in csv_header:
        # print(row)

    for row in fileToRead:

        total_votes += 1

        candidate = row[2]

        if candidate in candidate_votes:

            candidate_votes[candidate] += 1

        else:
            candidate_votes[candidate] = 1

# Calculate percentage of votes per candidate using a loop

for candidate, votes in candidate_votes.items():

    percentPerCandidate[candidate] = (votes / total_votes) * 100

# Find the winner based on popular vote
    
winner = max(candidate_votes, key=candidate_votes.get)


# The election results

# print("Election Results")
# print("")
# print("-------------------------")
# print("")
# print(f'Total Votes: {total_votes}')

# Use a dictionary of lists to save the election results

election_results = {
    "spacer1": [""],
    "header": ["Election Results"],
    "spacer2": [""],
    "separator1": ["-------------------------"],
    "spacer3": [""],
    "total_votes": [f"Total Votes: {total_votes}"],
    "spacer4": [""],
    "separator2": ["-------------------------"],
    "spacer5": [""],
    "candidate_results": [],
    "separator3": ["-------------------------"],
    "spacer6": [""],
    "winner": [],
    "spacer7": [""]
}

# Add candidate results and the expected space formating in final output

for candidate, votes in candidate_votes.items():

    election_results["candidate_results"].append(f"{candidate}: {percentPerCandidate[candidate]:.3f}% ({votes})")

    election_results["candidate_results"].append("")

# Add winner information and line formating
    
election_results["winner"].extend([

    f"Winner: {winner}",
    "-------------------------"
])

# Print to the terminal

for section, lines in election_results.items():

    for line in lines:

        print(line)


# Define the file path for the output file
    
results_folder = "analysis"

results_file = "electionanalysis.txt"

output_path = os.path.join(results_folder, results_file)

# Ensure the output folder exists

os.makedirs(results_folder, exist_ok=True)

# Write the analysis results to the output file

with open(output_path, 'w') as file:

    for section, lines in election_results.items():

        for line in lines:

            file.write(line + '\n')

print("Election analysis has been saved to 'electionanalysis.txt'.")