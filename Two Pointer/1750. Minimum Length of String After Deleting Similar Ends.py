# Time: O(n)

class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i , j = 0, n-1
        while i < j:
            i1 = i
            while i + 1 < j and s[i] == s[i + 1]:
                i += 1
            i += 1

            j1 = j
            while j - 1 > i and s[j] == s[j - 1] :
                j -= 1
            j -= 1

            # check if char of prefix == suffix or not.
            if s[i1] != s[j1]:
                # If not equal then return diff between j1 and i1
                return j1 - i1 + 1
        # After while loop either 1)  j == i in this case ans = 1
        # 2) j will be '1' less than 'i'. Here ans = 0. Will happen when all element will get cancelled
        return j - i + 1