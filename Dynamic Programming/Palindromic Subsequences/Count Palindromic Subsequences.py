# We also have to count duplicate subsequences

# Logic: 
"""
DP(L, R), is the number of palindromic subsequences in S[L .... R]. Its formulated as following.

i)      0 , if L>R
ii)     1 , if L=R
iii)    DP(L + 1, R) + DP(L, R-1) - DP(L+1, R-1) , if S[L] != S[R]
iv)     DP(L + 1, R) + DP(L, R-1) + 1 , if S[L] = S[R]

iii) Why the third one?
if S[L] != S[R] then we have two choices: DP(L + 1, R) + DP(L, R-1) but in this 'DP(L+1, R-1)' is getting added two times
that's why we will remove this.
if S[L] != S[R]:
    DP(L + 1, R) + DP(L, R-1) - DP(L+1, R-1)

# Note: see the fig inside: https://leetcode.com/problems/count-different-palindromic-subsequences/solutions/272297/dp-c-clear-solution-explained/
for see how 'DP(L+1, R-1)' is getting added two times.

iv) if S[L] == S[R]:
then we have two choice:
a) include both 'L' and 'R'  => DP(L+1, R-1) + 1(only border element)
b) we don't include both =>  DP(L + 1, R) + DP(L, R-1) 
Note: b) DP(L+1, R-1) will come two times so we have to subtract 'DP(L+1, R-1)' in 'b)'.
finally when we don't include both => DP(L + 1, R) + DP(L, R-1) - DP(L+1, R-1)

So total if S[L] == S[R]  => 'a' + 'b' = DP(L+1, R-1) + 1 + DP(L + 1, R) + DP(L, R-1) - DP(L+1, R-1) => DP(L + 1, R) + DP(L, R-1) + 1

"""

# Recursive + memoisation
class Solution:
    def __init__(self):
        self.mod = 10**9 + 7  
        
    def countPS(self,string):
        n = len(string)
        dp = [[-1 for x in range(n)] for y in range(n)]

        return self.solve(string, 0, n - 1, dp)
    
    def solve(self, s, i, j, dp):
        if i == j:
            # Base case: when the indices are the same, there is one palindrome
            return 1
        if i > j:
            # Base case: when the first index is greater than the second, there are no palindromes
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i] == s[j]:
            # If the characters at indices i and j are the same, we can form palindromic subsequences
            # by including or excluding both characters, so we add 1 and make recursive calls.
            dp[i][j] =  (1 + self.solve(s, i + 1, j, dp) + self.solve(s, i, j - 1, dp)) % self.mod
        else:
            # If the characters at indices i and j are different, we exclude one of them and make recursive calls.
            dp[i][j] =  (self.solve(s, i + 1, j, dp) + self.solve(s, i, j - 1, dp) - self.solve(s, i + 1, j - 1, dp)) % self.mod
        return dp[i][j] % self.mod

# Tabulation
class Solution:
    def countPS(self,s):
        n = len(s)
        self.mod = 10**9 + 7 
        dp = [[0 for x in range(n)] for y in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] =  (1 + dp[i+1][j] + dp[i][j-1]) % self.mod
                else:
                    dp[i][j] =  (dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]) % self.mod
                    
        return dp[0][n-1] % self.mod

# java
"""
class Solution {
    public int countPS(String s) {
        int n = s.length();
        int mod = 1000000007;
        
        // Create a 2D DP array to store results of subproblems
        int[][] dp = new int[n][n];
        
        // Single characters are palindromic subsequences
        for (int i = 0; i < n; i++) {
            dp[i][i] = 1;
        }
        
        // Fill the DP table
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = (1 + dp[i + 1][j] + dp[i][j - 1]) % mod;
                } else {
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + mod) % mod;
                }
            }
        }
        
        // Return the result for the entire string
        return dp[0][n - 1];
    }
}

"""

# extension
# 1) 730. Count Different Palindromic Subsequences
# count distinct palindromic subsequences