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

# Method 3: Optimised solution in O(n*logn) 
# Same method one :  question " 1044. Longest Duplicate Substring"

class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s)  # Length of the input string
        base, mod = 26, 2**63 - 1  # Base for hash (26 for 26 lowercase letters), large prime modulus
        
        def search(L: int) -> bool:
            """ 
            Helper function to check if there is a repeating substring of length L.
            Uses rolling hash (Rabin-Karp) to detect duplicates.
            Returns True if a duplicate is found, False otherwise.
            """
            current_hash, baseL = 0, pow(base, L, mod)  # Initialize the hash, and precompute base^L % mod
            seen_hashes = set()  # Set to store hashes of substrings we've seen

            # Step 1: Compute the hash for the first substring of length L
            for i in range(L):
                current_hash = (current_hash * base + ord(s[i]) - ord('a')) % mod  # Calculate initial hash
            seen_hashes.add(current_hash)  # Store the hash of the first substring

            # Step 2: Slide over the string, updating the hash for each new substring of length L
            for i in range(1, n - L + 1):
                # Rolling hash: add the new character and remove the old character
                current_hash = (current_hash * base + ord(s[i + L - 1]) - ord('a')) % mod  # Add new char
                current_hash = (current_hash - (ord(s[i - 1]) - ord('a')) * baseL) % mod  # Remove old char

                # Check if the new hash has been seen before
                if current_hash in seen_hashes:
                    return True  # Found a duplicate substring with this hash
                seen_hashes.add(current_hash)  # Add the new hash to the set
            
            return False  # No duplicate substring of length L was found

        # Binary search for the longest length of repeating substring
        low, high, result = 1, n - 1, 0
        
        while low <= high:
            mid = (low + high) // 2  # Check the middle value of the current range
            if search(mid):  # If we find a duplicate substring of length mid
                result = mid  # Update result, since we found a repeating substring
                low = mid + 1  # Try to find a longer one, search in the upper half
            else:
                high = mid - 1  # No repeating substring of this length, search in the lower half
        
        return result  # Return the length of the longest repeating substring

