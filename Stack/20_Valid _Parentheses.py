# method 1: 
# simplest solution
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

# Java Code 
"""
import java.util.*;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        stack.push('0');  // initializing stack with '0' to check at last
        // stack == [] won't handle the case when s = ']' etc.

        int n = s.length();
        for (int i = 0; i < n; i++) {
            // push if any opening bracket comes
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[') {
                stack.push(s.charAt(i));
            } else {
                // pop if any closing bracket come of same type
                // if closing bracket is not of same type then 'invalid'
                if (s.charAt(i) == ')') {
                    if (stack.pop() != '(') return false;
                }
                if (s.charAt(i) == '}') {
                    if (stack.pop() != '{') return false;
                }
                if (s.charAt(i) == ']') {
                    if (stack.pop() != '[') return false;
                }
            }
        }
        return stack.size() == 1 && stack.peek() == '0';  // means no extra char remaining in stack
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
    bool isValid(string s) {
        stack<char> stack;
        stack.push('0');  // initializing stack with '0' to check at last
        // stack == [] won't handle the case when s = ']' etc.

        int n = s.length();
        for (int i = 0; i < n; i++) {
            // push if any opening bracket comes
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                stack.push(s[i]);
            } else {
                // pop if any closing bracket come of same type
                // if closing bracket is not of same type then 'invalid'
                if (s[i] == ')') {
                    if (stack.top() != '(') return false;
                    stack.pop();
                }
                if (s[i] == '}') {
                    if (stack.top() != '{') return false;
                    stack.pop();
                }
                if (s[i] == ']') {
                    if (stack.top() != '[') return false;
                    stack.pop();
                }
            }
        }
        return stack.size() == 1 && stack.top() == '0';  // means no extra char remaining in stack
    }
};

"""

# method 2: 
# concise one
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

# Java Code 
"""
import java.util.*;

public class Solution {
    public boolean valid(String s) {
        Stack<Character> stack = new Stack<>();
        stack.push('0');  // initialising to check whether stack is empty or not 

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(')');
            } else if (s.charAt(i) == '{') {
                stack.push('}');
            } else if (s.charAt(i) == '[') {
                stack.push(']');
            } else if (stack.pop() != s.charAt(i)) {
                // if stack is empty or current char
                // is not equal to ele on top of the stack
                // then it means not valid
                return false;
            }
        }

        // after traversing all the string if stack is empty
        // then valid otherwise not
        return stack.size() == 1 && stack.peek() == '0';
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
    bool valid(string s) {
        stack<char> stack;
        stack.push('0');  // initialising to check whether stack is empty or not 

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                stack.push(')');
            } else if (s[i] == '{') {
                stack.push('}');
            } else if (s[i] == '[') {
                stack.push(']');
            } else if (stack.top() != s[i]) {
                // if stack is empty or current char
                // is not equal to ele on top of the stack
                // then it means not valid
                return false;
            } else {
                stack.pop();
            }
        }

        // after traversing all the string if stack is empty
        // then valid otherwise not
        return stack.size() == 1 && stack.top() == '0';
    }
};

"""