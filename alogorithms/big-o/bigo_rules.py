# There are 4 rules for big-o notation:
# Rule 1 : Worst Case
# Rule 2 : Remove Constants
# Rule 3 : Different terms for inputs
# Rule 4 : Drop Non Dominants


## Rule 1 Example:
# Worst Case: O(n) is when the loop runs for n times like 'n' is the length of the list (being last element)
from cmath import log


dum_ls = ['USA', 'India', 'UK', 'Canada', 'Australia','Guna', 'Germany', 'France', 'Italy', 'Spain']

def Findguna(list):
    for i in list:
        print("running for loop") # see this line is running for loop its run for loop for each element in list even after finding guna
        if i == 'Guna':
            print("Found Guna")
            break # use a break to avoid running for loop for all elements in list

# checking the time to find Guna in a list
Findguna(dum_ls)


## Rule 2 Example:
def printfirstitemthenfirsthalfsayhi100times(inp):
    print(inp[0]) # print first item

    middle_indx = len(inp) // 2
    indx = 0

    while indx < middle_indx:
        print(inp[indx]) # print first half of list
        indx += 1

    for i in range(100):
        print("hi") # print hi 100 times


a = [1,2,3,4,5,6,7,8,9,10]
printfirstitemthenfirsthalfsayhi100times(a)

# Big O notation for the above function is O(1 + n/2 + 100) = O(n)


# Rule 2 says Drop Constants
def compresstwoboxtw(boxes):
    for i in boxes:
        print(i)

    for j in boxes:
        print(j)

compresstwoboxtw([1,2,3,4,5,6,7,8,9,10])
# Big O notation for the above function is O(n + n) = O(2n) = O(n) as per Rule 2



## Rule 3 :  Different terms for an input
def loopboxed(boxes1,boxes2):
    for i in boxes1:
        print(i)

    for j in boxes2:
        print(j)

k = ['A','L','Q','Y','M','D','C','R']
j = ['B','C','A','M','N','D']
loopboxed(k,j)

# The Big-0 for the above will be O( n + n )



# Rule : 4 Drop Non Dominants
def printallpairs(nums):
    for k in nums:  # O(n)
        print("nums",k)
    

    for f in nums: # O(n)
        for s in nums: # O(n)
            print("And their Sum is :",f+s) 

nos = [1,2,3,4,5]
printallpairs(nos)


# The Big-0 for the above will be O(n + n * n) = O(n^2)

# As per Rule 4 we will drop Non Dominants
# So her n is non dominant , we will drop the n and  O(n*n) = O(n^2)