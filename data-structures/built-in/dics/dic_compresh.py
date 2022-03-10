# Python Dictionary Compression

sal_info_keys = ['A','B','C']
sal_info_values = [100,200,300]

sal_vals = {}

for key,value in zip(sal_info_keys,sal_info_values):
    sal_vals[key] = value

print(sal_vals)

#vals = {return value for loop in range of sal_info_keys}
vals = {sal_info_keys[indx]:sal_info_values[indx] for indx in range(0,len(sal_info_keys))}

print("vals",vals)


salary = {'A':100,'B':200,'C':300}

sal_300 = {}
for k in salary:
    if salary[k] > 200:
        sal_300[k] = salary[k]

print(sal_300)


res = {i:k for i , k in salary.items() if k>200}
print(res)