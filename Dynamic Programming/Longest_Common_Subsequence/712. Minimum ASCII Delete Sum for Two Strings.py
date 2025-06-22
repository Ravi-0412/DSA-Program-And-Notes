# Method 1: 

# Exactly same as : "583. Delete Operation for Two Strings".
# Exactly same only we need to add the ascii value of characters we are deleting.

# Exactly written same code of above Q only.

# Time: O(n^2)

class Solution:
    def minimumDeleteSum(self, word1: str, word2: str) -> int:
<<<<<<< HEAD
        if not word1 or not word2:
            sum = 0
            if word1:
                for c in word1:
                    sum += ord(c)
                    
            if word2:
                for c in word2:
                    sum += ord(c)
            return sum
        ans = 0
        if word1[0] == word2[0]:
            ans = self.minimumDeleteSum(word1[1 : ], word2[1: ])
        else:
            ans = min(ord(word1[0]) + self.minimumDeleteSum(word1[1 : ], word2), ord(word2[0]) + self.minimumDeleteSum(word1, word2[1: ]))
        return ans
    
# Java Code 
"""
class Solution {
    public int minimumDeleteSum(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        Integer[][] dp = new Integer[m + 1][n + 1];
        return helper(0, 0, word1, word2, dp);
    }

    private int helper(int i, int j, String w1, String w2, Integer[][] dp) {
        if (i == w1.length() && j == w2.length()) return 0;

        if (dp[i][j] != null) return dp[i][j];

        if (i == w1.length()) {
            int sum = 0;
            for (int k = j; k < w2.length(); k++) sum += w2.charAt(k);
            return dp[i][j] = sum;
        }
        if (j == w2.length()) {
            int sum = 0;
            for (int k = i; k < w1.length(); k++) sum += w1.charAt(k);
            return dp[i][j] = sum;
        }

        int ans;
        if (w1.charAt(i) == w2.charAt(j)) {
            ans = helper(i + 1, j + 1, w1, w2, dp);
        } else {
            ans = Math.min(w1.charAt(i) + helper(i + 1, j, w1, w2, dp),
                           w2.charAt(j) + helper(i, j + 1, w1, w2, dp));
        }

        dp[i][j] = ans;
        return ans;
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
    int minimumDeleteSum(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return helper(0, 0, word1, word2, dp);
    }

private:
    int helper(int i, int j, const string& w1, const string& w2, vector<vector<int>>& dp) {
        if (i == w1.size() && j == w2.size()) return 0;

        if (dp[i][j] != -1) return dp[i][j];

        if (i == w1.size()) {
            int sum = 0;
            for (int k = j; k < w2.size(); k++) sum += w2[k];
            return dp[i][j] = sum;
        }
        if (j == w2.size()) {
            int sum = 0;
            for (int k = i; k < w1.size(); k++) sum += w1[k];
            return dp[i][j] = sum;
        }

        int ans;
        if (w1[i] == w2[j]) {
            ans = helper(i + 1, j + 1, w1, w2, dp);
        } else {
            ans = min(w1[i] + helper(i + 1, j, w1, w2, dp),
                      w2[j] + helper(i, j + 1, w1, w2, dp));
        }

        return dp[i][j] = ans;
    }
};
"""
=======
        m, n = len(word1), len(word2)
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        def solve(i, j):
            if i == m or j == n:
                total = 0
                # Add ASCII values of remaining characters in word1
                for k in range(i, m):
                    total += ord(word1[k])
                # Add ASCII values of remaining characters in word2
                for k in range(j, n):
                    total += ord(word2[k])
                return total

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                ans = solve(i + 1, j + 1)
            else:
                delete_from_word1 = ord(word1[i]) + solve(i + 1, j)
                delete_from_word2 = ord(word2[j]) + solve(i, j + 1)
                ans = min(delete_from_word1, delete_from_word2)

            dp[i][j] = ans
            return ans

        return solve(0, 0)

>>>>>>> a40de18 (verified Binary Search and DP)
