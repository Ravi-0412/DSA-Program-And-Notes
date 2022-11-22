# logic: any ele will always get inserted at leaf
# so keep on going using bst property till you reach any leaf

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root== None:
            return TreeNode(val)
        if root.val> val:
            root.left= self.insertIntoBST(root.left,val)
        else:
            root.right= self.insertIntoBST(root.right,val)
        return root