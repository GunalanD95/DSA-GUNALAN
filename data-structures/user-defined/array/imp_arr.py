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
        del self.data[num]
        self.length -= 1
        return self.data


newarr = Array();
newarr.append(1)
newarr.append(2)
newarr.append(3)
newarr.pop()
newarr.delete(0)
newarr.append(4)
print("newarr",newarr.data)