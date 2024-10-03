class Solution:
    def calculate(self, s: str) -> int:
        def update(op, num):
            if op== "+":
                stack.append(num)
            if op== "-":
                stack.append(-1*num)

        all_operators= {"+", "-",  ")"}
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
                    while isinstance(stack[-1], int):
                        num+= stack.pop()
                    # now perform the operation for poping the operator in stack(just after pre '(' )
                    update(stack.pop(), num)
                num, lastOperator= 0, c   # if 'c' is ')' then also there won't be any problem because after ')' 
                                        # there must be any operator i.e '+' or '-' so lastOperator will be updated by '+' or  '-' only for next index.
        return sum(stack)
