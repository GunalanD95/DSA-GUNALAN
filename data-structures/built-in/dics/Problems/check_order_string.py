# Python | Check order of character in string using OrderedDict( )
from collections import OrderedDict

def check_order(input,pattern):
    dic = OrderedDict.fromkeys(input)

    ptr = 0
    for k,v in dic.items():
        print(k,v)


if __name__ == '__main__':
    input = 'abcd'
    pattern = 'bacd'
    check_order(input,pattern)