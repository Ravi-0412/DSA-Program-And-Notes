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