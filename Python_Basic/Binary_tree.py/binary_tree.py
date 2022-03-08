# from binarytree import Node

# # Syntax: binarytree.Node(value, left=None, right=None)
# # Parameters: 
# # value: Contains the data for a node. This value must be number. 
# # left: Conatins the details of left node child. 
# # right: Contains details of the right node child. 

# root = Node(3)
# root.left = Node(6)
# root.right = Node(8)
 
# # Getting binary tree
# print('Binary tree :', root)  # will print the binary tree
# print('Binary tree :', root.inorder)    # will give the inorder traversal of tree
#                                       # in the form of list 
# print('Size of tree :', root.size) # will give no of nodes in the tree
# print('Height of tree :', root.height)
# print('Properties of tree : \n', root.properties)


# building a binary tree from the list:-

# a given list contains the nodes of tree
#  such that the element at index i has its 
# left child at index 2*i+1, the right child 
# at index 2*i+2 and parent at (i – 1)//2. 
# The elements at index j for j>len(list)//2 are leaf nodes.
#  None indicates the absence of a node at that index. 

# from binarytree import build
# nodes =[3, 6, 8, 2, 11, None, 13]
# binary_tree= build(nodes)
# print(binary_tree)
# print(binary_tree.values)   # will return a list containing all the node value of the tree



# building a random binary tree:- 

# Syntax: binarytree.tree(height=3, is_perfect=False)
# Parameters: 
# height: It is the height of the tree and its value can be between the range 0-9 (inclusive) 
# is_perfect: If set True a perfect binary is created.
# Returns: Root node of the binary tree.

from binarytree import tree
root= tree()   # if no parameter passed it will create tree of any height with any value
print(root)

root2 = tree(height = 2)  # will create any tree of height '2'
print("Binary tree of given height :")
print(root2)

root3 = tree(height = 2, is_perfect = True)  # will create a balanced tree of any node value
print("Perfect binary tree of given height :")
print(root3)

