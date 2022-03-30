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

print("small using min-a",findsmall(a))
print("small using min-b",findsmall(b))


# 3 using  loop
b = [100,20, 10, 20, 1]
a = [10, 20, 4]

def findsmallnum(ls):
    minm = ls[0]
    for i in range(0,len(ls)):
        if minm > ls[i]:
            minm = ls[i]
            print("mim:",minm,"ls:",ls[i])

    return minm


print("mim b",findsmallnum(b))
# print("mim a",findsmallnum(a))
