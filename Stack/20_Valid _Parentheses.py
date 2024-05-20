# method 1: simplest solution
# How to think of stack?
# agar koi closing bracket dikha tb , pichla wala same type ka open bracket hona chahiye.
# first opened will be closed at last.

class Solution:
    def isValid(self, s: str) -> bool:
        stack= [0] # initialising stack with '0' to check at last
        # stack == [] won't handle the case when s = ']' etc..
        n= len(s)
        for i in range(n):
            # push if any opening bracket comes
            if s[i]== '(' or s[i]== '{' or s[i]== '[':
                stack.append(s[i])
            # pop if any closing bracket come of same type
            # if closing bracket is not of  same type then 'invalid'
            else:
                if s[i]== ')':
                    if stack.pop() != '(':
                        return False
                if s[i]== '}':
                    if stack.pop() != '{':
                        return False
                if s[i]== ']':
                    if stack.pop() != '[':
                        return False
        return stack == [0]    # means no extra char remaining in stack 


# method 2: concise one
# logic: push closing braces of the current braces after seeing the opening braces
# and when you encouter the closed parenthesis check the ele on top of stack
# if same as current char then continue the loop
# at last check for empty stack.
class Solution:
    def valid(self, s): 
        stack= [0] # initialising to check whether stack is empty or not 
        for i in range(len(s)):
            if s[i]== '(':
                stack.append(')')
            elif s[i]== '{':
                stack.append('}')
            elif s[i]== '[':
                stack.append(']')
            elif stack.pop()!= s[i]: # if stack is empty or current char
                                                    # is not equal to ele on top of the stack
                                                    # then it means not valid
                return False
        return stack== [0]   # after traversing all the string if stack is empty
                            # then valid otherwise not

# java
"""
# Method 1:
import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        stack.push('0'); // Initializing stack with '0' to check at last

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            // Push if any opening bracket comes
            if (current == '(' || current == '{' || current == '[') {
                stack.push(current);
            } 
            // Pop if any closing bracket comes of the same type
            // If closing bracket is not of the same type then 'invalid'
            else {
                if (current == ')') {
                    if (stack.pop() != '(') {
                        return false;
                    }
                } else if (current == '}') {
                    if (stack.pop() != '{') {
                        return false;
                    }
                } else if (current == ']') {
                    if (stack.pop() != '[') {
                        return false;
                    }
                }
            }
        }

        // Means no extra char remaining in stack
        return stack.size() == 1 && stack.peek() == '0';
    }
}

# Method 2:
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        stack.push('0'); // Initializing to check whether stack is empty or not

        for (int i = 0; i < s.length(); i++) {
            char current = s.charAt(i);
            if (current == '(') {
                stack.push(')');
            } else if (current == '{') {
                stack.push('}');
            } else if (current == '[') {
                stack.push(']');
            } else if (stack.pop() != current) {
                // If stack is empty or current char is not equal to ele on top of the stack
                // then it means not valid
                return false;
            }
        }

        // After traversing all the string if stack is empty then valid otherwise not
        return stack.size() == 1 && stack.peek() == '0';
    }
    }

    
"""