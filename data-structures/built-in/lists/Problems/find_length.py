# Python | Ways to find length of list
import time


list_d = [1,2,3,4,5,6,7,8,9,10]

# 1 Using len()s
len1 = len(list_d)
print("len list_d: :",len1)


# 2 Navive way
count = 0 
for i in list_d:
    count+=1
print("count list_d: :",count)


# 3 Using length_hint()

from operator import length_hint
len_2 = length_hint(list_d)
print("length_hint list_d: :",len_2)


# Performance Analysis – Naive vs len() vs length_hint()

# Initializing list
test_list = list(range(1,10000000))
# Printing test_list
 
# Finding length of list
# using loop
# Initializing counter
start_time_naive = time.time()
counter = 0
for i in test_list:
     
    # incrementing counter
    counter = counter + 1
end_time_naive = str(time.time() - start_time_naive)
 
# Finding length of list
# using len()
start_time_len = time.time()
list_len = len(test_list)
end_time_len = str(time.time() - start_time_len)
 
# Finding length of list
# using length_hint()
start_time_hint = time.time()
list_len_hint = length_hint(test_list)
end_time_hint = str(time.time() - start_time_hint)
 
# Printing Times of each
print ("Time taken using naive method is : " + end_time_naive)
print ("Time taken using len() is : " + end_time_len)
print ("Time taken using length_hint() is : " + end_time_hint)