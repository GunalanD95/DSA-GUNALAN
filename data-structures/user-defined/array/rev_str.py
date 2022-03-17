# Create a function that reverses a string.
# Hi there! should be 
# !ereht si eH


from audioop import reverse


def reverse_str(string):
    if type(string) == str:
        arr = list(string)
        rv = arr[::-1]
        k = ''.join(rv)
        return k
    else:
        print("Please enter a valid input")

print(reverse_str('gunalan'))
reverse_str(1)

# Method 2

def rev_str(strng):
    if type(strng) == str:
        bck = ''
        for i in strng:
            bck = i + bck
        return bck
    else:
        print("Please enter a valid input")

print(rev_str('gunalan'))


# Method 3 

def rev2(string):
    return string[::-1]

print(rev2('gunalan'))