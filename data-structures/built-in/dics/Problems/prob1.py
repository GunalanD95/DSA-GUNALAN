# Problem Statement – Here are the major tasks that are needed to be performed. 
 

# Create a dictionary and display its keys alphabetically.
# Display both the keys and values sorted in alphabetical order by the key.
# Same as part (ii), but sorted in alphabetical order by the value.


dics = {'e':4,'a':2,'c':2,'f':1,'d':4,'b':11}


# 1
alphabet_keys = [i for i in sorted(dics.keys())]
print("alphabet_keys",alphabet_keys)

# 2
for i in sorted(dics.keys()):
    print((i,dics[i]))

# 3
for k,v in sorted(dics.items(),key =lambda kv:(kv[1], kv[0])):
    print(k,v)
    