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
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        return self.data


newarr = Array();
newarr.append(1) # 0
newarr.append(2) # 1
newarr.append(3) # 2
newarr.append(4) # 3
print("newarr",newarr.data)
newarr.delete(0)
print("newarr",newarr.data)