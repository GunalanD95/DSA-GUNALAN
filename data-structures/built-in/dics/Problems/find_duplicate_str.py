#Python – Find all duplicate characters in string

# 1 Using Counter

from collections import Counter

def find_dup(inp):
    st =  Counter(inp)
    dup = []
    for i in st:
        if st[i] > 1:
            dup.append(i)

    return dup


print(find_dup('Gunalan'))
