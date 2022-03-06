sales = {'apple': 2, 'orange': 3, 'grape': 1, 'banana': 4}


# access a key

org = sales['orange']
print(org)


# changing a value of a key

sales['apple'] = 5
print(sales)

# add a key-value pair
sales['watermelon'] = 6
print(sales)

# delete a key-value pair
del sales['watermelon']
print(sales)


# find the length of the dic
print("length",len(sales))


# delete all the key-value pairs
sales.clear()
print(sales)