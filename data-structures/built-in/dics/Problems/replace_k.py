#  Python – Replace String by Kth Dictionary value

test_list = ['Gfg', 'is', 'Best']
k = 0
# subs_dict = {'Gfg' : [5, 6, 7], 'is' : [7, 4, 2]}
subs_dict = {'Gfg' : [5, 6, 7], 'Best' : [7, 4, 2]}

# Naive approach

def changestring(ls):
    for i in range(len(ls)):
        for j in subs_dict:
            if ls[i] == j:
                ls[i] = subs_dict[j][k]
    return ls

print(changestring(test_list))


# 2 using list comp:
res = [ele if ele not in subs_dict else subs_dict[ele][k] for ele in test_list]
print("res",res)
