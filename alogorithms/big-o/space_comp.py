# Space Complexity

'''
    Space complexity is a parallel concept to time complexity. 
    If we need to create an array of size n,
    this will require O(n) space. If we create a two-dimensional array of size n*n, 
    this will require O(n2) space.
'''

def fooo(n):
    for i in range(n):
        print("I WILL PRINT")


fooo(10)

# The Big - O of this function for the above function
# Time Complexity - O(n)
# Space Complexity - O(1)

def arrayNtime(n):
    arr = []
    for i in range(n):
        arr.append('hi')
    return arr

print(arrayNtime(10))

# The Big - O of this function for the above function
# Time Complexity - O(n)
# Space Complexity - O(n) - This is because we are creating a new array of size n
