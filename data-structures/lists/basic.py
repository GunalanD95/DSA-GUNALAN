# Python Lists


# creation of empty list
emp_list = []


#List of strings
list_strings = ['A', 'B', 'C', 'D']

# List of integers
list_integers = [1, 2, 3, 4]


# List of mixed data types
list_mixed = ['A', 1, 2, 'B', 3, 4, 'C', 5, 6, 'D', 7, 8, 'E', 9, 10]

# List Creation using list comprehension
list_comprehsion = [ i for i in range(1, 11)]
print(list_comprehsion)

list_even = [i for i in range(0,10,2)]
print(list_even)

list_3 = list(range(0,10,3))
print(list_3)

list_odd = [i for i in range(1,10) if i%2 != 0]
print(list_odd)


#Creating list from comma separated values
string_comma = 'A,B,C,D'
print(string_comma.split(','))

#Creating list with character as elements
name = "Gunalan"
print("name",list(name))

#Creating list with integer as elements

num = 2231744
#print("num",list(num)) it will throw TypeError: 'int' object is not iterable
print([int(i) for i in str(num)])