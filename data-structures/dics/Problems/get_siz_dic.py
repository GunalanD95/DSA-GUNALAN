# Find the size of a Dictionary in Python
import sys

# 1

dic1 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}

print("size of dic1 is:",sys.getsizeof(dic1) ,"bytes") # get size will return the size with bytes

# 2

dic2 = {"A": 1, "B": 2, "C": 3}
print("Size of dic2: " + str(dic2.__sizeof__()) + " bytes")
