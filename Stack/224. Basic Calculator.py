# Time = space = O(n)

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

# Java
"""
using two stack , because in python we can store different types in list but it won't work in 
java when we will use 'stack'. So changed the lastOperator character by 'int' i.e 1 (for +) and -1 (for -).
"""

"""
public int calculate(String s) {
    Stack<Integer> stack = new Stack<Integer>();
    int result = 0;
    int number = 0;
    int sign = 1;
    for(int i = 0; i < s.length(); i++){
        char c = s.charAt(i);
        if(Character.isDigit(c)){
            number = 10 * number + (int)(c - '0');
        }else if(c == '+'){
            result += sign * number;
            number = 0;
            sign = 1;
        }else if(c == '-'){
            result += sign * number;
            number = 0;
            sign = -1;
        }else if(c == '('){
            //we push the result first, then sign;
            stack.push(result);
            stack.push(sign);
            //reset the sign and result for the value in the parenthesis
            sign = 1;   
            result = 0;
        }else if(c == ')'){
            result += sign * number;  
            number = 0;
            result *= stack.pop();    //stack.pop() is the sign before the parenthesis
            result += stack.pop();   //stack.pop() now is the result calculated before the parenthesis
            
        }
    }
    if(number != 0) result += sign * number;
    return result;
}
"""
