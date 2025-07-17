#let us start with binary trees.
#trees have nodes and the topmost node is the root.
#nodes have children(sub-nodes)
#no cycles
 #defining a tree node

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None #left child
        self.right = None

root = Node(10)
root.left = Node(5)
root.right = Node(15)


#tree traversal: in-order, pre-order, post-order
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)