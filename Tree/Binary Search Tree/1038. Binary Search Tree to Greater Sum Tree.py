# method 1: 
# Brute force
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        inorder = [0]*101  # if 'num' is present in bst then inorder[num] = num

        def findInorder(root):
            if not root:
                return 0
            inorder[root.val] = root.val
            findInorder(root.left)
            findInorder(root.right)

        def update(root):
            if not root:
                return 
            root.val = inorder[root.val]    # this will be new value
            update(root.left)
            update(root.right)

        findInorder(root)

        for i in range(99, -1, -1):
            inorder[i] = inorder[i] + inorder[i + 1]
        # after this inorder[i] = sum from 'i' to last index.
        # now update the value of all nodes
        update(root)
        return root

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode bstToGst(TreeNode root) {
        int[] inorder = new int[101];  // if 'num' is present in bst then inorder[num] = num

        findInorder(root, inorder);

        for (int i = 99; i >= 0; i--) {
            inorder[i] = inorder[i] + inorder[i + 1];
        }
        // after this inorder[i] = sum from 'i' to last index.
        // now update the value of all nodes
        update(root, inorder);

        return root;
    }

    void findInorder(TreeNode root, int[] inorder) {
        if (root == null) return;
        inorder[root.val] = root.val;
        findInorder(root.left, inorder);
        findInorder(root.right, inorder);
    }

    void update(TreeNode root, int[] inorder) {
        if (root == null) return;
        root.val = inorder[root.val];  // this will be new value
        update(root.left, inorder);
        update(root.right, inorder);
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* bstToGst(TreeNode* root) {
        vector<int> inorder(101, 0);  // if 'num' is present in bst then inorder[num] = num

        findInorder(root, inorder);

        for (int i = 99; i >= 0; --i) {
            inorder[i] = inorder[i] + inorder[i + 1];
        }
        // after this inorder[i] = sum from 'i' to last index.
        // now update the value of all nodes
        update(root, inorder);

        return root;
    }

    void findInorder(TreeNode* root, vector<int>& inorder) {
        if (!root) return;
        inorder[root->val] = root->val;
        findInorder(root->left, inorder);
        findInorder(root->right, inorder);
    }

    void update(TreeNode* root, const vector<int>& inorder) {
        if (!root) return;
        root->val = inorder[root->val];  // this will be new value
        update(root->left, inorder);
        update(root->right, inorder);
    }
};
"""
# method 2:

# logic: We need to do the work from biggest to smallest, right to left.
# pre(value) will record the previous value the we get, which the total sum of bigger values.
# For each node, we update root.val with root.val + pre.

# time: O(n)
# space: O(height)

class Solution:
    value = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root.right: 
            self.bstToGst(root.right)
        root.val = self.value = root.val + self.value
        if root.left:
            self.bstToGst(root.left)
        return root

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int value = 0;

    public TreeNode bstToGst(TreeNode root) {
        if (root == null) return null;

        if (root.right != null) {
            bstToGst(root.right);
        }
        root.val = value = root.val + value;
        if (root.left != null) {
            bstToGst(root.left);
        }
        return root;
    }
}
"""
# C++ Code 
"""
struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int value = 0;

    TreeNode* bstToGst(TreeNode* root) {
        if (!root) return nullptr;

        if (root->right) {
            bstToGst(root->right);
        }
        root->val = value = root->val + value;
        if (root->left) {
            bstToGst(root->left);
        }
        return root;
    }
};
"""
# Method 3: 
# Other way to write method 2
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node, rightSum):
            if not node: return rightSum
            rightSum = dfs(node.right, rightSum)
            node.val += rightSum
            return dfs(node.left, node.val)
        dfs(root, 0)
        return root


# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode bstToGst(TreeNode root) {
        dfs(root, 0);
        return root;
    }

    private int dfs(TreeNode node, int rightSum) {
        if (node == null) return rightSum;

        rightSum = dfs(node.right, rightSum);
        node.val += rightSum;

        return dfs(node.left, node.val);
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
    TreeNode* bstToGst(TreeNode* root) {
        dfs(root, 0);
        return root;
    }

    int dfs(TreeNode* node, int rightSum) {
        if (!node) return rightSum;

        rightSum = dfs(node->right, rightSum);
        node->val += rightSum;

        return dfs(node->left, node->val);
    }
};
"""
# same question
# 1) 538. Convert BST to Greater Tree
