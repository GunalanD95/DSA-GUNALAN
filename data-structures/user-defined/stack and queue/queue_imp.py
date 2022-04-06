# Implementation of a queue 

class Node:
    def __init__(self,value):
        self.value = value
        self.next = next

class Queue():

    def __init__(self) -> None:
        self.top =  None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top != None:
            return self.top.value



    def enqueue(self,value):
        newNode = Node(value)
        if self.isEmpty():
            self.top = newNode
            self.top.next = newNode
            self.bottom = newNode
            self.bottom.next = None
            self.length += 1

        else:
            self.bottom.next = newNode
            self.bottom = newNode
            self.bottom.next = None
            self.length += 1


    def dequeue(self):
        if self.top  == self.bottom:
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

    def print_stack(self):
        cur = self.top
        ar = []
        while  cur != None:
            ar.append(cur.value)
            cur = cur.next
        return ar    


sr = Queue()
sr.enqueue(99)
sr.enqueue(1)
sr.enqueue(2)
sr.enqueue(3)
sr.enqueue(4)
print("queue",sr.print_stack())
print("peek",sr.peek())
print("dequeue",sr.dequeue())
print("queue",sr.print_stack())
    