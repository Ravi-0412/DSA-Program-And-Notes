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
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def maxDepth(self, root):
        if root== None:
            return 0
        l= self.maxDepth(root.left)
        r= self.maxDepth(root.right)
        return 1+ max(l,r)

# more concise way of writing above code
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
# there is lot of repitition in above method.

# Note vvi: To make decision on a node , we need maximum node count from its left and right subtree.

# note: we have to take care of "True/False" as well as height at the same time.

# just the height logic only , instead of  returning booleans we are returning in integer 
# so that if subtree is unbalanced then it automatically make its parent unbalanced automatically.

# and also we have to return the height also which will be a positive number so replaced the boolean return value 
# with integer return to handle all these cases.

# bottom up approach , ans from bottom is getting updated to upper level.. Can say DP only.
# here we only need left and right tree ans to make a decision for current root that's why not storing ans anywhere.

# Note VVI(Generalisation of DP in tree): calculate for left and right part of a node
# then make a decision for cur node i.e (update the ans) based on left and right part and return the ans to upper level (to parent).

# Note: updating the ans and returning to the upper level might be different 
# so always make another function(say helper function) if you got that both will be different and keep 'ans' as global variable.
#  in helper function, just keep updating the ans after getting value from left and right part and return the value according to the function.

# Note: we will return when any of the subtree will be balanced.

# Note: '-1' means tree is unbalanced. we can return any integer that can't be height (means any negative integer) like -1,-2....
# all will work fine.

# Note: we can't return True/False based on True/false because in Python True->1 and False->0 and '0' and '1' can be our height also.

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


# Method 3:
# Simplest way of writing above logic using 'ans' as global variable.
# Do by this only

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:   
        self.ans= True   # without 'self' it is not working

        def maxDepth(root):  # check if subtree starting from root is balanced.
            if root== None:
                return 0
            l = maxDepth(root.left)
            r = maxDepth(root.right)
            if abs(l - r) > 1:
                self.ans = False
            return 1 + max(l, r)

        maxDepth(root)
        return self.ans
