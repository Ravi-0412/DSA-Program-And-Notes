# Logic: each leaf node has only one of two ways it can be monitored:
# i)  Place a camera on the leaf node.
# ii) Place a camera on the parent node of the leaf node.

# Bt placing on parent will be reduce the no of cameras because then more node can be monitored if leaf node.

# VVi: In similar way we have to decide whether it's better to put camera at node or its parent recursively 
# for each monitored node.  We can then treat these nodes as 'new' leaf nodes and repeat the process.

# Note: It will be better to go bottom up because going top down it will be very difficult to decide and minimise ans.

# Q) how do we keep track of which nodes have been monitored?
# We can use different values to track this.
# 0 as unmonitored, 1 as monitored (camera), and 2 as monitored (no camera).

# As I traverse up the binary tree, I can easily obtain the identity of the current node by obtaining the minimum of the two child nodes
# (accounting for leaf nodes as edge cases) and deciding from there based on the list above.

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
