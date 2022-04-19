# Queue for BST Printing
class Node:
    def __init__(self,value) -> None:
        
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        
        self.top = None
        self.bottom = None
        self.length = 0

    def enqueue(self,value):
        if self.top == None:
            newNode = Node(value)
            self.top = newNode
            self.top.next = newNode  
            self.bottom = newNode
            self.bottom.next = None         
            self.length += 1

        else:
            newNode = Node(value)
            self.bottom.next = newNode
            self.bottom = newNode
            self.bottom.next = None
            self.length += 1

    def dequeue(self):
        if self.top == self.bottom:
            self.top = None
            self.length -= 1
            return self.bottom.value

        if self.top:
            temp = self.top
            self.top = temp.next
            self.length -= 1
            return temp.value

    def print_stack(self):
        cur = self.top
        ar = []
        while  cur != None:
            ar.append(cur.value)
            cur = cur.next
        return ar    

    def peek(self):
        if self.top != None:
            return self.top.value



q = Queue() 
q.enqueue(7)
q.enqueue(99)
q.enqueue(990)
q.enqueue(778)
print(q.print_stack())
print(q.dequeue())
print(q.print_stack())
print(q.peek())