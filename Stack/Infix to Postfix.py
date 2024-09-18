# why in case of operator we are poping till we get any operator having lower precedence than the current one?
# Ans: Because higher precedence operator we have to evaluate first , 
# so if stack has operator with precedence >= precedence of s[i] then, we will pop that.
# stack will store the operator in strictly increasing order of precedence.

# logic: when we see any operator we do the operation for previous seen operator 
# if stack is not empty and they have higher precedence i.e pop them and add into the res.
# Associativity will not matter here.

# Why we convert to postfix?
# Ans:
# computer cannot differentiate the operators and parenthesis easily.
# We convert so that we don't have to worry about 'precedence and associativity' of operators.
# so that we can calculate ans directly after seeing an operator.

class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        precedence= { '+':1, '-': 1, '*':2 ,'/':2, '%': 2, '^':3}
        res= ""
        
        stack= [] # will store the operator in strictly increasing order of precedence.
        # traverse from left to right and if you encounter any operand , output it
        # and if you encounter any opeartor push or pop(while pop you have to output)
        for c in exp:
            # if 'c' is an operand then output it to the result
            if 96< ord(c) <123 or 64< ord(c)< 91 or '0'<=c<='9':   # took the ascii value to avoid writing all the char.
                res+= c 
            
             # if you encounter '(', push it 
            elif c== '(' :
                stack.append(c)
            # # if exp[i] is ')', then pop and output it till you encounter a '(' brace or stack becomes empty
            # # after while loop fails ,stack top will contain '(', so pop it
            elif c== ')':
                while stack[-1]!= '(' :
                    res+= str(stack.pop())
                stack.pop()   # this will pop the '('
            # if any operator comes
            # pop and output until you get one of the lower precedence than the current operator : exp[i] 
            # because higher precednce operator have to be evaluated first
            # or you stack becomes empty or until left parenthesis is encountered
            else:
                while stack and stack[-1]!='(' and (precedence[c] <= precedence[stack[-1]] ) :
                        res+= str(stack.pop())

                stack.append(c)
                    
        # now pop the remaining operator from the  stack and output it until stack becomes empty
        while stack :
            res+= str(stack.pop())
        return res
                    



