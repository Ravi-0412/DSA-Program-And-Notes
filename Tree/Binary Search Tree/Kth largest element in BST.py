# method 1: 
# Just same as 'Kth smallest element in BST".
# Logic: Largest node will be the rightmost node.
# so once you find '.right' of any node = None then that will be the largest node as of now.
# And to get the next largest node , move to its left.

# If it's left is also None then it will do backtrack function call to previous node and calculate in same way.

class Solution:
    def kthLargest(self,root, k):
        
        def findKthLargest(root):
            if root.right:
                findKthLargest(root.right)
            self.count -= 1
            if self.count == 0:
                self.ans = root.data
                return
            # next greater we will get from left side of root
            if root.left:
                findKthLargest(root.left)

        self.ans = -1
        self.count = k
        findKthLargest(root)
        return self.ans

# Java Code 
"""
class Node {
    int data;
    Node left, right;
    Node(int x) { data = x; }
}

class Solution {
    int count;
    int ans = -1;

    public int kthLargest(Node root, int k) {
        count = k;
        findKthLargest(root);
        return ans;
    }

    void findKthLargest(Node root) {
        if (root.right != null) {
            findKthLargest(root.right);
        }

        count--;
        if (count == 0) {
            ans = root.data;
            return;
        }

        // next greater we will get from left side of root
        if (root.left != null) {
            findKthLargest(root.left);
        }
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
    int count;
    int ans = -1;

    int kthLargest(Node* root, int k) {
        count = k;
        findKthLargest(root);
        return ans;
    }

    void findKthLargest(Node* root) {
        if (root->right) {
            findKthLargest(root->right);
        }

        count--;
        if (count == 0) {
            ans = root->data;
            return;
        }

        // next greater we will get from left side of root
        if (root->left) {
            findKthLargest(root->left);
        }
    }
};
"""