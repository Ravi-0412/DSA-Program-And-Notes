# time= space= O(n)

# Note: No need to check for 'left closest char other than * using while loop when we will see any *' 
# because the 'non char than * will get removed by the previous *.

# so only that char will get removed when it will be just adjacent to the current "*" directly or
# indirectly(after removing char in between).

class Solution:
    def removeStars(self, s: str) -> str:
        stack= []
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                if stack and stack[-1] != "*":
                    stack.pop()
        return "".join(stack)
