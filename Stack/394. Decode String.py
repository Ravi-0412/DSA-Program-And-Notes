n# Method 1: 

# when you see this type of problem involving nested brackets call with this type of logic then use stack.

# using one stack.
# just like solve 'postfix and infix' evalauation.

# Logic: Push everything except ']' and when you see ']'
# evaluate for pre '[' and put result of this into stack.

# Note: before every '[', there will be a number.

# time: will depend on 'num' before every bracket but will be linear time only.

class Solution:
    def decodeString(self, s: str) -> str:
        stack= []
        for i in range(len(s)):
            if s[i]!= ']':   # push everything into stack until you see ']'.
                stack.append(s[i])
            else:   # means we have seen ']' .
                # first find the string . So start poping till we find '[' .
                temp= ""
                while stack[-1] != '[':
                    temp= stack.pop() + temp
                stack.pop()  # Removing '[' bracket
                # before every '[', there will be a number but this can be of more than one digit.
                # find the number.
                num= ""
                while stack and stack[-1].isdigit():  # checking stack empty in case it doesn't any number then stack will be empty.
                    num= stack.pop() + num
                # now multiply 'temp' with 'num' to get the string till one of '[' and put into stack. num will be a string.
                temp= temp*int(num)
                stack.append(temp)
        return "".join(stack)

# Java Code 
"""
import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ']') {
                // push everything into stack until you see ']'.
                stack.push(String.valueOf(s.charAt(i)));
            } else {
                // means we have seen ']'.
                // first find the string. So start popping till we find '['.
                String temp = "";
                while (!stack.peek().equals("[")) {
                    temp = stack.pop() + temp;
                }
                stack.pop(); // Removing '[' bracket

                // before every '[', there will be a number but this can be of more than one digit.
                // find the number.
                String num = "";
                while (!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) {
                    num = stack.pop() + num;
                }

                // now multiply 'temp' with 'num' to get the string till one of '[' and put into stack. num will be a string.
                int repeat = Integer.parseInt(num);
                StringBuilder repeated = new StringBuilder();
                for (int j = 0; j < repeat; j++) {
                    repeated.append(temp);
                }
                stack.push(repeated.toString());
            }
        }

        // Join everything in the stack to return final string
        StringBuilder result = new StringBuilder();
        for (String str : stack) {
            result.append(str);
        }
        return result.toString();
    }
}
"""

# C++ Code
"""
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<string> stack;

        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != ']') {
                // push everything into stack until you see ']'.
                stack.push(string(1, s[i]));
            } else {
                // means we have seen ']'.
                // first find the string. So start popping till we find '['.
                string temp = "";
                while (!stack.empty() && stack.top() != "[") {
                    temp = stack.top() + temp;
                    stack.pop();
                }
                stack.pop(); // Removing '[' bracket

                // before every '[', there will be a number but this can be of more than one digit.
                // find the number.
                string num = "";
                while (!stack.empty() && isdigit(stack.top()[0])) {
                    num = stack.top() + num;
                    stack.pop();
                }

                // now multiply 'temp' with 'num' to get the string till one of '[' and put into stack. num will be a string.
                int repeat = stoi(num);
                string expanded = "";
                for (int j = 0; j < repeat; ++j) {
                    expanded += temp;
                }
                stack.push(expanded);
            }
        }

        // Join everything in the stack to return final string
        string result = "";
        while (!stack.empty()) {
            result = stack.top() + result;
            stack.pop();
        }
        return result;
    }
};
"""
# Method 2:
# Similar idea to "772. Basic Calculator III"

# We need to keep track of two things before every '[' :
# 1) The number k (how many times to repeat)
# 2) The string built so far

# When we see a '[' :
# - It means we have just finished reading a number k.
# - So we push (current_string, k) onto the stack.
# - Then we reset current_string and k to start fresh for the substring inside the brackets.

# When we see a ']' :
# - We pop the last saved (previous_string, repeat_count) from the stack.
# - The current_string now contains the decoded substring inside the brackets.
# - We repeat this substring repeat_count times.
# - Then append it to previous_string.

# This way, the stack helps us handle nested brackets by remembering
# the string and repeat count from outer levels.

# time = sapce = O(n)

class Solution(object):
    def decodeString(self, s):
        stack = []
        current_string = ""
        k = 0
        for char in s:
            if char == "[" :
                # Just finished parsing this k, save current string and k for when we pop
                stack.append((current_string, k))
                # Reset current_string and k for this new frame
                current_string = ""
                k = 0
            elif char == "]":
                # We have completed this frame, get the last current_string and k from when the frame 
                # opened, which is the k we need to duplicate the current current_string by
                last_string, last_k = stack.pop()
                current_string = last_string + last_k * current_string
                # No need to put current_string into stack.
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                current_string += char
        
        return current_string

# Java Code 
"""
class Solution {
    public String decodeString(String s) {
        Stack<String> strStack = new Stack<>();
        Stack<Integer> numStack = new Stack<>();
        String current_string = "";
        int k = 0;

        for (char ch : s.toCharArray()) {
            if (ch == '[') {
                // Just finished parsing this k, save current string and k for when we pop
                strStack.push(current_string);
                numStack.push(k);
                // Reset current_string and k for this new frame
                current_string = "";
                k = 0;
            } else if (ch == ']') {
                // We have completed this frame, get the last current_string and k from when the frame 
                // opened, which is the k we need to duplicate the current current_string by
                String last_string = strStack.pop();
                int last_k = numStack.pop();
                current_string = last_string + current_string.repeat(last_k);
                // No need to put current_string into stack.
            } else if (Character.isDigit(ch)) {
                k = k * 10 + (ch - '0');
            } else {
                current_string += ch;
            }
        }

        return current_string;
    }
}
"""

# C++ Code 
"""
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<string> strStack;
        stack<int> numStack;
        string current_string = "";
        int k = 0;

        for (char ch : s) {
            if (ch == '[') {
                // Just finished parsing this k, save current string and k for when we pop
                strStack.push(current_string);
                numStack.push(k);
                // Reset current_string and k for this new frame
                current_string = "";
                k = 0;
            } else if (ch == ']') {
                // We have completed this frame, get the last current_string and k from when the frame 
                // opened, which is the k we need to duplicate the current current_string by
                string last_string = strStack.top(); strStack.pop();
                int last_k = numStack.top(); numStack.pop();
                string expanded = "";
                for (int i = 0; i < last_k; ++i) expanded += current_string;
                current_string = last_string + expanded;
                // No need to put current_string into stack.
            } else if (isdigit(ch)) {
                k = k * 10 + (ch - '0');
            } else {
                current_string += ch;
            }
        }

        return current_string;
    }
};
"""
