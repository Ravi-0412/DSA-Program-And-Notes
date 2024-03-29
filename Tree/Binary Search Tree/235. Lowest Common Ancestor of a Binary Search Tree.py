# Binary tree method can be applied here 
# but better to use the BST property and do 
# In Binary tree there is no way we can decide about both the nodes like in which subtree they will lie

# just traverse till you find both the nodes in different subtree
# as soon as you will find the nodes in different subtree that will be the ans 
# as the current node will be the parent for both

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if root== None:     # No need of this as it won't reach till 'root= None', it will get returned before only
        #     return root 
        if root.val> p.val and root.val> q.val:  # both lie in the left subtree of that node
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val< p.val and root.val< q.val:   # both lie in the right subtree of that node
            return self.lowestCommonAncestor(root.right, p, q)
        # means one lie left and other lie in right or (one tree is LCA of other) so return root itself
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

