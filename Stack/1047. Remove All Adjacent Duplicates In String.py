# time= space= O(n)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack= []
        for c in s:
            # check if same char id present at the top of stack.
            # used 'if' because we only need to delete only twp adjacent char
            if stack and stack[-1]== c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


# Later try by two pointer also