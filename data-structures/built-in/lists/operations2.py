# Get Length of the list

len_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("len_list",len(len_list))


# Min and Max method
print("least number",min(len_list))
print("greatest number",max(len_list))


# Count method in the list
count_list = ['guna','lan','guna','dev','guna','lan','guna','lan','guna','lan']
print("count_list",count_list.count('guna')) # count method will return the number of times the element is present in the list


# Check if the element is present in the list
if 'guna' in count_list:
    print("guna is present in the list")
else:
    print("guna is not present in the list")


# Get last element in the list
print("last element is",count_list[-1])
print("last element is",count_list[len(count_list)-1]) # this will return the last element in the list



