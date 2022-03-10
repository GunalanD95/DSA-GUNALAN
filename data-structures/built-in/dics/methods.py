# a sample dictionary

sample = {'A': '100', 'B': '200', 'C': '300', 'D': '100', 'E': '500'}


# get a value of a key using GET METHOD
A = sample.get('A')
print("A",A)


# if not found will display the default message
G = sample.get('G','G not found')
print("G",G)

# list all keys in the dictionary
print("sample.keys()",sample.keys())

for k in sample.keys():
    print(k)

# list all values in the dictionary
print("sample.values()",sample.values())

for v in sample.values():
    print(v)


# list all items in the dictionary
print("sample.items()",sample.items())

for i , j in sample.items():
    print(i,j)

# delete and return the key mentioned
P = sample.pop('A')
print("P",P)
print("sample pop A",sample)


# popitem will remove  the last item in the dictionary
sample.popitem()
print("sample popitem",sample)


# sort the dictionary
sorted_sample_values  = sorted(sample.values())
sorted_sample_keys = sorted(sample.keys())
print("sample sort values",sorted_sample_values)
print("sample sort keys",sorted_sample_keys)