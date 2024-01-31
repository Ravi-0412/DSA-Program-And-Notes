# logic:
# traverse the string right to left and do the same as postfix evaluation
# no need to make special case in this for '^' as we are already traversing
# from right to left.

# Note: we reverses 's' and applied logic of 'infix -> postfix'  for infix -> prefix conversion
# so for evaluation also just reverse 's' (or traverse right -> left) and apply logic of postfix evaluation.


def InfixEvaluation(str1):

    stack= []
    lst1= str1.split(" ")

    for i in range(len(lst1)-1,-1,-1): 
        if lst1[i]== ' ': # if current char is space skip it
            continue
        elif lst1[i] in "+-*/%^":
            op1,op2= int(stack.pop()), int(stack.pop())
            if lst1[i] == "+":
                stack.append(op1+op2)
            elif lst1[i] == "-":
                stack.append(op1-op2)
            elif lst1[i] == "*":
                stack.append(op1*op2)
            elif lst1[i] == "/":
                 stack.append(int(op1/op2))
            elif lst1[i] == "%":
                 stack.append(int(op1%op2))
            elif lst1[i] == "^":
                 stack.append(int(op1^op2))    

        else:  # if it a operand
            stack.append(lst1[i])     
        print(stack)
    return stack[-1] # or stack.pop()

infix= "- / * 20 * 50 + 3 6 300 2"
# infix= "-+8/632"
print("value after evaluating: ",InfixEvaluation(infix))