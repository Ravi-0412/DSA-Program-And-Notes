# logic: Brute force just checked the left and right height for every node
# time: 0(n^2)
# space: O(n): if skew tree recursion depth will go O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root== None:
            return True
        l= self.maxDepth(root.left)
        r= self.maxDepth(root.right)
        if  abs((l-r)) > 1:
            return False
        # if root is balanced then check for its child
        left= self.isBalanced(root.left)
        right= self.isBalanced(root.right)
        if left== False or right== False:
            return False
        return True
    
    def maxDepth(self, root):
        if root== None:
            return 0
        l= self.maxDepth(root.left)
        r= self.maxDepth(root.right)
        return 1+ max(l,r)

# concise way of writing above code
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root== None:
            return True
        l= self.maxDepth(root.left)
        r= self.maxDepth(root.right)
        return abs((l-r)) <=1 and  self.isBalanced(root.left) and  self.isBalanced(root.right)  # if all three follows then only it is balanced
    
    def maxDepth(self, root):
        if root== None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# method 2: O(n)
# just the height logic only , instead of  returning bolleans we are returning in integer so that if subtree is unbalanced then it automatically make its parent unbalanced 
# and also we have to return the height which will be a positive number so replaced the boolean return value with integer return to handle all these cases

# bottom up approach , ans from bottom is getting updated to uper level.. Can say DP only
# here we only need left and right tree ans to make a decision for current root that's why not storing ans in any list 
# '-1' means tree is unbalanced 

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # just apply the logic odf maxDepth
        def check(root):  # totally height logic only just wrotw few conditioj in between that's it
            if root== None:
                return 0
            left= check(root.left)
            if left== -1:
                return -1
            right= check(root.right)
            if right== -1:
                return -1
            if abs((left-right))> 1:  # any if one return -1 then it will automatically become >1 adding the node height "+1"
                return -1
            # if balanced then return the max height 
            return 1+ max(left,right)
            
        return check(root)!= -1  # if not equal to '-1' means balanced

# concise way of writing above code

# '-1' means tree is unbalanced 
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # just apply the logic odf maxDepth
        def check(root):
            if root== None:
                return 0
            left= check(root.left)
            right= check(root.right)
            if left== -1 or right== -1 or abs((left-right))> 1: # if any one of them is unbalance
                return -1
            # if balanced then return the max height 
            return 1+ max(left,right)
            
        return check(root)!= -1  # if not equal to '-1' means balanced


