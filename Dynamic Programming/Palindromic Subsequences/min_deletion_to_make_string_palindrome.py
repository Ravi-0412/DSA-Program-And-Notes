# Note: if only deletion is allowed , then for making both string same . Make both equal to lcs(here longest palindromic subsequence )
# just find the length of longest palindromic subsequence and
# subtract this from the length of the string as these are extra char 
# beyond longest palindromic sequence so we have to delete this only
# that will be the ans
class Solution:
    def minDeletions(self, Str, n): 
        S1= Str[::-1]
        # print(S)
        x,y= n, n
        longest_palindrome_length= self.Lcs(x,y,Str,S1)
        char_to_delete= n- longest_palindrome_length
        return char_to_delete
    def Lcs(self,x,y,s1,s2):
        dp= [[0 for i in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1, y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i][j-1], dp[i-1][j])
        return dp[x][y]

