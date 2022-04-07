class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class MyQueue:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, x: int) -> None:
        newNode = Node(x)
        if self.empty():
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

    def pop(self) -> int:
        if self.top  == self.bottom:
            self.top == None
            self.bottom = None
            self.length -=1
            return self.top.value
            
        else:
            temp = self.top
            self.top =  temp.next
            self.length -=1
            return temp.value
        

    def peek(self) -> int:
        if self.top != None:
            return self.top.value
        

    def empty(self) -> bool:
        if self.length  == 0:
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


myQueue = MyQueue()
myQueue.push(1)
print(myQueue.print_stack())
# myQueue.push(2)
print(myQueue.print_stack())
print(myQueue.peek())
print(myQueue.pop())
myQueue.empty(); 