# time: O(n)

class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.ans, self.ind= [], 0
        # ind: will tell which value to chekc from voyage for current root.

        def dfs(root):
            if not root or self.ind >= len(voyage):
                return
            if root.val != voyage[self.ind] :
                # means it is not possible to get the desired order from here.
                # root ka value equal to hona hi chahiye nhi to possible nhi hoga.
                self.ans.append(None)
                return
            dr= 1
            self.ind+= 1
            if root.left and root.left.val != voyage[self.ind]:
                # means we have to swap left and right child.
                self.ans.append(root.val)
                dr= -1   # change the direction also because after swap we will have to move right to left.
            
            for child in [root.left, root.right][::dr] :
                dfs(child)

        dfs(root)
        return [-1] if None in self.ans else self.ans
