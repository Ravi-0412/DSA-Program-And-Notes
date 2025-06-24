# method 1:
# Just applied 3rd method of Q: "98. Validate Binary Search Tree"
# Only one difference: just return 'sum' also with minimum and maximum value


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0    # Taken '0' instead of 'float('-inf') because in case of all negative values we have to return '0' only(empty bst)

        def check(root):
            if not root:
                return [float('inf'), float('-inf'), 0]  # [minimum, maximum, sum]. For base case return such value which will be valid always
            min1, max1, sum1 = check(root.left)
            min2, max2, sum2 = check(root.right)
            if root.val <= max1 or root.val >= min2:
                # not valid so return such values which will be invalid always
                return [float('-inf'), float('inf'), 0]
            self.ans = max(self.ans, sum1 + sum2 + root.val)
            return [min(min1, root.val), max(root.val, max2), sum1 + sum2 + root.val]

        check(root)
        return self.ans

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int ans = 0;  // Taken '0' instead of 'Integer.MIN_VALUE' because in case of all negative values we have to return '0' only (empty BST)

    public int maxSumBST(TreeNode root) {
        check(root);
        return ans;
    }

    // Returns int[]{min, max, sum}
    private int[] check(TreeNode root) {
        if (root == null) {
            return new int[]{Integer.MAX_VALUE, Integer.MIN_VALUE, 0};  // [minimum, maximum, sum]. For base case return such value which will be valid always
        }

        int[] left = check(root.left);
        int[] right = check(root.right);

        if (root.val <= left[1] || root.val >= right[0]) {
            // not valid so return such values which will be invalid always
            return new int[]{Integer.MIN_VALUE, Integer.MAX_VALUE, 0};
        }

        int sum = left[2] + right[2] + root.val;
        ans = Math.max(ans, sum);

        return new int[]{Math.min(left[0], root.val), Math.max(root.val, right[1]), sum};
    }
}
"""
# C++ Code 
"""
#include <algorithm>
#include <climits>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int ans = 0;  // Taken '0' instead of 'INT_MIN' because in case of all negative values we have to return '0' only (empty BST)

    int maxSumBST(TreeNode* root) {
        check(root);
        return ans;
    }

    // Returns vector: {min, max, sum}
    vector<int> check(TreeNode* root) {
        if (!root) {
            return {INT_MAX, INT_MIN, 0};  // [minimum, maximum, sum]. For base case return such value which will be valid always
        }

        vector<int> left = check(root->left);
        vector<int> right = check(root->right);

        if (root->val <= left[1] || root->val >= right[0]) {
            // not valid so return such values which will be invalid always
            return {INT_MIN, INT_MAX, 0};
        }

        int sum = left[2] + right[2] + root->val;
        ans = max(ans, sum);

        return {min(left[0], root->val), max(root->val, right[1]), sum};
    }
};
"""