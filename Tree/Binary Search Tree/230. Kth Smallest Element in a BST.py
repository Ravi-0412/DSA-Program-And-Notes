# method 1:

"""
Do any traversal and then sort the ans and then return the kth ele from start
time: O(n*logn), space: O(n)
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        all_vals = inorder(root)
        all_vals.sort()
        return all_vals[k - 1]

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> allVals = inorder(root);  // all_vals = inorder(root)
        // no need to sort — inorder traversal of BST gives sorted values
        return allVals.get(k - 1);
    }

    private List<Integer> inorder(TreeNode node) {
        List<Integer> res = new ArrayList<>();
        if (node == null) return res;
        res.addAll(inorder(node.left));
        res.add(node.val);
        res.addAll(inorder(node.right));
        return res;
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
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        vector<int> allVals = inorder(root);  // all_vals = inorder(root)
        // no need to sort — inorder traversal of BST gives sorted values
        return allVals[k - 1];
    }

    vector<int> inorder(TreeNode* node) {
        vector<int> res;
        if (!node) return res;
        vector<int> left = inorder(node->left);
        vector<int> right = inorder(node->right);
        res.insert(res.end(), left.begin(), left.end());
        res.push_back(node->val);
        res.insert(res.end(), right.begin(), right.end());
        return res;
    }
};
"""
# method 2: 
"""
just find the inorder traversal of the tree and return the kth element from the start
inorder always give the ans in sorted form for BST
time: O(n), space: O(n) for ans + recursion depth
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result[k - 1]

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    List<Integer> result = new ArrayList<>();

    public int kthSmallest(TreeNode root, int k) {
        inorder(root); 
        return result.get(k - 1);
    }

    void inorder(TreeNode node) {
        if (node == null) return;
        inorder(node.left);
        result.add(node.val);
        inorder(node.right);
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
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> result;

    int kthSmallest(TreeNode* root, int k) {
        inorder(root);  // perform in-order traversal and populate result
        return result[k - 1];
    }

    void inorder(TreeNode* node) {
        if (!node) return;
        inorder(node->left);
        result.push_back(node->val);
        inorder(node->right);
    }
};
"""
# Method 3
"""
Rather than storing the ans in any array just keep a count for method 2
and increment the count when you add any ele to the ans 
and when count reaches 'k' just print the value of that node
time: O(n), space: O(n) recursion depth.

Note: to avoid the space complexity we can use the morris inorder traversal.
"""

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.result

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int count = 0;
    Integer result = null;

    public int kthSmallest(TreeNode root, int k) {
        inorder(root, k);
        return result;
    }

    void inorder(TreeNode node, int k) {
        if (node == null || result != null) return;
        inorder(node.left, k);
        count++;
        if (count == k) {
            result = node.val;
            return;
        }
        inorder(node.right, k);
    }
}
"""
# C++ Code 
"""
#include <optional>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int count = 0;
    int result = -1;

    int kthSmallest(TreeNode* root, int k) {
        inorder(root, k);
        return result;
    }

    void inorder(TreeNode* node, int k) {
        if (!node || result != -1) return;
        inorder(node->left, k);
        count++;
        if (count == k) {
            result = node->val;
            return;
        }
        inorder(node->right, k);
    }
};
"""

# Method 4: 
"""
Optimsing to O(1) space
Logic: Smallest node will be the leftmost node.
so once you find '.left' of any node = None then that will be the smallest node as of now.
And to get the next smaller node , move to its right.

