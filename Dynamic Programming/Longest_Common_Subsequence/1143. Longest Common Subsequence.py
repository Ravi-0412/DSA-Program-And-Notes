# method 1: 
# Recursive way
"""
LCS(m, n) = length of LCS between text1[0..m-1] and text2[0..n-1]

1) Base Case:

-- If either string is empty (m == 0 or n == 0), the LCS is 0.

2) Matching Characters:
If the last characters match:
text1[m - 1] == text2[n - 1]
→ We can include this character in the LCS:
→ LCS(m, n) = 1 + LCS(m - 1, n - 1)

3) Non-Matching Characters:

If they don't match:
→ We have two choices — skip one character from either string:
→ LCS(m, n) = max(LCS(m - 1, n), LCS(m, n - 1))

LCS(m, n) =
    0                          if m == 0 or n == 0
    1 + LCS(m-1, n-1)          if text1[m-1] == text2[n-1]
    max(LCS(m-1, n), LCS(m, n-1)) otherwise

"""
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

<<<<<<< HEAD
# Java Code 
"""
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        return LCS(m, n, text1, text2);
    }

    private int LCS(int m, int n, String s1, String s2) {
        if (m == 0 || n == 0) {
            return 0;
        }
        if (s1.charAt(m - 1) == s2.charAt(n - 1)) {
            return 1 + LCS(m - 1, n - 1, s1, s2);
        }
        // else: // s1[m -1] != s2[n -1]
        return Math.max(LCS(m, n - 1, s1, s2), LCS(m - 1, n, s1, s2));
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length(), n = text2.length();
        return LCS(m, n, text1, text2);
    }

private:
    int LCS(int m, int n, const string& s1, const string& s2) {
        if (m == 0 || n == 0) {
            return 0;
        }
        if (s1[m - 1] == s2[n - 1]) {
            return 1 + LCS(m - 1, n - 1, s1, s2);
        }
        // else: // s1[m -1] != s2[n -1]
        return max(LCS(m, n - 1, s1, s2), LCS(m - 1, n, s1, s2));
    }
};
"""

# method 2: memoization
=======
# method 2: 
# memoization
# Time = O(m*n)
>>>>>>> a40de18 (verified Binary Search and DP)
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

# Java Code 
"""
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[n + 1][m + 1];
        
        for (int i = 0; i <= n; i++)
            for (int j = 0; j <= m; j++)
                dp[i][j] = -1;
        
        return LCS(m, n, text1, text2, dp);
    }

    private int LCS(int m, int n, String s1, String s2, int[][] dp) {
        if (m == 0 || n == 0)
            return 0;
        if (dp[n][m] != -1)
            return dp[n][m];
        else if (s1.charAt(m - 1) == s2.charAt(n - 1))
            dp[n][m] = 1 + LCS(m - 1, n - 1, s1, s2, dp);
        else // s1[m -1] != s2[n -1]
            dp[n][m] = Math.max(LCS(m, n - 1, s1, s2, dp), LCS(m - 1, n, s1, s2, dp));
        return dp[n][m];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length(), n = text2.length();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1));
        return LCS(m, n, text1, text2, dp);
    }

private:
    int LCS(int m, int n, const string& s1, const string& s2, vector<vector<int>>& dp) {
        if (m == 0 || n == 0)
            return 0;
        if (dp[n][m] != -1)
            return dp[n][m];
        else if (s1[m - 1] == s2[n - 1])
            dp[n][m] = 1 + LCS(m - 1, n - 1, s1, s2, dp);
        else // s1[m -1] != s2[n -1]
            dp[n][m] = max(LCS(m, n - 1, s1, s2, dp), LCS(m - 1, n, s1, s2, dp));
        return dp[n][m];
    }
};
"""

# method 3: 
# Bottom up approach
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


<<<<<<< HEAD
# Java Code 
"""
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int x = text1.length(), y = text2.length();
        return lcs(x, y, text1, text2);
    }

    private int lcs(int x, int y, String s1, String s2) {
        int[][] dp = new int[x + 1][y + 1];
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[x][y];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int x = text1.length(), y = text2.length();
        return lcs(x, y, text1, text2);
    }

private:
    int lcs(int x, int y, const string& s1, const string& s2) {
        vector<vector<int>> dp(x + 1, vector<int>(y + 1, 0));
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[x][y];
    }
};
"""
=======
>>>>>>> a40de18 (verified Binary Search and DP)

# method 4: optimise the space

# Related Question
"""
1) Printing Longest Common Subsequence
2) Longest Common Substring
"""
