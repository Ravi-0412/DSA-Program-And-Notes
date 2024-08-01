# Logic: Concatenate both word and aply same logic as '516. Longest Palindromic Subsequence' only diff:
# when we find any palindrome check whether indices are from different string.

# Time & Space: O((m+n)^2), where m <= 1000 is length of word1, n <= 1000 is length of word2

class Solution(object):
    def longestPalindrome(self, word1, word2):
        word = word1 + word2
        n = len(word)
        ans = 0
        dp = [[0]*n for i in range(n)]
        for i in range(n):
            dp[i][i] = 1   
        for l in range(n-1, -1, -1):
            for r in range(l + 1, n):
                if word[l] == word[r]:
                    dp[l][r] = dp[l+1][r-1] + 2
                    if l < len(word1) and r >= len(word1):  
                        # Check if this palindrome begins with word1[i] and ends with word2[j]
                        # i.e both indices belong to different string
                        ans = max(ans, dp[l][r])
                else:
                    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
        return ans
    

# my 1st thought and mistake
# Thought just reverse 'word2' and then find LCS between 'word1' and 'reversed_word2'.
# And double the ans and add '1' because single letter can come in between.
# But it won't work when subsewuences are contigous in both string.
# e.g: word1 = "cfe" , word2 = "ef"
# Output : 5 but ans should be = 4

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word2[::-1]
        x, y = len(word1), len(word2)
        return self.Lcs(x, y, word1, s)
    
    def Lcs(self,x,y,s1,s2):
        dp= [[0 for i in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1, y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i][j-1], dp[i-1][j])
        ans = 2* dp[x][y] 
        if ans == 0:
            return 0
        return ans if ans == len(s1) + len(s2) else ans + 1
        