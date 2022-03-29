# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str({'value': self.data, 'next': self.next , 'prev': self.prev})

class DoublyLinkedList:

    def __init__(self,data) -> None:
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self,data):
        newNode = Node(data)
        temp = self.tail
        self.tail = newNode
        self.tail.prev = temp.data
        self.head.next = newNode.data
        self.length += 1


    def prepend(self,data):
        newNode = Node(data)
        temp = self.head
        self.head = newNode
        self.head.next = temp.data
        self.length += 1

    def getLength(self):
        return print(self.length)

lk = DoublyLinkedList(4)
lk.append(5)
lk.prepend(10)
print(lk.tail)
print(lk.head) 