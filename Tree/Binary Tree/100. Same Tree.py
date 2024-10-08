# on gfg
# time: O(min(m,n))
# check whether both are structurally and value wise same
# better and concise and more intuitive
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if any of them is None then both should be None for same tree
        if p== None or q== None:  # this will check that they are structurally same 
            return p == q   
        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
              # this will check all nodes are value wise same

# in java
"""
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // If either of the nodes is null, both must be null to be considered the same tree
        if (p == null || q == null) {
            return p == q;
        }
        // Check if the current nodes' values are equal and recurse on left and right subtrees
        return (p.val == q.val) && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
"""


# Related q: 
# 101. Symmetric Tree
