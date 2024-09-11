
def InfixToPrefix(str1):
    str2=reverse(str1)
    print("reversed initial string:", str2)
    postfix= InfixtoPostfix(str2)
    print("reversed string after postfix conversion:",postfix)
    prefix= reverse(postfix)
    print("our prefix string is: ", prefix)
    # return prefix

def reverse(str1):
    str2= ""
    for i in str1:
        if i== '(':
            i= ')'
        elif i== ')':
            i= '('
        str2= i + str2
    return str2


# all thing will be done same but in case of operators pop until if you find any
# 1) operator strictly greater than current one in case of '+', '-', '*', '/' as we have to reverse it once more:

# Q) why not poping for "="?
# because "=" take care of associativity in case of equal precedence and for ('+', '-', '*', '/'),
# it is left to right.
# But this associativity thing will be allready taken care when we will reverse the string for final ans.

# 2)  in case of '^' pop until you find any ele greater than or equal'^' since it is right associative.
# '^' is rigth associative so it won't be taken care automatically while reversing.
# So here we will do left -> right and after reversing it will become right -> left for equal precedence.

def InfixtoPostfix(exp):
        precedence= { '+':1, '-': 1, '*':2 ,'/':2, '%': 2, '^':3}
        res= ""  
        stack= [0]
        for i in range(len(exp)):
            if 96< ord(exp[i]) <123 or 64< ord(exp[i])< 91 or '0'<=exp[i]<='9':   
                res+= str(exp[i])  
            elif exp[i]== '(' :
                stack.append(exp[i])
            elif exp[i]== ')':
                while stack[-1]!= '(' :
                    res+= str(stack.pop())
                stack.pop()   # this will pop the '('
            # if any operator comes
            # pop and output until you get one of the strictly lower precedence operator in stack
            # than the current operator : exp[i] 
            # because higher precednce operator have to be evaluated first
            # or you stack becomes empty or until left parenthesis is encountered

            elif exp[i]== '+' or exp[i]== '-' or exp[i]== '*' or exp[i]== '/' or exp[i]== '%' or exp[i]== '^':
                if exp[i]!= '^':
                    while stack[-1]!=0 and stack[-1]!='(' and (precedence.get(exp[i]) < precedence.get(stack[-1])) :
                        res+= str(stack.pop())
                    # now push the operator
                    stack.append(exp[i])
                    
                else:  # if opearator is "^" then pop till you get any operator with greater or equal
                      # precedence than "^" (only diff bw other operator)
                    while stack[-1]!=0 and stack[-1]!='(' and (precedence.get(exp[i])<= precedence.get(stack[-1])) :
                        res+= str(stack.pop())
                    # now push the operator
                    stack.append(exp[i])
                    
        # now pop the remaining operator from the  stack and output it until stack becomes empty
        while stack[-1]!= 0:
            res+= str(stack.pop())
        return res


# str1= "a*b+c/d"
# str1= "(a+b*c)+(c+d)"
str1= "(a+b^c^d)+(c/d+a)"
print("initial string is: ", str1)
InfixToPrefix(str1)
