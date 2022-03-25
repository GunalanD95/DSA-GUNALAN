# Basics of Linked Lists

list1 = ['apple', 'banana', 'cherry']

# Linked List : A list in which each element points to the next element in the list

# apple -> banana -> cherry

# apple 
# 7897 --> banana
            # 7897 --> cherry
                       # 2456 --> None


# Pointer : A pointer is a variable that holds the address of another variable

obj1 = {'a': 'David'}
obj2 = obj1                        # The objects are passed to function by reference

# ids of obj1 and obj2 are same 
print(id(obj1), id(obj2))
obj1['a'] = 'John'
del obj1
obj2 = {'c': 'king'}
print(obj2)
print(id(obj2))