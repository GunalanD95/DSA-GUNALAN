class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def isEmpty(self):
        if self.head:
            return True

    def prepend(self,value):
        if self.isEmpty():
            return None
        else:
            newNode = Node(value)
            temp = self.head
            self.head = newNode
            self.head.next = temp
            self.length +=1
            