import os
import csv

# changing directory to exercise directory
cd = os.getcwd()
os.chdir(cd + "\Exercise Files")
print("os.chdir",os.getcwd())


# reading the file and appending to a dictionary
file = open("TreeOrdersSubset.csv")
csvreader = csv.reader(file)

dics = {}
for data in csvreader:
    key = data[0]

    # checking for duplicate keys

    if key not in dics:
        value = data[1]
        dics[key] = value

    # if duplicate keys, add value 
    else:
        value = data[1]
        prev_count = dics[key]
        dics[key] = int(prev_count) + int(value)

print("dics",dics)