# //Google Question
# //Given an array = [2,5,1,2,3,5,1,2,4]:
# //It should return 2

# //Given an array = [2,1,1,2,3,5,1,2,4]:
# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return undefined


# function firstRecurringCharacter(input) 
# }

# //Bonus... What if we had this:
# // [2,5,5,2,3,5,1,2,4]
# // return 5 because the pairs are before 2,2
a = [2,5,1,2,3,5,1,2,4]
b = [2,1,1,2,3,5,1,2,4]

c =[2,5,5,2,3,5,1,2,4]

def firstrecurchar(inp):
    res = {}
    for i in inp:
        if i in res:
            print(f'{i} is the first recurring element')
            break
        else:
            res[i] = 0
            
firstrecurchar(a)
firstrecurchar(b)    
firstrecurchar(c)    

# the big O is O(n)



# 2 Naive Solution

def FirstRecurringCharacter(input):
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if input[i] == input[j]:
                return input[i]
    return None


print('Naive:',FirstRecurringCharacter(a))
# the big O is O(n^2)