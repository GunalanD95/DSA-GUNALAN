# Python | Merging two Dictionaries


# 1 using update method we can merge two dictionaries
a = {'A': 1, 'B': 2, 'C': 3}
b = {'B': 4, 'C': 5, 'D': 6}


def Merge1(a,b):
    return(a.update(b))

print(Merge1(a,b)) # this will return None
print(a) # this will return {'A': 1, 'B': 4, 'C': 5, 'D': 6}



# 2 Using ** in Python 
c = {'A': 22, 'B': 222, 'C': 2222}
d = {'B': 33, 'C': 335, 'D': 336}


def Merge2(a,b):
    res = {**a,**b}
    return(res)

print(Merge2(c,d)) # this will return {'A': 22, 'B': 33, 'C': 335, 'D': 336}




# 3 Using  “|” operator  from Python 3.9
d = {'USA': 1, 'UK': 2, 'India': 3}
e = {'CHINA': 4, 'RUSSIA': 5, 'JAPAN': 6}

def Merge3(c,d):
    rs = c | d
    return(rs)

print(Merge3(d,e))




