# Just exact logic as :"392. Is Subsequence"

# Logic: Just find till which index in 't' you are able to find subsequence in 's'.
# For this we can apply same logic as : "392. Is Subsequence".
# Suppose from index 'j' you are not able to find then 
# you have to append 'len(t) - j' char at the end.

# Time: O(n)

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        i , j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return n - j