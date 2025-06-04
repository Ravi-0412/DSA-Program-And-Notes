def PreorderRecursive(self,root):
        if root== None:
            return
        print(root.data,end=" ")
        self.PreorderRecursive(root.left)
        self.PreorderRecursive(root.right)

# iterative way
# Logic: first push the right subtree in the stack as we have to 
# print 'left' side first and stack is LIFO
def PreorderIterative(self,root):
    if root== None:
        return 
    stack= []
    stack.append(root)
    while stack:
        curr= stack.pop()
        print(curr.data, end=" ")
        if curr.right: 
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

# Easier way
def PreorderIterative(self, root):
    if root is None:
        return 
    
    stack = []
    curr = root
    
    while curr or stack:
        while curr:
            print(curr.data, end=" ")  # Process current node
            stack.append(curr)  # Push current node to stack
            curr = curr.left  # Move to left child
        
        curr = stack.pop()  # Backtrack
        curr = curr.right  # Move to right child


# do by recursive inside the given function only and store the ans in a list(Leetcode q)
# same way we can do for other traversals.
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        if not root:
            return ans
        ans.append(root.val)
        ans+= self.preorderTraversal(root.left)
        ans+= self.preorderTraversal(root.right)
        return ans


# other way of writing above code
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left=  self.preorderTraversal(root.left)
        right= self.preorderTraversal(root.right)
        return [root.val] + left +  right   # just the logic of inorder traversal.
    

def InorderRecursive(self,root):
    if root== None:
        return
    self.InorderRecursive(root.left)
    print(root.data,end=" ")
    self.InorderRecursive(root.right)  

# recursive way: returning the ans in a list inside same function 
# just same as preorder,only change of meaning
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return []
        l= self.inorderTraversal(root.left)
        r= self.inorderTraversal(root.right)
        return l+ [root.val] + r        # just the meaning of inorder

# Note vvi: iterative one
# easier one. just the conversion of iterative form when we start from root.left
# logic: just keep on going left and when left is none then pop the last added one(just same as recursive code, think little)

class Solution:
    def InOrder(self,root):
        if root== None:
            return []
        ans=  []
        stack= []
        stack.append(root)
        curr= root
        while stack :
            if curr.left== None:
                temp= stack.pop()
                ans.append(temp.data)
                if temp.right:
                    curr= temp.right
                    stack.append(temp.right)
            else:
                stack.append(curr.left)
                curr= curr.left
        return ans


# another concise way of iterative approach of inorder traversal. 
# just the conversion if we start from root. 
# logic: if root is not None we append and move to the left 
# if none then we print the last added ele into the stack and move to right

# better one. This will help in solving a lot of problem of BST
#  by just adding few lines or modifying few lines 
def InorderIterative(self,root):
    if root== None:
        return 
    stack, ans= [], []
    while stack or root:
        while root:  # keep going left 
            stack.append(root)
            root= root.left
        # if None, it means no left child then print the stack top (just pop).
        # it means we have reached the leftmost node.
        curr= stack.pop()
        ans.append(curr.val)
        root= curr.right  # move the pointer to check the right child.
    return ans



def PostorderRecursive(self,root):
    if root== None:
        return
    self.InorderRecursive(root.left) 
    self.InorderRecursive(root.right)
    print(root.data,end=" ")

# returning the ans inside a list in same function
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return []
        l= self.postorderTraversal(root.left)
        r= self.postorderTraversal(root.right)
        return l + r + [root.val]     # just the meaning of postorder
    
# Direct karna difficult h but agar hm reverse way me print kar de to last me hm ans ko reverse karke final ans mil jayega i.e:
# agar [left, right, root] ke jagah -> [root, right, left] solve kar de and then last me ans ko reverse kar denge.

# or usko hm preorder jaisa solve kar sakte h.
# append left 1st than right because we want right before left .
    

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return 
        stack, ans= [], []
        stack.append(root)
        while stack:
            curr= stack.pop()
            ans.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return ans[::-1]

# Simpler way
from typing import Optional, List

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack, ans = [], []
        curr = root

        while curr or stack:
            while curr:
                ans.append(curr.val)  # Process current node (reverse of postorder)
                stack.append(curr)  # Push to stack
                curr = curr.right  # Move to right child first
            
            curr = stack.pop()  # Backtrack
            curr = curr.left  # Move to left child
        
        return ans[::-1]  # Reverse to get postorder (left → right → root)

