## SETS OPERATIONS

odd = {1,3,5,7,9}
even = {0,2,4,6,8,10}
primes = {2,3,5,7}


# Union in sets
u = odd.union(even) # union of odd and even will combine the elements of both sets
print("union",u)


# Intersection in sets
i = odd.intersection(even) # intersection will check for similar elements present in both sets
print("intersection of odd and even",i)

i_o = primes.intersection(odd) # intersection of primes and odd will give only odd primes
print("intersection of primes and odd",i_o)

i_e = primes.intersection(even) # intersection of primes and even will give only even primes
print("intersection of primes and even",i_e)


set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}

diffA = set_a.difference(set_b) # will return the elements not in b from a
print("difference A",diffA)

diffB = set_b.difference(set_a) # will return the elements nnot in a from b
print("difference B",diffB)


sys_diff = set_a.symmetric_difference(set_b) # will return the elements not in both a and b
print("symmetric difference",sys_diff)


# Intersection of sets with update method , this will update the sets with common elements
set_a.intersection_update(set_b)
print("set_a",set_a)


# Difference update method , will remove common elements from sets
set_a.difference_update(set_b)
print("set_a",set_a)

# Symmetric difference update method , will remove common elements from sets
set_a.symmetric_difference_update(set_b)
print("set_a",set_a)


# Checking for subset by using issubset method

a = {1,2,3,4,5}
b = {1,2,3}
sub_a = a.issubset(b)  #checking if a is subset of b
sub_b = b.issubset(a)  #checking if b is subset of a
print("subset a",sub_a)
print("subset b",sub_b)

# vice versa for superset
sup_a = a.issuperset(b) #checking if a is superset of b
sup_b = b.issuperset(a) #checking if b is superset of a
print("superset a",sup_a)
print("superset b",sup_b)


# Check if there is no common elements in sets

num_1 = {1,2,3,4,5}
num_2 = {6,7,8,9,10}

dis = num_1.isdisjoint(num_2) # checking if there is no common elements in sets
print("disjoint",dis)