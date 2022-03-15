# Check if element exists in list in Python

check_list = [ 'Russia', 'USA', 'India', 'Australia' ]

# 1 Using in operator

if 'India' in check_list:
    print("India is in list")
else:
    print("India is not in list")

# 2 Navive way
for i in check_list:
    if i == 'India':
        print("India is in list using for loop")
        break

