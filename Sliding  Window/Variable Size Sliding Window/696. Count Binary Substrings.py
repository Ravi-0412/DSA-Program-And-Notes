# Logic: First, I count the number of 1 or 0 grouped consecutively.
# For example "0110001111" will be [1, 2, 3, 4].

# Second, for any possible substrings with 1 and 0 grouped consecutively, 
# the number of valid substring will be the minimum number of 0 and 1.
# For example "0001111", will be min(3, 4) = 3, ("01", "0011", "000111").


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        consecutive_count = []  # will store count of consecutive '0' / '1' 
        i = 0
        while i < len(s):
            cnt = 1
            i += 1
            while i < len(s) and s[i -1] == s[i]:
                i += 1
                cnt += 1
            consecutive_count.append(cnt)

        ans = 0
        for i in range(1, len(consecutive_count)):
            # will form valid substring with adjacent only and number = min(i-1, i)
            ans += min(consecutive_count[i - 1] , consecutive_count[i])
        return ans        
    
# Method 2: Optimising space
# we only care about current_count and pre_count.
# so just use two variables instead of using an array.

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur = 1  # Current sequence length
        pre = 0  # Previous sequence length
        res = 0  # Result to store the count of valid substrings

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            # If current character is the same as the previous one, increment `cur`
            if s[i] == s[i - 1]:
                cur += 1
            else:
                # Otherwise, add the minimum of `cur` and `pre` to `res`
                res += min(cur, pre)
                # Update `pre` to the length of the current sequence
                pre = cur
                # Reset `cur` to 1 for the new sequence
                cur = 1

        # Add the last comparison between the final `cur` and `pre` to `res`
        res += min(cur, pre)

        return res


# java
"""
class Solution {
    public int countBinarySubstrings(String s) {
        int cur = 1;   // Current sequence length
        int pre = 0;   // Previous sequence length
        int res = 0;   // Result to store the count of valid substrings

        // Iterate through the string starting from the second character
        for (int i = 1; i < s.length(); i++) {
            // If current character is the same as the previous one, increment `cur`
            if (s.charAt(i) == s.charAt(i - 1)) {
                cur++;
            } else {
                // Otherwise, add the minimum of `cur` and `pre` to `res`
                res += Math.min(cur, pre);
                // Update `pre` to the length of the current sequence
                pre = cur;
                // Reset `cur` to 1 for the new sequence
                cur = 1;
            }
        }

        // Add the last comparison between the final `cur` and `pre` to `res`
        res += Math.min(cur, pre);

        return res;
    }
}
"""