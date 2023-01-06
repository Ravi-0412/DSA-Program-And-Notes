class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, stack= [], []
        
        def Backtrack(openP, closeP):
            if openP== closeP== n:  # means stack will be containing one of the valid parenthesis.
                ans.append("".join(stack))
                return
            # can only add '(' if the openP < n
            if openP < n:
                stack.append('(')
                Backtrack(openP +1, closeP)
                stack.pop()
            # only add close paranthesis if no of open Paranthesis is greater than the no of close paranthesis.
            if closeP < openP:
                stack.append(')')
                Backtrack(openP, closeP +1)
                stack.pop()
        
        Backtrack(0,0)    # this will tell the no of open and closed paranthesis we have added till now.
        return ans