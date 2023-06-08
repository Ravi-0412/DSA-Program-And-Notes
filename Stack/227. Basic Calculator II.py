# method 1: convert the infix to postfif/prefix and then evaluate that.

# method 2:

# intuition?
# Ans: Just store the result of all operation snad put the num into stack.
# At last sum(stack) will give the ans.

# logic: All these operator have associativity from left to right.
# we are keeping track of last_operator and num.
# After seeing any operator, we will do the operation for last_operator since we need atleast two num for doing operation for any operator.
# After doing the operation acc to meaning of operator, we will push the result into stack.
# And will make num= 0 and last_operator= curr_operator when we will encounter new operator.

# At last return the sum of stack.

# time: O(n).

# method 1:
class Solution:
    def calculate(self, s: str) -> int:
        stack= []
        num, lastOperator= 0, "+"
        for c in s:
            if c== ' ':
                continue
            if c.isdigit():  # for more than one digit number
                num= num*10 + int(c)
            else:
                if lastOperator== "+" :
                    stack.append(num)
                elif lastOperator== "-" :
                    stack.append(-1* num)
                elif lastOperator== "*" :
                    temp= stack.pop()
                    stack.append(temp * num)
                elif lastOperator== "/" :
                    temp= stack.pop()
                    stack.append(int(temp / num))
                num, lastOperator= 0, c
        # doing the operation for last operator as it will be left to operate.
        if lastOperator== "+" :
            stack.append(num)
        elif lastOperator== "-" :
            stack.append(-1* num)
        elif lastOperator== "*" :
            temp= stack.pop()
            stack.append(temp * num)
        elif lastOperator== "/" :
            temp= stack.pop()
            stack.append(int(temp / num))
        return sum(stack)


# concise way of above logic.
# Better one.
# we have to do the same operation after last index also. so taking index.
class Solution:
    def calculate(self, s: str) -> int:
        stack= []
        num, lastOperator= 0, "+"
        all_operators= {"+", "-", "*", "/"}
        for i in range(len(s)):
            c= s[i]
            # if c== ' ':  # writing this will give erorr if there is space at last then we will not do the operation for last index.
            #     continue   # for skipping, use the 'continue' or nothing. This will depend on the Q.
            if c.isdigit():
                num= num*10 + int(c)

            if c in all_operators or i== len(s)-1:   # either operator or last index.

                if lastOperator== "+" :
                    stack.append(num)
                elif lastOperator== "-" :
                    stack.append(-1* num)
                elif lastOperator== "*" :
                    temp= stack.pop()
                    stack.append(temp * num)
                elif lastOperator== "/" :
                    temp= stack.pop()
                    stack.append(int(temp / num))   # if temp is '-' then python will behave differently so writing like this('/' instead of  '//').

                num, lastOperator= 0, c
        return sum(stack)
    
