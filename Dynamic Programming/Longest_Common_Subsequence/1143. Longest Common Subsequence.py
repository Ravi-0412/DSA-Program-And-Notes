# method 1: Recursive way
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n= len(text1), len(text2)
        return self.LCS(m, n, text1, text2)
    def LCS(self, m, n, s1, s2):
        if m==0 or n==0:
            return 0
        if s1[m -1] == s2[n -1]:
            return 1+ self.LCS(m-1, n-1, s1, s2)
        # else: # s1[m -1] != s2[n -1]
        return max (self.LCS(m, n-1, s1, s2), self.LCS(m-1, n, s1, s2))

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
        else: # s1[m -1] != s2[n -1]
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

# Java
"""
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        return LCS(m, n, text1, text2);
    }
    
    private int LCS(int m, int n, String s1, String s2) {
        // Base case: if one of the strings is empty, no common subsequence.
        if (m == 0 || n == 0) {
            return 0;
        }
        // If the characters at the end of both strings are the same,
        // consider it as part of the subsequence.
        if (s1.charAt(m - 1) == s2.charAt(n - 1)) {
            return 1 + LCS(m - 1, n - 1, s1, s2);
        }
        // Otherwise, take the maximum between reducing either of the strings.
        return Math.max(LCS(m, n - 1, s1, s2), LCS(m - 1, n, s1, s2));
    }
}
"""

# Java : Tabulation
"""
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();
        
        // Initialize a dp table with all values set to -1.
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= m; j++) {
                dp[i][j] = -1;
            }
        }
        
        // Call the recursive function to calculate LCS
        return LCS(m, n, text1, text2, dp);
    }
    
    private int LCS(int m, int n, String s1, String s2, int[][] dp) {
        // Base case: if either string is empty, LCS is 0.
        if (m == 0 || n == 0) {
            return 0;
        }
        
        // If already computed, return the value from dp array.
        if (dp[n][m] != -1) {
            return dp[n][m];
        }
        
        // If the characters at the end of both strings match.
        if (s1.charAt(m - 1) == s2.charAt(n - 1)) {
            dp[n][m] = 1 + LCS(m - 1, n - 1, s1, s2, dp);
        } else {
            // If characters do not match, consider both possibilities.
            dp[n][m] = Math.max(LCS(m, n - 1, s1, s2, dp), LCS(m - 1, n, s1, s2, dp));
        }
        
        // Return the value after calculation.
        return dp[n][m];
    }
}

"""

# method 4: optimise the space

