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