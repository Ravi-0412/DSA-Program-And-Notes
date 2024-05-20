# Method 1:

# Binary tree method can be applied here 
# but better to use the BST property and do .
# In Binary tree there is no way we can decide about both the nodes like in which subtree they will lie i.e either left or right.

# just traverse till you find both the nodes in different subtree
# as soon as you will find the nodes in different subtree that will be the ans 
# as the current node will be the parent for both

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root== None:     # No need of this as it won't reach till 'root= None', it will get returned before only
        #     return root 
        if root.val > p.val and root.val > q.val:  # both lie in the left subtree of that node
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:   # both lie in the right subtree of that node
            return self.lowestCommonAncestor(root.right, p, q)
        # means one lie left and other lie in right or (one tree is LCA of other) so return root itself
        return root

# Method 2:
# iterative way of above
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val> p.val and root.val> q.val:  # both lie in the left subtree of that node
                root= root.left
            elif root.val< p.val and root.val< q.val:   # both lie in the right subtree of that node
                root= root.right
            else: # means one lie left and other lie in right or (one tree is LCA of other) so return root itself
                return root

# Java
"""
// method 1:

public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root.val > p.val && root.val > q.val) {  // both nodes are in the left subtree
            return lowestCommonAncestor(root.left, p, q);
        }
        if (root.val < p.val && root.val < q.val) {  // both nodes are in the right subtree
            return lowestCommonAncestor(root.right, p, q);
        }
        // One node is in the left subtree and the other is in the right subtree, or one node is the LCA of the other
        return root;
    }
}

// method 2:
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        while (root != null) {
            if (root.val > p.val && root.val > q.val) {  // both nodes are in the left subtree
                root = root.left;
            } else if (root.val < p.val && root.val < q.val) {  // both nodes are in the right subtree
                root = root.right;
            } else {  // One node is in the left subtree and the other is in the right subtree. So root is the ans
                return root;
            }
        }
        return null;  // In case root is null
    }
}
"""