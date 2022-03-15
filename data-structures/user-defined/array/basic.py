# Arrays in Python are zero-indexed.

arr = ['orange', 'banana', 'apple', 'mango']
# 4 *  4 =  16 bytes of memory


# Accessing elements in an array
print("get 3rd ele:",arr[2])                             # O(1)


# Adding elements to an array using #APPEND 
arr.append('grapes')                                     # O(1)
print("After appending:",arr)


# Pop Method
arr.pop()                                                # O(1)
print("After pop:",arr)


# Adding elements to an array using #INSERT at index 0
arr.insert(0,'grapes')                                    # O(n)
print("After inserting:",arr)


# Adding elements to an array using #Slicing
arr[1] = 'watermelon'                                     # O(n)
print("After slicing:",arr)