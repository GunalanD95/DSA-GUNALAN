# Python Slicing

countries = ['USA', 'Germany', 'India', 'Russia', 'China', 'South Korea', 'Japan']

# Slicing a list using [start:end:step]

print(countries[0:3]) # 0 will be the start and 3-1=2 will be the end
print(countries[:3]) # start will be 0 as default

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Slicing a list using [start:end:step]
print(numbers[0:len(numbers):2])  # start at 0 and end at the end of the list and step by 2



#Slicing a list in reverse order
print(countries[::-1])


# Assigning values using slice
countries[0] = 'Russia'
print(countries)