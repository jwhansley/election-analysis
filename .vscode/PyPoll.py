# The data we need to retrieve

# add our dependencies
import csv
import os

# assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0

# candidate options and candidate votes
candidate_options = []

#1. declare the empy dictions
candidate_votes = {}

# winning candidate and winning count ticker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read the header row
    headers = next(file_reader)
    
    # print each row in the CSV
    for row in file_reader:
        #2. add to the total vote count
        total_votes += 1

        # print the candidate name from each row
        candidate_name = row[2]

        # if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #...add it to the list of candidates
            candidate_options.append(candidate_name)

            #2. begin tracking the candidates vote counts
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# determine the percentage of votes for each candidate by looping through the counts
# iterate through the candidate list
for candidate_name in candidate_votes:

    #2. retrieve the vote count of a candidate
    votes = candidate_votes[candidate_name]

    #3. calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # print each candidates name, vote count, and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes})\n")

    # determine winning vote count and candidate
    #1. determine if the votes are greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        #2. if true then set winning_count = votes and winning percentage = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage

        #3. set the winning_candidate equal to the candidates name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------\n")
print(winning_candidate_summary)

#2. the complete list of candidates who received votes

# print the candidate name from each row


#3. the percentage of votes each candidate won

#4. the total number of votes each candidate won

#5. the winner of the election based on popular vote