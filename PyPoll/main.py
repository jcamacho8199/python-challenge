import os
import csv

voters = []
candidates = []

election = os.path.join("Resources", "election_data.csv")
with open(election, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    for row in csvreader:
        voters.append(row[0]) 
        candidates.append(row[2])  

total_votes = len(voters)
        
votes_khan = 0
votes_correy = 0
votes_li = 0
votes_otooley = 0

i = 0
for i in range(total_votes):
    if candidates[i] == "Khan":
        votes_khan += 1
    if candidates[i] == "Correy":
        votes_correy += 1
    if candidates[i] == "Li":
        votes_li += 1
    if candidates[i] == "O'Tooley":
        votes_otooley += 1   
        
pct_khan = 0
pct_correy = 0
pct_li = 0
pct_otooley = 0

pct_khan = format(round(((votes_khan/total_votes) * 100)),'.3f')
pct_correy = format(round(((votes_correy/total_votes) * 100)),'.3f')
pct_li = format(round(((votes_li/total_votes) * 100)),'.3f')
pct_otooley = format(round(((votes_otooley/total_votes) * 100)),'.3f')

all_candidates = ["Khan","Correy","Li","O'Tooley"]
all_votes = [votes_khan,votes_correy,votes_li,votes_otooley]

for v in range(len(all_candidates)):
    max_vote = max(all_votes)
    max_index = all_votes.index(max_vote)
    max_candidate = all_candidates[max_index]

    min_vote = min(all_votes)
    min_index = all_votes.index(min_vote)
    min_candidate = all_candidates[min_index]       
        
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: " + str(total_votes))
print(f"-------------------------")
print(f"Khan: " + str(pct_khan) + "% (" + str(votes_khan) + ")")
print(f"Correy: " + str(pct_correy) + "% (" + str(votes_correy) + ")")
print(f"Li: " + str(pct_li) + "% (" + str(votes_li) + ")")
print(f"O'Tooley: " + str(pct_otooley) + "% (" + str(votes_otooley) + ")")
print(f"-------------------------")
print(f"Winner: " + str(max_candidate))
print(f"-------------------------")

with open("pypoll_output.txt", "w") as text_file:
    print(f"Election Results", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Total Votes: " + str(total_votes), file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Khan: " + str(pct_khan) + "% (" + str(votes_khan) + ")", file=text_file)
    print(f"Correy: " + str(pct_correy) + "% (" + str(votes_correy) + ")", file=text_file)
    print(f"Li: " + str(pct_li) + "% (" + str(votes_li) + ")", file=text_file)
    print(f"O'Tooley: " + str(pct_otooley) + "% (" + str(votes_otooley) + ")", file=text_file)
    print(f"-------------------------", file=text_file)
    print(f"Winner: " + str(max_candidate), file=text_file)
    print(f"-------------------------", file=text_file)