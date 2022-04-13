# Python | Remove all duplicates words from a given sentence

from tkinter import N


inp = "Geeks for Geeks"
inp2 = "Python is great and Java is also great"

# 1 Using Loop 

def removedup(strng):
    n = strng.split()
    new = []
    for i in n:
        if i in new:
            pass
        else:
            new.append(i)

    return ' '.join(new)

print("using loop",removedup(inp))
print("using loop",removedup(inp2))


# 2 using counter
from collections import Counter

def removedup2(strng):
    inpt = strng.split()
    stn = Counter(inpt)
    return " ".join(stn)

print("using counter",removedup2(inp))
print("using counter",removedup2(inp2))