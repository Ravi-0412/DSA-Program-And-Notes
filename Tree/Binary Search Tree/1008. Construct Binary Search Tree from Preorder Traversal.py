# Method 1:
#  just find out the inorder traversal by sorting the array and Apply "convert into binary tree given preorder and inorder"
# of binary tree.
# Time: O(n* logn)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder= sorted(preorder)
        return self.buildTree(preorder, inorder)
    
    def buildTree(self, preorder, inorder):
        if not inorder: # or preorder
            return None
        root= TreeNode(preorder[0])   # this will be the root

        # find the index of 1st ele of prerorder in inorder to check all nodes will go the left of parent and right of parent.
        ind= inorder.index(preorder[0])
        # all the ele from index '1' till 'ind' will come to the left in preorder(1st ele already included.) and all the ele before the indx in inorder will come to the left subtree(ind ele already included)
        root.left=  self.buildTree(preorder[1:ind+1], inorder[:ind])
        # all the ele after the indx will come to right of both preorder and inorder.
        root.right= self.buildTree(preorder[ind+1 :], inorder[ind+1 :])                

        return root

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        int[] inorder = preorder.clone();
        java.util.Arrays.sort(inorder);  // inorder = sorted(preorder)
        return buildTree(preorder, 0, preorder.length - 1, inorder, 0, inorder.length - 1);
    }

    public TreeNode buildTree(int[] preorder, int preStart, int preEnd, int[] inorder, int inStart, int inEnd) {
        if (inStart > inEnd) return null;

        TreeNode root = new TreeNode(preorder[preStart]);  // this will be the root

        // find the index of 1st ele of preorder in inorder to check all nodes
        // will go to the left of parent and right of parent.
        int ind = inStart;
        while (inorder[ind] != preorder[preStart]) ind++;

        // number of elements in left subtree
        int leftSize = ind - inStart;

        // all the ele from index '1' till 'ind' will come to the left in preorder
        // and all the ele before the indx in inorder will come to the left subtree
        root.left = buildTree(preorder, preStart + 1, preStart + leftSize, inorder, inStart, ind - 1);

        // all the ele after the indx will come to right of both preorder and inorder.
        root.right = buildTree(preorder, preStart + leftSize + 1, preEnd, inorder, ind + 1, inEnd);

        return root;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        vector<int> inorder = preorder;
        sort(inorder.begin(), inorder.end());  // inorder = sorted(preorder)
        return buildTree(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }

    TreeNode* buildTree(const vector<int>& preorder, int preStart, int preEnd,
                        const vector<int>& inorder, int inStart, int inEnd) {
        if (inStart > inEnd) return nullptr;

        TreeNode* root = new TreeNode(preorder[preStart]);  // this will be the root

        // find the index of 1st ele of preorder in inorder to check all nodes
        // will go to the left of parent and right of parent.
        int ind = inStart;
        while (inorder[ind] != preorder[preStart]) ind++;

        // number of elements in left subtree
        int leftSize = ind - inStart;

        // all the ele from index '1' till 'ind' will come to the left in preorder
        // and all the ele before the indx in inorder will come to the left subtree
        root->left = buildTree(preorder, preStart + 1, preStart + leftSize, inorder, inStart, ind - 1);

        // all the ele after the indx will come to right of both preorder and inorder.
        root->right = buildTree(preorder, preStart + leftSize + 1, preEnd, inorder, ind + 1, inEnd);

        return root;
    }
};
"""

# method 2: 
# simply sort and then apply the "convert the given sorted array into Balanced BST".
# time: O(n*logn) for both methods.

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        # Step 1: Sort the preorder traversal to get inorder traversal
        inorder = sorted(preorder)

        # Step 2: Build a map for quick lookup of indices in inorder
        index_map = {val: i for i, val in enumerate(inorder)}

        # Step 3: Recursive function to build tree from inorder using preorder
        def build_tree(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Find the root index in the inorder array
            in_root_index = index_map[root_val]
            left_tree_size = in_root_index - in_start

            # Recursively build left and right subtrees
            root.left = build_tree(pre_start + 1, pre_start + left_tree_size, in_start, in_root_index - 1)
            root.right = build_tree(pre_start + left_tree_size + 1, pre_end, in_root_index + 1, in_end)

            return root

        return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)

# Java Code 
"""
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        if (preorder == null || preorder.length == 0) return null;

        // Step 1: Sort the preorder traversal to get inorder traversal
        int[] inorder = Arrays.copyOf(preorder, preorder.length);
        Arrays.sort(inorder);

        // Step 2: Build a map for quick lookup of indices in inorder
        Map<Integer, Integer> indexMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            indexMap.put(inorder[i], i);
        }

        // Step 3: Recursive function to build tree from inorder using preorder
        return buildTree(preorder, 0, preorder.length - 1, 0, inorder.length - 1, indexMap);
    }

    private TreeNode buildTree(int[] preorder, int preStart, int preEnd,
                               int inStart, int inEnd, Map<Integer, Integer> indexMap) {
        if (preStart > preEnd || inStart > inEnd) return null;

        int rootVal = preorder[preStart];
        TreeNode root = new TreeNode(rootVal);

        // Find the root index in the inorder array
        int inRootIndex = indexMap.get(rootVal);
        int leftTreeSize = inRootIndex - inStart;

        // Recursively build left and right subtrees
        root.left = buildTree(preorder, preStart + 1, preStart + leftTreeSize,
                              inStart, inRootIndex - 1, indexMap);
        root.right = buildTree(preorder, preStart + leftTreeSize + 1, preEnd,
                               inRootIndex + 1, inEnd, indexMap);

        return root;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        if (preorder.empty()) return nullptr;

        // Step 1: Sort the preorder traversal to get inorder traversal
        vector<int> inorder = preorder;
        sort(inorder.begin(), inorder.end());

        // Step 2: Build a map for quick lookup of indices in inorder
        unordered_map<int, int> indexMap;
        for (int i = 0; i < inorder.size(); ++i) {
            indexMap[inorder[i]] = i;
        }

        // Step 3: Recursive function to build tree from inorder using preorder
        return buildTree(preorder, 0, preorder.size() - 1,
                         0, inorder.size() - 1, indexMap);
    }

    TreeNode* buildTree(const vector<int>& preorder, int preStart, int preEnd,
                        int inStart, int inEnd,
                        unordered_map<int, int>& indexMap) {
        if (preStart > preEnd || inStart > inEnd) return nullptr;

        int rootVal = preorder[preStart];
        TreeNode* root = new TreeNode(rootVal);

        // Find the root index in the inorder array
        int inRootIndex = indexMap[rootVal];
        int leftTreeSize = inRootIndex - inStart;

        // Recursively build left and right subtrees
        root->left = buildTree(preorder, preStart + 1, preStart + leftTreeSize,
                               inStart, inRootIndex - 1, indexMap);
        root->right = buildTree(preorder, preStart + leftTreeSize + 1, preEnd,
                                inRootIndex + 1, inEnd, indexMap);

        return root;
    }
};
"""

# method 3: 
# Take each ele in preorder and apply the normal method to form BST i.e insert node in BST one by one.
# time: O(n*logn).

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        def insert(root, val):
            if not root:
                return TreeNode(val)
            if val < root.val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
            return root

        root = TreeNode(preorder[0])
        for val in preorder[1:]:
            insert(root, val)

        return root

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        if (preorder.length == 0) return null;

        TreeNode root = new TreeNode(preorder[0]);
        for (int i = 1; i < preorder.length; i++) {
            insert(root, preorder[i]);
        }
        return root;
    }

    private TreeNode insert(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);

        if (val < root.val) {
            root.left = insert(root.left, val);
        } else {
            root.right = insert(root.right, val);
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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        if (preorder.empty()) return nullptr;

        TreeNode* root = new TreeNode(preorder[0]);
        for (int i = 1; i < preorder.size(); ++i) {
            insert(root, preorder[i]);
        }
        return root;
    }

private:
    TreeNode* insert(TreeNode* root, int val) {
        if (!root) return new TreeNode(val);

        if (val < root->val) {
            root->left = insert(root->left, val);
        } else {
            root->right = insert(root->right, val);
        }
        return root;
    }
};
"""

