# Method 1: Using 'Z- algo'.

# See the q: "2223. Sum of Scores of Built Strings" for detailed explanation.

# Time : O(m + n)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m , n = len(haystack) , len(needle)
        # Make a new string combining both the string with one special character(to avoid comparison beyond that char)
        # jiska find karna h usko phle and jisme find karna h usko bad me.
        # Kyonki prefix == sufffix chahiye and jiska karna h wo prefix hona chahiye.
        s = needle + '$' + haystack   # any special symbol which is not allowed in string 
        # Now apply 'Z - Algo'.
        z = [0] * (m + n + 1)  # '1' for special symbol
        total = m + n + 1
        l , r = 0, 0
        for i in range(1, total):
            if i < r:
                z[i] = min(r -i , z[i - l])
            while i + z[i] < total and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] > r:
                l , r = i, i + z[i]
        # Now find the 1st index in 'z' for which z[i] == len(needle) that will be our ans.
        print(z)
        # only we need to check in string 'haystack' and that will start from 'n+1'.
        for i in range(n + 1, total):  
            if z[i] == n:  # len(needle)
                return i - n - 1  # then actual index in haystack will be excluding the len(needle) + 1(special symbol)
        return -1

