# logic: Bottom up (can say DP only)
# Logic: For each node check that is root of the ans.
 # Just similar to  :"543. Diameter of Binary Tree"
# find the path sum at each node 

# for max ans, we have 4 choices like:
#  1) add the current root val to left subtree ans 2) add the current root val to right subtree ans
#  3) add the current root val to left subtree ans + right subtreea ans 6) only return the current root value

# But for returning to the above level we have only three choices as it should be path connected  to upper level.
# 1) left part + current node 2) right part +current node  3) only the current node.  
# current path must be there in all cases then only path can be connected.

# vvi: Code structure and logic is similar to "Diameter Q" but have little difference.
# the difference from "Diameter of tree" is that here ans can be between any node,even single node value can be the ans because value is in negative also.
# not only between the leaf to leaf like "Diameter Q"
# time: O(n)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            # return the lowest possible value in base case so that it doesnt affect the ans. 
            # returning '0' will affect if node values will be "-ve" becuase then max will be '0' and we will get the wrong ans.
            if root== None:
                return float('-inf') 
            l= dfs(root.left)
            r= dfs(root.right)
            self.ans= max(self.ans, l+ root.val, r+ root.val, l+ r+ root.val, root.val)
            return max(l+ root.val, r+ root.val, root.val)
        
        self.ans= float('-inf')
        dfs(root)
        return self.ans

# Java
"""
// Not able to writ ein exact same format

// other way of writing above code
public class Solution {
    int maxSum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        if (root == null)
            return 0;

        dfs(root);
        return maxSum;
    }

    private int dfs(TreeNode root) {
        if (root == null)
            return 0;

        int leftSum = Math.max(0, dfs(root.left)); // Max sum in the left subtree
        int rightSum = Math.max(0, dfs(root.right)); // Max sum in the right subtree

        // Calculate the maximum path sum passing through the current node
        int currentSum = leftSum + rightSum + root.val;

        // Update the maximum path sum found so far
        maxSum = Math.max(maxSum, currentSum);

        // Return the maximum sum of the path from the current node to its parent
        return Math.max(leftSum, rightSum) + root.val;
    }
}

"""
