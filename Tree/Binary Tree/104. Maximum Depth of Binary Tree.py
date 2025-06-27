# Method 1

# One liner
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right)) if root else 0

# method 2:
#  more readable and better  than above 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root== None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


# Method 3: 
# Little more expansion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root== None:
            return 0
        l= self.maxDepth(root.left)
        r= self.maxDepth(root.right)
        return 1+ max(l,r)
