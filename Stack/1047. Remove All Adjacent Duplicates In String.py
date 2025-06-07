# time= space= O(n)

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack= []
        for c in s:
            # check if same char id present at the top of stack.
            # used 'if' because we only need to delete only twp adjacent char
            if stack and stack[-1]== c:
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

# Java Code 
"""
import java.util.Stack;

class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            // Check if the same character is present at the top of the stack.
            // Used 'if' because we only need to delete **only two adjacent characters**.
            if (!stack.isEmpty() && stack.peek() == c) {
                stack.pop();
            } else {
                stack.push(c);
            }
        }

        // Construct the final result from stack
        StringBuilder result = new StringBuilder();
        while (!stack.isEmpty()) {
            result.insert(0, stack.pop());
        }

        return result.toString();
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
    string removeDuplicates(string s) {
        stack<char> st;

        for (char c : s) {
            // Check if the same character is present at the top of the stack.
            // Used 'if' because we only need to delete **only two adjacent characters**.
            if (!st.empty() && st.top() == c) {
                st.pop();
            } else {
                st.push(c);
            }
        }

        // Construct the final result from stack
        string result;
        while (!st.empty()) {
            result = st.top() + result;
            st.pop();
        }

        return result;
    }
};
"""
# Later try by two pointer also


# Related Q:
"""
1) 2390. Removing Stars From a String
2) 3174. Clear Digits
3) 1209. Remove All Adjacent Duplicates in String II
"""
