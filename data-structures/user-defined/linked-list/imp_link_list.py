# 10 --> 5 ---> 3 ---> 1 ---> None

linklist = {
    'head': {
        'value': 10,
        'next': {
            'value': 5,
            'next': {
                'value': 3,
                'next': {
                    'value': 1,
                    'next': None
                }
            }
        }
    }
}

# print("Linked List:", linklist)


# Linked List Implementation

# Node Class 
class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return str({'value': self.value, 'next': self.next})


class LinkedList():
    
    def __init__(self,value):

        self.head = {'value': value, 'next': None}
        self.tail = self.head                  # tail is the last node in the list 
        self.length = 1

    def append(self,value):
        new_node = {'value': value, 'next': None}
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1


    def prepend(self,value):
        newNode = {'value': value, 'next': None}
        newNode['next'] = self.head
        self.head = newNode
        self.length += 1


    def print_list(self):
        array = []
        currentNode = self.head
        while  currentNode != None:
            array.append(currentNode['value'])
            currentNode = currentNode['next']
        return array

    def insert(self,indx,value):

        if (indx == 0):
            self.prepend(value)

        elif (indx >= self.length):
            self.append(value)

        else:
            new_Node = {
                'value': value,
                'next' : None
            }
            
            currentIndx = self.getcurrentNode(indx - 1)
        return self.print_list() 
        



    def  __str__(self):
        return f"LinkedList: {self.head} ---> {self.tail} ---> {self.length}"



new_LinkedList = LinkedList(10)
new_LinkedList.append(9)
new_LinkedList.append(8)
new_LinkedList.prepend(11)
print("New Linked List: head", new_LinkedList.head)
print("New Linked List: tail", new_LinkedList.tail)
print("New Linked List: length", new_LinkedList.length)


print("New Linked List:", new_LinkedList.print_list())

print("LinkedList Insert:",new_LinkedList.insert(1,33))