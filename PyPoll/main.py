import os
import csv

#PyPoll

def elections(inputfile, outputfile):
    if not os.path.exists(inputfile):
        print("File does not exist")
        return

    tot_votes = 0

    with open(inputfile, newline="", encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        firstrow = next(csvreader, None)
        candidate_pct_votes = 0.0
        max_votes = 0
        i = 0
        mydict = {}

        for row in csvreader:
            voter_id = row[0]
            county = row[1]
            candidate = row[2]
            tot_votes += 1

            if candidate not in mydict:
                mydict[candidate] = 0

            mydict[candidate] += 1

    # basic enumerate without condition:

    print("Election Results for ", inputfile)
    print("------------------------------------------------------")
    print("Total Votes : " + str(tot_votes))
    winner = None
    max_votes = 0
    for candidate in mydict.keys():
        print("------------------------------------------------------")
        print('Candidate', candidate, 'got', mydict[candidate], 'votes.')
        print('candidate', candidate, 'got ', (mydict[candidate] / tot_votes) * 100, 'percent of votes')
        if winner is None or mydict[candidate] > max_votes:
            winner = candidate
            max_votes = mydict[candidate]

        print("------------------------------------------------------")
    print('Candidate', winner, 'is the winner with', max_votes, 'votes')
    print("------------------------------------------------------")

# Specify the file to write to
    output_path = os.path.join(outputfile)
#print (output_path)

    with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)

        csvwriter.writerow(["Election Results"])
        csvwriter.writerow(["------------------------------------------------------"])

# works fine until here - then get a tot_votes not defined error in like 62
        csvwriter.writerow(["Total Votes : " + str(tot_votes)])

        for c in mydict.keys():
            csvwriter.writerow(["Candidate " + str(c) + " got " + str(mydict[c]) + " votes. "])
            csvwriter.writerow(["Candidate " + str(c) + " got " + str(mydict[c] / tot_votes * 100) + " percent of votes. "])
            csvwriter.writerow(["------------------------------------------------------"])

        csvwriter.writerow(["candidate " + str(winner) + " is the winner with " + str(max_votes) + " votes and " + str(mydict[winner] / tot_votes * 100) + " percent of votes. "])

#Calls to main module
elections("election_data_1.csv", "election_results_1.txt")
elections("election_data_2.csv", "election_results_2.txt")