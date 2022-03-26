# Dictionary and counter in Python to find winner of election

# Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.
# Examples: 
 

# Input :  votes[] = {"john", "johnny", "jackie", 
#                     "johnny", "john", "jackie", 
#                     "jamie", "jamie", "john",
#                     "johnny", "jamie", "johnny", 
#                     "john"};

votes =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']

# 1 Naive solution
from collections import Counter

def get_votes(votes):
    d = {}
    vss = Counter(votes)
    for v in vss.values():
        d[v] = []

    for (key,value) in vss.items():
        d[value].append(key)

    maxVote = sorted(d.keys(),reverse=True)[0]

    if len(d[maxVote])>1:
        print (sorted(d[maxVote])[0])
    else:
        print (d[maxVote][0])

get_votes(votes)