#PyPoll
# modules so file works across devices
import os
import csv

# set path for file
# csvpath = os.path.join('Resources', 'election_data.csv')
csvpath = "Resources/election_data.csv"
# set path for text file creation
# 
#output_path = os.path.join("analysis", "election_results.csv")
output_path = "analysis/election_results.txt"
# create dictinoary to store election data
candidate_votes = {}
candidate = []
election_results = ''
voter_output = {}

# list varibles 
vote_percent = 0
total_votes = 0
winning_count = 0
winning_candidate = ''
# create function for vote_percent to incorporate formating

# open csv file 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    header = next(csvreader)

    #run calculation through rows
    for row in csvreader:
        candidate = row[2]

        #adding up all votes
        total_votes += 1

        # add votes to candidate name in dictionary 
        if candidate in candidate_votes.keys():
            candidate_votes[candidate] += 1 
        else: 
            candidate_votes[candidate] = 1
 
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = votes/total_votes * 100
        if votes >= winning_count:
            winning_count = votes
            winning_candidate = candidate
            # print(vote_percentage)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="") 
 
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"Winner: {winning_candidate} with {winning_count} votes\n"
        f"-------------------------\n")
    print(election_results)

            # for writing txt file of results
    with open(output_path, 'w') as f:
        f.write(election_results)
        for candidate in candidate_votes:
            votes = candidate_votes.get(candidate)
            vote_percentage = votes/total_votes * 100
            if votes >= winning_count:
                winning_count = votes
                winning_candidate = candidate
            # print(vote_percentage)
            voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
            f.write(voter_output)






