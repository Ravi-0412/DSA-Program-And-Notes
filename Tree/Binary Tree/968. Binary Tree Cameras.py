

"""
Logic: each leaf node has only one of two ways it can be monitored:
i)  Place a camera on the leaf node.
ii) Place a camera on the parent node of the leaf node.

But placing on parent will be reduce the no of cameras because then more node can be monitored.

Three states, returned from each node to its parent:
      State 0: "NOT COVERED"  - no camera on me and no child has a camera; my parent must put a camera to cover me
      State 1: "HAS CAMERA"   - camera on me; covers me, my children and my parent
      State 2: "COVERED"      - no camera on me, but a child has one and covers me (null nodes also return this)

Going Bottom up, for each node: 
i)   If any child needs a camera (i.e. child returned 0) → this node must have a camera
ii)  If any child has a camera (i.e. child returned 1) → this node is covered
iii) If both children are covered and do not have cameras → this node needs a camera

Going bottom-up, for each node (checked in this order):
      i)   If any child is NOT COVERED (0) -> put a camera here, return 1
      ii)  Else if any child HAS a CAMERA (1) -> I am covered, return 2
      iii) Else (both children COVERED without camera) -> I am NOT COVERED, return 0 and let my parent cover me

  The root has no parent, so if it returns 0, add one camera for it.

Note : The order of the checks is essential. Say why out loud. "Is a child uncovered?" must come before "does a child have a camera?". 
Example: one child is uncovered and the other has a camera. If you checked for the camera first, you'd return
COVERED and leave the uncovered child uncovered forever

time: O(n) , space : O(h)
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

# Better & meaningful way
"""
Use named constants instead of 0, 1, 2. Writing if left == NOT_COVERED reads better in an interview than if left == 0.
"""
class Solution:
      def minCameraCover(self, root: Optional[TreeNode]) -> int:
          NOT_COVERED, HAS_CAMERA, COVERED = 0, 1, 2
          cameras = 0

          def state(node):
              nonlocal cameras
              if not node:
                  return COVERED                       # forces nothing, watches nobody
              left, right = state(node.left), state(node.right)
              if NOT_COVERED in (left, right):         # checked first: an uncovered child must be fixed
                  cameras += 1
                  return HAS_CAMERA
              if HAS_CAMERA in (left, right):
                  return COVERED
              return NOT_COVERED                       # my parent will cover me

          if state(root) == NOT_COVERED:               # the root has no parent to rely on
              cameras += 1
          return cameras


# Method 2:
"""
  When you aren't sure the greedy rule is correct, compute the minimum number of cameras for each state at every node. 
  This also works when the greedy rule breaks, for example when each node's camera has a different cost.


The one rule

  Every node must end up covered. A child can be covered in exactly three ways:

  child_cam   → it has its own camera
  child_cov   → one of its own children covers it
  child_wait  → nobody below covers it; it relies on ME having a camera
  Each value is the minimum number of cameras in that child's subtree, given that state.

  Line 1: I have a camera
  
  camera_here = 1 + min(left_cam, left_cov, left_wait) + min(right_cam, right_cov, right_wait)
          [📷 me]          my camera covers both children
          /     \          → each child can be in ANY state, including "wait"
       left     right      → take the cheapest of the 3 for each child
  - 1 is my own camera.
  - Each child may be cam, cov, or wait, because my camera rescues a waiting child. So take the minimum of all three for each child.
  
  Line 2: no camera on me, but a child covers me

  covered_by_child = min(left_cam + min(right_cam, right_cov),
                         right_cam + min(left_cam, left_cov))
  Option A: the left child has a camera    Option B: the right child has a camera
            [me]                                  [me]
           /    \                                /    \
       [📷 L]   R = cam or cov              L = cam or cov   [📷 R]
  - At least one child must have a camera, so that it covers me. Try each side as the watcher and keep the cheaper option.
  - The other child can be cam or cov, but not wait: I have no camera, so I can't rescue it.
  
  Line 3: no camera on me, and no child covers me

  waits_for_parent = left_cov + right_cov
          [me]             no camera on me → I can't rescue a waiting child
         /    \            no child camera → otherwise I'd be "covered", not "waiting"
     L = cov  R = cov      → both children must be covered by THEIR children
  - The children can't be cam: then I'd be covered, which is Line 2's state.
  - The children can't be wait: nobody would cover them.
  - So both must be cov.

  Summary

  ┌──────────────────┬───────────────────┬────────────────────┬───────────────────────────┐
  │     My state     │ Left child may be │ Right child may be │        Extra rule         │
  ├──────────────────┼───────────────────┼────────────────────┼───────────────────────────┤
  │ camera_here      │ cam / cov / wait  │ cam / cov / wait   │ +1 for my camera          │
  ├──────────────────┼───────────────────┼────────────────────┼───────────────────────────┤
  │ covered_by_child │ cam / cov         │ cam / cov          │ at least one child is cam │
  ├──────────────────┼───────────────────┼────────────────────┼───────────────────────────┤
  │ waits_for_parent │ cov               │ cov                │                           │
  └──────────────────┴───────────────────┴────────────────────┴───────────────────────────┘

  The null base case: (inf, 0, 0)
  
  null cam  = inf   → you can't place a camera on nothing
  null cov  = 0     → nothing to cover, costs nothing
  null wait = 0     → only ever used inside a min next to cov = 0, so it doesn't change anything

  A small dry run

      A
     /
    B          (B is a leaf)

  B: children are null = (inf, 0, 0)
     camera_here      = 1 + 0 + 0                = 1
     covered_by_child = min(inf + 0, inf + 0)    = inf   (a leaf has no child to watch it)
     waits_for_parent = 0 + 0                    = 0
     B = (1, inf, 0)

  A: left = B (1, inf, 0), right = null (inf, 0, 0)
     camera_here      = 1 + min(1, inf, 0) + min(inf, 0, 0) = 1 + 0 + 0 = 1   ← B waits, A's camera covers it
     covered_by_child = min(1 + min(inf, 0), inf + …)       = 1               ← camera on B covers A
     waits_for_parent = inf + 0                              = inf

  answer = min(camera_here, covered_by_child) = 1 ✓
  The answer skips waits_for_parent for the root, because the root has no parent to wait for.

"""

class Solution:
      def minCameraCover(self, root: Optional[TreeNode]) -> int:
          def costs(node):
              """(min cameras if node has a camera,
                  min if node has no camera but a child covers it,
                  min if node has no camera, isn't covered, and waits for its parent)"""
              if not node:
                  return math.inf, 0, 0                      # a null child can't hold a camera and needs nothing
              left_cam, left_cov, left_wait = costs(node.left)
              right_cam, right_cov, right_wait = costs(node.right)

              camera_here = 1 + min(left_cam, left_cov, left_wait) + min(right_cam, right_cov, right_wait)
              covered_by_child = min(left_cam + min(right_cam, right_cov),     # the left child watches me
                                     right_cam + min(left_cam, left_cov))      # the right child watches me
              waits_for_parent = left_cov + right_cov                          # children covered, no camera
              return camera_here, covered_by_child, waits_for_parent

          camera_here, covered_by_child, _ = costs(root)
          return min(camera_here, covered_by_child)  
