# method 1: 
"""
store the inorder 
now problem reduces to "Two sum"
then apply the two pointer approach for find the pair since inorder will be a sorted array 
space= time= O(n)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Step 1: Get the in-order traversal (sorted array)
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        nums = inorder(root)
        
        # Step 2: Apply two-pointer approach
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1

        return False

# Java Code 
"""
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public boolean findTarget(TreeNode root, int k) {
        // Step 1: Get the in-order traversal (sorted array)
        List<Integer> nums = inorder(root);

        // Step 2: Apply two-pointer approach
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int total = nums.get(left) + nums.get(right);
            if (total == k) return true;
            else if (total < k) left++;
            else right--;
        }

        return false;
    }

    private List<Integer> inorder(TreeNode node) {
        if (node == null) return new ArrayList<>();
        List<Integer> res = new ArrayList<>();
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
    TreeNode* left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        // Step 1: Get the in-order traversal (sorted array)
        vector<int> nums = inorder(root);

        // Step 2: Apply two-pointer approach
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int total = nums[left] + nums[right];
            if (total == k) return true;
            else if (total < k) left++;
            else right--;
        }

        return false;
    }

    vector<int> inorder(TreeNode* node) {
        if (!node) return {};
        vector<int> left = inorder(node->left);
        vector<int> right = inorder(node->right);
        left.push_back(node->val);
        left.insert(left.end(), right.begin(), right.end());
        return left;
    }
};
"""

# method 2:
"""
just store the remaining sum w.r.t each number you pop for inorder 
After poping check whether that number is present in the hashmap for not
if already presen then it means sum exist otherwise add the curr poped node into stack.
space= time= O(n)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return Falseclass Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return Falseclass Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return Falseclass Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return Falseclass Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = []
        curr = root

        while curr or stack:
            # Traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            # Check if current value is in the seen set
            if curr.val in seen:
                return True
            else:
                # Store the needed complement to reach k
                seen.add(k - curr.val)

            # Move to right subtree
            curr = curr.right

        return False

# Java Code 
"""
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> seen = new HashSet<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            // Traverse left
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }

            curr = stack.pop();

            // Check if current value is in the seen set
            if (seen.contains(curr.val)) {
                return true;
            } else {
                // Store the needed complement to reach k
                seen.add(k - curr.val);
            }

            // Move to right subtree
            curr = curr.right;
        }

        return false;
    }
}
"""
# C++ Code 
"""
#include <unordered_set>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> seen;
        stack<TreeNode*> st;
        TreeNode* curr = root;

        while (curr || !st.empty()) {
            // Traverse left
            while (curr) {
                st.push(curr);
                curr = curr->left;
            }

            curr = st.top(); st.pop();

            // Check if current value is in the seen set
            if (seen.count(curr->val)) {
                return true;
            } else {
                // Store the needed complement to reach k
                seen.insert(k - curr->val);
            }

            // Move to right subtree
            curr = curr->right;
        }

        return false;
    }
};
"""
# method 3:
"""
just use the 'BST iterator' i.e 'next' and 'prev'
next will give element from start i.e smallest one and 'prev' will give element from last i.e largest one.
Now problem reduces to "Two sum" with two pointer approach 'next' and 'prev'.

for getting the 'prev' just push all the right ele first and for any node you pop 
push their 'left'. 
just the opposite of 'next'.

time: O(n)
space: O(H)*2= O(H)
this Q is based on this approach only since in this we are using a lot of property of BST
"""

class BSTIterator:
    def __init__(self, root, reverse):  # taking reverse also so that we don't have to make separate function 
                                        # for getting 'next' and 'prev', for smallest and greatest one.
        self.stack= []
        self.reverse= reverse
        self.PushAll(root)
        
    def next(self) -> int:
        temp= self.stack.pop()
        if self.reverse:
            self.PushAll(temp.left)  
        else:
            self.PushAll(temp.right)
        return temp.val
        
    def hasNext(self) -> bool:
        return self.stack != []
    
    def PushAll(self, root):
        # push everything that comes on the left/right of root based on 'reverse' value.
        curr= root
        while curr:
            self.stack.append(curr)
            if self.reverse:  # means we have to get element from last so put all the right nodes into the stack
                curr= curr.right
            else:
                curr= curr.left
                
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        start= BSTIterator(root, False)    # get element from start i.e smallest one first
        end=   BSTIterator(root, True)     # get element from end i.e   largest one first so made reverse= "True"
        i= start.next()
        j= end.next()
        while i< j:
            if i + j== k:
                return True
            elif i + j < k:
                i= start.next()
            else: 
                j= end.next()
        return False

# Java Code 
"""
import java.util.Stack;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

// BSTIterator that can iterate forward (in-order) or backward (reverse in-order)
class BSTIterator {
    private Stack<TreeNode> stack = new Stack<>();
    private boolean reverse;

    // taking reverse also so that we don't have to make separate function
    // for getting 'next' and 'prev', for smallest and greatest one.
    public BSTIterator(TreeNode root, boolean reverse) {
        this.reverse = reverse;
        pushAll(root);
    }

    public int next() {
        TreeNode temp = stack.pop();
        if (reverse) {
            pushAll(temp.left);
        } else {
            pushAll(temp.right);
        }
        return temp.val;
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }

    // push everything that comes on the left/right of root based on 'reverse' value.
    private void pushAll(TreeNode node) {
        while (node != null) {
            stack.push(node);
            if (reverse) {  // means we have to get element from last so put all the right nodes into the stack
                node = node.right;
            } else {
                node = node.left;
            }
        }
    }
}

class Solution {
    public boolean findTarget(TreeNode root, int k) {
        BSTIterator start = new BSTIterator(root, false);  // get element from start i.e smallest one first
        BSTIterator end = new BSTIterator(root, true);     // get element from end i.e largest one first

        int i = start.next();
        int j = end.next();

        while (i < j) {
            if (i + j == k) {
                return true;
            } else if (i + j < k) {
                i = start.next();
            } else {
                j = end.next();
            }
        }
        return false;
    }
}
"""
# C++ Code 
"""
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) {}
};

// BSTIterator that can iterate forward (in-order) or backward (reverse in-order)
class BSTIterator {
    stack<TreeNode*> stk;
    bool reverse;

public:
    // taking reverse also so that we don't have to make separate function
    // for getting 'next' and 'prev', for smallest and greatest one.
    BSTIterator(TreeNode* root, bool rev): reverse(rev) {
        pushAll(root);
    }

    int next() {
        TreeNode* temp = stk.top(); stk.pop();
        if (reverse) {
            pushAll(temp->left);
        } else {
            pushAll(temp->right);
        }
        return temp->val;
    }

    bool hasNext() const {
        return !stk.empty();
    }

private:
    // push everything that comes on the left/right of root based on 'reverse' value.
    void pushAll(TreeNode* node) {
        while (node) {
            stk.push(node);
            if (reverse) {  // means we have to get element from last so put all the right nodes into the stack
                node = node->right;
            } else {
                node = node->left;
            }
        }
    }
};

class Solution {
public:
    bool findTarget(TreeNode* root, int k) {
        BSTIterator start(root, false);  // get element from start i.e smallest one first
        BSTIterator end(root, true);     // get element from end i.e largest one first

        int i = start.next();
        int j = end.next();

        while (i < j) {
            if (i + j == k) return true;
            else if (i + j < k) i = start.next();
            else j = end.next();
        }
        return false;
    }
};
"""