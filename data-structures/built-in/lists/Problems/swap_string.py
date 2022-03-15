# Python – Swap elements in String list

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']

# Using Replace method  

res = [i.replace('best','worst').replace('is','for') for i in test_list] # replace all 'best' with 'worst'
print("res :",res)


# Using join() + replace() + split()

res_2 = ' '.join(test_list).replace('best','worst').replace('is','for').split()
print("res_2 :",res_2)