# Method 4:

"""
Idea is simple: 
1) First item in preorder list is the root to be considered.
2) For next item in preorder list, there are 2 cases to consider:
2.a) If value is less than last item in stack, it is the left child of last item.
2.b) If value is greater than last item in stack, pop it.
      The last popped item will be the parent and the item will be the right child of the parent.
"""

"""
How to think of this logic?
Q. How to come up with this logic?
Ans: Just given the preorder, draw the BST on paper and analyse how you are putting the nodes and 
which Data Structure we can use to get BST directly from preorder.

Q. why we are directly adding when num is samller and poping before adding when num is greater?
Ans: if smaller means that must be the left child of the just previous ele in stack , 
Because we are doing acc to the preorder and in preorder we will move to left after root and 
it is BST so smaller ele will be on left.(root, left right,)
vvi: until we find any ele greater than top of stack, all those num will be go as left child only(like skew tree).
And we will find any ele greater then we will search for the node to which 'num' will be the right child.  
(now direction of tree will change).
i.e we will find the last smaller ele from the current num. 'num' will be the right child of that ele.

That's why we are using stack.
"""

# Time = space = O(n)

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # The first element is always the root in a preorder traversal
        root = TreeNode(preorder[0])
        # Stack stores the 'path' of ancestors we can still attach children to
        stack = [root]
        
        for value in preorder[1:]:
            # Case 1: Value is smaller than the current node (top of stack)
            # In a BST, this MUST be the left child.
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left) # Move deeper into the left branch
            
            # Case 2: Value is larger than the current node
            # This means the current 'left-leaning' branch is finished.
            # We must find the lowest ancestor that this value can be a right child of.
            else:
                while stack and stack[-1].val < value:
                    # 'last' will eventually hold the node that becomes the parent
                    last = stack.pop()
                
                # Attach the value as the right child of the last popped ancestor
                last.right = TreeNode(value)
                # This new right child is now the current path, so add it to the stack
                stack.append(last.right)
                
        return root


# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        TreeNode root = new TreeNode(preorder[0]);
        java.util.Stack<TreeNode> stack = new java.util.Stack<>();
        stack.push(root);

        for (int i = 1; i < preorder.length; i++) {
            TreeNode node = new TreeNode(preorder[i]);

            if (preorder[i] < stack.peek().val) {
                stack.peek().left = node;
                stack.push(node);
            } else {
                TreeNode last = null;
                while (!stack.isEmpty() && stack.peek().val < preorder[i]) {
                    last = stack.pop();
                }
                last.right = node;
                stack.push(node);
            }
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

struct TreeNode {
    int val;
    TreeNode* left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        TreeNode* root = new TreeNode(preorder[0]);
        stack<TreeNode*> st;
        st.push(root);

        for (int i = 1; i < preorder.size(); ++i) {
            TreeNode* node = new TreeNode(preorder[i]);

            if (preorder[i] < st.top()->val) {
                st.top()->left = node;
                st.push(node);
            } else {
                TreeNode* last = nullptr;
                while (!st.empty() && st.top()->val < preorder[i]) {
                    last = st.top();
                    st.pop();
                }
                last->right = node;
                st.push(node);
            }
        }

        return root;
    }
};
"""

# Method 5: 
"""
with Recursion
Time: O(n), space = O(H) 

Instead of searching for where the left subtree ends and the right begins, we can simply tell each recursive call what the maximum possible value it is allowed to accept.
    When we go Left, the current node's value becomes the new upper bound.
    When we go Right, the upper bound remains the same as what the parent was told.

"""

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Track our current position in the preorder list across recursive calls
        self.index = 0
        
        def solve(upper_bound):
            # If we've used all values or the current value exceeds the 
            # allowed limit for this subtree, this branch is finished.
            if self.index == len(preorder) or preorder[self.index] > upper_bound:
                return None
            
            # Create the root for the current subtree
            root_val = preorder[self.index]
            root = TreeNode(root_val)
            self.index += 1
            
            # For the LEFT subtree, the values must be smaller than the current root
            root.left = solve(root_val)
            
            # For the RIGHT subtree, the values can be anything up to the 
            # parent's upper bound.
            root.right = solve(upper_bound)
            
            return root
            
        # Initially, the root can be any value (infinity)
        return solve(float('inf'))