#Java Code
"""
import java.util.*;

class Solution {
    // Recursive preorder
    public void PreorderRecursive(TreeNode root) {
        if (root == null) {
            return;
        }
        System.out.print(root.data + " ");
        PreorderRecursive(root.left);
        PreorderRecursive(root.right);
    }

    // Iterative preorder (logic: push right first so left is processed first)
    public void PreorderIterative(TreeNode root) {
        if (root == null) return;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            System.out.print(curr.data + " ");
            if (curr.right != null) stack.push(curr.right);
            if (curr.left != null) stack.push(curr.left);
        }
    }

    // Easier iterative preorder
    public void PreorderIterativeEasier(TreeNode root) {
        if (root == null) return;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                System.out.print(curr.data + " ");
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            curr = curr.right;
        }
    }

    // Recursive preorder with returning list
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;
        ans.add(root.val);
        ans.addAll(preorderTraversal(root.left));
        ans.addAll(preorderTraversal(root.right));
        return ans;
    }

    // Another way of writing preorderTraversal
    public List<Integer> preorderTraversalAlt(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<Integer> left = preorderTraversalAlt(root.left);
        List<Integer> right = preorderTraversalAlt(root.right);
        List<Integer> res = new ArrayList<>();
        res.add(root.val);
        res.addAll(left);
        res.addAll(right);
        return res;
    }

    // Recursive inorder
    public void InorderRecursive(TreeNode root) {
        if (root == null) return;
        InorderRecursive(root.left);
        System.out.print(root.data + " ");
        InorderRecursive(root.right);
    }

    // Recursive inorder returning list
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<Integer> l = inorderTraversal(root.left);
        List<Integer> r = inorderTraversal(root.right);
        List<Integer> res = new ArrayList<>();
        res.addAll(l);
        res.add(root.val);
        res.addAll(r);
        return res;
    }

    // Iterative inorder approach 1 (with stack and current pointer)
    public List<Integer> InOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<Integer> ans = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        TreeNode curr = root;
        while (!stack.isEmpty()) {
            if (curr.left == null) {
                TreeNode temp = stack.pop();
                ans.add(temp.data);
                if (temp.right != null) {
                    curr = temp.right;
                    stack.push(temp.right);
                }
            } else {
                stack.push(curr.left);
                curr = curr.left;
            }
        }
        return ans;
    }

    // Iterative inorder approach 2 (better and concise)
    public List<Integer> InorderIterative(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        while (root != null || !stack.isEmpty()) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            TreeNode curr = stack.pop();
            ans.add(curr.val);
            root = curr.right;
        }
        return ans;
    }

    // Recursive postorder (printing)
    public void PostorderRecursive(TreeNode root) {
        if (root == null) return;
        InorderRecursive(root.left);
        InorderRecursive(root.right);
        System.out.print(root.data + " ");
    }

    // Recursive postorder returning list
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<Integer> l = postorderTraversal(root.left);
        List<Integer> r = postorderTraversal(root.right);
        List<Integer> res = new ArrayList<>();
        res.addAll(l);
        res.addAll(r);
        res.add(root.val);
        return res;
    }

    // Iterative postorder using reverse preorder and then reverse answer
    public List<Integer> postorderTraversalIterative(TreeNode root) {
        if (root == null) return new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            ans.add(curr.val);
            if (curr.left != null) stack.push(curr.left);
            if (curr.right != null) stack.push(curr.right);
        }
        Collections.reverse(ans);
        return ans;
    }

    // Simpler iterative postorder (reverse of [root, right, left])
    public List<Integer> postorderTraversalSimpler(TreeNode root) {
        if (root == null) return new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                ans.add(curr.val);
                stack.push(curr);
                curr = curr.right;
            }
            curr = stack.pop();
            curr = curr.left;
        }
        Collections.reverse(ans);
        return ans;
    }
}
"""

