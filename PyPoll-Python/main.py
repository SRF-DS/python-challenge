#!/usr/bin/env python
# coding: utf-8

import os
import csv
from collections import Counter

# File path
urlpath = "C:\\Users\\sebif\\Cargo_Bay\\python-challenge\\PyPoll-Python\\Resources\\"
file_path = os.path.join(urlpath, "election_data.csv")

# Initialize variables
total_votes = 0
candidates = []
vote_counts = Counter()

# Read the CSV file
with open(file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        vote_counts[candidate] += 1
        if candidate not in candidates:
            candidates.append(candidate)

# Calculate results
results = []
for candidate in candidates:
    votes = vote_counts[candidate]
    vote_ratio = votes / total_votes
    results.append((candidate, votes, vote_ratio))

# Determine the winner
winner = max(results, key=lambda x: x[1])[0]

# Print the analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes, ratio in results:
    print(f"{candidate}: {ratio:.3%} ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes, ratio in results:
        file.write(f"{candidate}: {ratio:.3%} ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print(f"\nResults have been saved to {output_path}")