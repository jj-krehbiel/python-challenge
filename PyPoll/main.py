#import modules
import os
import csv

#make path to csv file
csvpath = os.path.join('PyPoll_Resources', 'election_data.csv')

#declare variables
vote_count = 0
khan_votes = 0
correy_votes = 0
otooley_votes = 0
li_votes = 0

#open csv file
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        #make a variable that will add row count
        vote_count += 1
       
       #count votes for each candidate
        if row[2] == "Khan":
            khan_votes += 1

        if row[2] == "Correy":
            correy_votes += 1

        if row[2] == "Li":
            li_votes += 1

        if row[2] == "O'Tooley":
            otooley_votes += 1

#calculate vote percentage
kahn_percent = (float(khan_votes)/vote_count) * 100
correy_percent = (float(correy_votes)/vote_count) * 100 
li_percent = (float(li_votes)/vote_count) * 100 
otooley_percent = (float(otooley_votes)/vote_count) * 100  

#compare each candidates votes to determine winner
if khan_votes > correy_votes and khan_votes > li_votes and khan_votes > otooley_votes:
    winner = "Khan"

if correy_votes > khan_votes and correy_votes > li_votes and correy_votes > otooley_votes:
    winner = "Correy"

if li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes:
    winner = "Li"

if otooley_votes > khan_votes and otooley_votes > correy_votes and otooley_votes > li_votes:
    winner = "O'Tooley"

#Print outputs
print("Khan: " + format(kahn_percent, ".2f") + "% (" + str(khan_votes) +")")
print("Correy: " + format(correy_percent, ".2f") + "% (" + str(correy_votes) +")")
print("Li: " + format(li_percent, ".2f") + "% (" + str(li_votes) +")")
print("O'Tooley: " + format(otooley_percent, ".2f") + "% (" + str(otooley_votes) +")")
print("Winner: " + winner)



#Turn it into a text file
with open ("PyPoll_Analysis/election_analysis.txt", "w") as file:
    file.write("Total Votes Cast: " + str(vote_count))
    file.write("\n")
    file.write("Khan: " + format(kahn_percent, ".2f") + "% (" + str(khan_votes) +")")
    file.write("\n")
    file.write("Correy: " + format(correy_percent, ".2f") + "% (" + str(correy_votes) +")")
    file.write("\n")
    file.write("Li: " + format(li_percent, ".2f") + "% (" + str(li_votes) +")")
    file.write("\n")
    file.write("O'Tooley: " + format(otooley_percent, ".2f") + "% (" + str(otooley_votes) +")")
    file.write("\n")
    file.write("Winner: " + winner)

