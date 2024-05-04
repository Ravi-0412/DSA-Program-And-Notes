# Reccursive -> Maximum Reccursion Depth Exceeded

# 1) ceiling:

class Solution:
    def __init__(self):
        self.ceil = None
    def getSuccessor(self, root, val):
        if root == None:
            return self.ceil
        if root.val == val:
            return self.getSuccessor(root.right,val)
        if root.val < val:
            return self.getSuccessor(root.right,val)
        if root.val > val:
            self.ceil = root
            return self.getSuccessor(root.left,val)

# Iterative

class Solution:
    def getSuccessor(self, root, val):
        ceil = -1
        while root:
            if root.val == val:
                # root = root.right  # if asked to get strictly greater
                return val
            elif root.val < val:
                root = root.right
            else:
                ceil = root.val
                root = root.left

        return ceil

# 2) Floor
# Submitted on gfg

class Solution:
    def floor(self, root, x):
        floor = -1
        while root:
            if root.data == x:
                # root = root.left    # if asked to get strictly smaller
                return x
            elif root.data < x:
                floor  = root.data  # No meed to take maximum because last node that we will get in this case will be our ans due to BST
                root = root.right
            else:
                root = root.left

        return floor
    
# Other way
# Just write the iterative inorder and get the ans.