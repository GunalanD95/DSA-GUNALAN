import timeit

ak = [[1,2,3],[4,5,6],[7,8,9]]

# Using Nested Loops
start = timeit.timeit()

sort_arr = []
for i in ak:
    print(i)
    for j in i:
        sort_arr.append(j)

print("sorted array",sort_arr)

end = timeit.timeit()


# using extends method
start1 = timeit.timeit()

ext_arr = []
for l in ak:
    ext_arr.extend(l)

print("extends array:",ext_arr)

end1 = timeit.timeit()

# List Comp
start2 = timeit.timeit()
result = []
[result.extend(el) for el in ak]
print("list comp",result) 

end2 = timeit.timeit()


print(end - start)
print(end1 - start1)
print(end2 - start2)



# 4 Using Merge Sorted Array
def mergesortedarray(ar1,ar2):
    size_1 = len(ar1)
    size_2 = len(ar2)
    
    res = []
    i, j = 0, 0
    
    while i < size_1 and j < size_2:
        if ar1[i] < ar2[j]:
            res.append(ar1[i])
            i += 1
    
        else:
            res.append(ar2[j])
            j += 1
        
    res = res + ar1[i:] + ar2[j:]
    return res


a = [1,2,3,4,5]
b = [6,7,8,9,10]
print(mergesortedarray(a,b))


