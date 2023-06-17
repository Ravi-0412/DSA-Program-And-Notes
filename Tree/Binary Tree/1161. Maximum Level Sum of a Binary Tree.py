# logic: just we have to return the level which has maximum some and 
# in case more than one level has maximum sum return the lowest one.

# time: O(n)

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum = collections.defaultdict(int)

        def dfs(root , level):
            if not root:
                return
            levelSum[level] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 1)
        maxSum = float('-inf')
        ans= float('inf')
        for key, value in levelSum.items():
            if value > maxSum:
                maxSum = value
                ans = key
            elif value == maxSum:
                ans = min(ans, key)
        return ans


# my initial mistake
# Reason: Initially any level can have max till now but later it's value can decrease 
# and ans will not change so incorrect.
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelSum = collections.defaultdict(int)
        self.maxSum = float('-inf')
        self.ans= 1

        def dfs(root , level):
            if not root:
                return
            levelSum[level] += root.val
            if levelSum[level] > self.maxSum:
                self.maxSum = levelSum[level]
                self.ans = level
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 1)
        print(levelSum, self.ans, self.maxSum)
        return self.ans