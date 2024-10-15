# Method 1:
# Logic:
"""
Store all substring in Hashmap and keep on checking for longest repeating.
"""

# Time: O(n^3), o(n^2) : for all possible substring and O(n) average : for checking if present in hashmp or not.

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        substring_count = {}
        max_len = 0

        # Generate all possible substrings
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if substring in substring_count:
                    substring_count[substring] += 1
                else:
                    substring_count[substring] = 1
                
                # If the substring appears more than once, it's a repeating substring
                if substring_count[substring] > 1:
                    max_len = max(max_len, j - i)  # j - i is the length of the substring

        return max_len

# Method 2: Using DP
# Logic:
"""
1) Let dp[i][j] represent the length of the longest common substring between the suffixes starting
at index i and index j of the string, under the condition that i != j (to avoid matching the substring with itself.
2) Recurrence Relation:
If s[i-1] == s[j-1] and i != j, then dp[i][j] = dp[i-1][j-1] + 1.
Otherwise, dp[i][j] = 0 (i.e., no common substring at these indices).
3) Result: Track the maximum value in the DP table, which will give the length of the longest repeating substring.

"""
# Time: O(n^2)

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)
        # dp[i][j] will store the length of the longest common substring ending at s[i-1] and s[j-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        max_len = 0  # Variable to track the maximum length of the repeating substring
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # Only check for repeating substrings where indices are not the same
                if s[i - 1] == s[j - 1] and i != j:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])  # Update max_len if we found a longer substring
        
        return max_len
