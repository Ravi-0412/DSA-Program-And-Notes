# Logic: just same logic as "104. maximum depth"
# But here in case of skew tree at any node ,we have to take the skew tree path.

# If both left and right subtree has node then return min(l, r).
# Otherwise move in the direction that have node.

# Time : O(n)

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l and r:
            return 1 + min(l, r)
        if l:
            return 1 + l
        return 1 + r
    


# doing like this will give error.
# Reason: if at node if skew tree starts then, it will return '0' for that node.
# Bt we should move towards skew tree.

# Rectified this mistake using the condition in above solution.

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return 1 + min(l, r)