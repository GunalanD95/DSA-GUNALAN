# BST 


class Node:

    def __init__(self,value) -> None:
        self.value = value
        self.left  = None
        self.right = None


class BST:

    def __init__(self) -> None:
        self.root = None

    def isEmpty(self):
        if self.root == None:
            return True
    
    def insert(self,value):
        if self.isEmpty():
            newNode = Node(value)
            self.root = newNode
        else:
            self._insert(value,self.root)

    
    def _insert(self,value,curNode):
        if curNode.value > value:
            if curNode.left == None:
                newNode = Node(value)
                curNode.left = newNode
            else:
                self._insert(value,curNode.left)

        if curNode.value < value:
            if curNode.right == None:
                newNode = Node(value)
                curNode.right = newNode
            else:
                self._insert(value,curNode.right)


        if curNode.value == value:
            print("BST doesn't allow duplicate nodes")
        



    def search(self,value):
        if self.isEmpty():
            return None

        else:
            self._search(value,self.root)

    def _search(self,value,curNode):
        if value == curNode.value:
            print("found it",curNode.value)

        if value < curNode.value and curNode.left:
            self._search(value,curNode.left)

        if value > curNode.value:
            if curNode.right:
                self._search(value,curNode.right)



    def preorderTraversal(self):
        if self.isEmpty():
            return str("No Data is there")

        else:
            self._preorderTraversal(self.root)

    
    def _preorderTraversal(self,curNode):
        print("data",curNode.value)
        if curNode.left:
            self._preorderTraversal(curNode.left)
        
        if curNode.right:
            self._preorderTraversal(curNode.right)

    def inorderTraversal():
        pass

    def postorderTraversal():
        pass




bs = BST()

# Insertion
bs.insert(50)
bs.insert(25)
bs.insert(75)
bs.insert(10)
bs.insert(35)
bs.insert(5)
bs.insert(13)
bs.insert(30)
bs.insert(42)

# Lookup
bs.search(77)
bs.search(5)


# Traversal 

print(bs.preorderTraversal())