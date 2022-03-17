# Cloning a list

countries = ['USA', 'Canada', 'Mexico', 'France', 'Germany']

# 1 Using copy

def clone1(ls):
    newls = ls.copy()
    return newls

print("clone1:",clone1(countries))


# 2  Using slicing technique  - fast

def clone2(ls):
    newls = ls[:]
    return newls

print("clone2:",clone2(countries))


# 3 Using extend method

def clone3(ls):
    newls = []
    newls.extend(ls)
    return newls

print("clone3:",clone3(countries))

# 4 Using the list() method 


def clone4(li1):
    li_copy = list(li1)
    return li_copy

print("clone4:",clone4(countries))