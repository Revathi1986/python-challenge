import os
import csv
pypollcsv = os.path.join("Resources","election_data.csv")
count = 0
list_canditate =[]
unique_candidate =[]
count_vote = []
per_vote = []
with open (pypollcsv,newline="")as csvfile:
    csvreader = csv.reader(csvfile,delimiter =",")
    csv_header = next(csvreader)
    for row in csvreader:
        count = count + 1
        list_canditate.append(row[2])
    for A in set (list_canditate):
        unique_candidate.append(A)
        B = list_canditate.count(A)
        count_vote.append(B)
        C =(B/count)*100
        per_vote.append(C)
    winning_count_vote = max(count_vote)
    winner = unique_candidate[count_vote.index (winning_count_vote)]
print("                                                    ")
print("election results")
print("                                                        ")
print("total votes:" + str(count))
print("                                                         ")
for i in range (len(unique_candidate)):
        print(unique_candidate[i] + ":" + str (per_vote[i])+ " % ("+str(count_vote[i])+")")
print("                                                     ")
print("the winner is:"+ winner)
print("                                                          ")