#C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    // Recursive preorder
    void PreorderRecursive(TreeNode* root) {
        if (root == nullptr) return;
        cout << root->data << " ";
        PreorderRecursive(root->left);
        PreorderRecursive(root->right);
    }

    // Iterative preorder (push right first)
    void PreorderIterative(TreeNode* root) {
        if (root == nullptr) return;
        stack<TreeNode*> st;
        st.push(root);
        while (!st.empty()) {
            TreeNode* curr = st.top(); st.pop();
            cout << curr->data << " ";
            if (curr->right) st.push(curr->right);
            if (curr->left) st.push(curr->left);
        }
    }

    // Easier iterative preorder
    void PreorderIterativeEasier(TreeNode* root) {
        if (root == nullptr) return;
        stack<TreeNode*> st;
        TreeNode* curr = root;
        while (curr || !st.empty()) {
            while (curr) {
                cout << curr->data << " ";
                st.push(curr);
                curr = curr->left;
            }
            curr = st.top(); st.pop();
            curr = curr->right;
        }
    }

    // Recursive preorder returning vector
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (!root) return ans;
        ans.push_back(root->val);
        vector<int> left = preorderTraversal(root->left);
        vector<int> right = preorderTraversal(root->right);
        ans.insert(ans.end(), left.begin(), left.end());
        ans.insert(ans.end(), right.begin(), right.end());
        return ans;
    }

    // Another way of writing preorderTraversal
    vector<int> preorderTraversalAlt(TreeNode* root) {
        if (!root) return {};
        vector<int> left = preorderTraversalAlt(root->left);
        vector<int> right = preorderTraversalAlt(root->right);
        vector<int> res = {root->val};
        res.insert(res.end(), left.begin(), left.end());
        res.insert(res.end(), right.begin(), right.end());
        return res;
    }

    // Recursive inorder (print)
    void InorderRecursive(TreeNode* root) {
        if (root == nullptr) return;
        InorderRecursive(root->left);
        cout << root->data << " ";
        InorderRecursive(root->right);
    }

    // Recursive inorder returning vector
    vector<int> inorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> l = inorderTraversal(root->left);
        vector<int> r = inorderTraversal(root->right);
        vector<int> res;
        res.insert(res.end(), l.begin(), l.end());
        res.push_back(root->val);
        res.insert(res.end(), r.begin(), r.end());
        return res;
    }

    // Iterative inorder approach 1
    vector<int> InOrder(TreeNode* root) {
        vector<int> ans;
        if (!root) return ans;
        stack<TreeNode*> st;
        st.push(root);
        TreeNode* curr = root;
        while (!st.empty()) {
            if (curr->left == nullptr) {
                TreeNode* temp = st.top(); st.pop();
                ans.push_back(temp->data);
                if (temp->right) {
                    curr = temp->right;
                    st.push(temp->right);
                }
            } else {
                st.push(curr->left);
                curr = curr->left;
            }
        }
        return ans;
    }

    // Iterative inorder approach 2
    vector<int> InorderIterative(TreeNode* root) {
        vector<int> ans;
        stack<TreeNode*> st;
        while (root || !st.empty()) {
            while (root) {
                st.push(root);
                root = root->left;
            }
            TreeNode* curr = st.top(); st.pop();
            ans.push_back(curr->val);
            root = curr->right;
        }
        return ans;
    }

    // Recursive postorder (print)
    void PostorderRecursive(TreeNode* root) {
        if (!root) return;
        InorderRecursive(root->left);
        InorderRecursive(root->right);
        cout << root->data << " ";
    }

    // Recursive postorder returning vector
    vector<int> postorderTraversal(TreeNode* root) {
        if (!root) return {};
        vector<int> l = postorderTraversal(root->left);
        vector<int> r = postorderTraversal(root->right);
        vector<int> res;
        res.insert(res.end(), l.begin(), l.end());
        res.insert(res.end(), r.begin(), r.end());
        res.push_back(root->val);
        return res;
    }

    // Iterative postorder using reverse preorder
    vector<int> postorderTraversalIterative(TreeNode* root) {
        if (!root) return {};
        stack<TreeNode*> st;
        vector<int> ans;
        st.push(root);
        while (!st.empty()) {
            TreeNode* curr = st.top(); st.pop();
            ans.push_back(curr->val);
            if (curr->left) st.push(curr->left);
            if (curr->right) st.push(curr->right);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }

    // Simpler iterative postorder (reverse of [root, right, left])
    vector<int> postorderTraversalSimpler(TreeNode* root) {
        if (!root) return {};
        stack<TreeNode*> st;
        vector<int> ans;
        TreeNode* curr = root;
        while (curr || !st.empty()) {
            while (curr) {
                ans.push_back(curr->val);
                st.push(curr);
                curr = curr->right;
            }
            curr = st.top(); st.pop();
            curr = curr->left;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};

"""
