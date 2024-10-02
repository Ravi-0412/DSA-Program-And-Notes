# method 1: convert the infix to postfix/prefix and then evaluate that.

# method 2:

# intuition?
# Ans: Just store the result of all operations and put the num into stack.
# At last sum(stack) will give the ans.

# logic: All these operator have associativity from left to right.
# we are keeping track of last_operator and num.
# After seeing any operator, we will do the operation for last_operator not current one.
# since we need atleast two num for doing operation for any operator i.e one to left and one to right of operator.
# Left num we will get from stack top and right one we will get from last_num.

# After doing the operation acc to meaning of operator, we will push the result into stack.
# And will make num= 0 and last_operator= curr_operator when we will encounter new operator.

# At last return the sum of stack.

# time: O(n).

# method 1:
class Solution:
    def calculate(self, s: str) -> int:
        stack= []
        num, lastOperator= 0, "+"  # default one
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
            if c.isdigit():   # All numbers are positive so checking this is fine
                num= num*10 + int(c)

            if c in all_operators or i== len(s)-1:   # either operator or last index.

                if lastOperator== "+" :
                    stack.append(num)
                elif lastOperator== "-" :
                    stack.append(-1* num)
                # In case of '*' or '/' left operand will be on top of stack
                elif lastOperator== "*" :
                    temp= stack.pop()
                    stack.append(temp * num)
                elif lastOperator== "/" :
                    temp= stack.pop()
                    stack.append(int(temp / num))   # if temp is '-' then python will behave differently so writing like this('/' instead of  '//').

                num, lastOperator= 0, c
        return sum(stack)
# Java
"""
import java.util.Stack;

public class Solution {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        int num = 0;
        char lastOperator = '+';
        char[] allOperators = {'+', '-', '*', '/'};

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0'); // Build the number
            }

            // If c is an operator or it's the last character
            if (isOperator(c) || i == s.length() - 1) {
                switch (lastOperator) {
                    case '+':
                        stack.push(num);
                        break;
                    case '-':
                        stack.push(-num);
                        break;
                    case '*':
                        stack.push(stack.pop() * num);
                        break;
                    case '/':
                        stack.push(stack.pop() / num);
                        break;
                }
                num = 0; // Reset number
                lastOperator = c; // Update last operator
            }
        }

        // Sum all values in the stack
        int result = 0;
        while (!stack.isEmpty()) {
            result += stack.pop();
        }

        return result;
    }

    private boolean isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/';
    }
}

"""


# Optimising to O(1) space
"""
We only need last calculated value say 'tempsum' to do operation with current operator that we will see.
And for ans just maintain one variable say 'sum'.
"""

class Solution:
    def calculate(self, s: str) -> int:
        sum_ = 0
        temp_sum = 0
        num = 0
        last_sign = '+'
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
                
            if i == len(s) - 1 or (not c.isdigit() and c != ' '):
                if last_sign == '+':
                    sum_ += temp_sum
                    temp_sum = num
                elif last_sign == '-':
                    sum_ += temp_sum
                    temp_sum = -num
                elif last_sign == '*':
                    temp_sum *= num
                elif last_sign == '/':
                    temp_sum = int(temp_sum / num)  # Use int to truncate towards 0
                
                last_sign = c
                num = 0
        
        sum_ += temp_sum
        return sum_
# Java
"""
public class Solution {
    public int calculate(String s) {
        int sum = 0;
        int tempSum = 0;
        int num = 0;
        char lastSign = '+';
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) num = num * 10 + c - '0';
            if (i == s.length() - 1 || !Character.isDigit(c) && c!=' ') {
                switch(lastSign) {
                    case '+':
                        sum+=tempSum;
                        tempSum = num;
                        break;
                    case '-':
                        sum+=tempSum;
                        tempSum = -num;
                        break;
                    case '*':
                        tempSum *= num;
                        break;
                    case '/':
                        tempSum /= num;
                        break;
                }
                lastSign = c;
                num=0;
            }
        }
        sum+=tempSum;
        return sum;
    }
}
"""

# Similar / extended Q:
# 772 · Basic Calculator III
