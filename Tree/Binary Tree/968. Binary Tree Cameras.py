# time: O(n)

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            if not root:
                return 0
            ans= dfs(root.left) + dfs(root.right)
            cur= min(root.left.val if root.left else float('inf'), root.right.val if root.right else float('inf') )
            if cur== 0:
                # at least one child node requires monitoring, this node must have a camera
                ans+= 1
                root.val= 1
            elif cur== 1:
                # at least one child node is a camera, this node is already monitored
                root.val= 2
            # if curr == float('inf'), the current node is a leaf node; let the parent node monitor this node
            # if curr == 2, all child nodes are being monitored; treat the current node as a leaf node
            return ans

        # ensure that root node is monitored, otherwise, add a camera onto root node
        return dfs(root) + (root.val== 0)
