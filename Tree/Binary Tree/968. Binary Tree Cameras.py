"""
Logic: each leaf node has only one of two ways it can be monitored:
i)  Place a camera on the leaf node.
ii) Place a camera on the parent node of the leaf node.

But placing on parent will be reduce the no of cameras because then more node can be monitored.

0: This node needs a camera
1: This node has a camera
2: This node is already monitored.

Going Bottom up, for each node: 
i)   If any child needs a camera (i.e. child returned 0) → this node must have a camera
ii)  If any child has a camera (i.e. child returned 1) → this node is covered
iii) If both children are covered and do not have cameras → this node needs a camera

time: O(n)
"""

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0  # Counter to track the number of cameras placed

        def dfs(node):
            if not node:
                return 2  # Null nodes are considered covered

            left = dfs(node.left)   
            right = dfs(node.right) 

            # If any child needs a camera, place a camera at this node
            if left == 0 or right == 0:
                self.cameras += 1
                return 1  # Node has a camera

            # If any child has a camera, this node is covered
            if left == 1 or right == 1:
                return 2  # Node is covered

            # If both children are covered but do not have cameras, this node needs a camera
            return 0  # Node needs a camera

        # After DFS, if root is still not covered, we need to place a camera at the root
        if dfs(root) == 0:
            self.cameras += 1

        return self.cameras

# Java
"""
class Solution {
    private int cameras = 0;

    public int minCameraCover(TreeNode root) {
        // 0: needs camera, 1: has camera, 2: covered
        if (dfs(root) == 0) {
            cameras++;
        }
        return cameras;
    }

    private int dfs(TreeNode node) {
        if (node == null) return 2;

        int left = dfs(node.left);
        int right = dfs(node.right);

        if (left == 0 || right == 0) {
            cameras++;
            return 1; // place camera here
        }

        if (left == 1 || right == 1) {
            return 2; // this node is covered
        }

        return 0; // this node needs a camera
    }
}
"""

