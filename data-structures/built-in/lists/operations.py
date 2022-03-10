# Converting dictionary keys / values to list
dics = {'a': 1, 'b': 2, 'c': 3}

print("keys",list(dics.keys()))
print("values",list(dics.values()))


# add a element into the list
salary = [10000, 20000, 30000, 40000]

salary.append(50000) # append() adds an element at the end of the list
print("append salary",salary)

# access the element at the specified index
print(salary[0])


# change the element in the list using index
salary[0] = 25000
print("change salary",salary)

# remove an element from the list
salary.remove(25000)
print("remove salary",salary)


# Add a list to another list
domestic = ['India', 'China', 'Japan']
west = ['USA', 'Canada', 'Mexico']

domestic.extend(west) # extend() adds the elements of a list to another list
print(domestic)


# Add an element to the list into a specific index
domestic.insert(2, 'Australia') # insert() adds an element at the specified index
print(domestic)


# Get the index of an element
print("Position of australia",domestic.index('Australia'))


# Pop method removes the element at the specified index if not specified, it removes the last element
print("before pop",domestic)
domestic.pop()
print("after pop",domestic)

domestic.pop(0) # removing india using its index 0 
print("after pop remove",domestic)


# Sort Method using the default sorting which is ascending order or descending order
sort_num = [2 , 3, 4 , 5 , 2 , 1, 11 , 10, 20, 30, 40, 50 , 22 , 33 , 55 , 66 , 77 , 88 , 99 , 100]

sort_num.sort() # this will sort the list in ascending order by default
print("sort_num",sort_num) 

sort_num.sort(reverse=True) # this will sort the list in descending order
print("sort_num",sort_num)


# Reverse the list
rev_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rev_list.reverse()
print("reverse list",rev_list)