# import 
import csv
import os


#input and output file details
file_for_analysis = "Resources/election_data.csv"
output = open("Analysis/Pypoll_report.txt", "w")

# Starting points for various variables 
Total_votes=0
votescast=0
totalvotescast=0
candidates=[]
numberwon = {}
percentwon=0
winnername=""
winnervotes=0

#Open CSV as Reader
with open(file_for_analysis) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)

#The total number of votes cast
    for row in csv_reader:
        Total_votes +=1
    
#A complete list of candidates who received votes
#The total number of votes each candidate won
        if row[2] not in candidates:
            candidates.append(row[2])
            numberwon[row[2]]=0
        numberwon[row[2]]+=1
        
#Print
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {Total_votes}")
print(f"-------------------------")
output.write(f"Election Results\n")
output.write(f"-------------------------\n")
output.write(f"Total Votes: {Total_votes}\n")
output.write(f"-------------------------\n")

#The percentage of votes each candidate won
for name in numberwon:
    votes = numberwon[name]
    percentage = votes / Total_votes
    poll = percentage * 100
    print(f"{name}: {poll:.3f}% ({votes})")
    output.write(f"{name}: {poll:.3f}% ({votes})\n")

#The winner of the election based on popular vote.
    if votes > winnervotes: 
        winnervotes = votes
        winnername = name
#Print 
print(f"-------------------------")
print(f"Winner: {winnername}")
output.write(f"-------------------------\n")
output.write(f"Winner: {winnername}\n")

