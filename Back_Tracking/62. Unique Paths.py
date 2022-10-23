# correct only but giving tle
# just reverse the problem i.e you have to reach (0,0) from (m-1,n-1) that's why u can take go left or up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base case
        # after reaching 1st row or 1st col there will be only path i.e either go left only or up only
        if m== 1 or n==1:   
            return 1
        return self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)

# optimising the above solution using dp: memoization
# time: O(n^2) 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[-1 for i in range(n)]for i in range(m)]
        return self.helper(m-1,n-1,dp)   # called with (m-1,n-1) so that we directly use (m,n) in helper
    
    def helper(self,m,n,dp):
        if m==0 or n==0:
            return 1
        if dp[m][n]!= -1:
            return dp[m][n]
        dp[m][n]= self.helper(m,n-1,dp) + self.helper(m-1,n,dp)
        return dp[m][n]

# tabulation: bottom up (0,0) to (m-1,n-1). but for filling with base case you have to think opposite i.e from (m-1,n-1) to (0,0)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[-1 for i in range(n)]for i in range(m)]
        # initialise with base cases, 1st row and 1st col with 1
        for i in range(m):
            for j in range(n):
                if i== 0 or j==0:  
                    dp[i][j]= 1   # 1st row and 1st col with '1'
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]= dp[i][j-1] + dp[i-1][j]
        return dp[m-1][n-1]

# concise way of writing the above one
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[1 for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j]= dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

# tabulation: top down
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0 for j in range(n)] for i in range(m)]
        # initialise with base cases, last row and last col with 1
        for i in range(m):
            for j in range(n):
                if i== m-1 or j== n-1:
                    dp[i][j]= 1
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j]= dp[i+1][j] + dp[i][j+1]
        return dp[0][0]




