# K’th Non-repeating Character in Python using List Comprehension and OrderedDict


# 1 - Using NAIVE Approach
from collections import OrderedDict

txt = 'geeksforgeeks'
# k = 3
k = 2
# k = 4

dum = {}
for i in txt:
    if i in dum:
        dum[i] += 1
    else:
        dum[i] = 1

list1 = [k for k,v in dum.items() if v == 1]
print(list1)
print("O/P",list1[k-1] if len(list1) >= k else print("No such character"))