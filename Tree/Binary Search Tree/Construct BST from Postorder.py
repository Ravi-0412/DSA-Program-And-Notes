# Method 1: 

# Similar logic as: "1008. Construct Binary Search Tree from Preorder Traversal"

# Easiest one: using method 4 of "1008. Construct Binary Search Tree from Preorder Traversal".
class Solution:
    def constructTree(self, post, n):
        def build(post):
            if not post:
                return None

            root = TreeNode(post[-1])  # Last element is the root
            i = len(post) - 2
            # Find the 1st element smaller than root.val. 
            while i >= 0 and post[i] > root.val:
                i -= 1

            root.right = build(post[i+1:-1])  # Elements greater than root, will go on right
            root.left = build(post[:i+1])     # Elements smaller than root, will go on left
            return root

        return build(post)

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode constructTree(int[] post, int n) {
        return build(post, 0, n - 1);
    }

    private TreeNode build(int[] post, int start, int end) {
        if (start > end) return null;

        TreeNode root = new TreeNode(post[end]);  // Last element is the root
        int i = end - 1;

        // Find the 1st element smaller than root.val.
        while (i >= start && post[i] > root.val) {
            i--;
        }

        root.right = build(post, i + 1, end - 1);  // Elements greater than root, will go on right
        root.left = build(post, start, i);        // Elements smaller than root, will go on left
        return root;
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* constructTree(vector<int>& post, int n) {
        return build(post, 0, n - 1);
    }

private:
    TreeNode* build(const vector<int>& post, int start, int end) {
        if (start > end) return nullptr;

        TreeNode* root = new TreeNode(post[end]);  // Last element is the root
        int i = end - 1;

        // Find the 1st element smaller than root.val.
        while (i >= start && post[i] > root->val) {
            i--;
        }

        root->right = build(post, i + 1, end - 1);  // Elements greater than root, will go on right
        root->left = build(post, start, i);        // Elements smaller than root, will go on left
        return root;
    }
};
"""

# Method 2: 
# logic: Since here last node will be the parent so we will traverse from right side(root side).
# if any ele will be greater that will be right child and we can add them directly to the right of tree.
# And if smaller then we we have to search for the node for which 'num' will be the left child.
# Reason for above logic: for post (left, right, root). so if greater then will go to right side directly.

# vvi: Difference from 'given preoder and construct BST'?
# Ans: 1) in preorder we were traversing from left to right(from root) and here from right to left (from root only).
# 2) in preoder if 'num' was smaller then we were directly adding and in this we are directly adding if num is greater.

# time= space= O(n)

class Solution:
    def constructTree(self,post,n):
        n= len(post)
        root=  Node(post[-1])  # last ele will be the root only.
        stack= [root]
        for i in range(n-2, -1, -1):
            num= post[i]
            node= Node(num)
            if num > stack[-1].val:  # means num will be the right child. so directly add.
                stack[-1].right= node
            else: # Finding the last greater ele than 'num' in stack for which 'num' can be the left child.
                #  so pop until you find any smaller ele than 'num'.
                while stack and num < stack[-1].val:
                    last= stack.pop()
                # last will be the just greater than 'num' and num will be the left of 'last' only.
                last.left= node
            stack.append(node)
        return root

# Java Code 
"""
class Node {
    int val;
    Node left, right;
    Node(int x) { val = x; }
}

class Solution {
    public Node constructTree(int[] post, int n) {
        n = post.length;
        Node root = new Node(post[n - 1]);  // last ele will be the root only.
        java.util.Stack<Node> stack = new java.util.Stack<>();
        stack.push(root);

        for (int i = n - 2; i >= 0; i--) {
            int num = post[i];
            Node node = new Node(num);

            if (num > stack.peek().val) {  // means num will be the right child. so directly add.
                stack.peek().right = node;
            } else {  // Finding the last greater ele than 'num' in stack for which 'num' can be the left child.
                // so pop until you find any smaller ele than 'num'.
                Node last = null;
                while (!stack.isEmpty() && num < stack.peek().val) {
                    last = stack.pop();
                }
                // last will be the just greater than 'num' and num will be the left of 'last' only.
                last.left = node;
            }
            stack.push(node);
        }

        return root;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <stack>
using namespace std;

struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    Node* constructTree(vector<int>& post, int n) {
        n = post.size();
        Node* root = new Node(post[n - 1]);  // last ele will be the root only.
        stack<Node*> st;
        st.push(root);

        for (int i = n - 2; i >= 0; --i) {
            int num = post[i];
            Node* node = new Node(num);

            if (num > st.top()->val) {  // means num will be the right child. so directly add.
                st.top()->right = node;
            } else {  // Finding the last greater ele than 'num' in stack for which 'num' can be the left child.
                // so pop until you find any smaller ele than 'num'.
                Node* last = nullptr;
                while (!st.empty() && num < st.top()->val) {
                    last = st.top();
                    st.pop();
                }
                // last will be the just greater than 'num' and num will be the left of 'last' only.
                last->left = node;
            }
            st.push(node);
        }

        return root;
    }
};
"""