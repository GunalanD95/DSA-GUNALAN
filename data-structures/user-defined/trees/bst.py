# BST 


class Node:

    def __init__(self,value) -> None:
        self.value = value
        self.left  = None
        self.right = None


class BST:

    def __init__(self) -> None:
        self.root = None

    
    def insert(self,value):
        if self.root == None:
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
        


bs = BST()
bs.insert(10)
print(bs.insert(11))
bs.insert(5)

print("root",bs.root.value)
print("left",bs.root.left.value)
print("right",bs.root.right.value)