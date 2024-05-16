# Logic: Just traverse bottom-up and evaluate for each node.
# time: O(n)
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            # if leaf 
            return True if root.val == 1 else False
        l = self.evaluateTree(root.left)
        r = self.evaluateTree(root.right)
        # if root val = 2 then take 'OR' else take 'AND' and return 
        return (l | r) if root.val == 2 else (l & r)