'''
    Hash tables are a type of data structure in which the address or the index value of the data element
    is generated from a hash function. That makes accessing the data faster as the index value behaves as a key 
    for the data value. In other words Hash table stores key-value pairs but the key is generated through a hashing function.
'''

# Declare a dictionary 
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Accessing the dictionary with its key
print ("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])


'''
    keys are immutable so we cannot change the key.

    duplicate keys are not allowed.

    but values can have duplicates.

    values can be accessed by their key.

    key search is fast .

    key ordering depends on the insertion order.

'''