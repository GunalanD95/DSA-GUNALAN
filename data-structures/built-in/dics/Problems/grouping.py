# Python – Group Similar items to Dictionary Values List
from collections import defaultdict
  
# initializing list
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
  
# printing original list
print("The original list : " + str(test_list))
  
# using defaultdict for default list 
res = defaultdict(list)

for ele in test_list:
      
    # appending Similar values
    res[ele].append(ele)
  
# printing result 
print("Similar grouped dictionary : " + str(dict(res)))