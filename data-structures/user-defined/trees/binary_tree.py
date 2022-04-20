# Binary Tree - DATA
from queue import Queue

# Binary Tree Node
class BinaryTreeNode:
    def __init__(self,value) -> None:
        self.value = value
        self.left = None
        self.right = None


    def __str__(self) -> str:
        return str({'left': self.left, 'right': self.right, 'value': self.value})


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

        if value == cur_node.value:
            raise ValueError("Duplicates not allowed")

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
                return is_found
            return False
        else:
            print("No Data in the Tree")


    def _search(self,value,cur_node):
        if value > cur_node.value and cur_node.right:
            return self._search(value,cur_node.right)

        elif value < cur_node.value and cur_node.left:
            return self._search(value,cur_node.left)


        if value == cur_node.value:
            return cur_node


    def remove(self,value):
        if self.root == None:
            return None

        return self._remove(self.root,value)

    def _remove(self,cur_node,value):
        if self.root == None:
            return None
        elif value < cur_node.value:
            cur_node = cur_node.left
            self._remove(cur_node,value)

        elif value > cur_node.value:
            cur_node = cur_node.right
            self._remove(cur_node,value)

        if value == cur_node.value:
            if cur_node.left ==  None and cur_node.right ==  None:
                cur_node =  None
            
            elif cur_node.left ==  None:
                temp = cur_node
                cur_node = cur_node.right
                del temp
                
            elif cur_node.right ==  None:
                temp = cur_node
                cur_node = cur_node.left
                del temp

            else:
                temp =  self.findmin(cur_node.right)
                cur_node.value = temp
                cur_node.right = self._remove(cur_node.right,temp)


    def findmin(self,cur_node):
        current = cur_node
        print("current",current)
        while(current.left is not None):
            current = current.left
        print("min",current)
        return current.value


    def print_tree(self):
        if self.root == None:
            return 
        else:
            self._print_tree(self.root)


    def _print_tree(self,curNode):
        q = []
        q.append(curNode)
        # q.append(None)

        while len(q) != 0:
            curNode = q.pop(0)
            print(curNode.value,end= '   ')
            if curNode.left != None:
                q.append(curNode.left)
                # self._print_tree(curNode.left)
                
            if curNode.right != None:
                q.append(curNode.right)
                # self._print_tree(curNode.right)


                

        
bt = BinarySearchTreeNode()
bt.insert(9)
bt.insert(4)
bt.insert(6)
bt.insert(20)
bt.insert(77)
bt.insert(50)
bt.insert(1)
bt.insert(15)
print(bt.search(15))
print(bt.search(1))
print("remove",bt.remove(20))
print("remove",bt.remove(1))
print("bt",bt.root.value)
print("bt",bt.root.left.value)
print("bt",bt.root.right.value)


bt.print_tree()