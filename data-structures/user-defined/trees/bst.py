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
        print("preorder data",curNode.value)
        if curNode.left:
            self._preorderTraversal(curNode.left)
        
        if curNode.right:
            self._preorderTraversal(curNode.right)

    def inorderTraversal(self):
        if self.isEmpty():
            return str("No Data is there")

        else:
            self._inorderTraversal(self.root)

    def _inorderTraversal(self,curNode):
        if curNode.left:
            self._inorderTraversal(curNode.left)

        print("inorder data",curNode.value)
        if curNode.right:
            self._inorderTraversal(curNode.right)

    def postorderTraversal(self):
        if self.isEmpty():
            return str("No Data is there")

        else:
            self._postorderTraversal(self.root)

    def _postorderTraversal(self,curNode):
        if curNode.left:
            self._postorderTraversal(curNode.left)

        
        if curNode.right:
            self._postorderTraversal(curNode.right)

        print("posorder data",curNode.value)


    def height(self):
        '''
        height of a node = number of edges in the longest path from root to the leaf node

        height of a tree = height of the root

        height of the tree with 1 node = 0
        '''
        if self.isEmpty():
            return None
        

        return self._height(self.root)



    def _height(self,curnode):
        if curnode is None:
            return -1

        left_height = self._height(curnode.left)
        right_height = self._height(curnode.right)

        return 1 + max(left_height,right_height)
        

    def print_tree(self):
        if self.isEmpty():
            return None
        

        return self._print_tree(self.root,0,self.height())       

    def _print_tree(self,root,space,height):
        # Base case
        if root is None:
            return
 
        # increase distance between levels
        space += height
 
        # print right child first
        self._print_tree(root.right, space, height)
        print()
 
        # print the current node after padding with spaces
        for i in range(height, space):
            print(' ', end='')
 
        print(root.value, end='')
 
        # print left child
        print()
        self._print_tree(root.left, space, height)
        

        



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
bs.insert(1)

# Lookup
bs.search(77)
bs.search(5)


# Traversal 

print(bs.preorderTraversal())

print(bs.inorderTraversal())

print(bs.postorderTraversal())



# height
print("height",bs.height())


# print a tree

print("print",bs.print_tree())