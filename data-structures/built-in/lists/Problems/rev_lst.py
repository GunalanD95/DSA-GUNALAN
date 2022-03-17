# Reversing a List in Python

rv = [10, 11, 12, 13, 14, 15]


# 1 Using reversed
def rev1(ls):
    return [i for i in reversed(ls)]

print("rev1",rev1(rv))

# 2 Using reverse
def rev2(ls):
    ls.reverse()
    return ls

print("rev2",rev2(rv))

# 3 Using the slicing technique

def rev3(ls):
    kv = ls[::-1]
    return kv

print("rev3",rev3(rv))
