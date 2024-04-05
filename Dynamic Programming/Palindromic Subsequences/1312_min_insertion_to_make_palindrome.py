# just find the length of longest palindromic subsequence and
# subtract this from the length of the string as these are extra char 
# beyond longest palindromic sequence so we have to insert copy of these characters 
# only to make the whole string palindrome
# that will be the ans

# ans will be same for only deletion OR only insertion to make a string palindrome.
class Solution:
    def minInsertions(self, s: str) -> int:
        s1= s[::-1]
        # print(S)
        x,y= len(s), len(s)
        longest_palindrome_length= self.Lcs(x,y,s,s1)
        char_to_insert= len(s)- longest_palindrome_length
        return char_to_insert
    
    def Lcs(self,x,y,s1,s2):
        dp= [[0 for i in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1, y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i][j-1], dp[i-1][j])
        return dp[x][y]