# submitted on GFG
# logic:  # scan the string and if you find any operand, push it into the stack and
        # if you find any operator(since here all are binary operator), pop two element
        # op1= stack[-2] and op2= stack[-1], res= op1 operator op2
        # from stack and apply operator bw them and put the result into the stack
        # at last top of stack will give the final result

# Note: Here no need to worry about 'precedence and associativity' because we convert from
# 'infix to postfix' only to get rid of these things so that we can calculate ans directly after seeing an operator.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []  # store the operand not operator like infix to postfix
        operator= {"+", "-", "*", "/"}
        for c in tokens:
            if c in operator:  
                op2= stack.pop()
                op1= stack.pop()
                if c== '+' :
                    res= op1 + op2
                if c== '-' :
                    res= op1 - op2
                if c== '*' :
                    res= op1 * op2
                if c== '/' :
                    res= int(op1 / op2)
            
                stack.append(res)
            else:  # means number
                stack.append(int(c))

        return stack[-1]

# my mistakes
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack= []  # store the operand not operator like infix to postfix
        for c in tokens:
            if c.isdigit():  # will give False when no will be '-ve'. so '-ve' no won't get added to the stack.
                stack.append(c)
            else:  # means there is operator
                print(stack)
                op2= int(stack.pop())
                op1= int(stack.pop())
                if c== '+' :
                    res= op1 + op2
                if c== '-' :
                    res= op1 - op2
                if c== '*' :
                    res= op1 * op2
                if c== '/' :
                    res= int(op1 / op2)
                
                stack.append(res)

        return stack[-1]

# How isdigit() work in python?
# The str.isdigit() method in Python checks if all the characters in the string are digits. 
# It returns True if the string consists of digits only, and False otherwise.
# vi:  However, it does not account for negative signs or decimal points, 
# which means it will return False for negative numbers or floating-point numbers.

# e.g: 
print("-123".isdigit())  # Output: False
print("123".isdigit())   # Output: True
print("123.45".isdigit())  # Output: False


# Java
"""
import java.util.*;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        Set<String> operators = new HashSet<>(Arrays.asList("+", "-", "*", "/"));

        for (String token : tokens) {
            if (operators.contains(token)) {
                int op2 = stack.pop();
                int op1 = stack.pop();
                int res = 0;
                switch (token) {
                    case "+":
                        res = op1 + op2;
                        break;
                    case "-":
                        res = op1 - op2;
                        break;
                    case "*":
                        res = op1 * op2;
                        break;
                    case "/":
                        res = op1 / op2;
                        break;
                }
                stack.push(res);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();
    }
}
"""
