# time: O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q= deque([root])
        ans, level= [], []
        while q:
            for i in range(len(q)):  # we have to print level by level in a list
                curr= q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(level)
            level= []   # to store the ans of next level
        return ans

# Java
"""
import java.util.*;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();  // Return empty list instead of null
        }
        
        List<List<Integer>> ans = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        
        while (!q.isEmpty()) {
            int size = q.size();
            List<Integer> level = new ArrayList<>();
            
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                level.add(curr.val);
                if (curr.left != null) {
                    q.offer(curr.left);
                }
                if (curr.right != null) {
                    q.offer(curr.right);
                }
            }
            
            ans.add(level);
        }
        
        return ans;
    }
}
"""
#C++ Code 
"""
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) {
            return {};  // equivalent to returning None
        }
        queue<TreeNode*> q;
        q.push(root);
        vector<vector<int>> ans;
        vector<int> level;
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; ++i) {  // we have to print level by level in a list
                TreeNode* curr = q.front();
                q.pop();
                level.push_back(curr->val);
                if (curr->left) {
                    q.push(curr->left);
                }
                if (curr->right) {
                    q.push(curr->right);
                }
            }
            ans.push_back(level);
            level.clear();   // to store the ans of next level
        }
        return ans;
    }
};

"""

# Related q:
# 1) 515. Find Largest Value in Each Tree Row

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        q= deque([root])
        ans = []
        while q:
            maxi = float('-inf')
            for i in range(len(q)):  # we have to print level by level in a list
                cur= q.popleft()
                maxi = max(maxi, cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            ans.append(maxi)
        return ans

# Java Code 
"""
import java.util.*;

class Solution {
    public List<Integer> largestValues(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        
        List<Integer> ans = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        
        while (!q.isEmpty()) {
            int size = q.size();
            int maxi = Integer.MIN_VALUE;
            
            for (int i = 0; i < size; i++) {
                TreeNode cur = q.poll();
                maxi = Math.max(maxi, cur.val);
                
                if (cur.left != null) {
                    q.offer(cur.left);
                }
                if (cur.right != null) {
                    q.offer(cur.right);
                }
            }
            ans.add(maxi); // Store the maximum value of the current level
        }
        return ans;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        if (!root) {
            return {};  // return if root is null
        }
        queue<TreeNode*> q;
        q.push(root);
        vector<int> ans;
        while (!q.empty()) {
            int maxi = INT_MIN;
            for (int i = 0; i < q.size(); ++i) {  // we have to print level by level in a list
                TreeNode* cur = q.front();
                q.pop();
                maxi = max(maxi, cur->val);
                if (cur->left) {
                    q.push(cur->left);
                }
                if (cur->right) {
                    q.push(cur->right);
                }
            }
            ans.push_back(maxi);
        }
        return ans;
    }
};

"""

# 2) 513. Find Bottom Left Tree Value
# simplied: Find the 1st node of last level

# a) When you find node at greater level , update the ans.
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append((0, root))
        maxLevel = -1
        ans = None
        while q:
            l , node = q.popleft()
            if l > maxLevel :
                maxLevel = l
                ans = node.val
            if node.left:
                q.append((l + 1, node.left))
            if node.right:
                q.append((l + 1, node.right))
        return ans


# b) Append right to left then last poped node will be our ans
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        while q:
            root = q.popleft()   # change root then only we will be able to return correct ans at last.
            if root.right:
                q.append(root.right)
            if root.left:
                q.append(root.left)
            
        return root.val  # value of last poped node

#Java Code 
"""
// a) When you find node at greater level, update the ans.
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        Queue<Pair<Integer, TreeNode>> q = new LinkedList<>();
        q.offer(new Pair<>(0, root));
        int maxLevel = -1;
        Integer ans = null;
        while (!q.isEmpty()) {
            Pair<Integer, TreeNode> p = q.poll();
            int l = p.getKey();
            TreeNode node = p.getValue();
            if (l > maxLevel) {
                maxLevel = l;
                ans = node.val;
            }
            if (node.left != null) {
                q.offer(new Pair<>(l + 1, node.left));
            }
            if (node.right != null) {
                q.offer(new Pair<>(l + 1, node.right));
            }
        }
        return ans;
    }
}

// b) Append right to left then last popped node will be our ans
class Solution {
    public int findBottomLeftValue(TreeNode root) {
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            root = q.poll();  // change root then only we will be able to return correct ans at last.
            if (root.right != null) {
                q.offer(root.right);
            }
            if (root.left != null) {
                q.offer(root.left);
            }
        }
        return root.val;  // value of last popped node
    }
}
"""
# C++ Code 
"""
#include <queue>
#include <utility>  // for std::pair

// a) When you find node at greater level, update the ans.
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        std::queue<std::pair<int, TreeNode*>> q;
        q.push({0, root});
        int maxLevel = -1;
        int ans = 0;
        while (!q.empty()) {
            auto p = q.front();
            q.pop();
            int l = p.first;
            TreeNode* node = p.second;
            if (l > maxLevel) {
                maxLevel = l;
                ans = node->val;
            }
            if (node->left) {
                q.push({l + 1, node->left});
            }
            if (node->right) {
                q.push({l + 1, node->right});
            }
        }
        return ans;
    }
};

// b) Append right to left then last popped node will be our ans
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        std::queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            root = q.front();  // change root then only we will be able to return correct ans at last.
            q.pop();
            if (root->right) {
                q.push(root->right);
            }
            if (root->left) {
                q.push(root->left);
            }
        }
        return root->val;  // value of last popped node
    }
};
"""
"""
Other Related Questions:
3) 103. Binary Tree Zigzag Level Order Traversal
4) 1609. Even Odd Tree
5) 1161. Maximum Level Sum of a Binary Tree
6) 116. Populating Next Right Pointers in Each Node
7) 199. Binary Tree Right Side View
8) Left View of a Binary Tree
"""
    
