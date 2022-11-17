# symmetric tree means tree should be mirror of itself
# so we need to check the left side and right side at same time like "identical tree "
# just use the logic of symmetric that we studied in maths
# left== right and right== left 
class Solution:
    def isSymmetric(self, root):
        if root==None or root.left==None and root.right== None: # if none or contain only single node
            return True
        return self.isMirror(root.left,root.right)   # now check for the left and right subtree  
        
    def isMirror(self,root1, root2):
        # if any of them is None then both should be None
        if root1== None or root2== None:
            return root1==root2    
        return (root1.data==root2.data) and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)  # here the diff from "identical trees"

