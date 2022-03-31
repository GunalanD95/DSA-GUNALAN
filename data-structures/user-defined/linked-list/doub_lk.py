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


    def insert(self,indx,value):
        if indx == 0:
            self.prepend(value)
        elif indx >= self.length:
            self.append(value)
        else:
            newNode = Node(value)                  # create a new node
            temp = self.head                       # create a temp node
            for i in range(indx-1):                # loop through the list to reach the leader index
                temp = temp.next                   # move the temp node to the next node
                # print("temp",temp)                
            newNode.next = temp.next               # set the new node's next to the leader's next
            temp.next = newNode                    # set the leader's next to the new node
            newNode.prev = temp                    # set the new node's prev to the leader
            self.length += 1                       # increment the length of the list


    def remove(self,indx):
        if indx == 0:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            
        elif indx == self.length - 1:
            temp = self.tail
            self.tail = temp.prev
            self.tail.next = None

        elif indx > self.length -1:
            print("Invalid index")

        else:
            leader = self.head                    # create a leader node
            for i in range(indx-1):
                leader = leader.next              # move the leader node to the next node

            unwanted = leader.next                # create a unwanted node
            leader.next = unwanted.next           # set the leader's next to the unwanted node tail
            unwanted.next.prev = leader           # set the unwanted node's next's prev to the leader
            unwanted.next = None                   # set the unwanted node's next to None
            unwanted.prev = None                   # set the unwanted node's prev to None
            self.length -= 1                       # decrement the length of the list
            
            



dl = DoublyLinkedList()
dl.append(1)
dl.append(2)
dl.append(3)
dl.append(4)
dl.prepend(99)
dl.prepend(55)
# print("head",dl.head)
# print("tail",dl.tail)
# print("print_list",dl.print_list())
# dl.insert(3,105)
print("print_list",dl.print_list())
# dl.remove(0)
# dl.remove(6)
dl.remove(2)
print("print_list",dl.print_list())
                        