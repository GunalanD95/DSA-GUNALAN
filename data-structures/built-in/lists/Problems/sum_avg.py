# Find sum and average of List in Python

lst = [4, 5, 1, 2, 9, 7, 10, 8]


# 1 Naive Method

def sum_avg(ls):
    sums = sum(ls)
    avg = sums / len(ls)
    res = f'avg is {avg} and sum is {sums} for the list {ls}'
    return res

print(sum_avg(lst))


# 2 Another Naive Method 

count = 0 
sum = 0
for i in lst:
    sum += i
    count += 1
avg = sum / count
print(f'avg is {avg} and sum is {sum} for the list {lst}')