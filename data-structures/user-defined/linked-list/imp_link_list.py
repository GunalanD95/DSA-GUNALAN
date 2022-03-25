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

class LinkedList():
    
    def __init__(self,value):

        self.head = {
            'value': value,
            'next': None
        }

        self.tail = self.head                  # tail is the last node in the list 

        self.length = 1

    def append(self,value):
        new_node = {'value': value, 
                             'next': None  }
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1


    def prepend(self,value):
        self.head['value'] = value
        self.length += 1




    def  __str__(self):
        return f"LinkedList: {self.head} ---> {self.tail} ---> {self.length}"



new_LinkedList = LinkedList(10)
new_LinkedList.append(9)
new_LinkedList.append(8)
new_LinkedList.prepend(11)
print("New Linked List: head", new_LinkedList.head)
print("New Linked List: tail", new_LinkedList.tail)
print("New Linked List: length", new_LinkedList.length)