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

# Java Code 
"""
using two stack , because in python we can store different types in list but it won't work in 
java when we will use 'stack'. So changed the lastOperator character by 'int' i.e 1 (for +) and -1 (for -).
"""

"""
import java.util.Stack;

class Solution {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        Stack<Character> operators = new Stack<>();
        int num = 0;
        char lastOperator = '+';

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            }

            if (c == '(') {
                operators.push(lastOperator);
                num = 0;
                lastOperator = '+';
            }

            if (c == '+' || c == '-' || c == ')' || i == s.length() - 1) {
                update(stack, lastOperator, num);

                if (c == ')') {
                    num = 0;
                    while (!stack.isEmpty() && stack.peek() instanceof Integer) {
                        num += stack.pop();
                    }
                    update(stack, operators.pop(), num);
                }

                num = 0;
                lastOperator = c;
            }
        }

        int result = 0;
        while (!stack.isEmpty()) {
            result += stack.pop();
        }
        return result;
    }

    private void update(Stack<Integer> stack, char op, int num) {
        if (op == '+') {
            stack.push(num);
        } else if (op == '-') {
            stack.push(-num);
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
        stack<int> stack;
        stack<char> operators;
        int num = 0;
        char lastOperator = '+';
        
        auto update = [&](char op, int val) {
            if (op == '+') {
                stack.push(val);
            } else if (op == '-') {
                stack.push(-val);
            }
        };

        for (int i = 0; i < s.size(); i++) {
            char c = s[i];

            if (isdigit(c)) {
                num = num * 10 + (c - '0');
            }

            if (c == '(') {
                operators.push(lastOperator);
                num = 0;
                lastOperator = '+';
            }

            if (c == '+' || c == '-' || c == ')' || i == s.size() - 1) {
                update(lastOperator, num);
                
                if (c == ')') {
                    num = 0;
                    while (!stack.empty() && isdigit(stack.top())) {
                        num += stack.top();
                        stack.pop();
                    }
                    update(operators.top(), num);
                    operators.pop();
                }
                
                num = 0;
                lastOperator = c;
            }
        }

        int result = 0;
        while (!stack.empty()) {
            result += stack.top();
            stack.pop();
        }
        return result;
    }
};
"""
