# Python program to count positive and negative numbers in a list

list1 = [2, -7, 5, -64, -14]

# 1 Using for loop

def countval(ls):
    countp = 0 
    countn = 0
    for i in ls:
        if i >= 0:
            countp += 1
        else:
            countn += 1
    return str({'negative': countn,'positive': countp})

print(countval(list1))


# 2 Using While Loop
leng = 0
pos , neg = 0 , 0

while leng < len(list1):
    if list1[leng] >= 0:
        pos += 1
    else:
        neg += 1
    leng += 1
print(str({'negative': neg,'positive': pos}))