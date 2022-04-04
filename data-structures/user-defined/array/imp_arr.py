# Implemeting a Array


class Array(object):

    def __init__(self):
        self.length = 0
        self.data = {}

    def get_index(self,indx):
        return self.data[indx]

    def append(self,num):
        self.data[self.length] = num
        self.length += 1
        return self.length

    def pop(self):
        del self.data[self.length-1]
        self.length -= 1
        return self.data

    def delete(self,num):
        item = self.data[num]
        self.indexitems(num)
        return item

    def indexitems(self,num):
        for i in range(num,self.length-1):
            print("j",self.data[i])
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        return self.data

    def insert(self,indx,value):
        for i in range(indx,self.length):          
            self.data[i+1] = self.data[i]
        self.data[indx] = value
        self.length += 1

    def print_list(self):
        cur = self.data
        ar = []
        for i in cur:
            ar.append(cur[i])
        return ar


newarr = Array();
newarr.append(1) # 0
newarr.append(2) # 1
newarr.append(3) # 2
newarr.append(4) # 3
newarr.append(99) # 4
print("before del",newarr.data)
newarr.delete(1)
print("newarr aft del",newarr.data)
newarr.insert(1,888)
print("newarr aft insert 888",newarr.data)