# Logic: For each node check that is root of the ans.

# Note: whenever you have to find distance between any two nodes then that will be equal to 
# => distance of both the nodes from their lowest common ancesstor.
# and here we have to find the maximum of all such distances. 
# so we will treat every node as lowest common ancesstor(because at any node we can get the ans and 
# every node can be lowest common ancesstor).
# and will update the ans according to the "sum of nodes to its left + right part"(sum of height of subtree only)

# logic: just find the sum of left subtree height and right subtree height of all nodes
# max of all will be your ans and this will be maximum only between two leaves

# Note vvi: another way of asking this Q can be " longest path between any two leaves".


# optimised way ,O(n)
# bottom up approach.
# we can traverse recursively and store the final ans in same function as height and final ans will differ that's why made another fn

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans= 0
        def Height(root):   # just excatly logic of height only
            if root== None:
                return 0
            left= Height(root.left)
            right= Height(root.right)
            self.ans= max(self.ans, left+ right)   # ans when 'root' is lcs 
            return 1+ max(left, right)    # root will contribute either to left or right so take max(left, right)
        
        # read from here    
        Height(root)
        return self.ans

# Note vvi: When we will apply DP in tree then return function and ans can be different .
# so keep updating ans seeing the possible ans and return the function accordingly.
# at last return the ans.

# e.g: "543. Diameter Q", "124. Tree path sum"
    

# Related Q:
# 1) 124. Binary Tree Maximum Path Sum
# 2) 2246. Longest Path With Different Adjacent Characters


# Java
"""
class Solution {
    int ans;

    public int diameterOfBinaryTree(TreeNode root) {
        ans = 0;
        height(root);
        return ans;
    }

    private int height(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = height(root.left);
        int right = height(root.right);
        ans = Math.max(ans, left + right);
        return 1 + Math.max(left, right);
    }
}
"""