# don't know why this is not workinfg
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + (self.maxDepth(root.left),self.maxDepth(root.right)) if root else 0

#  more readable and better  than above but not working in leetcode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root== None:
            return 0
        return 1 + (self.maxDepth(root.left),self.maxDepth(root.right))


# working on leetcode
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root== None:
            return 0
        l= self.maxDepth(root.left)
        r= self.maxDepth(root.right)
        return 1+ max(l,r)