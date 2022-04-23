# Binary Tree   

class Node:

    def __init__(self,value) -> None:
        
        self.value = value
        self.left = None
        self.right = None


class Tree():

    def __init__(self) -> None:
        self.root = None

    def insert(self,value):
        if self.root == None:
            newNode = Node(value)
            self.root = newNode
        else:
            self._insert(self.root,value)


    def _insert(self,curNode,value):
        newNode = Node(value)
            
        if value < curNode.value:
            if curNode.left ==  None:
                curNode.left = newNode
            else:
                self._insert(curNode.left,value)

        if value > curNode.value:
            if curNode.right == None:
                curNode.right = newNode
            else:
                self._insert(curNode.right,value)

        if value == curNode.value:
            print("Value already present in the tree ")          

    def preorderTrav(self):
        if self.root == None:
            return
        else:
            self._preorderTrav(self.root)

    def _preorderTrav(self,curNode):
        print(curNode.value)
        if curNode.left:
            self._preorderTrav(curNode.left)
        
        if curNode.right:
            self._preorderTrav(curNode.right)


    def inorderTrav(self):
        if self.root == None:
            return
        else:
            self._inorderTrav(self.root)


    def _inorderTrav(self,curNode):
        if curNode.left:
            self._inorderTrav(curNode.left)
        print(curNode.value)

        if curNode.right:
            self._inorderTrav(curNode.right)


    def postOrder(self):
        if self.root == None:
            return 
        else:
            self._postOrder(self.root)

    def _postOrder(self,curNode):
        if curNode.left:
            self._postOrder(curNode.left)

        if curNode.right:
            self._postOrder(curNode.right)

        print(curNode.value)

# Represents a Binary  Tree

bst = Tree()

# insert 
bst.insert(9)
bst.insert(4)
bst.insert(3)
bst.insert(12)
bst.insert(15)
bst.insert(10)
bst.insert(88)
bst.insert(2)
bst.insert(6)
bst.insert(5)



# traversal 
bst.preorderTrav()
print(" ")
bst.inorderTrav()
print(" ")
bst.postOrder()