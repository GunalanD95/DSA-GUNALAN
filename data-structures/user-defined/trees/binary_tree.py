# Binary Tree - DATA
import json

from pandas import json_normalize
from sqlalchemy import true

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
            self._insert(value,self.root)


    def _insert(self,value,cur_node):
        if value < cur_node.value:
            newNode = BinaryTreeNode(value)
            if cur_node.left is None:
                cur_node.left = newNode
            else:
                self._insert(value,cur_node.left)

        elif value > cur_node.value:
            newNode = BinaryTreeNode(value)
            if cur_node.right is None:
                cur_node.right = newNode
            else:
                self._insert(value,cur_node.right)

        else:
            print("Value already in tree!")


    def search(self,value):
        if self.root:
            is_found =  self._search(value,self.root)
            if is_found:
                return True
            return False
        else:
            print("No Data in the Tree")


    def _search(self,value,cur_node):
        if value > cur_node.value and cur_node.right:
            return self._search(value,cur_node.right)

        elif value < cur_node.value and cur_node.left:
            return self._search(value,cur_node.left)


        if value == cur_node.value:
            return True


    def lookup(self,value):
        pass



bt = BinarySearchTreeNode()
bt.insert(9)
bt.insert(4)
bt.insert(6)
bt.insert(20)
bt.insert(170)
bt.insert(15)
print(bt.search(15))
print("bt",bt.root.value)
print("bt",bt.root.left.value)
print("bt",bt.root.right.value)
