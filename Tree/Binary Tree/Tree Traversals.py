# 1) Preorder 

# 1.1) Recursive

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans= []
        if not root:
            return ans
        ans.append(root.val)
        ans+= self.preorderTraversal(root.left)
        ans+= self.preorderTraversal(root.right)
        return ans

# Java Code 
"""
import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) {
            return ans;
        }
        ans.add(root.val);
        ans.addAll(preorderTraversal(root.left));
        ans.addAll(preorderTraversal(root.right));
        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> ans;
        if (root == nullptr) {
            return ans;
        }
        ans.push_back(root->val);
        vector<int> left = preorderTraversal(root->left);
        ans.insert(ans.end(), left.begin(), left.end());
        vector<int> right = preorderTraversal(root->right);
        ans.insert(ans.end(), right.begin(), right.end());
        return ans;
    }
};
"""
# 1.1.1) Other way of writing recursive code
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left=  self.preorderTraversal(root.left)
        right= self.preorderTraversal(root.right)
        return [root.val] + left +  right   # just the logic of inorder traversal.
 
# Java Code 
"""
import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<Integer> left = preorderTraversal(root.left);
        List<Integer> right = preorderTraversal(root.right);
        List<Integer> result = new ArrayList<>();
        result.add(root.val);
        result.addAll(left);
        result.addAll(right);
        return result;  // just the logic of inorder traversal.
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        vector<int> left = preorderTraversal(root->left);
        vector<int> right = preorderTraversal(root->right);
        vector<int> result;
        result.push_back(root->val);
        result.insert(result.end(), left.begin(), left.end());
        result.insert(result.end(), right.begin(), right.end());
        return result;  // just the logic of inorder traversal.
    }
};
"""
# 1.2) Iterative
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

# Java Code 
"""
import java.util.Stack;

class TreeNode {
    int data;
    TreeNode left, right;
    TreeNode(int x) { data = x; }
}

class Solution {
    public void PreorderIterative(TreeNode root) {
        if (root == null) {
            return;
        }
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            System.out.print(curr.data + " ");
            if (curr.right != null) {
                stack.push(curr.right);
            }
            if (curr.left != null) {
                stack.push(curr.left);
            }
        }
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <stack>
using namespace std;

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : data(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    void PreorderIterative(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        stack<TreeNode*> stack;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* curr = stack.top();
            stack.pop();
            cout << curr->data << " ";
            if (curr->right != nullptr) {
                stack.push(curr->right);
            }
            if (curr->left != nullptr) {
                stack.push(curr->left);
            }
        }
    }
};
"""

# 1.3) Easier way for iterative
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

# Java Code 
"""
import java.util.Stack;

class TreeNode {
    int data;
    TreeNode left, right;
    TreeNode(int x) { data = x; }
}

class Solution {
    public void PreorderIterative(TreeNode root) {
        if (root == null) {
            return;
        }

        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                System.out.print(curr.data + " ");  // Process current node
                stack.push(curr);  // Push current node to stack
                curr = curr.left;  // Move to left child
            }

            curr = stack.pop();  // Backtrack
            curr = curr.right;  // Move to right child
        }
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <stack>
using namespace std;

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : data(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    void PreorderIterative(TreeNode* root) {
        if (root == nullptr) {
            return;
        }

        stack<TreeNode*> stack;
        TreeNode* curr = root;
        while (curr != nullptr || !stack.empty()) {
            while (curr != nullptr) {
                cout << curr->data << " ";  // Process current node
                stack.push(curr);  // Push current node to stack
                curr = curr->left;  // Move to left child
            }

            curr = stack.top(); stack.pop();  // Backtrack
            curr = curr->right;  // Move to right child
        }
    }
};
"""

# 2) Inorder    

# 2.1) Recursive

# recursive way: returning the ans in a list inside same function 
# just same as preorder,only change of meaning
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return []
        l= self.inorderTraversal(root.left)
        r= self.inorderTraversal(root.right)
        return l+ [root.val] + r        # just the meaning of inorder


# Java Code 
"""
import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<Integer> l = inorderTraversal(root.left);
        List<Integer> r = inorderTraversal(root.right);
        List<Integer> result = new ArrayList<>();
        result.addAll(l);
        result.add(root.val);
        result.addAll(r);
        return result;  // just the meaning of inorder
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        vector<int> l = inorderTraversal(root->left);
        vector<int> r = inorderTraversal(root->right);
        vector<int> result;
        result.insert(result.end(), l.begin(), l.end());
        result.push_back(root->val);
        result.insert(result.end(), r.begin(), r.end());
        return result;  // just the meaning of inorder
    }
};
"""

# 2.2) 
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