If it's right is also None then it will do backtrack function call to previous node and calculate in same way.
"""

# My mistake
# Note: if we do taking 'k' in function call only then we will get wrong ans
# because after backtrack value of 'k' will be won't change for that function.
# but it should change globally like above.

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findKthSmallest(root, k):
            if root.left:
                findKthSmallest(root.left, k)
            k -= 1
            if k == 0:
                self.ans = root.val
                return
            # next smaller we will get from right side of root
            if root.right:
                findKthSmallest(root.right, k)

        self.ans = -1
        findKthSmallest(root, k)
        return self.ans
    
# Correct solution

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findKthSmallest(root):
            if root.left:
                findKthSmallest(root.left)
            self.count -= 1
            if self.count == 0:
                self.ans = root.val
                return
            # next smaller we will get from right side of root
            if root.right:
                findKthSmallest(root.right)

        self.ans = -1
        self.count = k
        findKthSmallest(root)
        return self.ans

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int count;
    int ans = -1;

    public int kthSmallest(TreeNode root, int k) {
        this.count = k;
        findKthSmallest(root);
        return ans;
    }

    void findKthSmallest(TreeNode root) {
        if (root.left != null) {
            findKthSmallest(root.left);
        }

        count--;
        if (count == 0) {
            ans = root.val;
            return;
        }

        // next smaller we will get from right side of root
        if (root.right != null) {
            findKthSmallest(root.right);
        }
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
    int count;
    int ans = -1;

    int kthSmallest(TreeNode* root, int k) {
        count = k;
        findKthSmallest(root);
        return ans;
    }

    void findKthSmallest(TreeNode* root) {
        if (root->left) {
            findKthSmallest(root->left);
        }

        count--;
        if (count == 0) {
            ans = root->val;
            return;
        }

        // next smaller we will get from right side of root
        if (root->right) {
            findKthSmallest(root->right);
        }
    }
};
"""

# Method 5: 
        
# Solution by taking 'k' as parameter and without ans as global variable
"""
Why are we returning root.val, k both , why are we not only returning root.val?
In each recursive call, k needs to be updated and passed to the next call
(because k decreases as we visit nodes). If we don't return the updated k, 
we won't know which node is the k-th smallest as the recursion unwinds.
Return Early (root.val): The value of the k-th smallest element can only be found at one point, 
and we need to pass that result up through the recursion without continuing the traversal once it's found.


Note : Q) Why Method 5 is working and Method 4(My mistake) is not.
i) left, k = findKthSmallest(root.left, k)   => Replacing k with the updated value returned by the recursive call.
ii) ❌ First version: k is passed by value and modified locally — changes aren't reflected across recursive calls, so the count is lost.

✅ Second version: Returns the updated k along with the result — each call gets the new k, maintaining correct state across recursion.
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findKthSmallest(root, k):
            if not root:
                return None, k
            
            # Explore the left subtree
            left, k = findKthSmallest(root.left, k)
            if left is not None:
                return left, k  # If k-th smallest is found in left subtree, return it
            
            # Decrement k as we process the current node
            k -= 1
            if k == 0:
                return root.val, k  # If the current node is the k-th smallest, return it
            
            # Explore the right subtree
            return findKthSmallest(root.right, k)

        result, _ = findKthSmallest(root, k)
        return result

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Pair result = findKthSmallest(root, k);
        return result.value;
    }

    class Pair {
        int value;
        int k;
        Pair(int value, int k) {
            this.value = value;
            this.k = k;
        }
    }

    private Pair findKthSmallest(TreeNode root, int k) {
        if (root == null) return new Pair(-1, k);

        // Explore the left subtree
        Pair left = findKthSmallest(root.left, k);
        if (left.value != -1) return left;  // If k-th smallest is found in left subtree, return it

        // Decrement k as we process the current node
        k = left.k - 1;
        if (k == 0) return new Pair(root.val, k);  // If the current node is the k-th smallest, return it

        // Explore the right subtree
        return findKthSmallest(root.right, k);
    }
}
"""
# C++ Code 
"""
#include <utility>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        pair<int, int> result = findKthSmallest(root, k);
        return result.first;
    }

    pair<int, int> findKthSmallest(TreeNode* root, int k) {
        if (!root) return {-1, k};

        // Explore the left subtree
        auto left = findKthSmallest(root->left, k);
        if (left.first != -1) return left;  // If k-th smallest is found in left subtree, return it

        // Decrement k as we process the current node
        k = left.second - 1;
        if (k == 0) return {root->val, k};  // If the current node is the k-th smallest, return it

        // Explore the right subtree
        return findKthSmallest(root->right, k);
    }
};
"""