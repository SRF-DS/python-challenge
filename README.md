Documentation of my process to complete the python - challenge:

Conceptual Framework I began witht the question "what is the most efficient way of completing this challenge?"
I determined that would be using pandas dataframes and the jupyter notebook because it is the most powerful data analysis tool we have learned so far.
Functions downstream from using these tools I determined is the easiest method of drilling down on this data.
  -Testing code as I go
  -running smaller portions of the code
  - simpler saving
  - simpler debugging

Prompt 1: [Inserted Assignment Instructions]
Prompt 2: I inserted the code I made myself up until 
"net_total_pnl = bank_df['Profit/Losses'].sum()"
net_total_pnl

The code from this point required no debugging and created the files successfully after I adjusted the pathing so it could write the file to the correct place.

PyBank completed

PyPoll
I imported the beginning lines of code since it similarly applied.
I had no issues coding on my own until I reached #Calculate total vote won and total percentage vote won

Iteration of code block 1:
#ref code greatest_decrease_date = bank_df.loc[bank_df['Change'] == greatest_decrease, 'Date'].iloc[0]
voted_for = poll_df.loc[poll_df['Candidate'] == 'Charles Casper Stockham'].count()
vote_ratio = voted_for / total_votes
print(voted_for)
print(vote_ratio)

Problem: This would print multiple lines for each instead of printing in one line.

Prompt [inserted that code into perplexity] + Generate single output per candidate name
Iteration of code block 2:
candidate_name = 'Charles Casper Stockham'
voted_for = poll_df.loc[poll_df['Candidate'] == candidate_name, 'Ballot ID'].count()
vote_ratio = voted_for / total_votes
print(f"Votes for {candidate_name}:")
print(voted_for)
print(f"\nVote ratio for {candidate_name}:")
print(f"{vote_ratio:.6f}")

Problem: This would create the correct output but would not loop so was a progress stepping stone

prompt [Generate loop to create multiple output cycling through 3/3 candidates]
results = []
for candidate in candidates:
    voted_for = poll_df.loc[poll_df['Candidate'] == candidate, 'Ballot ID'].count()
    vote_ratio = voted_for / total_votes
    results.append((candidate, voted_for, vote_ratio))

Rest of code generated worked effectively simply needed minor pathing fixes so the files could write to the write place.

Thank you for reviewing my processes.

References for sourcing code : 
PythonDALesson2 (from second day of class)
Good_Movies (from second day of class)
Pandas Recap (from second day of class)
Perplexity AI

