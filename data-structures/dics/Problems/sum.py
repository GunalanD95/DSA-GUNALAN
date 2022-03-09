# Problem : Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.

from typing import final


a = {'a': 100, 'b':200, 'c':300}

# 1
sums  = 0
for i in a:
    sums+=a[i]

print("Sum",sums)


# 2
def sum_dic(mydic):
    ls = []
    for i in mydic:
        ls.append(mydic[i])
    print(ls)
    final = sum(ls)
    return final

print("Sum",sum_dic(a))