# just think from basic like how we evaluate the 'valid parenthesis Q'.
# parenthesis is valid only if 'openp==0 at last', it means at last no '(' or ')' left and both were equal in number.

# since here we are generating the valid parenthesis, so will get the valid one when 'no of openP== closeP'.
# so we will keep track of both 'openP an closeP' count.

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

            # like in 'evaluate valid paranthesis we only decrease the 'openP' value when we encounter ')' and count of 'openP' should be >0 before decr.
            # i.e indirectly we are incr the 'closeP' value.
            # so same case here, we can only add ')' in ans when 'no of closeP < no of openP'
            if closeP < openP:
                stack.append(')')
                Backtrack(openP, closeP +1)
                stack.pop()
        
        Backtrack(0,0)    # this will tell the no of open and closed paranthesis we have added till now.
        return ans

