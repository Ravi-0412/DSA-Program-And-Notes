# Just extension  of "525. Contiguous Array"

"""
Logic: For each substring, we count how many vowels and consonants it contains.
Check Conditions: vowels == consonants and (vowels * consonants) % k == 0

Time : O(n^2)
"""

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        vowels_set = set("aeiou")
        
        for i in range(n):
            v = 0
            c = 0
            for j in range(i, n):
                if s[j] in vowels_set:
                    v += 1
                else:
                    c += 1
                # check if beautiful subarray
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans

# Method 2:
# Optimised one : Do it later by understanding properly
"""
"""
