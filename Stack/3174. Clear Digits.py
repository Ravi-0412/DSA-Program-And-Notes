# Just same method as: "1047. Remove All Adjacent Duplicates In String".
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c.isdigit():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)