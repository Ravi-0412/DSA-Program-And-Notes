# logic: Bottom up (can say DP only)
# find the path sum at each node 

# for max ans, we have 6 choices like:
# 1)only left subtree ans 2) only right subtree ans 3) add the current root val to left subtree ans
# 4) add the current root val to right subtree ans 5) add the current root val to left subtree ans + right subtreea ans 6) only return the current root value

# But for returning to the above level we have only three choices as it should be connected only to upper level.
# 1) left part + current node 2) right part +current node  3) only the current node

# the difference from "Diameter of tree" is that here ans can be between any node,even single node value can be the ans.
# not only between the leaf to leaf like "Diameter Q"
# time: O(n)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if root== None:
                return float('-inf')
            l= dfs(root.left)
            r= dfs(root.right)
            self.ans= max(self.ans,l, r, l+ root.val, r+ root.val, l+ r+ root.val, root.val)
            return max(l+ root.val, r+ root.val, root.val)
            # return max(l+ root.val, r+ root.val, l+ r+ root.val, root.val)
        
        self.ans= float('-inf')
        dfs(root)
        return self.ans


