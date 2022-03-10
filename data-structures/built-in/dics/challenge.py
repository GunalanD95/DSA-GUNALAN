import os
import csv

cd = os.getcwd()
print("current directory",cd)

# changing directory to exercise directory
os.chdir(cd + "\Exercise Files")
print("os.chdir",os.getcwd())

# list all files in the directorys
print("os.listdir",os.listdir())


# reading the file and appending to a dictionary
file = open("TreeOrdersSubset.csv")
csvreader = csv.reader(file)

dics = {}
for data in csvreader:
    key = data[0]
    value = data[1]
    dics.update({key:value})

print("dics",dics)