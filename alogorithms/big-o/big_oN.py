# write a function to find something inside a list
import time

ls = ['Guna']

dum_ls = ['USA', 'India', 'UK', 'Canada', 'Australia', 'Germany', 'France', 'Italy', 'Spain', 'Guna']

list_1000000 = list(range(1, 1000000))
list_1000000.append('Guna')  

def Findguna(list):
    start = time.time()
    for i in list:
        if i == 'Guna':
            print("Found Guna")
    end =  time.time()
    tot = end -  start 
    print(f'Time taken for this fun is {tot} seconds')

# checking the time to find Guna in a list

Findguna(ls)

Findguna(dum_ls)

# will load a list of 1000000 elements of a list

Findguna(list_1000000) # now if u see here it will take a lot of time to find Guna