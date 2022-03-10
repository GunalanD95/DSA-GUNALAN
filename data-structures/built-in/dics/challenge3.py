import os 
import csv

cd = os.getcwd()
chng_dir = cd + '\Exercise Files'
os.chdir(chng_dir)

treeOrder10 = {}

with open('treeorderssubsetnodupes.csv') as file:
    reader = csv.reader(file)

    for data in reader:
        key = data[0]
        

        if key not in treeOrder10:
            value  = data[1]
            treeOrder10[key] = int(value)

        else:
            value  = data[1]
            prv_count = treeOrder10[key]
            treeOrder10[key] = int(prv_count) + int(value)


treeOrder = {k:v for k ,v in treeOrder10.items() if v > 10}

print("treeOrder",treeOrder)