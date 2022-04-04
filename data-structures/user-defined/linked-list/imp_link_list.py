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
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


    def __str__(self):
        return str({'value': self.data, 'next': self.next})


class LinkedList:
    
    def __init__(self,value):

        self.head = {'value': value, 'next': None}
        # self.head = Node(value)
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

    # A -> B -> C -> D -> E -> None
    # E -> D -> C -> B -> A -> None
    def reverse(self):
        if self.head['next'] == None:
            return self.head

        curNode = self.head                            # create a temp node to traverse the list
        self.tail = self.head                          # set the tail to the head
        prev = None                                    # create a temp node to store the previous node
        nxt = None                                     # create a temp node to store the next node
        while curNode:                                 # while the current node is not None
            nxt = curNode['next']                      # store the next node 
            curNode['next']= prev                      # reverse the link
            prev = curNode                             # store the current node to the previous node
            curNode = nxt                              # move the current node to the next node

        self.head['next'] = None                       # set the head to the previous node
        self.head = prev
        return self.print_list()

    def insert(self,indx,value):
        headNode = self.head
        if (indx == 0):
            self.prepend(value)

        elif (indx >= self.length):
            self.append(value)

        else:
            while (indx != 0):          
                indx -= 1
    
                if (indx == 1):
                    newNode = {'value': value, 'next': None}
                    newNode['next'] = headNode['next']
                    headNode['next'] = newNode
                    break
                
                headNode = headNode['next']
                if headNode == None:
                    break           
            if indx != 1:
                print("position out of range")       
        return self.head
            
    def ins_pos(self,pos,value):
        newNode = {'value': value, 'next': None}
        temp = self.head
        for i in range(pos-1):
            print("st",temp)
            temp = temp['next']
            print("end",temp)

        newNode['next'] = temp['next']
        temp['next'] = newNode
        self.length += 1

    def remove(self,indx):
        temp = self.head
        if (indx == 0):
            new_head = temp['next']
            temp = new_head
            self.length -= 1
        else:
            for i in range(indx-1):                           # get the leader node of the index
                temp = temp['next']
            leader = temp
            unwantedNoder = leader['next']
            new_follower = unwantedNoder['next']
            leader['next'] = new_follower
            self.length -= 1
            return unwantedNoder['value']


    def  __str__(self):
        return f"LinkedList: {self.head} ---> {self.tail} ---> {self.length}"



new_LinkedList = LinkedList(10)
new_LinkedList.append(9)
new_LinkedList.append(8)
new_LinkedList.append(55)
new_LinkedList.prepend(11)

print("New Linked List: length", new_LinkedList.length)

print("New Linked List:", new_LinkedList.print_list())

# print("LinkedList Insert:",new_LinkedList.insert(2,33))
print("LinkedList Insert:",new_LinkedList.insert(4,99))


print("LinkedList Insert at index 2:",new_LinkedList.ins_pos(2,33))
print("New Linked List:", new_LinkedList.print_list())
print("LinkedList Remove at index 3:",new_LinkedList.remove(3))
print("LinkedList Remove at index 5:",new_LinkedList.remove(5))
print("New Linked List:", new_LinkedList.print_list())


print("New Linked List: head", new_LinkedList.head)
print("New Linked List: tail", new_LinkedList.tail)

print("reverse a list",new_LinkedList.reverse())