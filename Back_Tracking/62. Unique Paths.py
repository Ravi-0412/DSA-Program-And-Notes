# Method 1: 

# correct only but will give TLE
# just reverse the problem i.e you have to reach (0,0) from (m-1,n-1) that's why u can take go left or up
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # base case
        # after reaching 1st row or 1st col there will be only path i.e either go left only or up only
        if m== 1 or n==1:   
            return 1
        return self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)

# Method 2:
# memoization
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

# Method 3: 
# tabulation:
# Bottom up (0,0) to (m-1,n-1). but for filling with base case you have to think opposite i.e from (m-1,n-1) to (0,0)
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

# Method 4: 
# concise way of writing the above one
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[1 for j in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1, n):
                dp[i][j]= dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


# Method 5: 
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

# Method 6:
"""
Optimising space

Time : O(2 *N)

Q) But we are creating array for each row so it should not be N*N ?
ans: No. While it looks like we are creating a new array N times, 
at any single point in time, only two arrays exist in the computer's memory: pre and cur.
When the loop finishes one row, the "old" pre is no longer needed.Python’s Garbage Collector 
sees that nothing is pointing to the old array and frees up that memory.
Therefore, the peak memory usage (the most memory the program uses at once) is just 2*N
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * (n + 1)
        cur = [1] * (n + 1) # Only create these TWO once.
        
        for r in range(2, m + 1):
            for c in range(2, n + 1):
                cur[c] = cur[c - 1] + pre[c]
            
            # Instead of cur.copy() or creating a new list, 
            # we SWAP the references. Now 'pre' becomes the row we just finished.
            pre, cur = cur, pre 
            
        return pre[n]

# Method 7:
# Space optimisation with only single array

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Start with your 'pre' array concept: row 1 is all 1s
        dp = [1] * (n + 1)
        
        # Your loop: for r from 2 to m
        for r in range(2, m + 1):
            # Your inner loop: for c from 2 to n
            for c in range(2, n + 1):
                # dp[c] currently holds the value from 'pre[c]' (row above)
                # dp[c-1] currently holds the value from 'cur[c-1]' (left neighbor)
                dp[c] = dp[c] + dp[c - 1]
                
        return dp[n]

# method 8:
"""

Total moves = (m-1) downs + (n-1) rights

Total steps = m + n - 2

Choose where the downs (or rights) go

Formula
Unique Paths
To go from the top-left to bottom-right in an m × n grid:
• You must move exactly (m - 1) steps DOWN.
• You must move exactly (n - 1) steps RIGHT.
• Total steps = (m - 1) + (n - 1) = m + n - 2.

Every valid path is just a unique ordering of these moves.

So the problem becomes:
"How many ways can we arrange (m - 1) downs among (m + n - 2) total steps?"

That is a combinations problem:
Unique Paths = C(m + n - 2, m - 1)​

Time : O(min(m-1, n-1))


"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Total moves needed
        N = m + n - 2
        # We choose the smaller of (m-1) and (n-1)
        # to minimize the loop length
        k = min(m - 1, n - 1)
        res = 1

        # Compute C(N, k) iteratively:
        # C(N, k) = (N-k+1)(N-k+2)...N / (1·2·...·k)
        for i in range(1, k + 1):
            # Multiply next numerator term
            # and divide by next denominator term
            res = res * (N - k + i) // i

        return res
