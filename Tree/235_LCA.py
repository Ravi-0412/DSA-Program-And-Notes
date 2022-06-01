# just traverse till you find both the nodes in different subtree
# as asson as you will find the nodes in different subtree that will be the ans 
# as the current node will be the parent for both

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root== None:
            return root 
        if root.val> p.val and root.val> q.val:  # both lie in the left subtree of that node
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val< p.val and root.val< q.val:   # both lie in the right subtree of that node
            return self.lowestCommonAncestor(root.right, p, q)
        else: # means one lie left and other lie in right or (one tree is LCA of other) so return root itself
            return root


# iterative way of above
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while root:
        if root.val> p.val and root.val> q.val:  # both lie in the left subtree of that node
            root= root.left
        elif root.val< p.val and root.val< q.val:   # both lie in the right subtree of that node
            root= root.right
        else: # means one lie left and other lie in right or (one tree is LCA of other) so return root itself
            return root

