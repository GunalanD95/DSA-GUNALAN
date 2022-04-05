# Python program to find largest number in a list


b = [100,20, 10, 20, 1]
a = [10, 20,994]


# 1 Naive approach

def finflarg(ls):
    big = 0
    for i in ls:
        if i > big:
            big = i

    return big


print(finflarg(a))
print(finflarg(b))


# 2nd Largest element

def findsec(ls):
    big = ls[0]
    dev = []
    for i in ls:
        if i > big:
            dev.append(i)

    return dev[-1]

print(findsec(a))
print(findsec(b))


