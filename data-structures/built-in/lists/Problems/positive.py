# Python program to print positive numbers in a list

test_1  =[12, -7, 5, 64, -14]
test_2 = [12, 14, -95, 3]


# 1 Using Naive Method loop

def ReturnPos(ls):
    lst = []
    for i in ls:
        if i > 0:
            lst.append(i)

    return lst

print(ReturnPos(test_1))
print(ReturnPos(test_2))


# 2 Using While Loop

list1 = [-10, 21, -4, -45, -66, 93]
num = 0
  
# using while loop     
while(num < len(list1)):
      
    # checking condition
    if list1[num] >= 0:
        print(list1[num], end = " ")
      
    # increment num 
    num += 1