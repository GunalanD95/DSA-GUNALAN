import itertools
from collections import deque
from this import d


animals = ['cat', 'dog', 'monkey']


# for loop in python for list

for i in animals:
    print(i)

for i in range(len(animals)):
    print(i,"position:", animals[i])


#join all elements in list

cont = ['hello', 'world', 'how', 'are', 'you']
string = ' '.join(cont)
print(string)


# convert a list of lists into a single list using itertools

lists = [['cat', 'dog', 'monkey'], ['lion', 'tiger', 'bear']]

ls = list(itertools.chain(*lists))
print(ls)


# filter duplicates in list

dup = ['cat', 'dog', 'monkey', 'cat', 'dog']

lst = [i for i in dup if dup.count(i )> 1]
print(lst)



