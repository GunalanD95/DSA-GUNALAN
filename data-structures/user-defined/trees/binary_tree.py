# Binary Tree - DATA


# Binary Tree Node
class BinaryTreeNode:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTreeNode():

    def __init__(self) -> None:
        self.root = None


    def insert(self,value):
        newNode = BinaryTreeNode(value)
        if self.root == None:
            self.root = newNode

        else:
            while True:
                cur =  self.root
                if value < cur.value:
                    if cur.left != None:
                        cur.left = newNode
                    cur = cur.left
                    if cur == None:
                        break
                    
                else:
                    if cur.right != None:
                        cur.right = newNode
                    cur = cur.right
                
                    


    def lookup(self,value):
        pass

    def __str__(self):
        return str(self.root)


bt = BinarySearchTreeNode()
bt.insert(9)
bt.insert(4)
bt.insert(6)
bt.insert(20)
bt.insert(170)
bt.insert(15)
bt.insert(1)
print("bt",bt.root.value)