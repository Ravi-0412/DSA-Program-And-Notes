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

# Method 2:
# Better one. Just similar logic as "772. Basic Calculator III".

# We need to keep track of number and string before '['.
# So when you see '[' then append string and num before '[' into stack.
# And start from scratch .

# When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
# push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
# the enclosed string k times.
    
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
//Method 1
import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        Stack<String> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c != ']') {
                stack.push(Character.toString(c)); // Push everything until we see ']'
            } else {
                // Pop characters to form the substring inside brackets
                StringBuilder temp = new StringBuilder();
                while (!stack.peek().equals("[")) {
                    temp.insert(0, stack.pop());
                }
                stack.pop(); // Remove '['

                // Find the number before '['
                StringBuilder numStr = new StringBuilder();
                while (!stack.isEmpty() && Character.isDigit(stack.peek().charAt(0))) {
                    numStr.insert(0, stack.pop());
                }
                
                int num = Integer.parseInt(numStr.toString());
                String expanded = temp.toString().repeat(num);
                stack.push(expanded);
            }
        }

        // Construct the final result
        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.insert(0, stack.pop());
        }
        return result.toString();
    }
}
//Method 2
import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        Stack<Pair<String, Integer>> stack = new Stack<>();
        String currentString = "";
        int k = 0;

        for (char c : s.toCharArray()) {
            if (c == '[') {
                // Save current string and k for when we pop
                stack.push(new Pair<>(currentString, k));
                // Reset current string and k
                currentString = "";
                k = 0;
            } else if (c == ']') {
                // Retrieve previous string and repeat count
                Pair<String, Integer> last = stack.pop();
                currentString = last.getKey() + currentString.repeat(last.getValue());
            } else if (Character.isDigit(c)) {
                k = k * 10 + (c - '0'); // Build number
            } else {
                currentString += c; // Build string
            }
        }

        return currentString;
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
    string decodeString(string s) {
        stack<string> st;
        
        for (char c : s) {
            if (c != ']') {
                st.push(string(1, c)); // Push everything until we see ']'
            } else {
                // Pop characters to form the substring inside brackets
                string temp = "";
                while (st.top() != "[") {
                    temp = st.top() + temp;
                    st.pop();
                }
                st.pop(); // Remove '['

                // Find the number before '['
                string numStr = "";
                while (!st.empty() && isdigit(st.top()[0])) {
                    numStr = st.top() + numStr;
                    st.pop();
                }
                
                int num = stoi(numStr);
                string expanded = "";
                for (int i = 0; i < num; i++) {
                    expanded += temp;
                }
                st.push(expanded);
            }
        }

        // Construct the final result
        string result = "";
        while (!st.empty()) {
            result = st.top() + result;
            st.pop();
        }
        return result;
    }
};
//Method 2
#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<pair<string, int>> st;
        string currentString = "";
        int k = 0;

        for (char c : s) {
            if (c == '[') {
                // Save current string and k for when we pop
                st.push({currentString, k});
                // Reset current string and k
                currentString = "";
                k = 0;
            } else if (c == ']') {
                // Retrieve previous string and repeat count
                auto last = st.top(); st.pop();
                currentString = last.first + string(last.second, currentString);
            } else if (isdigit(c)) {
                k = k * 10 + (c - '0'); // Build number
            } else {
                currentString += c; // Build string
            }
        }

        return currentString;
    }
};
"""

# Similar Question:
# 856. Score of Parentheses
