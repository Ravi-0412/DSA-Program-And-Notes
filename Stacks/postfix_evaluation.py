# submitted on GFG
# logic:  # scan the string and if you find any operand, push it into the stack and
        # if you find any operator(since here all are binary operator), pop two element
        # op1= stack[-2] and op2= stack[-1], res= op1 operator op2
        # from stack and apply operator bw them and put the result into the stack
        # at last top of stack will give the final result
class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        stack= []  # store the operand not operator like infix to postfix
        for i in range(len(S)):
            if '0'<= S[i]<= '9':
                stack.append(S[i])
            elif S[i]== '+' :
                # op2= stack.pop()  # this will give error : "  can’t multiply sequence by non-int of type ‘str"
                # op1= stack.pop()  # so first convert the strinmg into int 
                                    # as we are taking string as input and and want to do opeartion on int type
                op2= int(stack.pop())
                op1= int(stack.pop())
                # res= (op1)('S[i]')(op2)
                res= op1 + op2
                stack.append(res)
            elif S[i]== '-' :
                op2= int(stack.pop())
                op1= int(stack.pop())
                res= op1 - op2
                stack.append(res)
            elif S[i]== '*' :
                op2= int(stack.pop())
                op1= int(stack.pop())
                res= op1 * op2
                stack.append(res)
            elif S[i]== '/' :
                op2= int(stack.pop())
                op1= int(stack.pop())
                res= op1 // op2
                stack.append(res)
        return stack[-1]


# little concise way(submittted on leetcode)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []  
        for t in tokens:
            if t not in "+-/*":
                stack.append(int(t))
            else:
                op2,op1= stack.pop(), stack.pop()
                if t == "+":
                    stack.append(op1+op2)
                elif t == "-":
                    stack.append(op1-op2)
                elif t == "*":
                    stack.append(op1*op2)
                # else:   
                #     stack.append(op1//op2)  # this will not truncate towards zero beacuse
                                              # for -2.344, it will give -3 not 3
                                              # it will not work properly it one of the number is negative
                else:
                     stack.append(int(float(op1)/op2))   # this will work properly in this case
        return stack.pop()
        