def InfixEvaluation(str1):

    stack= []
    lst1= str1.split(" ")
    # traverse the string right to lest and do the same as postfix evaluation
    # no need to make speciula case in this for '^' as we are already traversing
    # from right to left
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

                 
        # else: # if it is a digit
        #         # since digit can contain more than one letter
        #         #so we have to make it as a single digit
        #     temp= ""
        #     while lst1[i]!= ' ':
        #         temp= lst1[i]+ temp
        #         i-= 1
        #     stack.append(temp)        

        else:  # if it a operand
            stack.append(lst1[i])     
        print(stack)
    return stack[-1] # or stack.pop()

infix= "- / * 20 * 50 + 3 6 300 2"
# infix= "-+8/632"
print("value after evaluating: ",InfixEvaluation(infix))