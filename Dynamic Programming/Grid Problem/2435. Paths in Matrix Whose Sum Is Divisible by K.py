# Brute force

# Note: Here write lru_cache will give wrong ans.
# Reason: Because here we are not returning values to parent function.
#  we have arrived the same state i.e (r, c, curSum) may be via different path
# but we are returning directly so that won't be added as ans.

# may give less number than expected.

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m , n = len(grid) , len(grid[0])
        self.ans = 0

        @lru_cache(None)
        def  dfs(r, c, curSum):
            if r == m - 1 and c == n-1:
                if curSum % k == 0:
                    self.ans += 1
                return
            if r + 1 < m:
                dfs(r + 1, c , curSum + grid[r + 1][c])
            if c + 1 < n:
                dfs(r, c + 1, curSum + grid[r][c+ 1])

        dfs(0, 0, grid[0][0])
        return self.ans

# Other way:
# for any (r,c)
# we can add the the ans of its down and right function call.

# Note: using '@lru_cache(None)' here is giving 'memory limit exceeded'

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m , n = len(grid) , len(grid[0])
        mod = 10 **9 + 7

        def  dfs(r, c, curSum):
            if r >= m or c >= n:
                return 0
            if r == m - 1 and c == n-1:
                # return (curSum + grid[r][c]) % k == 0
                if (curSum + grid[r][c]) % k == 0:
                    return 1
                return 0
            if dp[r][c][curSum] != -1:
                return dp[r][c][curSum]
            ans = 0
            ans += dfs(r + 1, c , (curSum + grid[r][c]) % k)  # for curSum do modulus by 'k' otherwise will go out of bound.
            ans += dfs(r, c + 1,  (curSum + grid[r][c]) % k)
            ans = ans % mod
            dp[r][c][curSum] = ans
            return ans 

        dp = [[[-1 for s in range(k + 1)] for j in range(n + 1)] for i in range(m + 1)]  
        return dfs(0, 0, 0)
