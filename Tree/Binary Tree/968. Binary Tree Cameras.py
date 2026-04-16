

"""
Logic: each leaf node has only one of two ways it can be monitored:
i)  Place a camera on the leaf node.
ii) Place a camera on the parent node of the leaf node.

But placing on parent will be reduce the no of cameras because then more node can be monitored.

We define three states for any node:
    State 0: "I am UNCOVERED." (I have no camera and no one is watching me)
    State 1: "I HAVE A CAMERA." (I am a camera; I cover myself, my kids, and my parent)
    State 2: "I AM COVERED." (I don't have a camera, but one of my kids is watching me)

Going Bottom up, for each node: 
i)   If any child needs a camera (i.e. child returned 0) → this node must have a camera
ii)  If any child has a camera (i.e. child returned 1) → this node is covered
iii) If both children are covered and do not have cameras → this node needs a camera

time: O(n)
"""

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0
        
        def dfs(node):
            # Base Case: If we reach a null child (empty space)
            # We treat it as "Covered" (State 2) so it doesn't force us to 
            # put cameras on the leaves unnecessarily.
            if not node:
                return 2
            
            # Go all the way down to the bottom first (Post-order traversal)
            left_child_state = dfs(node.left)
            right_child_state = dfs(node.right)
            
            # --- DECISION TIME ---
            
            # CASE 1: One of my children is "UNCOVERED" (State 0)
            # If a child is naked, I MUST put a camera here to save them.
            if left_child_state == 0 or right_child_state == 0:
                self.cameras += 1
                return 1 # Now I am a camera
            
            # CASE 2: One of my children HAS A CAMERA (State 1)
            # If a child is a camera, they are looking up at me. I am safe!
            if left_child_state == 1 or right_child_state == 1:
                return 2 # Now I am covered
            
            # CASE 3: Both children are "COVERED" (State 2) but have NO camera
            # My kids are safe, but they aren't looking at me. 
            # I am now "UNCOVERED" (State 0). I'll wait for my parent to save me.
            return 0

        # After the DFS finishes, check the very top (the Root).
        # If the root says "I am UNCOVERED," there's no parent left to save it.
        # We must put a camera on the root itself.
        # Needed this check separately because some node is dependent on it's parent node also to cover it ("I won't cover myself; I'll wait for my parent to cover me.) 
        if dfs(root) == 0:
            self.cameras += 1
            
        return self.cameras

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int cameras = 0;  // Counter to track the number of cameras placed

    public int minCameraCover(TreeNode root) {
        if (dfs(root) == 0) {
            cameras++;  // If root is still not covered, we need to place a camera at the root
        }
        return cameras;
    }

    private int dfs(TreeNode node) {
        if (node == null) {
            return 2;  // Null nodes are considered covered
        }

        int left = dfs(node.left);
        int right = dfs(node.right);

        // If any child needs a camera, place a camera at this node
        if (left == 0 || right == 0) {
            cameras++;
            return 1;  // Node has a camera
        }

        // If any child has a camera, this node is covered
        if (left == 1 || right == 1) {
            return 2;  // Node is covered
        }

        // If both children are covered but do not have cameras, this node needs a camera
        return 0;  // Node needs a camera
    }
}
"""
# C++ Code 
"""
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int cameras = 0;  // Counter to track the number of cameras placed

    int minCameraCover(TreeNode* root) {
        if (dfs(root) == 0) {
            cameras++;  // If root is still not covered, we need to place a camera at the root
        }
        return cameras;
    }

    int dfs(TreeNode* node) {
        if (!node) return 2;  // Null nodes are considered covered

        int left = dfs(node->left);
        int right = dfs(node->right);

        // If any child needs a camera, place a camera at this node
        if (left == 0 || right == 0) {
            cameras++;
            return 1;  // Node has a camera
        }

        // If any child has a camera, this node is covered
        if (left == 1 || right == 1) {
            return 2;  // Node is covered
        }

        // If both children are covered but do not have cameras, this node needs a camera
        return 0;  // Node needs a camera
    }
};
"""

