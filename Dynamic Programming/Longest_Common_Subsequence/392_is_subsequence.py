# if s is a subsequence of 't' then lcs of 's' and 't'
# must be equal to the 's' itself as lcs of two strings is
# always less than or equal to the length of min(length of either string)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x,y= len(s), len(t)
        lcs_length= self.lcs(x,y,s,t)
        if lcs_length== x:  # check if length of lcs= len(substring)
            return True
        return False
    def lcs(self,x,y,s1,s2):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]
