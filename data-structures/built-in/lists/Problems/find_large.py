# Python program to find largest number in a list

a = [10, 20,994]
b = [100,20, 10, 20, 1]



# 1 Naive approach

def finflarg(ls):
    big = 0
    temp = 0
    for i in range(0,len(ls)):
        if ls[i] > temp:
            temp  = ls[i]
            big = i

    return big


# print(finflarg(a))
# print(finflarg(b))


# 2nd Largest element


a = [10, 20,994,555]
b = [100,20, 10, 20, 1]
c = [10, 20,44,222,657,653,12,3,555]

def findsec(ls):
    largest = finflarg(ls)
    res = -1
    for i in range(0,len(ls)):
       if ls[i] != ls[largest]:
           if res == -1:
               res = i
           elif ls[i] > ls[res]:
               res = i

    return ls[res]

print(findsec(a))
print(findsec(b))
print(findsec(c))


