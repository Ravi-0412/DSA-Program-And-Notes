# Syntax: binarytree.bst(height=3, is_perfect=False)
# Parameters: 
# height: It is the height of the tree and its value can be between the range 0-9 (inclusive) 
# is_perfect: If set True a perfect binary is created.
# Returns: Root node of the BST. 


# from binarytree import bst

# # Create a random BST
# # of any height
# root = bst()
# print('BST of any height : \n',root)

# # Create a random BST of
# # given height
# root2 = bst(height = 2)
# print('BST of given height : \n',root2)

# # Create a random perfect
# # BST of given height
# root3 = bst(height = 2,is_perfect = True)
# print('Perfect BST of given height : \n',root3)



# creating a min/max heap:- 

# To generate minheap, we need to set the is_max attribute as False.
# Syntax: binarytree.heap(height=3, is_max=True, is_perfect=False)
# Parameters: 
# height: It is the height of the tree and its value can be between the range 0-9 (inclusive) 
# is_max: If set True generates a max heap else min heap. 
# is_perfect: If set True a perfect binary is created.
# Returns: Root node of the heap.

from binarytree import heap
# Create a random max-heap
root = heap()
print('Max-heap of any height : \n',root)

# Create a random max-heap
# of given height
root2 = heap(height = 2)
print('Max-heap of given height : \n',root2)

# Create a random perfect
# min-heap of given height
root3 = heap(height = 2,is_max = False,is_perfect = True)
print('Perfect min-heap of given height : \n',root3)