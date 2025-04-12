# logic: just reverse the string and find lcs of actual and reversed string
# lcs will be our final ans as for palindrome reading from both sides will be same
# so the subsequence in one must be there in other also
# and largest subsequence will be our ans
class Solution:
    def longestPalinSubseq(self, S):
        S1= S[::-1]
        # print(S)
        x,y= len(S), len(S)
        return self.Lcs(x,y,S,S1)
    def Lcs(self,x,y,s1,s2):
        dp= [[0 for i in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1, y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i][j-1], dp[i-1][j])
        return dp[x][y]

# Method 2: Travsersing in same string 's'
# Recursion + memoisation 

# Logic: 
    # Let dp(l, r) denote the length of the longest palindromic subsequence of s[l..r].
    # There are 2 options:
    #     If s[l] == s[r] then dp[l][r] = dp[l+1][r-1] + 2
    #     Elif s[l] != s[r] then dp[l][r] = max(dp[l+1][r], dp[l][r-1]).
    # Then dp(0, n-1) is our result.


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def helper(l: int, r: int) -> int:
            if l == r:
                return 1
            if l > r:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            
            if s[l] == s[r]:
                dp[l][r] = 2 + helper(l + 1, r - 1)
            else:
                dp[l][r] = max(helper(l + 1, r), helper(l, r - 1))
            
            return dp[l][r]

        return helper(0, n - 1)

# Tabulation
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for l in range(n-1, -1, -1):
            for r in range(l + 1, n):      
                if s[l] == s[r]:
                    dp[l][r] = 2 + dp[l + 1][r -1] 
                else:
                    dp[l][r] = max(dp[l + 1][r] , dp[l][r-1])
        return dp[0][n-1]
