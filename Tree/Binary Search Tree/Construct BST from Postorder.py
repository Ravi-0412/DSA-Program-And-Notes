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
"""
logic: Since here last node will be the parent so we will traverse from right side(root side).
if any ele will be greater that will be right child and we can add them directly to the right of tree.
And if smaller then we we have to search for the node for which 'num' will be the left child.
Reason for above logic: for post (left, right, root). so if greater then will go to right side directly.

vvi: Difference from 'given preoder and construct BST'?
Ans: 1) in preorder we were traversing from left to right(from root) and here from right to left (from root only).
2) in preoder if 'num' was smaller then we were directly adding and in this we are directly adding if num is greater.

time= space= O(n)
"""

class Solution:
    def constructTree(self, post, n):
        if not post: return None
        
        # In Postorder (Left-Right-Root), the last element is the Root.
        # By iterating backwards, we process: Root -> Right -> Left.
        root = Node(post[-1])
        stack = [root]
        
        # Iterate from the second-to-last element down to the first
        for i in range(len(post) - 2, -1, -1):
            num = post[i]
            node = Node(num)
            
            # If current number is GREATER than top of stack, it's a Right Child.
            # (In reverse postorder, we see Right before Left).
            if num > stack[-1].val:
                stack[-1].right = node
            else:
                # If current number is SMALLER, we've finished the right side.
                # Pop until we find the node for which 'num' is the Left Child.
                while stack and num < stack[-1].val:
                    last = stack.pop()
                last.left = node
            
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

# Method 3:
# Recursive one
"""
we use the Lower Bound trick. Since we process the array from the end (Root), the logic is:The last element is the Root.
The elements immediately to its left that are greater than it belong to its Right Subtree.
The elements even further left that are smaller than it belong to its Left Subtree.

Thought Process:
We use a global pointer self.index starting at n-1.
For the Right Subtree, the values must be greater than the parent's value but smaller than the "upper limit."
For the Left Subtree, the values must be smaller than the parent's value but greater than the "lower limit."

Q) solve(float('-inf')) , why it can't be upper bound : infinity  like preorder ?
-> The reason we switch from an Upper Bound (in Preorder) to a Lower Bound (in Postorder) is because 
of the direction in which we are moving through the values relative to the Root.

The Logic: Direction of ConstraintIn a BST, the Root acts as a "partition" between small and large values.
1. Preorder (Root ->  Left -> Right)
Direction: We process the Root, then immediately move into the Left Subtree.
The Constraint: To know when the Left Subtree ends, we need to know the Upper Bound (the Root's value).
Why? Because as long as numbers are smaller than the Root, they could be part of the left side. 
The moment we see something larger than the Upper Bound, we know we've hit the Right Subtree.

2. Postorder (Moving Backwards: Root -> Right -> Left)
Direction: We process the Root, then (moving backwards) we immediately move into the Right Subtree.
The Constraint: To know when the Right Subtree ends, we need to know the Lower Bound (the Root's value).
Why? Because in the Right Subtree, all values must be greater than the Root. 
As long as the numbers we see are larger than the Root, they could be part of the right side. 
The moment we see something smaller than the Lower Bound, we know we have finally "crossed over" into the Left Subtree.
"""

class Solution:
    def constructTree(self, post, n):
        self.index = n - 1
        
        # We pass a lower bound. Any value smaller than this bound
        # cannot belong to the current subtree.
        def solve(lower_bound):
            if self.index < 0 or post[self.index] < lower_bound:
                return None
            
            # Create root from the end of the current range
            val = post[self.index]
            root = Node(val)
            self.index -= 1
            
            # IMPORTANT: We must build the RIGHT subtree first 
            # because we are moving backwards through [Left, Right, Root]
            
            # Right subtree values must be > root.val
            root.right = solve(val)
            
            # Left subtree values must be > parent's lower_bound
            root.left = solve(lower_bound)
            
            return root

        return solve(float('-inf'))
