# Slicing in Tuples

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(a[0:5])


# Reverse a tuple using slicing
print(a[::-1])


# Unpacking a tuple
my_tuple = 'Gunalan',23,'Developer' # no of elements should be same as no of variables
name,age,position = my_tuple
print("Name:",name)
print("Age:",age)
print("Position:",position)

es_tuple = (0,1,2,3,4,5,6,6,7,8,9)

i1 ,*i2 , i3 = es_tuple # i1 = 0, i2 = (1,2,3,4,5,6,7,8,9), i3 = 9
print("i1",i1)
print("i2",i2)
print("i3",i3)

