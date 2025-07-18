# method 1: 

"""
in other words we have to find: "Maximum sum of nodes in Binary tree such that no two are adjacent."

time: O(n)

just bottom up DP

logic: everything will depend on whether we include root or not for each subtre. i.e

1) when we include the current node, then we can't include any of its child. so take max of both the child when they are not included.
2) when we don't include the current node, then we have four choices and we have to max of all four:
a) when we don't include any of its child.
b) when we don't include left child and include the right child.
c) when we include left child and don't include the right child.
d) when we don't include any of its child.
vvi: All these four condition will get handled by 'withoutRoot= max(leftPair) + max(rightPair)'.
"""


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # return pair: [withRoot, withoutRoot]
        def dfs(root):
            if not root:
                return [0, 0]     # [withRoot, withoutRoot]
            leftPair=  dfs(root.left)
            rightPair= dfs(root.right)
            # when we include the current node
            withRoot=  root.val + leftPair[1] + rightPair[1]  
            # when we don't include the current node
            withoutRoot= max(leftPair) + max(rightPair)   
            return [withRoot, withoutRoot]
        
        return max(dfs(root))   # return max([withRoot, withoutRoot])

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public int rob(TreeNode root) {
        int[] result = dfs(root);
        return Math.max(result[0], result[1]);  // return max([withRoot, withoutRoot])
    }

    // return pair: [withRoot, withoutRoot]
    private int[] dfs(TreeNode root) {
        if (root == null) {
            return new int[]{0, 0};  // [withRoot, withoutRoot]
        }

        int[] leftPair = dfs(root.left);
        int[] rightPair = dfs(root.right);

        // when we include the current node
        int withRoot = root.val + leftPair[1] + rightPair[1];
        // when we don't include the current node
        int withoutRoot = Math.max(leftPair[0], leftPair[1]) + Math.max(rightPair[0], rightPair[1]);

        return new int[]{withRoot, withoutRoot};
    }
}
"""
# C++ Code 
"""
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
    int rob(TreeNode* root) {
        auto result = dfs(root);
        return max(result.first, result.second);  // return max([withRoot, withoutRoot])
    }

    // return pair: [withRoot, withoutRoot]
    pair<int, int> dfs(TreeNode* root) {
        if (!root) return {0, 0};  // [withRoot, withoutRoot]

        auto leftPair = dfs(root->left);
        auto rightPair = dfs(root->right);

        // when we include the current node
        int withRoot = root->val + leftPair.second + rightPair.second;
        // when we don't include the current node
        int withoutRoot = max(leftPair.first, leftPair.second) + max(rightPair.first, rightPair.second);

        return {withRoot, withoutRoot};
    }
};
"""