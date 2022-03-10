# 1 Ways to sort list of dictionaries by values in Python – Using itemgetter

from operator import itemgetter

# Initializing list of dictionaries
lis = [{ "name" : "Nandini", "age" : 20}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]

print("using itemgetter ",sorted(lis, key=itemgetter('age')))


# using sorted and itemgetter to print list sorted by both age and name
# notice that "Manjeet" now comes before "Nandini"
print("using itemgetter ",sorted(lis, key=itemgetter('age', 'name')))


# 2 Ways to sort list of dictionaries by values in Python – Using lambda function


print("using lambda",sorted(lis,key= lambda x: x['age']))
print("using lambda",sorted(lis,key= lambda x: (x['age'],x['name'])))