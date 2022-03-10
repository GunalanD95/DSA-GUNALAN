# Operations in sets


# Add an element to a set
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
my_set.add(5)
print("myset:",my_set)

# add mutiple elements in a set using the update method
my_set.update([6,7,8,9,10])
print("myset:",my_set)


# remove an element from a set
my_set.remove(1)
print("remove 1 myset:",my_set)

my_set.discard(99) # wont raise an error if the element is not in the set unlike remove


# pop method in a set
my_set.pop() # will remove and return an element from the set
print("pop myset:",my_set)

# delete the set
my_set.clear()
print("clear myset:",my_set)


# check if an element is in the set
count = {'INDIA','CHINA','USA','RUSSIA'}

if 'INDIA' in count:
    print(f'{"INDIA"} is in the set')
else:
    print(f'{"INDIA"} is not in the set')