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
# Java
"""
import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            
            if (ch != ']') {
                // Push each character onto the stack
                stack.push(ch);
            } else {
                // We encountered ']', so we need to decode the substring
                
                // Collect the characters to form the string to be repeated
                StringBuilder temp = new StringBuilder();
                while (stack.peek() != '[') {
                    temp.append(stack.pop());
                }
                
                // Pop the '['
                stack.pop();

                // Collect the digits (which can be more than one digit) to form the multiplier
                StringBuilder numStr = new StringBuilder();
                while (!stack.isEmpty() && Character.isDigit(stack.peek())) {
                    numStr.append(stack.pop());
                }

                // Reverse the number string and convert it to an integer
                int num = Integer.parseInt(numStr.reverse().toString());

                // Reverse the collected string and repeat it
                String repeatedStr = temp.reverse().toString().repeat(num);

                // Push the repeated string back onto the stack
                for (char c : repeatedStr.toCharArray()) {
                    stack.push(c);
                }
            }
        }
        
        // Build the final result by appending characters (in the correct order)
        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.append(stack.pop());
        }
        
        // Reverse the result at the end to get the correct final string
        return result.reverse().toString();
    }
}
"""

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
# Java
"""
import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        Stack<Object> stack = new Stack<>();  // Use a single stack to store both strings and integers
        StringBuilder currentString = new StringBuilder();
        int k = 0;
        
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                // Build the number k
                k = k * 10 + (ch - '0');
            } else if (ch == '[') {
                // Push the current string and k onto the stack
                stack.push(currentString.toString());
                stack.push(k);
                // Reset currentString and k for the new frame
                currentString = new StringBuilder();
                k = 0;
            } else if (ch == ']') {
                // Pop the multiplier k
                int repeatTimes = (int) stack.pop();
                // Pop the last string
                String lastString = (String) stack.pop();
                // Repeat the current string k times and append it to the last string
                currentString = new StringBuilder(lastString).append(currentString.toString().repeat(repeatTimes));
            } else {
                // Append the character to the current string
                currentString.append(ch);
            }
        }
        
        return currentString.toString();
    }
}
"""

# Similar Question:
# 856. Score of Parentheses
