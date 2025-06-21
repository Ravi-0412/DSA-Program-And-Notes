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

