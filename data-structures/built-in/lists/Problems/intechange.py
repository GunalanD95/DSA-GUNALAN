# Python program to interchange first and last elements in a list

# 1 Using list slicing and assignment operator

ls = [1,2,3,4,5,6,7,8,9,10]

def interchangels(list):
    last_e = list[-1]
    first_e = list[0]
    list[0] = last_e
    list[-1] = first_e
    return list

interchangels(ls)
print("1 :",ls)


# 2 Swapping first and last elements in a list

ls_1 = [2,4,6,8,10]

def swapp(ls):
    ls[0], ls[-1] = ls[-1], ls[0]
    return ls

print("2 :",swapp(ls_1))


# 3 Using Tuple Variable

ls_2 = [5,10,15,20,25]

def swap_tuple(ls):
    tup = (ls[0], ls[-1])
    ls[-1], ls[0]  = tup # unpacking using tuples
    return ls

print("3 :",swap_tuple(ls_2))


# 4 Using * operand. 

ls_3 = ["A", "B", "C", "D", "E"]

def swap_oper(ls):
    start , *middle , end = ls # * will capture all unallocated 
    ls[0] = end
    ls[-1] = start
    return ls

print("4 :",swap_oper(ls_3))


# Using Pop

pop_list = ['INDIA', 'USA', 'UK', 'AUSTRALIA', 'SOUTH AFRICA']

def swap_pop(ls):
    last_e = ls.pop(-1)
    first_e = ls.pop(0)
    ls.insert(0,last_e)
    ls.append(first_e)
    return ls

print("5 :",swap_pop(pop_list))