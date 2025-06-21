# method 1:
# Recursion + memoisation

# How do we calculate for 1D?
# Ans: from every index find the "length of  longest strictly increasing subarray" and add those length to get the final ans.

# E.g: arr= [1,2,3,4,3]

# Let's try to pick each element/index as our starting point and find the answer.
# 1 -> [1,2,3,4] = 4, 2 -> [2,3,4] = 3, 3-> [3,4] = 2, [4] = 1, [3] = 1. 
# Summing these individual values will produce the answer. But what do these individual results essentially mean?

# Let's look at [1,2,3,4] = 4, this means starting from 1 we have a total of 4 increasing sequences/paths. 
# [1,2,3,4], [1,2,3], [1,2], [1]. We are calculating the same for each starting point.

# Note: The 2D version is similar as it forms a DAG and hence are no cycles in the graph/path.

# In same way we are doing for 2D.

# Note: Just same as '329. Longest Increasing Path in a Matrix'
# Isme number chahiye isliye adjacent wale ka 'sum le lo ' and '1' add karke 
# return kar do .

# time : O(4*m *n) .At each recursion at max you have 4 directions thus O(1) further calls and we have a total of m*n states for the DP.
# SPACE: o(m * n)

# Note: It's strictly increasing so we don't need visited array.
 
from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        
        # Initialize dp with -1 to mark uncomputed cells
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            total = 1  # path that starts and ends at (i, j)
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    total += dfs(ni, nj)
                    total %= mod
            dp[i][j] = total
            return dp[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % mod
        return ans


# Method 2: 
# Tabulation

from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right

        dp = [[1] * n for _ in range(m)]  # base case: each cell contributes at least 1 path (itself)

        # Sort all cells by value to process in increasing order
        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda x: grid[x[0]][x[1]])

        for i, j in cells:
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < grid[i][j]:
                    dp[i][j] = (dp[i][j] + dp[ni][nj]) % mod

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dp[i][j]) % mod

        return ans
