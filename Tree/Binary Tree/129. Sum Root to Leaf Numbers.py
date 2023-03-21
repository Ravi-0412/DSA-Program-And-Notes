# method 1:
# just like we print all paths from root to leaf.
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans= 0

        def dfs(root, path):
            if root== None:   # without this won't work if there is left child but no right child
                return 
            if root.left== None and root.right== None:
                path+= str(root.val)
                self.ans+= int(path)
                return
            dfs(root.left, path + str(root.val))
            dfs(root.right, path + str(root.val))

        dfs(root, "")
        return self.ans

# can write like this also.
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans= 0
        # once it reaches the 'none' or leaf, it will start returning.
        def dfs(root, path):
            if root== None:
                return 0
            if root.left== None and root.right== None:
                path+= str(root.val)
                return int(path)
            return dfs(root.left, path + str(root.val)) + dfs(root.right, path + str(root.val))
            
        return dfs(root, "")

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


