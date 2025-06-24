# method 1: 

# Logic: Just go bottom up and check the value of each node with its children sum.
# Note: write base case for leaf node also because we don't have to check this for leaf node.

# Time: O(n)

class Solution:
    def isSumTree(self,root):
        self.ans = 1
        def check(root):
            if not root:
                return 0
            if root.left == None and root.right == None:
                return root.data
            l = check(root.left)
            r = check(root.right)
            if root.data != l + r:
                self.ans = 0
            return l + r + root.data
            
        check(root)
        return self.ans

# Java Code 
"""
class Node {
    int data;
    Node left, right;
    Node(int x) { data = x; }
}

class Solution {
    int ans = 1;

    public int isSumTree(Node root) {
        check(root);
        return ans;
    }

    private int check(Node root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return root.data;
        }
        int l = check(root.left);
        int r = check(root.right);
        if (root.data != l + r) {
            ans = 0;
        }
        return l + r + root.data;
    }
}
"""
# C++ Code 
"""
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int x) : data(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int ans = 1;

    int isSumTree(Node* root) {
        check(root);
        return ans;
    }

    int check(Node* root) {
        if (!root) return 0;
        if (!root->left && !root->right) return root->data;
        int l = check(root->left);
        int r = check(root->right);
        if (root->data != l + r) {
            ans = 0;
        }
        return l + r + root->data;
    }
};
"""

# Method 2:
# Instead of taking 'ans' as global variable ,
# return any integer in invalid case which can make all the upper nodes sum as invalid.

class Solution:
    def isSumTree(self,root):
        
        def check(root):
            if not root:
                return 0
            if root.left == None and root.right == None:
                return root.data
            l = check(root.left)
            r = check(root.right)
            if l == -1 or r == -1 or root.data != l + r:
                return -1
            return l + r + root.data
        
        return 1 if check(root) != -1 else 0

# Java Code 
"""
class Node {
    int data;
    Node left, right;
    Node(int x) { data = x; }
}

class Solution {
    public int isSumTree(Node root) {
        return check(root) != -1 ? 1 : 0;
    }

    private int check(Node root) {
        if (root == null) {
            return 0;
        }
        if (root.left == null && root.right == null) {
            return root.data;
        }

        int l = check(root.left);
        int r = check(root.right);

        if (l == -1 || r == -1 || root.data != l + r) {
            return -1;
        }

        return l + r + root.data;
    }
}
"""
# C++ Code 
"""
struct Node {
    int data;
    Node* left;
    Node* right;
    Node(int x): data(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int isSumTree(Node* root) {
        return check(root) != -1 ? 1 : 0;
    }

    int check(Node* root) {
        if (!root) return 0;
        if (!root->left && !root->right) return root->data;

        int l = check(root->left);
        int r = check(root->right);

        if (l == -1 || r == -1 || root->data != l + r) return -1;

        return l + r + root->data;
    }
};
"""