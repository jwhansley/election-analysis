# election-analysis

## Challenge Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.  The purpose of this election audit analysis was to automate process of:

1. Calculate the total number of votes casts
2. Get a complete list of the candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the eletion based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.9, VS Code 1.61

## Results
The analysis of the election show that:
  - There were 369,711 votes cast in the election
  - The county results were:
    - Jefferson county receieved 10.5% of the vote and 38,855 number of votes
    - Denver county receieved 82.8% of the vote and 306,055 number of votes
    - Arapahoe county receieved 6.7% of the vote and 24,801 number of votes
  - Denver County received the largest voter turnout
  - The candidates were:
    -  Charles Casper Stockham
    -  Diana DeGette
    -  Raymon Anthony Doane
  - The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
  - The winner of the election was:
    -  Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Summary
This is a script that can be utilized for any election to determine voter turnout and the winner of the election.  With a few modifications we can also expand the script to do a lot more analysis.  If we also had a table of the county population we could determine voter turnout against possible voter turn out, giving us insight into which counties are more active by percentage.  If we layer in party affiliation into the candidate data, we can also see if there's a party that's more prodominent in the election.

