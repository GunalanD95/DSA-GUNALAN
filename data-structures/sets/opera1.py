# SETS


# Iterating over a set

my_set = {'MESSI','CRISTIANO','NEYMAR'}

for i in my_set:
    print(i)


# accessing the elements of a set
# print(my_set[0]) # this is not possibe in set it will raise an error TypeError: 'set' object is not subscriptable



# Updating a set

my_set.update('GUNALAN')
print(my_set)


# copying a set

cop = {'CRISTIANO','NEYMAR','MESSI'}
new = cop.copy()
print("new copy",cop)


# Forzenset is immutable unlike normal set  

A = {1,2,3,4,5}
B = A
B.add(99) # this will add to A , also since assignement is here points to heap space 
print("A",A)
print("B",B)


# now this can be avoided using forzensets

fr = frozenset({1,2,3,4,5})
cp = fr.copy()
cp.add(99) # AttributeError: 'frozenset' object has no attribute 'add'
