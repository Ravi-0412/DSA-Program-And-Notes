# Method 1: 

# Exactly same as : "583. Delete Operation for Two Strings".
# Exactly same only we need to add the ascii value of characters we are deleting.

# Exactly written same code of above Q only.

# Time: O(n^2)

class Solution:
    def minimumDeleteSum(self, word1: str, word2: str) -> int:
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

# Java Code 
"""
class Solution {
    public int minimumDeleteSum(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int[] row : dp) {
            java.util.Arrays.fill(row, -1);
        }

        return solve(0, 0, word1, word2, dp);
    }

    public int solve(int i, int j, String word1, String word2, int[][] dp) {
        int m = word1.length(), n = word2.length();
        if (i == m || j == n) {
            int total = 0;
            // Add ASCII values of remaining characters in word1
            for (int k = i; k < m; k++) {
                total += word1.charAt(k);
            }
            // Add ASCII values of remaining characters in word2
            for (int k = j; k < n; k++) {
                total += word2.charAt(k);
            }
            return total;
        }

        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        int ans;
        if (word1.charAt(i) == word2.charAt(j)) {
            ans = solve(i + 1, j + 1, word1, word2, dp);
        } else {
            int delete_from_word1 = word1.charAt(i) + solve(i + 1, j, word1, word2, dp);
            int delete_from_word2 = word2.charAt(j) + solve(i, j + 1, word1, word2, dp);
            ans = Math.min(delete_from_word1, delete_from_word2);
        }

        dp[i][j] = ans;
        return ans;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int minimumDeleteSum(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return solve(0, 0, word1, word2, dp);
    }

    int solve(int i, int j, const string& word1, const string& word2, vector<vector<int>>& dp) {
        int m = word1.size(), n = word2.size();

        if (i == m || j == n) {
            int total = 0;
            // Add ASCII values of remaining characters in word1
            for (int k = i; k < m; ++k) {
                total += word1[k];
            }
            // Add ASCII values of remaining characters in word2
            for (int k = j; k < n; ++k) {
                total += word2[k];
            }
            return total;
        }

        if (dp[i][j] != -1) {
            return dp[i][j];
        }

        int ans;
        if (word1[i] == word2[j]) {
            ans = solve(i + 1, j + 1, word1, word2, dp);
        } else {
            int delete_from_word1 = word1[i] + solve(i + 1, j, word1, word2, dp);
            int delete_from_word2 = word2[j] + solve(i, j + 1, word1, word2, dp);
            ans = min(delete_from_word1, delete_from_word2);
        }

        dp[i][j] = ans;
        return ans;
    }
};
"""