# Method 1:

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

# Java Code 
"""
class Solution {
    public int longestPalinSubseq(String S) {
        String S1 = new StringBuilder(S).reverse().toString();
        int x = S.length(), y = S.length();
        return Lcs(x, y, S, S1);
    }

    private int Lcs(int x, int y, String s1, String s2) {
        int[][] dp = new int[x + 1][y + 1];
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }
        return dp[x][y];
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestPalinSubseq(string S) {
        string S1 = S;
        reverse(S1.begin(), S1.end());
        int x = S.length(), y = S.length();
        return Lcs(x, y, S, S1);
    }

private:
    int Lcs(int x, int y, const string& s1, const string& s2) {
        vector<vector<int>> dp(x + 1, vector<int>(y + 1, 0));
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1[i - 1] == s2[j - 1]) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
                }
            }
        }
        return dp[x][y];
    }
};
"""
# Method 2:
# Travsersing in same string 's'
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

# Java Code 
"""
class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            java.util.Arrays.fill(dp[i], -1);
        }

        return helper(0, n - 1, s, dp);
    }

    private int helper(int l, int r, String s, int[][] dp) {
        if (l == r) return 1;
        if (l > r) return 0;
        if (dp[l][r] != -1) return dp[l][r];

        if (s.charAt(l) == s.charAt(r)) {
            dp[l][r] = 2 + helper(l + 1, r - 1, s, dp);
        } else {
            dp[l][r] = Math.max(helper(l + 1, r, s, dp), helper(l, r - 1, s, dp));
        }

        return dp[l][r];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        return helper(0, n - 1, s, dp);
    }

private:
    int helper(int l, int r, const string& s, vector<vector<int>>& dp) {
        if (l == r) return 1;
        if (l > r) return 0;
        if (dp[l][r] != -1) return dp[l][r];

        if (s[l] == s[r]) {
            dp[l][r] = 2 + helper(l + 1, r - 1, s, dp);
        } else {
            dp[l][r] = max(helper(l + 1, r, s, dp), helper(l, r - 1, s, dp));
        }

        return dp[l][r];
    }
};
"""
# Method 3: 
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

# Java Code 
"""
class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        for (int l = n - 1; l >= 0; l--) {
            for (int r = l + 1; r < n; r++) {
                if (s.charAt(l) == s.charAt(r)) {
                    dp[l][r] = 2 + dp[l + 1][r - 1];
                } else {
                    dp[l][r] = Math.max(dp[l + 1][r], dp[l][r - 1]);
                }
            }
        }

        return dp[0][n - 1];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.length();
        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }

        for (int l = n - 1; l >= 0; l--) {
            for (int r = l + 1; r < n; r++) {
                if (s[l] == s[r]) {
                    dp[l][r] = 2 + dp[l + 1][r - 1];
                } else {
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1]);
                }
            }
        }

        return dp[0][n - 1];
    }
};
"""

"""
Related Questions:
1) Minimum number of deletions to make a string palindrome
2) 1312. Minimum Insertion Steps to Make a String Palindrome
3) 1771. Maximize Palindrome Length From Subsequences
"""
