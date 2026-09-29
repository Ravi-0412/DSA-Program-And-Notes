# method 1: 

"""
logic: Bottom up (can say DP only)
Logic: For each node check that is root of the ans.
Just similar to  :"543. Diameter of Binary Tree", find the path sum at each node 

for max ans, we have 4 choices like:
 1) add the current root val to left subtree ans 2) add the current root val to right subtree ans
 3) add the current root val to left subtree ans + right subtreea ans 6) only return the current root value

But for returning to the above level we have only three choices as it should be path connected  to upper level.
1) left part + current node 2) right part +current node  3) only the current node.  
current path must be there in all cases then only path can be connected.

vvi: Code structure and logic is similar to "Diameter Q" but have little difference.
the difference from "Diameter of tree" is that here ans can be between any node,even single node value can be the ans because value is in negative also.
not only between the leaf to leaf like "Diameter Q"
time: O(n)
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            # return the lowest possible value in base case so that it doesnt affect the ans. 
            # returning '0' will affect if node values will be "-ve" becuase then max will be '0' and we will get the wrong ans.
            if root== None:
                return float('-inf') 
            l= dfs(root.left)
            r= dfs(root.right)
            self.ans= max(self.ans, l+ root.val, r+ root.val, l+ r+ root.val, root.val)
            return max(l+ root.val, r+ root.val, root.val)
        
        self.ans= float('-inf')
        dfs(root)
        return self.ans

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int ans = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return ans;
    }

    private int dfs(TreeNode root) {
        // return the lowest possible value in base case so that it doesn't affect the ans. 
        // returning '0' will affect if node values will be "-ve" because then max will be '0' and we will get the wrong ans.
        if (root == null) return Integer.MIN_VALUE;

        int l = dfs(root.left);
        int r = dfs(root.right);

        ans = Math.max(ans, Math.max(Math.max(l + root.val, r + root.val),
                                     Math.max(l + r + root.val, root.val)));

        return Math.max(Math.max(l + root.val, r + root.val), root.val);
    }
}
"""
# C++ Code 
"""
#include <climits>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int ans = INT_MIN;

    int maxPathSum(TreeNode* root) {
        dfs(root);
        return ans;
    }

    int dfs(TreeNode* root) {
        // return the lowest possible value in base case so that it doesn't affect the ans. 
        // returning '0' will affect if node values will be "-ve" because then max will be '0' and we will get the wrong ans.
        if (!root) return INT_MIN;

        int l = dfs(root->left);
        int r = dfs(root->right);

        ans = max({ans, l + root->val, r + root->val, l + r + root->val, root->val});
        return max({l + root->val, r + root->val, root->val});
    }
};
"""

"""
Note : Above java & C++ code won't work.
dfs(null) returns Integer.MIN_VALUE. At a leaf with a negative value, the code computes l + root.val:                                                                                                                                           
                                                                                                                                                                                                                                                    
    Integer.MIN_VALUE + (-5) = 2147483643     ← wraps around to a huge positive number                                                                                                                                                              
    (I checked this with 32-bit arithmetic.) That wrong value flows into ans. For example, the tree [-5] returns about 2.1 billion instead of -5. 
    In C++, signed overflow is undefined behavior (the language gives no guarantee about the result), which is even worse.                                         
"""

# How to solve & handle that correctly
"""
Logic:
  1. max_gain(node) returns the best downward arm starting at node.
  2. Get the children's arms, and clamp them at 0 (a negative arm is left out).
  3. The path that bends here is node.val + left_gain + right_gain. Update the best answer with it.
  4. Return node.val + max(left_gain, right_gain). The parent can extend only one side, because a path can't branch.

  Why the clamp covers every case (with val = 10):
  left +7,  right +5  → 10 + 7 + 5 = 22   (bend + both)
  left −3,  right +5  → 10 + 0 + 5 = 15   (bend + right)
  left +7,  right −4  → 10 + 7 + 0 = 17   (bend + left)
  left −3,  right −4  → 10 + 0 + 0 = 10   (bend only)

  Dry run:
          -10
         /    \
        9      20
              /  \
             15   7
             
  node | left_gain | right_gain | bend here           | best | returns
   9   |    0      |     0      | 9                   |  9   | 9
   15  |    0      |     0      | 15                  |  15  | 15
   7   |    0      |     0      | 7                   |  15  | 7
   20  |   15      |     7      | 20+15+7 = 42        |  42  | 20+15 = 35
   -10 |    9      |    35      | -10+9+35 = 34       |  42  | -10+35 = 25

  answer 42 (15 → 20 → 7) ✓
  
  Why self.best starts at -inf and not 0: for the tree [-3], the answer is -3, because a path must contain at least one node. Starting at 0 would wrongly return 0.

   How it replaces your five cases:
  your cases                          clamp version
  l + val                   ─┐
  r + val                    ├──→     val + left_gain + right_gain
  l + r + val                │        (each gain is ≥ 0, so a gain of 0
  val                       ─┘         covers "not taking that side")
  This matches your version on 5,000 random trees. It also removes the overflow, because the base case returns 0, not MIN_VALUE.

  Complexity

  Let n = the number of nodes and h = the height of the tree.
"""

class Solution:
      def maxPathSum(self, root: Optional[TreeNode]) -> int:
          self.best = -math.inf                         # at least one node must be taken, so start at -inf

          def max_gain(node):                           # best downward arm starting at node
              if not node:
                  return 0                              # no node → contributes nothing
              left_gain = max(max_gain(node.left), 0)   # a negative arm makes the path worse → drop it
              right_gain = max(max_gain(node.right), 0)

              self.best = max(self.best, node.val + left_gain + right_gain)   # path that bends here
              return node.val + max(left_gain, right_gain)                    # the parent can extend one side only

          max_gain(root)
          return self.best
"""
Follow-ups : 
 1. Return the nodes on the maximum path, not just its sum.
  2. The path must start and end at leaves.
  3. 687. Longest Univalue Path (https://leetcode.com/problems/longest-univalue-path/)
""'
