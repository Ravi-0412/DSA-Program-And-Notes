# Logic:
"""
A useful trick (when doing any parentheses validation) is to greedily check balance left-to-right, and then right-to-left.

Left-to-right check ensures that we do not have orphan ')' parentheses.
Right-to-left checks for orphan '(' parentheses.

1) Check from left to right:
Traverse the string, treating every ( and unlocked position (0) as potential open brackets.
If the number of close brackets ) exceeds the available open brackets, the string cannot be valid.

2) Check from right to left:
Traverse the string in reverse, treating every ) and unlocked position (0) as potential close brackets.
If the number of open brackets ( exceeds the available close brackets, the string cannot be valid.

3) If both passes succeed, it means the flexible positions can accommodate the required parentheses to balance the string.
"""

# Time: O(n) , space: O(1)

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False

        open_count = 0
        for i in range(n):
            if s[i] == '(' or locked[i] == '0':
                open_count += 1
            else:
                open_count -= 1
            if open_count < 0:
                return False

        close_count = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                close_count += 1
            else:
                close_count -= 1
            if close_count < 0:
                return False

        return True

# Java
"""
class Solution {
    public boolean canBeValid(String s, String locked) {
        int n = s.length();
        if (n % 2 != 0) {
            return false;
        }

        int openCount = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(' || locked.charAt(i) == '0') {
                openCount++;
            } else {
                openCount--;
            }
            if (openCount < 0) {
                return false;
            }
        }

        int closeCount = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == ')' || locked.charAt(i) == '0') {
                closeCount++;
            } else {
                closeCount--;
            }
            if (closeCount < 0) {
                return false;
            }
        }

        return true;
    }
}
"""
