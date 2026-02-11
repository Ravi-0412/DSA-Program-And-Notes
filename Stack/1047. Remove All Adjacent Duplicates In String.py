# method 1

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

# Method 2: 
# Using Two Pointer
class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr = list(s)   # convert to list to allow in-place updates
        i = 0           # acts like stack pointer (top)

        for c in arr:
            if i > 0 and arr[i - 1] == c:
                i -= 1          # pop
            else:
                arr[i] = c      # push
                i += 1

        return "".join(arr[:i])

# Java
"""
class Solution {
    public String removeDuplicates(String s) {
        char[] arr = s.toCharArray();
        int i = 0;  // acts like stack top

        for (char c : arr) {
            if (i > 0 && arr[i - 1] == c) {
                i--;        // pop (remove duplicate pair)
            } else {
                arr[i] = c; // push
                i++;
            }
        }

        return new String(arr, 0, i);
    }
}
"""

# C++
"""
class Solution {
public:
    string removeDuplicates(string s) {
        int i = 0;  // stack pointer

        for (char c : s) {
            if (i > 0 && s[i - 1] == c) {
                i--;        // pop
            } else {
                s[i] = c;   // push
                i++;
            }
        }

        return s.substr(0, i);
    }
};
"""

# Extesnion 
"""
1) 2390. Removing Stars From a String
2) 3174. Clear Digits
3) 1209. Remove All Adjacent Duplicates in String II
"""
