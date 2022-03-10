# Tuples are ordered , immutable , allow duplicate elements

#Creation of tuple
tuple_f = (1,2,3,'guna',2.0,-1)
print("tuple:",tuple_f)

tuple_wo = 'guna',2,'lan'
print("tuple_wo:",tuple_wo)


tuple_w = ('gunalan',) # putting , will recongize this as a tuple
print("tuple_w",tuple_w)

#Creation of tuple from a list
built_in = tuple([1,2,3,'f',5,1,'guna'])
print("built in fun",built_in)


#Accessing an element inside tuple
tp = (100,200,300)
print("0th pos:",tp[0])


#Iterating through the tuple
for i in range(0,len(tp)):
    print(i,tp[i])


#Tuples are immuTABLE
#tp[0] = 122 #TypeError: 'tuple' object does not support item assignment
