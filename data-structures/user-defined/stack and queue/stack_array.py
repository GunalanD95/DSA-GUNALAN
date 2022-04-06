from pandas import array


class Stack():

    def __init__(self) -> None:
        self.array  = []


    def push(self,value):
        self.array.append(value)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.array.pop()

    def isEmpty(self):
        if len(self.array) == 0:
            return True
        else:
            return False


    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.array[-1]


    def length(self):
        return len(self.array)


    def __str__(self):
        return str(self.array)


stack = Stack()
stack.push(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(999)
print("length",stack.length())
print(stack)
print("peek",stack.peek())
print("pop",stack.pop())
print(stack)
