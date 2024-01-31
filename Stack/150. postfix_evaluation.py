# submitted on GFG
# logic:  # scan the string and if you find any operand, push it into the stack and
        # if you find any operator(since here all are binary operator), pop two element
        # op1= stack[-2] and op2= stack[-1], res= op1 operator op2
        # from stack and apply operator bw them and put the result into the stack
        # at last top of stack will give the final result

# Note: Here no need to worry about 'precedence and associativity' because we convert from
# 'infix to postfix' only to get rid of these things so that we can calculate ans directly after seeing an operator.

class Solution: 
    def evaluatePostfix(self, S):
        stack= []  # store the operand not operator like infix to postfix
        for i in range(len(S)):
            if '0'<= S[i]<= '9':
                stack.append(int(S[i]))
            else:  # means there is operator
                op2= stack.pop()
                op1= stack.pop()
                if S[i]== '+' :
                    res= op1 + op2
                if S[i]== '-' :
                    res= op1 - op2
                if S[i]== '*' :
                    res= op1 * op2
                if S[i]== '/' :
                    res= op1 // op2
                
                stack.append(res)
        return stack[-1]


# for leetcode
# when num can be negative also.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []  # store the operand not operator like infix to postfix
        operator= {"+", "-", "*", "/"}
        for c in tokens:
            if c in operator:  
                op2= stack.pop()
                op1= stack.pop()
                if c== '+' :
                    res= op1 + op2
                if c== '-' :
                    res= op1 - op2
                if c== '*' :
                    res= op1 * op2
                if c== '/' :
                    res= int(op1 / op2)
            
                stack.append(res)
            else:  # means number
                stack.append(int(c))

        return stack[-1]



# my mistakes
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []  # store the operand not operator like infix to postfix
        for c in tokens:
            if c.isdigit():  # will give False when no will be '-ve'. so '-ve' no won't get added to the stack.
                stack.append(c)
            else:  # means there is operator
                print(stack)
                op2= int(stack.pop())
                op1= int(stack.pop())
                if c== '+' :
                    res= op1 + op2
                if c== '-' :
                    res= op1 - op2
                if c== '*' :
                    res= op1 * op2
                if c== '/' :
                    res= int(op1 / op2)
                
                stack.append(res)

        return stack[-1]

        