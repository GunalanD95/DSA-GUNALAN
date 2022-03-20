# Python | Find common elements in three sorted arrays by dictionary intersection

a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]


def find_com(ar1,ar2,ar3):
    dic = {}
    for i in ar1:
        dic[i] = 1
    for i in ar2:
        if i in dic:
            dic[i] += 1
    for i in ar3:
        if i in dic:
            dic[i] += 1
    return [k for k,v in dic.items() if v == 3]
    


print(find_com(a,b,c))   