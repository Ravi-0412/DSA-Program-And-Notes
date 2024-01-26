# logic:
# Addition: for simple paranthesis
# multiplication: for nested paranthesis.

# method 1: using stack
# hm har ek ABC ka score stack me rakh rahe and last me sum of stack value return kar rhe.  A,B,C : nested paranthesis.

# jaise hi hmko ')' dikh rha h, usi samay hm uske liye value find karke add me dal de rhe. 
# isse sbse internal ka stack me ja rhe then external ke liye hm sbko add kar denge to ans aa jayega.

# vvi: in case of nested paranthesis we have to keep track of score of internal paranthesis.
# so we will put number instead of  braces.
# when we will see '(', push '0' into the stack when you see ')' add all value till you see '0' 
# (indirectly we are searching for next '(' on left for which we will evaluate now).

# while poping add all the values and then calculate the score using score= max(2*val, 1). And put this into the stack. 
# Note: we always have to multiply the val by '2' to calculate the score. like we can consider '()' also a single nested. 
# but for '()', score will be '1' but we will get 2*0= 0 so taking max of 'max(2*val, 1)'.

# Note: any () in the string gives a score depending on its depth.

# time= space= O(n)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack= []
        score= 0
        for c in s:
            val= 0
            if c== '(':
                stack.append(0)
            else:
                while stack[-1]!= 0:   # means till we get the '(' for which we are processing now.
                    val+= stack.pop()
                score= max(2*val, 1)     # taking max in case '()' then we will get '0' but it should be '1'.
                stack.pop()   # pop the curr number, means we have found the score for curr paranthesis. So add the curr score into stack after poping.
                stack.append(score)  
        return sum(stack)


# method 2:
# very logical and easy.
# any () in the string gives a score depending on its depth. 
# in above method, we are calculating one by one so we are multiplying all the values by '2' to get the score of that curr paranthesis.
# But here we are calculating the score at once acc to the depth so doing power of '2'. 
# https://leetcode.com/problems/score-of-parentheses/solutions/1856699/c-beats-100-omg-o-1-space-explained/

# Diff from above method :
# Ans: upper wale me har ke ')' milne pe score find kar rhe, yahan ek hi bar kar rhe pure depth ka.

# time: O(n), space: O(1).

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        depth, pre= 0, None
        ans= 0
        for c in s:
            if c== '(':
                depth+= 1
            else:
                # depth-= 1   
                if pre== '(':   # means we have not calculated for this depth. if pre= ')'' then ,
                                # we have alrady calculated the ans for this since in this we are calculating at once.
                    ans+= 2**depth
            pre= c
        return ans
