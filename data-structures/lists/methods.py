list_of_strings = ["hello", "world", "!"]


# reverse the list using reveresed() function
for i in reversed(list_of_strings) :
    print(i)

j = [i for i in reversed(list_of_strings)]
print(j)


# copy a list using copy() function
list_of_strings_copy = list_of_strings.copy()
print(list_of_strings_copy)


a = [1,2]
b = a
print("b",b) 
b[0] = 999
print("a",a)  # by this method, a is also changed since heap is copied


# using copy will eliminate the reference to the same object
c = ['a','b']
d = c.copy()
c[0] = 'c'
print("d",d)
print('c',c)
