# Python program to count Even and Odd numbers in a List

list1 = [2, 7, 5, 64, 14]

list2 = [12, 14, 95, 3]

# 1 Using Loop

def sum_od_even(ls):
    od = 0 
    evn = 0
    for i in ls:
        if i % 2 != 0:
            od += 1

        else:
            evn += 1
    return str({'odd': od, 'even': evn})

print("list1",sum_od_even(list1))
print("list2",sum_od_even(list2))


# 2 Using While Loop

def while_len(ls):
    num = 0 
    od , evn = 0 , 0
    while num < len(ls):
        if ls[num] % 2 != 0:
            od += 1

        else:
            evn += 1

        num +=1

    return str({'odd': od, 'even': evn})


print("list1 while_len",while_len(list1))
print("list2 while_len",while_len(list2))


# 3 Using list comprehension

list_1 = [i for i in list1 if i %2 != 0 ]
print("odd for list1",len(list_1))
print("even for list1",len(list1) - len(list_1))