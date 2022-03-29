# Python – Key with maximum unique values
# Given a dictionary with values list, extract key whose value has most unique values.

country_code = {'India' : [5, 7, 9, 4, 0], 
                'Australia' : [6, 7, 4, 3, 3], 
                'Nepal' : [9, 9, 6, 5, 5] }

# 1 Using Collections.Counter

from collections import Counter
count = []
for i in country_code.values():
    count1 = Counter(i)
    print(count1)
    count.append(count1)

res = list(max(count))
for k,v in country_code.items():
    if v == res:
        print("Key with maximum unique values is: ", k)



# 2 Using Loop
max_val = 0
max_key = None 

for sub in country_code:
    val_set = set(country_code[sub])               # converting to set will remove duplicate elements
    print("val_set",val_set)

    if len(val_set) > max_val:
        max_val = len(val_set)
        max_key = sub
print("Key with maximum unique values using loop method is: ", max_key)
