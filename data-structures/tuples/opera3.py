'''
Tuples are immutable sometimes it can be useful while  dealing with large data sets.

'''

import sys
import timeit

my_list = [1,2,3,4,5,6,7,8,9,10]
my_tuple = (1,2,3,4,5,6,7,8,9,10)

print(sys.getsizeof(my_list),"List Size in Bytes")
print(sys.getsizeof(my_tuple),"Tuple Size in Bytes")

print(timeit.timeit("my_list[0]",number=1000000,setup="from __main__ import my_list"))
print(timeit.timeit("my_tuple[0]",number=1000000,setup="from __main__ import my_tuple"))