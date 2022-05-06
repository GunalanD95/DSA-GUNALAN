# Python program to find largest number in a list

a = [10, 20, 4]
b = [20, 10, 20, 1, 100]

# 1 Naive method

def findlarge(a):
    large = 0
    for i in a:
        if i > large:
            large = i
    return large

print(findlarge(a))
print(findlarge(b))


# Python program to find small number in a 

def findsmall(ls):
    return min(ls)

# print("small using min-a",findsmall(a))
# print("small using min-b",findsmall(b))


# 3 using  loop
b = [98, 83, 54, 57, 36, 83, 7, 98, -3, 37]
a = [-15, -45, 43, 23, -63, 69, 35, 19, 37, -52]

def findsmallnum(ls):
    minm = ls[0]
    for i in range(0,len(ls)):
        if minm > ls[i]:
            minm = ls[i]

    return minm


print("mim b",findsmallnum(b))
print("mim a",findsmallnum(a))
print(findlarge(a))
print(findlarge(b))
