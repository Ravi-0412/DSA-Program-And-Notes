# method 1:
# just like we print all paths from root to leaf.
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans= 0

        def dfs(root, num):
            if root== None:
                return 
            num= num * 10 + root.val
            if root.left== None and root.right== None:
                self.ans+= num
                return
            dfs(root.left, num)
            dfs(root.right, num)

        dfs(root, 0)
        return self.ans
    

# method 2: better one
# same above logic only.
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans= 0

        def dfs(root, num):
            if root== None:
                return 
            num= num * 10 + root.val
            if root.left== None and root.right== None:
                self.ans+= num
                return
            dfs(root.left, num)
            dfs(root.right, num)

        dfs(root, 0)
        return self.ans


