# Python program to print even and odd numbers in a list

list1 = [2, 7, 5, 64, 14]
list2 = [12, 14, 95, 3]


# 1 Using for Loop

def getodd(ls):
    lk = []
    for i in ls:
        if i % 2 != 0:
            lk.append(i)
            
    return lk


def geteven(ls):
    lk = []
    for i in ls:
        if i % 2 == 0:
            lk.append(i)
            
    return lk

print("get odd",getodd(list1))
print("get odd 1",getodd(list2))
print("get even",geteven(list1))

print("get even 2",geteven(list2))

# 2 Using While Loop
print('\n')
num = 0 

while num < len(list1):
    if list1[num] % 2 == 0:
        print("even numbers are :",list1[num])
    num+=1

num1 = 0 
while num1 < len(list1):
    if list1[num1] % 2 != 0:
        print("odd numbers are :",list1[num1])
    num1+=1


