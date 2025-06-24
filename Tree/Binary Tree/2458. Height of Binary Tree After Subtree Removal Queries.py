# method 1:
# time: O(n^2)

# Logic: check for maxHeight after removing the cur node in queries.

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        def height(cur, nodeVal):
            if not cur:
                return 0
            if cur.val == nodeVal:
                return 0
            return 1 + max(height(cur.left, nodeVal), height(cur.right, nodeVal))

        ans = []       
        for nodeVal in queries:
            curHeight = height(root, nodeVal) - 1
            ans.append(curHeight)
        return ans

# Java Code 
"""
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public List<Integer> treeQueries(TreeNode root, int[] queries) {
        List<Integer> ans = new ArrayList<>();
        for (int nodeVal : queries) {
            int curHeight = height(root, nodeVal) - 1;
            ans.add(curHeight);
        }
        return ans;
    }

    private int height(TreeNode cur, int nodeVal) {
        if (cur == null) {
            return 0;
        }
        if (cur.val == nodeVal) {
            return 0;
        }
        return 1 + Math.max(height(cur.left, nodeVal), height(cur.right, nodeVal));
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
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        vector<int> ans;
        for (int nodeVal : queries) {
            int curHeight = height(root, nodeVal) - 1;
            ans.push_back(curHeight);
        }
        return ans;
    }

    int height(TreeNode* cur, int nodeVal) {
        if (!cur) {
            return 0;
        }
        if (cur->val == nodeVal) {
            return 0;
        }
        return 1 + max(height(cur->left, nodeVal), height(cur->right, nodeVal));
    }
};
"""
# Method 2: 
# Optimisation 
# Logic vvi: Max height without current node will be max height elsewhere in the tree or height of sibling node + curr depth
# And for getting the maxHeight , we need (curNode, curHeight, maxHeightPossible) as parameter in function.

# How to think?
# Because we can get maxHeight after deleting any node from 1) different subtree i.e max height elsewhere in the tree (maxHeight till now)
# 2) maxHeight from its sibling subtree

# Note : 'height' will repeat for same node value

# time: O(n*logn): we have to find the maxHeight we can get from sibling


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        heights = collections.defaultdict()
        def height(cur):
            if not cur:
                return 0
            if cur.val in heights:
                return heights[cur.val]
            h= 1 + max(height(cur.left), height(cur.right))
            heights[cur.val] = h
            return h

        ans = collections.defaultdict(int)   # [node : maxDepthAfterRemoving]
        def dfs(root, depth, maxDepth):
            if not root:
                return 
            ans[root.val] = maxDepth
            dfs(root.left , depth + 1 , max(maxDepth , depth + height(root.right)))   # for maxDepth taking prev 'depth' only so no need to add '+1' in maxDepth
                                # for 'left' we will find the maxHeight from its sibling i.e 'right' & same for 'right'.
            dfs(root.right , depth + 1 , max(maxDepth , depth + height(root.left)))
        
        dfs(root, 0, 0)
        # now max height that we will get after removing any node is stored in 'ans' i.e [node: maxDepth]
        return [ans[v] for v in queries]

# Java Code 
"""
import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    Map<Integer, Integer> heights = new HashMap<>();
    Map<Integer, Integer> ans = new HashMap<>();   // [node : maxDepthAfterRemoving]

    public List<Integer> treeQueries(TreeNode root, int[] queries) {
        height(root);
        dfs(root, 0, 0);  // initial depth and maxDepth = 0

        List<Integer> res = new ArrayList<>();
        for (int val : queries) {
            res.add(ans.getOrDefault(val, 0));
        }
        return res;
    }

    int height(TreeNode cur) {
        if (cur == null) return 0;
        if (heights.containsKey(cur.val)) return heights.get(cur.val);
        int h = 1 + Math.max(height(cur.left), height(cur.right));
        heights.put(cur.val, h);
        return h;
    }

    void dfs(TreeNode root, int depth, int maxDepth) {
        if (root == null) return;
        ans.put(root.val, maxDepth);
        dfs(root.left, depth + 1, Math.max(maxDepth, depth + height(root.right)));  // for maxDepth taking prev 'depth' only so no need to add '+1'
        dfs(root.right, depth + 1, Math.max(maxDepth, depth + height(root.left)));
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
    unordered_map<int, int> heights;
    unordered_map<int, int> ans;  // [node : maxDepthAfterRemoving]

    vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
        height(root);
        dfs(root, 0, 0);  // initial depth and maxDepth = 0

        vector<int> res;
        for (int v : queries) {
            res.push_back(ans[v]);
        }
        return res;
    }

    int height(TreeNode* cur) {
        if (!cur) return 0;
        if (heights.count(cur->val)) return heights[cur->val];
        int h = 1 + max(height(cur->left), height(cur->right));
        heights[cur->val] = h;
        return h;
    }

    void dfs(TreeNode* root, int depth, int maxDepth) {
        if (!root) return;
        ans[root->val] = maxDepth;
        dfs(root->left, depth + 1, max(maxDepth, depth + height(root->right)));  // for maxDepth taking prev 'depth' only
        dfs(root->right, depth + 1, max(maxDepth, depth + height(root->left)));
    }
};
"""