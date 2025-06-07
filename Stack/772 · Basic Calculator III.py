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

# Java Code 
"""
import java.util.Stack;

class Solution {
    public int calculate(String s) {
        Stack<Integer> numStack = new Stack<>();
        Stack<Character> opStack = new Stack<>();
        int num = 0;
        char lastOperator = '+';

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            }

            if (c == '(') {
                opStack.push(lastOperator);
                num = 0;
                lastOperator = '+';
            }

            if (c == '+' || c == '-' || c == '*' || c == '/' || c == ')' || i == s.length() - 1) {
                update(numStack, lastOperator, num);

                if (c == ')') {
                    num = 0;
                    while (!numStack.isEmpty() && numStack.peek() instanceof Integer) {
                        num += numStack.pop();
                    }
                    update(numStack, opStack.pop(), num);
                }

                num = 0;
                lastOperator = c;
            }
        }

        int result = 0;
        while (!numStack.isEmpty()) {
            result += numStack.pop();
        }
        return result;
    }

    private void update(Stack<Integer> numStack, char op, int num) {
        if (op == '+') {
            numStack.push(num);
        } else if (op == '-') {
            numStack.push(-num);
        } else if (op == '*') {
            numStack.push(numStack.pop() * num);
        } else if (op == '/') {
            numStack.push(numStack.pop() / num);
        }
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> numStack;
        stack<char> opStack;
        int num = 0;
        char lastOperator = '+';

        auto update = [&](char op, int val) {
            if (op == '+') {
                numStack.push(val);
            } else if (op == '-') {
                numStack.push(-val);
            } else if (op == '*') {
                int temp = numStack.top();
                numStack.pop();
                numStack.push(temp * val);
            } else if (op == '/') {
                int temp = numStack.top();
                numStack.pop();
                numStack.push(temp / val);
            }
        };

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];

            if (isdigit(c)) {
                num = num * 10 + (c - '0');
            }

            if (c == '(') {
                opStack.push(lastOperator);
                num = 0;
                lastOperator = '+';
            }

            if (c == '+' || c == '-' || c == '*' || c == '/' || c == ')' || i == s.size() - 1) {
                update(lastOperator, num);

                if (c == ')') {
                    num = 0;
                    while (!numStack.empty() && typeid(numStack.top()) == typeid(int)) {
                        num += numStack.top();
                        numStack.pop();
                    }
                    update(opStack.top(), num);
                    opStack.pop();
                }

                num = 0;
                lastOperator = c;
            }
        }

        int result = 0;
        while (!numStack.empty()) {
            result += numStack.top();
            numStack.pop();
        }
        return result;
    }
};
"""

# About 'isinstance(object, type)'
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.



# same ans for "224. Basic Calculator"


# Related Q:
# 394. Decode String