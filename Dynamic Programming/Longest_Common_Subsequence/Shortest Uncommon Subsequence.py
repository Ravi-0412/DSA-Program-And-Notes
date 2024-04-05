# Giving Tle : After 32 test case

# Logic: Similar to LCS.

# If any char of 's' is not present in 't' then that will be ans i.e ans = 1
# if present then we have two choice: # 1) include 's[i]' and 2) Don't include s[i] .
# For 1) we will start checking in 't' after we have found 'cur char of s' . 
# say char found at 'k' then we will check from 'k+1' in 't'.

class Solution:
    def shortestUnSub(self, s, t):
        
        def UnSub(i, j):
            if i == m:
                return 1000
            if j == n:
                # means there is some char in 's' and 't' is empty.
                # so any of the char from 's' can be our ans.
                # dp[i][j] = 1
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            # check if s[i] is present in t or not
            # if not present then this char can be ans only so return '1'
            k = j
            while k < n:
                if t[k] == s[i]:
                    break
                k += 1
            if k == n:
                # means s[i] is not present so simply return 1
                dp[i][j] = 1
                return 1
            # Now it means 's[i]' is present.
            # In this case we have two possibility :
            # 1) include 's[i]' and 2) Don't include s[i] .
            # for ans take minimum of both.
            dp[i][j] = min(1 + UnSub(i + 1, k + 1) , UnSub(i + 1, j))
            return dp[i][j]
            
        m , n = len(s) , len(t)
        dp = [[-1 for j in range(n + 1)] for i in range(m + 1)]
        ans = UnSub(0, 0)
        return ans if ans <= 500 else -1