# Python – Replace words from Dictionary
# Given String, replace it’s words from lookup dictionary.


test_str = 'geekforgeeks best for geeks'
repl_dict = {'geeks' : 'all CS aspirants'}

# 1 Using split method
p = test_str.split(' ')
def replacestr(p,repl_dict):
    for i in range(len(p)):
        if p[i] in repl_dict:
            p[i] = repl_dict.get(p[i])
    return ' '.join(p)

print(replacestr(p,repl_dict))


# 2 Using List Comprenhension

res = ' '.join(repl_dict.get(i,i) for i in test_str.split())
print(res,"res")