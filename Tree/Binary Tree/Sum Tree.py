# Logic: Just go bottom up and check the value of each node with its children sum.
# Note: write base case for leaf node also because we don't have to check this for leaf node.

# Time: O(n)

class Solution:
    def isSumTree(self,root):
        self.ans = 1
        def check(root):
            if not root:
                return 0
            if root.left == None and root.right == None:
                return root.data
            l = check(root.left)
            r = check(root.right)
            if root.data != l + r:
                self.ans = 0
            return l + r + root.data
            
        check(root)
        return self.ans


# Method 2:
# Instead of taking 'ans' as global variable ,
# return any integer in invalid case which can make all the upper nodes sum as invalid.

class Solution:
    def isSumTree(self,root):
        
        def check(root):
            if not root:
                return 0
            if root.left == None and root.right == None:
                return root.data
            l = check(root.left)
            r = check(root.right)
            if l == -1 or r == -1 or root.data != l + r:
                return -1
            return l + r + root.data
        
        return 1 if check(root) != -1 else 0