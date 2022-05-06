# Binary Search Tree using recursion


def search(arr,target,s,e):
    middle = s + (e - s) // 2
    
    if s > e:
        return -1

    if target == arr[middle]:
        return middle

    if target < arr[middle]:
        return search(arr,target,s,middle-1)

    if target > arr[middle]:
        return search(arr,target,s,middle+1)


ARR = [1,2,3,4,5,6,7,8,9,10]
(left, right) = (0, len(ARR) - 1)
k = search(ARR,9,left,right)
print(k)