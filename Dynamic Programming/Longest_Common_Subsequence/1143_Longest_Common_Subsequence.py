# method 1: Recursive way
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n= len(text1), len(text2)
        return self.LCS(m, n, text1, text2)
    def LCS(self, m, n, s1, s2):
        if m==0 or n==0:
            return 0
        elif s1[m -1] == s2[n -1]:
            return 1+ self.LCS(m-1, n-1, s1, s2)
        else: # s1[m -1] == s2[n -1]
            return max (self.LCS(m, n-1, s1, s2), self.LCS(m-1, n, s1, s2))SmallAns
        return ans

# method 2: memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n= len(text1), len(text2)
        dp= [[-1 for i in range(m+1)]for i in range(n+1)]
        return self.LCS(m, n, text1, text2, dp)
    def LCS(self, m, n, s1, s2, dp):
        if m==0 or n==0:
            return 0
        if dp[n][m]!= -1:
            return dp[n][m]
        elif s1[m -1] == s2[n -1]:
            dp[n][m]= 1+ self.LCS(m-1, n-1, s1, s2,dp)
        else: # s1[m -1] == s2[n -1]
            dp[n][m]= max (self.LCS(m, n-1, s1, s2,dp), self.LCS(m-1, n, s1, s2,dp))
        return dp[n][m]


# method 3: Bottom up approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x, y= len(text1), len(text2)
        return self.lcs(x,y,text1,text2)
    def lcs(self,x,y,s1,s2):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]

# method 4: optimise the space

