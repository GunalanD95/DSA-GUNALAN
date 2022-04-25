class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


class LinkedList():

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def isEmpty(self):
        if self.head == None:
            return True

    def length(self):
        return self.length

    def append(self,value):
        newNode = Node(value)

        if self.isEmpty():
            self.head = newNode
            return

        cur = self.head
        while cur.next !=None:
            cur = cur.next
        cur.next = newNode
        self.length +=1

    def prepend(self,value):
        newNode = Node(value)
        temp = self.head
        newNode.next = temp
        self.head = newNode
        self.length +=1

        



    def print_list(self):
        array = []
        currentNode = self.head
        while  currentNode != None:
            array.append(currentNode.value)
            currentNode = currentNode.next
        return array

lk = LinkedList()

# Prepend and Append



print(" ")
lk.append(20)
lk.append(25)
lk.append(30)
print(" ")
lk.prepend(5)
lk.prepend(10)
lk.prepend(15)



print("head",lk.head.next)

print(lk.print_list())

            