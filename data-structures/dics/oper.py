# dictionary with salarys as  name and amount as value

salary = { "A": "100", "B": "200", "C": "300", "D": "400", "E": "500" }


# checking if the key is in the dictionary using if else
if 'G' not in salary:
    salary['G'] = "600"
else:
    print(f'G is in the dictionary')

print("salary",salary)