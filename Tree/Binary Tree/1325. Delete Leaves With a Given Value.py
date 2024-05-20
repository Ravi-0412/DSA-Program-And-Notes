# LOgic: Just go bottom- up , return according to question and modify the child of current root.
# Time: O(n)

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.left == None and root.right == None:
            # if leaf and val = target
            return None if root.val == target else root
        l = self.removeLeafNodes(root.left, target)
        r = self.removeLeafNodes(root.right, target)
        # Now make 'l' and 'r' as left and right child of 'root'.
        root.left , root.right = l, r
        # Check if we need to delete root also. 
        # we only need to delete if root becomes leaf and root.val = target
        return None if l == None and r == None and root.val == target else root
