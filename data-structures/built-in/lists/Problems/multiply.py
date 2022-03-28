# Python | Multiply all numbers in the list 




a = [1, 2, 3] 
b =[3, 2, 4]

# 1 Naive Method
def TraversalMul(ls):
    res = 1
    for i in ls:
        res = res * i
    return print(res)

TraversalMul(a)
TraversalMul(b)

# 2 Using reduce
from functools import reduce

rs = reduce((lambda x, y: x * y),a)
print("res",rs)
        