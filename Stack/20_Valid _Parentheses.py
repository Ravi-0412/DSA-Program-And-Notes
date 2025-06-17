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
//Method 1
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        stack.push('0'); // Initializing stack with '0' to handle edge cases

        for (char c : s.toCharArray()) {
            // Push opening brackets onto the stack
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }
            // Process closing brackets
            else {
                if (c == ')' && stack.peek() != '(') return false;
                if (c == '}' && stack.peek() != '{') return false;
                if (c == ']' && stack.peek() != '[') return false;
                stack.pop(); // Pop the corresponding opening bracket
            }
        }

        return stack.size() == 1; // Stack should only contain the initialized '0' element
    }
}

//Method 2
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        stack.push('0'); // Initializing to check whether stack is empty at the end

        for (char c : s.toCharArray()) {
            if (c == '(') stack.push(')');
            else if (c == '{') stack.push('}');
            else if (c == '[') stack.push(']');
            else if (stack.pop() != c) return false; // If stack is empty or does not match expected closing bracket
        }

        return stack.size() == 1; // If stack is empty (except initial '0'), it's valid
    }
}
"""

# C++ Code 
"""
//Method 1

#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        st.push('0'); // Initializing stack with '0' to handle edge cases

        for (char c : s) {
            // Push opening brackets onto the stack
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
            // Process closing brackets
            else {
                if (c == ')' && st.top() != '(') return false;
                if (c == '}' && st.top() != '{') return false;
                if (c == ']' && st.top() != '[') return false;
                st.pop(); // Pop the corresponding opening bracket
            }
        }

        return st.size() == 1; // Stack should only contain the initialized '0' element
    }
};


//Method 2
#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        st.push('0'); // Initializing to check whether stack is empty at the end

        for (char c : s) {
            if (c == '(') st.push(')');
            else if (c == '{') st.push('}');
            else if (c == '[') st.push(']');
            else if (st.top() != c) return false; // If stack is empty or does not match expected closing bracket
            else st.pop();
        }

        return st.size() == 1; // If stack is empty (except initial '0'), it's valid
    }
};
"""