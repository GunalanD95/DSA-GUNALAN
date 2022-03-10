my_tp  = ['USA', 'China', 'Japan', 'Korea', 'India']



#Checking if an element is inside a tuple
if 'China' in my_tp:
    print('USA is in the list')
else:
    print('USA is not in the list')


char_tup  = ('g','u','n','a','l','a','n')

#Get Length of a tuple
print(len(char_tup))

#Converting tuple to character
print(''.join(char_tup))

#Count the number of times a character occurs in a tuple
print(char_tup.count('a'))

#Get the index of a elemet
print(char_tup.index('n'))
print(my_tp.index('Japan'))

#Convert a tuple to a list
tpp = (1,2,3,4,5)
lst = list(tpp)
print(lst)