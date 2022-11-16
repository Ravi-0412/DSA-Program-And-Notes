# logic: Bottom up (can say DP only)
# find the path sum at each node 
# for max ans, we have 6 choices like:
# 1)only left subtree ans 2) only right subtree ans 3) add the current root val to left subtree ans
# 4) add the current root val to right subtree ans 5) add the current root val to left subtree ans + right subtreea ans 6) only return the current root value

# But for returning to the above level we have only three choices i.e upper level take the three path as it should be connected only
# 1) left part + current node 2) right part +current node  3) only the current node

# time: O(n)
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans= [-999999]
        def dfs(root):
            if root== None:
                return -999999
            l= dfs(root.left)
            r= dfs(root.right)
            ans[0]= max(ans[0],l, r, l+ root.val, r+ root.val, l+ r+ root.val, root.val)   # storing the max ans
            return max(l+ root.val, r+ root.val, root.val)  # it simply returning the path the above level can take below
            # return max(l+ root.val, r+ root.val, l+ r+ root.val, root.val)     # mine mistake
            # return max(ans[0],l, r, l+ root.val, r+ root.val, l+ r+ root.val, root.val) # mine mistake 
        dfs(root)
        return ans[0]

 