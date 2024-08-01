# Time: O(n)

class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i , j = 0, n-1
        while i < j:
            if s[i] != s[j]:
                return j - i + 1
            while i + 1 < j and s[i] == s[i + 1]:
                i += 1
            i += 1
            while j - 1 > i and s[j] == s[j - 1] :  # j - i >= i will also work
                j -= 1
            j -= 1
         # After while loop either 1)  j == i in this case ans = 1
        # 2) j will be '1' less than 'i'. Here ans = 0. Will happen when all element will get cancelled
        return j - i + 1

# java
"""
class Solution {
    public int minimumLength(String s) {
        int n = s.length();
        int i = 0, j = n - 1;

        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return j - i + 1;
            }
            while (i + 1 < j && s.charAt(i) == s.charAt(i + 1)) {
                i++;
            }
            i++;
            while (j - 1 > i && s.charAt(j) == s.charAt(j - 1)) {
                j--;
            }
            j--;
        }

        // After the while loop, either j == i (ans = 1) or j is 1 less than i (ans = 0)
        return j - i + 1;
    }
}
"""