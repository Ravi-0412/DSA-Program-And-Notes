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

<<<<<<< HEAD
# Java Code 
"""
class Solution {
    public int longestRepeatingSubstring(String s) {
        int n = s.length();
        Map<String, Integer> substringCount = new HashMap<>();
        int maxLen = 0;

        // Generate all possible substrings
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                String substring = s.substring(i, j);
                substringCount.put(substring, substringCount.getOrDefault(substring, 0) + 1);

                // If the substring appears more than once, it's a repeating substring
                if (substringCount.get(substring) > 1) {
                    maxLen = Math.max(maxLen, j - i);  // j - i is the length of the substring
                }
            }
        }

        return maxLen;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int longestRepeatingSubstring(string s) {
        int n = s.length();
        unordered_map<string, int> substringCount;
        int maxLen = 0;

        // Generate all possible substrings
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                string substring = s.substr(i, j - i);
                substringCount[substring]++;

                // If the substring appears more than once, it's a repeating substring
                if (substringCount[substring] > 1) {
                    maxLen = max(maxLen, j - i);  // j - i is the length of the substring
                }
            }
        }

        return maxLen;
    }
};
"""

# Method 2: Using DP
=======

# Method 2: 
# Using DP
>>>>>>> a40de18 (verified Binary Search and DP)
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

<<<<<<< HEAD
# Java Code 
"""
class Solution {
    public int longestRepeatingSubstring(String s) {
        int n = s.length();
        // dp[i][j] will store the length of the longest common substring ending at s[i-1] and s[j-1]
        int[][] dp = new int[n + 1][n + 1];
        int maxLen = 0;  // Variable to track the maximum length of the repeating substring

        // Fill the DP table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                // Only check for repeating substrings where indices are not the same
                if (s.charAt(i - 1) == s.charAt(j - 1) && i != j) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    maxLen = Math.max(maxLen, dp[i][j]);  // Update maxLen if we found a longer substring
                }
            }
        }

        return maxLen;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int longestRepeatingSubstring(string s) {
        int n = s.length();
        // dp[i][j] will store the length of the longest common substring ending at s[i-1] and s[j-1]
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        int maxLen = 0;  // Variable to track the maximum length of the repeating substring

        // Fill the DP table
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                // Only check for repeating substrings where indices are not the same
                if (s[i - 1] == s[j - 1] && i != j) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    maxLen = max(maxLen, dp[i][j]);  // Update maxLen if we found a longer substring
                }
            }
        }

        return maxLen;
    }
};
"""
# Method 3: Optimised solution in O(n*logn) 
=======

# Method 3: 
# Optimised solution in O(n*logn) 
>>>>>>> a40de18 (verified Binary Search and DP)
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

# Java Code 
"""
class Solution {
    public int longestRepeatingSubstring(String s) {
        int n = s.length();  // Length of the input string
        int base = 26;
        long mod = (1L << 63) - 1;  // Base for hash (26 lowercase letters), large prime modulus

        // Binary search for the longest length of repeating substring
        int low = 1, high = n - 1, result = 0;

        while (low <= high) {
            int mid = (low + high) / 2;  // Check the middle value of the current range
            if (search(mid, s, base, mod)) {
                result = mid;      // Found a repeating substring
                low = mid + 1;     // Try to find a longer one
            } else {
                high = mid - 1;    // No repeating substring of this length
            }
        }

        return result;  // Return the length of the longest repeating substring
    }

    private boolean search(int L, String s, int base, long mod) {
        // Helper function to check if there is a repeating substring of length L using rolling hash
        int n = s.length();
        long currentHash = 0, baseL = 1;

        // Precompute base^L % mod
        for (int i = 0; i < L; i++) {
            baseL = (baseL * base) % mod;
            currentHash = (currentHash * base + s.charAt(i) - 'a') % mod;
        }

        Set<Long> seenHashes = new HashSet<>();
        seenHashes.add(currentHash);  // Store the hash of the first substring

        // Slide over the string, updating the rolling hash
        for (int i = 1; i <= n - L; i++) {
            currentHash = (currentHash * base + s.charAt(i + L - 1) - 'a') % mod;  // Add new char
            currentHash = (currentHash - (s.charAt(i - 1) - 'a') * baseL % mod + mod) % mod;  // Remove old char

            if (seenHashes.contains(currentHash))
                return true;  // Found a duplicate substring
            seenHashes.add(currentHash);  // Add new hash
        }

        return false;  // No duplicate substring of length L was found
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int longestRepeatingSubstring(string s) {
        int n = s.length();  // Length of the input string
        int base = 26;
        long long mod = (1LL << 63) - 1;  // Base for hash (26 lowercase letters), large prime modulus

        // Binary search for the longest length of repeating substring
        int low = 1, high = n - 1, result = 0;

        while (low <= high) {
            int mid = (low + high) / 2;  // Check the middle value of the current range
            if (search(mid, s, base, mod)) {
                result = mid;      // Found a repeating substring
                low = mid + 1;     // Try to find a longer one
            } else {
                high = mid - 1;    // No repeating substring of this length
            }
        }

        return result;  // Return the length of the longest repeating substring
    }

private:
    bool search(int L, const string& s, int base, long long mod) {
        // Helper function to check if there is a repeating substring of length L using rolling hash
        int n = s.length();
        long long currentHash = 0, baseL = 1;

        // Precompute base^L % mod
        for (int i = 0; i < L; i++) {
            baseL = (baseL * base) % mod;
            currentHash = (currentHash * base + s[i] - 'a') % mod;
        }

        unordered_set<long long> seenHashes;
        seenHashes.insert(currentHash);  // Store the hash of the first substring

        // Slide over the string, updating the rolling hash
        for (int i = 1; i <= n - L; i++) {
            currentHash = (currentHash * base + s[i + L - 1] - 'a') % mod;  // Add new char
            currentHash = (currentHash - (s[i - 1] - 'a') * baseL % mod + mod) % mod;  // Remove old char

            if (seenHashes.count(currentHash))
                return true;  // Found a duplicate substring
            seenHashes.insert(currentHash);  // Add new hash
        }

        return false;  // No duplicate substring of length L was found
    }
};
"""
