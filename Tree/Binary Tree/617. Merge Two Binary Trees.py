# time: O(n)

# logic: if any of the tree is None simply return the not_None tree.
# else make a node with node.val= sum of cur node value of both the tree and call for left and right part.

# same as we construct BST and other tree. when told to construct any tree think like this way first.
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1== None or root2== None:
            return root1 or root2
        # means both are not None.
        node= TreeNode(root1.val + root2.val)
        node.left=  self.mergeTrees(root1.left, root2.left)
        node.right= self.mergeTrees(root1.right, root2.right)
        return node
