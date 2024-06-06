# similar to unbounded knapsack.

# Logic: At each step check if copied and paste allowed or not using two variables.
# And take minimum of both cases when copy and paste is allowed.

# Recursive method got accepted . But we can optimise using DP.

class Solution:
    def minSteps(self, n: int) -> int:

        def noOfSteps(char_on_screen, copy_allowed, paste_allowed, copied_char):
            if char_on_screen == n:
                return 0
            ans = float('inf')
            if copy_allowed and char_on_screen * 2 <= n:
                    # copied_char will become = char_on_screen
                    ans = min(ans, 1+ noOfSteps(char_on_screen , False, True, char_on_screen))
            if paste_allowed and char_on_screen + copied_char <= n:
                # in this we can copy same no of character again and again i.e copied_Char.
                ans = min(ans, 1 + noOfSteps(char_on_screen + copied_char, True, True, copied_char))
            return ans

        return noOfSteps(1, True, False, 1)