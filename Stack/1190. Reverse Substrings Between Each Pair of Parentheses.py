# Time: O(n^2)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]  # Addding empty string to get original string only when we append something to it.
                      # otherwise we won't be able to add the current pop string with stack top because stack will be empty.
        for c in s:
            if c == '(':
                stack.append("")
            elif c == ')':
                # reverse the string on top of stack
                temp = stack.pop()[::-1]
                # then add the reversed string to stack top
                stack[-1] += temp
            else:
                stack[-1] += c   # add with stack top
        return stack.pop()

# Later do in O(n), link in sheet