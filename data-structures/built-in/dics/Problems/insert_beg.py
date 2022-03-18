# Python – Insertion at the beginning in OrderedDict
from collections import OrderedDict

dics = {
        'a': 1,
        'b': 2,
        'c': 3,
       }


# item to be inserted ('c', 3)
k = {'d':4}
k.update(dics)
print("dics",k)


# Using ** operator
a = {
        'a': 1,
        'b': 2,
        'c': 3,
       }

b = {'d':5}
res = {**b, **a}
print("res",res)