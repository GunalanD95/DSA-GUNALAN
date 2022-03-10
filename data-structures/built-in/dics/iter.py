# creating a dictionary using dict method

res = dict()
print(res)


# create a dictionary with states as key and abbreviation as value
res = {'Oregon': 'OR', 'Florida': 'FL', 'California': 'CA', 'New York': 'NY', 'Michigan': 'MI'}
print(res)

# iterating through a dictionary

if ('California' in res):
    print(f"California is in the dictionary with abbreviation {res['California']}") 


# for loop in dic

for i in res:
    print(i) # print the keys
    print(res[i]) # print the values