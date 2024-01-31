# logic: similar as basic calculator 2. Little modification for '(' and ')'.

# when we  see "(", we have to find the result first for this bracket and similar for nested bracket also.
# but we should keep track of operator before "(" also, so we push the operator(before '(' ) also in this case.
# Also make num= 0 and operator= "+", since we will calculate res for this bracet from scratch.
# just like we recursilvely calculate the ans for smaller subproblem.

# Note: we push only num in stack except when we see "(".

# when we see operator or ")" braces then we do update the stack acc to operation.
# After updating , we check if curr character is ")". 
# if ")":
#  we add all the res(of stack) till we see the operator in stack.
# When we see operator then we have to do operation for this operator with stack top and the sum of res of current braces.

# time= space= O(n)
class Solution:
    def calculate(self, s: str) -> int:

        def update(op, num):
            if op== "+":
                stack.append(num)
            if op== "-":
                stack.append(-1*num)
            if op== "*":
                stack.append(stack.pop() *num)
            if op== "/":
                stack.append(int(stack.pop()/num))

        all_operators= {"+", "-", "*", "/", ")"}
        lastOperator, num= "+", 0
        stack= []
        for i in range(len(s)):
            c= s[i]
            if c.isdigit():
                num= num*10 + int(c)
            if c== "(":
                stack.append(lastOperator)
                num, lastOperator= 0, "+"   # we will calculate now for bracket from scratch. Just like we are doing recurison 
            if c in all_operators or i== len(s)-1:
                update(lastOperator, num)   
                # check if c== ')'.
                if c== ")":
                    num= 0
                    # Find the last operator just before '(' that we had pushed into stack.
                    while isinstance(stack[-1], int):
                        num+= stack.pop()
                    # now perform the operation for operator in stack(just after pre '(' )
                    update(stack.pop(), num)
                num, lastOperator= 0, c
        return sum(stack)


# About 'isinstance(object, type)'
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.



# same ans for "224. Basic Calculator"


# Related Q:
# 394. Decode String