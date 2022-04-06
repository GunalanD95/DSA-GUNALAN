# Stacks and Queues: Basic

#Stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle.
#Queue is a container of objects (a linear collection) that are inserted and removed according to the first-in first-out (FIFO) principle.

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():

    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top != None:
            return self.top.value

    def push(self,value):
        if self.isEmpty():
            newNode = Node(value)
            self.top = newNode
            self.bottom = newNode
            self.top.next = newNode
            self.bottom.next = None
            self.length +=1

        else:
            newNode = Node(value)
            temp = self.top
            newNode.next = temp
            self.top = newNode
            self.length +=1

    def print_stack(self):
        cur = self.top
        ar = []
        while  cur != None:
            ar.append(cur.value)
            cur = cur.next
        return ar

    def pop(self):
        if self.top  == self.bottom:
            self.top = None
            self.bottom = None
            self.length -=1
            return self.top.value
            
        if self.top:
            temp = self.top
            self.top =  temp.next
            self.length -=1
            return temp.value


    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False


    def __str__(self):
        return str(self.print_stack())

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(20)
stack.push(30)
print("bottom",stack.bottom.value)
print("top",stack.top.value)
print("length",stack.length)
print("peek",stack.peek())
print("pop",stack.pop())
print(stack)