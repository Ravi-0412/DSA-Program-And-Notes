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

