# method 1: Recursive way
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ans= 0
        m, n= len(text1), len(text2)
        return self.LCS(m, n, text1, text2)
    def LCS(self, m, n, s1, s2):
        ans= 0
        if m==0 or n==0:
            return 0
        elif s1[m -1] == s2[n -1]:
            SmallAns= 1+ self.LCS(m-1, n-1, s1, s2)
            ans= ans+ SmallAns
        else: # s1[m -1] == s2[n -1]
            SmallAns= max (self.LCS(m, n-1, s1, s2), self.LCS(m-1, n, s1, s2))
            ans= ans+ SmallAns
        return ans

# method 2: memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ans= 0
        m, n= len(text1), len(text2)
        dp= [[-1 for i in range(m+1)]for i in range(n+1)]
        return self.LCS(m, n, text1, text2, dp)
    def LCS(self, m, n, s1, s2, dp):
        ans= 0
        if m==0 or n==0:
            return 0
        if dp[n][m]!= -1:
            return dp[n][m]
        elif s1[m -1] == s2[n -1]:
            dp[n][m]= 1+ self.LCS(m-1, n-1, s1, s2,dp)
        else: # s1[m -1] == s2[n -1]
            dp[n][m]= max (self.LCS(m, n-1, s1, s2,dp), self.LCS(m-1, n, s1, s2,dp))
        return dp[n][m]

# method 3:
def longestCommonSubstr(S1, S2, n, m):
    dp= [[0 for j in range(m+1)] for i in range(n+1)]
    final= 0 #this will store the maximum common substring till any point
            # like when string char will not match then there may be chances that
            # already calculated common susbtring can be the final ans
    for i in range(1,n+1):
        for j in range(1,m+1):
            if S1[i-1]== S2[j-1]:
                dp[i][j]= 1+ dp[i-1][j-1]
            else:  # when doesn't match
                dp[i][j]= 0   # and in case of not match we are initialising with zero , will count again
            final= max(final,dp[i][j])   # after every check update final 
                                         # final is just storing the max till that point
                                         # because pre cal one before(making dp[i][j]= 0) can be also the maximum
    return final