# Method 1 : 

# time: O(n^2).
# we are visiting every node only once but we are copying the path into 'ans'.
# Each time it can cost O(n) for copying after finding any answer.
# so time: O(n^2)

# logic: keep adding the node value into ans and keep decr the target.


# my mistake : This will print the every path two times
# Because when target will become zero at any node then that will call its child to print the ans.
# so we will get same ans two times for left and right child as well.
# Also this can give ans when it will not reach the leaf node also since we are only checking with target.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans, path= [], []
        self.AllPath(root, targetSum, path, ans)
        return ans
    
    def AllPath(self, root, target, path, ans):
        if target== 0:
            ans.append(path)
            return
        if root== None:
            return 
        self.AllPath(root.left, target- root.val, path + [root.val], ans)
        self.AllPath(root.right, target- root.val, path + [root.val], ans)



# correct solution
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans, path= [], []
        self.AllPath(root, targetSum, path, ans)
        return ans
    
    def AllPath(self, root, target, path, ans):
        if root== None:  # this should be the 1st base case.
            return
        if target== root.val and root.left== None and root.right== None: # value is equal to remaining target and root is a leaf.
            ans.append(path + [root.val]) 
            return
        self.AllPath(root.left, target- root.val, path + [root.val], ans)
        self.AllPath(root.right, target- root.val, path + [root.val], ans)


# Java 
"""
import java.util.*;

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> path = new ArrayList<>();
        allPath(root, targetSum, path, ans);
        return ans;
    }
    
    private void allPath(TreeNode root, int target, List<Integer> path, List<List<Integer>> ans) {
        if (root == null) {
            return;
        }
        
        // Create a new list with the current path and add current node's value
        List<Integer> newPath = new ArrayList<>(path);
        newPath.add(root.val);
        
        if (target == root.val && root.left == null && root.right == null) {
            ans.add(newPath);
            return;
        }
        
        allPath(root.left, target - root.val, newPath, ans);
        allPath(root.right, target - root.val, newPath, ans);
    }
}
"""
# C++ Code
"""
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> ans;
        vector<int> path;
        AllPath(root, targetSum, path, ans);
        return ans;
    }
    
    void AllPath(TreeNode* root, int target, vector<int> path, vector<vector<int>>& ans) {
        if (root == nullptr) {  // this should be the 1st base case.
            return;
        }
        if (target == root->val && root->left == nullptr && root->right == nullptr) { // value is equal to remaining target and root is a leaf.
            path.push_back(root->val);
            ans.push_back(path);
            return;
        }
        path.push_back(root->val);
        AllPath(root->left, target - root->val, path, ans);
        AllPath(root->right, target - root->val, path, ans);
    }
};

"""


# Related Q:
# 1) 129. Sum Root to Leaf Numbers
