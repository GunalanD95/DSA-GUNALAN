# Python | Sum of number digits in List

test_list = [12, 67, 98, 34]


#  Using Naive Method 

def find_sum_digits(ls):
    final = []
    for i in ls:
        k = [int(d) for d in str(i)]
        print(i,':',k)
        final.append(sum(k))
    return final


print(find_sum_digits(test_list))


# 2 Using loop + str() 
res = []
for e in test_list:
    sum = 0
    for dj in str(e):
        sum += int(dj)

    res.append(sum)

print ("List Integer Summation : " + str(res))


# 3 Using lambda and list comp
res3 = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))
     
# printing result
print ("List Integer Summation : " + str(res3))

