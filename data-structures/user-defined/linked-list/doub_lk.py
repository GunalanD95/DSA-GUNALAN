# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str({'value': self.data, 'next': self.next, 'prev': self.prev})

class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length += 1

        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.length += 1

    def print_list(self):
        arr = []
        temp = self.head
        print(temp)
        while temp is not None:
            arr.append(temp.data)
            temp = temp.next
        return arr
         

    def prepend(self,value):
        newNode = Node(value)
        temp = self.head
        newNode.next = temp
        self.head = newNode
        self.length += 1


dl = DoublyLinkedList()
dl.append(1)
dl.append(2)
dl.append(3)
dl.prepend(99)
print("head",dl.head)
print("tail",dl.tail)
print("print_list",dl.print_list())
                        