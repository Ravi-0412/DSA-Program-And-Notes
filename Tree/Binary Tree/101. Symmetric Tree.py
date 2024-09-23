# symmetric tree means tree should be mirror of itself
# so we need to check the left side and right side at same time like "identical tree "
# just use the logic of symmetric that we studied in maths
# left== right and right== left 
class Solution:
    def isSymmetric(self, root):
        if root==None or root.left==None and root.right== None: # if none or contain only single node
            return True
        return self.isMirror(root.left,root.right)   # now check for the left and right subtree  
        
    def isMirror(self,root1, root2):
        # if any of them is None then both should be None
        if root1== None or root2== None:
            return root1==root2    
        return (root1.data==root2.data) and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)  
                                                                # here the diff from "identical trees"

# java
"""
class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null || (root.left == null && root.right == null)) {  // if null or contains only single node
            return true;
        }
        return isMirror(root.left, root.right);  // now check for the left and right subtree  
    }

    private boolean isMirror(TreeNode root1, TreeNode root2) {
        // if any of them is null then both should be null
        if (root1 == null || root2 == null) {
            return root1 == root2;
        }
        // Check the symmetry for values and subtrees
        return (root1.val == root2.val) 
                && isMirror(root1.left, root2.right) 
                && isMirror(root1.right, root2.left);
    }
}
"""