# Java Code 
"""
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class TreeNode {
    int data;
    TreeNode left, right;
    TreeNode(int x) { data = x; }
}

class Solution {
    public List<Integer> InOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
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
}
"""
# C++ Code 
"""
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : data(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> InOrder(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        vector<int> ans;
        stack<TreeNode*> stack;
        stack.push(root);
        TreeNode* curr = root;
        while (!stack.empty()) {
            if (curr->left == nullptr) {
                TreeNode* temp = stack.top(); stack.pop();
                ans.push_back(temp->data);
                if (temp->right != nullptr) {
                    curr = temp->right;
                    stack.push(temp->right);
                }
            } else {
                stack.push(curr->left);
                curr = curr->left;
            }
        }
        return ans;
    }
};
"""

# 2.3) Another concise way of iterative approach of inorder traversal. 
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


# Java Code 
"""
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> InorderIterative(TreeNode root) {
        if (root == null) {
            return null;
        }
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        while (!stack.isEmpty() || root != null) {
            while (root != null) {  // keep going left 
                stack.push(root);
                root = root.left;
            }
            // if None, it means no left child then print the stack top (just pop).
            // it means we have reached the leftmost node.
            TreeNode curr = stack.pop();
            ans.add(curr.val);
            root = curr.right;  // move the pointer to check the right child.
        }
        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> InorderIterative(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        stack<TreeNode*> stack;
        vector<int> ans;
        while (!stack.empty() || root != nullptr) {
            while (root != nullptr) {  // keep going left 
                stack.push(root);
                root = root->left;
            }
            // if None, it means no left child then print the stack top (just pop).
            // it means we have reached the leftmost node.
            TreeNode* curr = stack.top(); stack.pop();
            ans.push_back(curr->val);
            root = curr->right;  // move the pointer to check the right child.
        }
        return ans;
    }
};
"""

# 3) PostOrder

# 3.1) Recursive

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root== None:
            return []
        l= self.postorderTraversal(root.left)
        r= self.postorderTraversal(root.right)
        return l + r + [root.val]     # just the meaning of postorder


# Java Code 
"""
import java.util.ArrayList;
import java.util.List;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<Integer> l = postorderTraversal(root.left);
        List<Integer> r = postorderTraversal(root.right);
        List<Integer> result = new ArrayList<>();
        result.addAll(l);
        result.addAll(r);
        result.add(root.val);
        return result;     // just the meaning of postorder
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        vector<int> l = postorderTraversal(root->left);
        vector<int> r = postorderTraversal(root->right);
        vector<int> result;
        result.insert(result.end(), l.begin(), l.end());
        result.insert(result.end(), r.begin(), r.end());
        result.push_back(root->val);
        return result;     // just the meaning of postorder
    }
};
"""

# 3.2) Iterative

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


# Java Code 
"""
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) {
            return null;
        }
        Stack<TreeNode> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode curr = stack.pop();
            ans.add(curr.val);
            if (curr.left != null) {
                stack.push(curr.left);
            }
            if (curr.right != null) {
                stack.push(curr.right);
            }
        }
        List<Integer> reversed = new ArrayList<>();
        for (int i = ans.size() - 1; i >= 0; i--) {
            reversed.add(ans.get(i));
        }
        return reversed;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        stack<TreeNode*> stack;
        vector<int> ans;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* curr = stack.top(); stack.pop();
            ans.push_back(curr->val);
            if (curr->left) {
                stack.push(curr->left);
            }
            if (curr->right) {
                stack.push(curr->right);
            }
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
"""

# 3.3) Iterative : Simpler way
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

# Java Code 
"""
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }

        Stack<TreeNode> stack = new Stack<>();
        List<Integer> ans = new ArrayList<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                ans.add(curr.val);  // Process current node (reverse of postorder)
                stack.push(curr);  // Push to stack
                curr = curr.right;  // Move to right child first
            }

            curr = stack.pop();  // Backtrack
            curr = curr.left;  // Move to left child
        }

        List<Integer> reversed = new ArrayList<>();
        for (int i = ans.size() - 1; i >= 0; i--) {
            reversed.add(ans.get(i));  // Reverse to get postorder (left → right → root)
        }
        return reversed;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }

        stack<TreeNode*> stack;
        vector<int> ans;
        TreeNode* curr = root;

        while (curr != nullptr || !stack.empty()) {
            while (curr != nullptr) {
                ans.push_back(curr->val);  // Process current node (reverse of postorder)
                stack.push(curr);  // Push to stack
                curr = curr->right;  // Move to right child first
            }

            curr = stack.top(); stack.pop();  // Backtrack
            curr = curr->left;  // Move to left child
        }

        reverse(ans.begin(), ans.end());  // Reverse to get postorder (left → right → root)
        return ans;
    }
};
"""