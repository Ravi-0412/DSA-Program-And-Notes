# Method 1: 

# Brute force: just like we do the Brute force in "Find Total no of subarray having sum k"
# from every node , count the ans possible.
# we can use any traversal to call the function to find the ans from each node.
# time: O(n^2)

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root== None:
            return 0
        self.noPaths= 0

        self.dfs(root, targetSum)   # can do any traversal
        return self.noPaths
    
    def dfs(self, root, target):  # calling for each node one by one.
        if root== None:
            return 
        self.AllPath(root, target)   # checking if we ca get any path starting from this node.
        self.dfs(root.left, target)
        self.dfs(root.right, target)
    
    def AllPath(self, root, target):
        if root== None:
            return
        if root.val== target:
            self.noPaths+= 1
            # return    # as we can get the ans also after this from same root like we get both positive and negative nodes.
        self.AllPath(root.left, target- root.val)
        self.AllPath(root.right, target- root.val)

# Java Code 
"""
class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int noPaths = 0;

    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return 0;
        }
        dfs(root, targetSum);   // can do any traversal
        return noPaths;
    }

    public void dfs(TreeNode root, int target) {  // calling for each node one by one.
        if (root == null) {
            return;
        }
        AllPath(root, target);   // checking if we ca get any path starting from this node.
        dfs(root.left, target);
        dfs(root.right, target);
    }

    public void AllPath(TreeNode root, int target) {
        if (root == null) {
            return;
        }
        if (root.val == target) {
            noPaths++;
            // return    // as we can get the ans also after this from same root like we get both positive and negative nodes.
        }
        AllPath(root.left, target - root.val);
        AllPath(root.right, target - root.val);
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
    int noPaths = 0;

    int pathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) {
            return 0;
        }
        dfs(root, targetSum);   // can do any traversal
        return noPaths;
    }

    void dfs(TreeNode* root, int target) {  // calling for each node one by one.
        if (root == nullptr) {
            return;
        }
        AllPath(root, target);   // checking if we ca get any path starting from this node.
        dfs(root->left, target);
        dfs(root->right, target);
    }

    void AllPath(TreeNode* root, int target) {
        if (root == nullptr) {
            return;
        }
        if (root->val == target) {
            noPaths++;
            // return    // as we can get the ans also after this from same root like we get both positive and negative nodes.
        }
        AllPath(root->left, target - root->val);
        AllPath(root->right, target - root->val);
    }
};
"""

# method 2: 

# optimisng to O(n): 
# just similar logic as basic of 'Two sum' and exactly same as "560.Find Total number of subarrays whose sum equals to k.".
# Don't think this as new q, it is the same Q only.
        
# just like we optimise the "560.Find Total number of subarrays whose sum equals to k." using hashmap.


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(root, preSum):
            if not root:
                return 
            curSum= preSum + root.val
            if (curSum- targetSum) in preSum_freq:   
                self.count+= preSum_freq[(curSum- targetSum)]
            # add the curSum into hashmap before going to it child. just like we are moving to next index in array for subarray sum= k
            preSum_freq[curSum]= 1 + preSum_freq.get(curSum, 0)
            # now call the function for left and right part
            dfs(root.left, curSum)   # now curSum will become preSum. just like subarary sum i.e for next index we used to add value in curSum calculated till now.
            dfs(root.right, curSum)
            # now current node is not going to matter anymore. Because after it will return to its parent then this node can't be the part of the other paths.
            preSum_freq[curSum]-= 1  # so reduce the freq by '1' that we had added because of this node.    

        self.count= 0
        preSum_freq= {0: 1}   # to handle the corner case when curSum== target then curSum- target= 0.
        dfs(root, 0)   # 0: preSum
        return self.count

# Java Code 
"""
import java.util.HashMap;
import java.util.Map;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    int count = 0;

    public int pathSum(TreeNode root, int targetSum) {
        Map<Integer, Integer> preSum_freq = new HashMap<>();
        preSum_freq.put(0, 1);   // to handle the corner case when curSum== target then curSum- target= 0.
        dfs(root, 0, targetSum, preSum_freq);   // 0: preSum
        return count;
    }

    public void dfs(TreeNode root, int preSum, int target, Map<Integer, Integer> preSum_freq) {
        if (root == null) {
            return;
        }
        int curSum = preSum + root.val;
        if (preSum_freq.containsKey(curSum - target)) {
            count += preSum_freq.get(curSum - target);
        }
        // add the curSum into hashmap before going to it child. just like we are moving to next index in array for subarray sum= k
        preSum_freq.put(curSum, preSum_freq.getOrDefault(curSum, 0) + 1);
        // now call the function for left and right part
        dfs(root.left, curSum, target, preSum_freq);   // now curSum will become preSum. just like subarary sum i.e for next index we used to add value in curSum calculated till now.
        dfs(root.right, curSum, target, preSum_freq);
        // now current node is not going to matter anymore. Because after it will return to its parent then this node can't be the part of the other paths.
        preSum_freq.put(curSum, preSum_freq.get(curSum) - 1);  // so reduce the freq by '1' that we had added because of this node.
    }
}
"""
# C++ Code 
"""
#include <unordered_map>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    int count = 0;

    int pathSum(TreeNode* root, int targetSum) {
        unordered_map<int, int> preSum_freq;
        preSum_freq[0] = 1;   // to handle the corner case when curSum== target then curSum- target= 0.
        dfs(root, 0, targetSum, preSum_freq);   // 0: preSum
        return count;
    }

    void dfs(TreeNode* root, int preSum, int target, unordered_map<int, int>& preSum_freq) {
        if (root == nullptr) {
            return;
        }
        int curSum = preSum + root->val;
        if (preSum_freq.count(curSum - target)) {
            count += preSum_freq[curSum - target];
        }
        // add the curSum into hashmap before going to it child. just like we are moving to next index in array for subarray sum= k
        preSum_freq[curSum] += 1;
        // now call the function for left and right part
        dfs(root->left, curSum, target, preSum_freq);   // now curSum will become preSum. just like subarary sum i.e for next index we used to add value in curSum calculated till now.
        dfs(root->right, curSum, target, preSum_freq);
        // now current node is not going to matter anymore. Because after it will return to its parent then this node can't be the part of the other paths.
        preSum_freq[curSum] -= 1;  // so reduce the freq by '1' that we had added because of this node.
    }
};
"""