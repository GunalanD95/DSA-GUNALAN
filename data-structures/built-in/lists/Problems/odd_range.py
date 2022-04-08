# Python program to print all even and odd numbers in a range

start = 4
end = 15

# 1 Using For Loop
for i in range(start,end+1):
    if i % 2 == 0:
        print("the even nos are:",i)

for i in range(start,end+1):
    if i % 2 != 0:
        print("the odd nos are:",i)

# 2 Using List comprehension

odd = [i for i in range(start,end+1) if i %2 == 0]
even = [i for i in range(start,end+1) if i %2 != 0]
print("odds are",odd)
print("even are",even)