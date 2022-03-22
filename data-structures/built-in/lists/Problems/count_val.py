# Python | Count occurrences of an element in a list


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]

a = 10

# 1 Using Naive Approach
count = 0
for i in lst:
    if a == i:
        count += 1

print(f"a has occured {count} times")


# 2 Using count method

lst2 = [15, 6, 7, 6, 12, 20, 10, 28, 10]
b = 6
print(f"a has occured {lst2.count(b)} times")


# 3 Using counter
from collections import Counter

l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
x = 3
d = Counter(l) # Counter method returns a dictionary with occurrences of all elements as a key-value pair, where key is the element and value is the number of times that element has occurred. 
print(d[x])