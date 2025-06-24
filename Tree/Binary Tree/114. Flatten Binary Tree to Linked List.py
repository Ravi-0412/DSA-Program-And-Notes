# Method 1:
# Just store the preorder traversal in a list and ten connect all those to get the ans.
# space = time = O(n)


# Method 2: Space optimisation to O(1)
# Logic: Agar hm first time kisi node ko dekhte hi connect karenge tb wrong ans dega.
# Kyonki hm dusre node ko tabhi isse connect kar sakte h jb dusar node already flattened ho.
# Iske liye hm bottom up jana hoga.

# Now 1) current node ka right ko 'left' wale ke saath karna h agar 'left' is not None else 'right' wale child ke saath.
# 2) Then left wala ka last node se 'right' ko connect kar dena h.
# 3) cur node ka left ko null kar dena h.
# 4) cur node ko return kar dena h

# Not vvi: Aise Question me yhi logic lagana h , bhut simple h.
# e.g: in Q "430. Flatten a Multilevel Doubly Linked List"

# time: O(n)

class Solution(object):
    def flatten(self, root):
        if not root:
            return None
        l = self.flatten(root.left)
        r = self.flatten(root.right)
        # first connect the next node that will come in preorder traversal 
        root.right = l if l else r   # if 'l' is not 'None' then it will come else 'r' will come
        # Now connect the right child with last node of left one. we only need to do this if both 'l' and 'r' are None
        if l and r:
            cur = l
            # 'l' and 'r' is already flattened so we need to tarverse with the help of 'right' pointer only.
            while cur.right:
                cur = cur.right
            cur.right = r  # 
        # Make 'cur' left pointer = None
        root.left = None  
        return root
    
# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode flatten(TreeNode root) {
        if (root == null) {
            return null;
        }
        TreeNode l = flatten(root.left);
        TreeNode r = flatten(root.right);
        // first connect the next node that will come in preorder traversal 
        root.right = (l != null) ? l : r;   // if 'l' is not 'None' then it will come else 'r' will come
        // Now connect the right child with last node of left one. we only need to do this if both 'l' and 'r' are None
        if (l != null && r != null) {
            TreeNode cur = l;
            // 'l' and 'r' is already flattened so we need to tarverse with the help of 'right' pointer only.
            while (cur.right != null) {
                cur = cur.right;
            }
            cur.right = r;  // 
        }
        // Make 'cur' left pointer = None
        root.left = null;  
        return root;
    }
}
"""
# C++ Code 
"""
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* flatten(TreeNode* root) {
        if (root == nullptr) {
            return nullptr;
        }
        TreeNode* l = flatten(root->left);
        TreeNode* r = flatten(root->right);
        // first connect the next node that will come in preorder traversal 
        root->right = (l != nullptr) ? l : r;   // if 'l' is not 'None' then it will come else 'r' will come
        // Now connect the right child with last node of left one. we only need to do this if both 'l' and 'r' are None
        if (l != nullptr && r != nullptr) {
            TreeNode* cur = l;
            // 'l' and 'r' is already flattened so we need to tarverse with the help of 'right' pointer only.
            while (cur->right != nullptr) {
                cur = cur->right;
            }
            cur->right = r;  // 
        }
        // Make 'cur' left pointer = None
        root->left = nullptr;  
        return root;
    }
};
"""

# method 2: 
# in above one first we were going root then left then right like preorder only
# in this we are going opposite first root then right and then then left   # reverse postorder
# logic(ye sb type Q ke liye): jisko bad me add karna h usko phle visit karke 'pre' bna do

# point left(for ans 'right') to pre and this will automatically point to the 'preorder successor' 
# make left pointer= None

# pre will conatain the ans calculated till now
# so make pre point to root after each node .
# and at last return pre

# basically instead of using while loop for pointing the right side with last node of left , pre is working here
# as pre is storing the ans calculated till now.

 
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.pre= None
        def dfs(root):
            if root== None:
                return  # not storing so simply return 
            dfs(root.right)
            dfs(root.left)
            root.right= self.pre
            root.left= None
            self.pre= root   # means we have visited till this root node
     
        dfs(root)
        return self.pre
    
# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    TreeNode pre = null;

    public TreeNode flatten(TreeNode root) {
        dfs(root);
        return pre;
    }

    void dfs(TreeNode root) {
        if (root == null) {
            return;  // not storing so simply return
        }
        dfs(root.right);
        dfs(root.left);
        root.right = pre;
        root.left = null;
        pre = root;   // means we have visited till this root node
    }
}
"""
# C++ Code 
"""
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* pre = nullptr;

    TreeNode* flatten(TreeNode* root) {
        dfs(root);
        return pre;
    }

    void dfs(TreeNode* root) {
        if (root == nullptr) {
            return;  // not storing so simply return
        }
        dfs(root->right);
        dfs(root->left);
        root->right = pre;
        root->left = nullptr;
        pre = root;   // means we have visited till this root node
    }
};
"""

# Method 3: 
# iterative one. just like do preorder only
# very simple: every time you get any node then add to the 'last of right' and make the last.left= None
# but extra space: o(n)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root== None:
            return root
        last= TreeNode(-1)  # can initialise with any val as it will start checking after we make connection from given root in the ans
        stack= [(root)]
        while stack:
            node= stack.pop()
            last.right= node
            last.left= None
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            last= node # to point the next node from the last added one

    
# Java Code 
"""
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public void flatten(TreeNode root) {
        if (root == null) {
            return;
        }
        TreeNode last = new TreeNode(-1);  // can initialise with any val as it will start checking after we make connection from given root in the ans
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            last.right = node;
            last.left = null;
            if (node.right != null) {
                stack.push(node.right);
            }
            if (node.left != null) {
                stack.push(node.left);
            }
            last = node; // to point the next node from the last added one
        }
    }
}
"""
# C++ Code 
"""
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
    void flatten(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        TreeNode* last = new TreeNode(-1);  // can initialise with any val as it will start checking after we make connection from given root in the ans
        stack<TreeNode*> stack;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* node = stack.top(); stack.pop();
            last->right = node;
            last->left = nullptr;
            if (node->right) {
                stack.push(node->right);
            }
            if (node->left) {
                stack.push(node->left);
            }
            last = node; // to point the next node from the last added one
        }
    }
};
"""