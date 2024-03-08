# Method 1:
# Time: O(n)

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root, d, count):
            if not root:
                return count            
            if d == 'L':
                # Means pre we have taken left
                # so if we take right then count will increase (zigzag)
                # else again we have to start from count = 0 if we take left.
                return max(dfs(root.left, 'L', 0), dfs(root.right, 'R', count + 1))
            else:
                return max(dfs(root.left, 'L', count+1), dfs(root.right, 'R', 0))
        
        return max(dfs(root.left, 'L', 0), dfs(root.right, 'R', 0))
    

# Method 2: 
# Find the length of valid 'left' and 'right' path for each node.

# Note: If we will try to maintain only single value for each node then it won't work.

# Time: O(n)
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def dfs(root):
            if not root:
                return (0, 0)
            _, r = dfs(root.left)  # since we have taken left so will consider the value of 'right' child 
            l , _ = dfs(root.right)
            self.ans = max(self.ans, r + 1, l + 1)
            return (r + 1, l + 1)

        dfs(root)
        return self.ans - 1  # in 'dfs' we were adding the cur node also so will do '-1'.

