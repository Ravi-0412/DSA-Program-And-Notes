# Logic: If you will see the rules properly,
# you can analyse that it is simply asking: " Maximum depth of any ( ".

# Here digits '0-9' and 'operator' won't matter.

# So when you see '(' depth will increase by 1 and when you will see ')' depth will decrease by 1.
# Just take maximum after each character.

class Solution:
    def maxDepth(self, s: str) -> int:
        skip = {"0", "1", "2","3", "4" ,"5","6","7","8","9", "+", "-", "*", "/"}
        depth = ans = 0
        for c in s:
            if c in skip: 
                continue
            if c == '(':
                depth += 1
            else:
                depth -= 1
            ans = max(ans, depth)
        return ans

        