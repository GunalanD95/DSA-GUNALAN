# Python program to swap two elements in a list pos1 = 1, pos2 = 3


# 1 Using assignment operator

a = [23, 65, 19, 90]

def swap_two1(ls):
    ls[0], ls[2] = ls[2], ls[0]
    return ls

print(swap_two1(a))


# 2 Using Tuple Packing

b = [23, 65, 19, 90]
def swap_two2(ls):
    tup = ls[0] , ls[2]
    print(tup)
    ls[2] , ls[0] = tup
    return ls

print(swap_two2(b))


# 3 Using Pop Function

c = [22,3,21,44,5,8]

def swap_two3(ls):
    first_e1 = ls.pop(0)
    third_e1 = ls.pop(2)
    ls[2] , ls[0] = first_e1 , third_e1

    return ls

print(swap_two3(c))



