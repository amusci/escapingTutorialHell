'''

Binary Tree:

Tree has one root.
0-2 Child nodes, where the nodes can also be null.
A leaf is a node with no children.

Binary Search Tree:

These contain a specific ordering property.

On any subtree, the left nodes are less than the root node, which is less than all the right nodes.

This ordering property can allow finding a node very fast.


Walking Through Binary Trees:

There are three ways to walk through a binary tree.

Inorder:
Visit left nodes, then root, then right nodes.

Preorder:
Visit the root first, then visit it's left nodes then it's right nodes.


Postorder:
Visit left nodes, then right nodes, then root.

Most used is Inorder, as it allows trees to be printed in order.



'''


class TreeNode:

    def __init__(self, value):
        # constructor

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:  # if the value you want to insert is less than the value of the current node (we go left)
            if self.left is None:  # if theres no value in the left node
                self.left = TreeNode(value)  # add the value to the empty left node
            else:
                self.left.insert(value)  # if the node already has a value, recursively call insert on the left node

        else:  # if value > the value of the node, it must be placed on the right
            if self.right is None:  # if the value of the is none
                self.right = TreeNode(value)  # add the value to the empty right node

            else:
                self.right.insert(value)  # if the node already has a value, recursively call insert on the right node

    def inorder_traversal(self):
        if self.left:  # if left node exists
            self.left.inorder_traversal()  # call inorder on that node, repeat until you reach most left node
        print(self.value)  # prints value of parent node
        if self.right:  # if right node exists
            self.right.inorder_traversal()  # recursively call

            #  note that we do NOT do another print, as we will print the left before the right, allowing it to be in
            #  the correct order


tree = TreeNode(10)
tree.insert(4)
tree.insert(8)
tree.insert(11)
tree.insert(12)
tree.insert(55)
tree.insert(16)
tree.insert(77)

# print(tree.right.right.right.left.value)  # this will be 16
tree.inorder_traversal()  # this will be 4, 8, 10, 11, 12, 16, 55, 77

# https://www.cs.usfca.edu/~galles/visualization/BST.html