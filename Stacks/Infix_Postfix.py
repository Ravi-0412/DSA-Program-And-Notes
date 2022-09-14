#User function Template for python3


class Solution:   
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        precedence= { '+':1, '-': 1, '*':2 ,'/':2, '%': 2, '^':3}
        res= ""  
        stack= [0] # just initialising the stack with any value for checking empty or non empty
        # traverse from left to right and if you encounter any operand , output it
        # and if you encounter any opeartor push or pop(while pop you have to output)
        for i in range(len(exp)):
            # exp[i] is an operand then output it to the result
            if 96< ord(exp[i]) <123 or 64< ord(exp[i])< 91 or '0'<=exp[i]<='9':   # took the ascii value to avoid writing all the char
                # res+= "exp[i]"  # will give error since we are adding the value at exp[i] 
                                 # string just append the string given in " " not its value
                # res+= exp[i]    # this will also give the error since concatenation in python is done with the
                                # same data type and here res is of type : str and exp[i]: is of type int
                                # so convert the exp[i] into string an then add only
                res+= str(exp[i])  # for appending a variable with value you have to write without "" with
                                    # proper data type           
             # if you encounter '(', push it 
            elif exp[i]== '(' :
                stack.append(exp[i])
            # # if exp[i] is ')', then pop and output it till you encounter a '(' brace or stack becomes empty
            # # after while loop fails ,stack top will contain '(', so pop it
            elif exp[i]== ')':
                while stack[-1]!= '(' :
                    res+= str(stack.pop())
                stack.pop()   # this will pop the '('
            # if any operator comes
            # pop and output until you get one of the lower precedence than the current operator : exp[i] 
            # because higher precednce operator have to be evaluated first
            # so pop and output until stack becomes empty or left parenthesis is encountered
            
            
            #due to below two lines  i was gettingh error again and again), i had written con: stack[-1]!='(' 
            # at last so when stack[-1]= '(' there was no map in dic for '('
            # since '^' is right associative but i was treating '^' as left associative only and was giving error 
            # for more than one consecutive '^' operator
            
            # elif exp[i]== '+' or exp[i]== '-' or exp[i]== '*' or exp[i]== '/' or exp[i]== '%' or exp[i]== '^':  
            #     while stack[-1]!=0 and (precedence.get(exp[i])<= precedence.get(stack[-1])) and stack[-1]!='('  :
            
            elif exp[i]== '+' or exp[i]== '-' or exp[i]== '*' or exp[i]== '/' or exp[i]== '%' or exp[i]== '^':
                if exp[i]!= '^':
                    while stack[-1]!=0 and stack[-1]!='(' and (precedence.get(exp[i])<= precedence.get(stack[-1])) :
                        res+= str(stack.pop())
                    # now push the operator
                    stack.append(exp[i])
                    
                else:  # if opearator is "^" then pop till you get any operator with greater precedence than "^" only
                       # not for equal precedence(only diff bw other operator)
                    while stack[-1]!=0 and stack[-1]!='(' and (precedence.get(exp[i])< precedence.get(stack[-1])) :
                        res+= str(stack.pop())
                    # now push the operator
                    stack.append(exp[i])
                    
        # now pop the remaining operator from the  stack and output it until stack becomes empty
        while stack[-1]!= 0:
            res+= str(stack.pop())
        return res
                    



