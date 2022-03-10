# converting two lists into a dictionary

sal_info_keys = ['A','B','C']
sal_info_values = [100,200,300]

sal_info ={}

index = 0

for key in sal_info_keys:
    value = sal_info_values[index]
    sal_info[key] = value
    index = index + 1

print("sal_info:",sal_info)