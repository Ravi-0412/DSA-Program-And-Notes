# logic: just go Bottom up and if you have find any '1' either from its child or cur node itslef then 
# we will include that node in ans.

# else will return None  (remove subtree starting from that node).

# time: O(n)

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left= self.pruneTree(root.left)
        root.right= self.pruneTree(root.right)
        if root.left== None and root.right== None and root.val== 0:
            return None
        return root
