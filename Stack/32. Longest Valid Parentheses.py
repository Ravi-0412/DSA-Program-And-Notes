# Method 1: 

# Brute force
# time: O(n^3)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans= 0
        # from each index check for every possible valid paranthesis.
        # first possible will start from 'i+1' (we require at least two ele for valid one)
        for i in range(len(s) -1):
            for j in range(i+1, len(s)):
                if self.isValid(0, s[i: j+1], 0):
                    ans= max(ans, j+1-i)
        return ans
    
    def isValid(self, i, s, open):
        if i== len(s):
            return open== 0
        if s[i]== '(':
            open+= 1
        else:
            open-= 1
            if open < 0:
                return False
        return self.isValid(i+1, s, open)


# method 2: 
# using stack
# logic: Put '(' always into stack
# and ')' when we are not able to find any valid after we see ')'.
# Pushing ')' will denote that after index of ')' , paranthesis are vlid.

# Implementation:
# when you see '(': push the index into the stack
# when you see ')': pop and check if stack is empty or not.
# if empty push the curr index into stack.
# if not empty then we got one valid ans.

# time= space= O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans= 0
        stack= [-1]   # initially fill the stack with '-1' to handle corner cases like s= '('.
        for i in range(len(s)):
            if s[i]== '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:   # means we have found invalid one 
                    stack.append(i)
                else:  # means we have found the valid one
                    ans= max(ans, i- stack[-1])  # substring after index 'stack[-1]' to 'i' will be a valid one
        return ans 


# method 3: 

# for valid one: open== close
# logic: for left to right: when at any index if we see open > close => it means till no string can be valid till this index.
# for right to left: close > open => no string can be valid till this index.

# why we need two pass?
# Ans: if we go only from either left to right, OR either from right to left then we may get the ans less than the required.
# e.g: "(()".. if we go from left to right then no way we will find open== close and we will get ans= 0
# But ans will be '2'. And this we will get when we will traverse from right to left.

# time: o(n), space: O(1)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n= len(s)
        ans= 0
        open= close= 0
        for i in range(n):
            if s[i]== '(':
                open+= 1
            else:
                close+= 1
            if open== close:
                ans= max(ans, 2*open)
            elif close> open:
                open= close= 0
        
        # Now check also from right to left
        open= close= 0
        for i in range(n-1, -1, -1):
            if s[i]== '(':
                open+= 1
            else:
                close+= 1
            if open== close:
                ans= max(ans, 2*open)
            elif open> close:
                open= close= 0
        return ans

# Java Code
"""
//Method 1
class Solution {
    private boolean isValid(String s, int i, int open) {
        if (i == s.length()) return open == 0;
        if (s.charAt(i) == '(') open++;
        else {
            open--;
            if (open < 0) return false;
        }
        return isValid(s, i + 1, open);
    }

    public int longestValidParentheses(String s) {
        int ans = 0;

        // Check every possible valid parentheses substring
        for (int i = 0; i < s.length() - 1; i++) {
            for (int j = i + 1; j < s.length(); j++) {
                if (isValid(s.substring(i, j + 1), 0, 0)) {
                    ans = Math.max(ans, j - i + 1);
                }
            }
        }

        return ans;
    }
}

//Method 2
import java.util.Stack;

class Solution {
    public int longestValidParentheses(String s) {
        int ans = 0;
        Stack<Integer> stack = new Stack<>();
        stack.push(-1); // Initially add -1 to handle edge cases

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                stack.pop();
                if (stack.isEmpty()) {
                    stack.push(i);
                } else {
                    ans = Math.max(ans, i - stack.peek()); // Valid substring between stack.peek() and i
                }
            }
        }

        return ans;
    }
}

//Method 3
class Solution {
    public int longestValidParentheses(String s) {
        int ans = 0, open = 0, close = 0;

        // Left to right traversal
        for (char c : s.toCharArray()) {
            if (c == '(') open++;
            else close++;

            if (open == close) ans = Math.max(ans, 2 * open);
            else if (close > open) open = close = 0;
        }

        // Right to left traversal
        open = close = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == '(') open++;
            else close++;

            if (open == close) ans = Math.max(ans, 2 * open);
            else if (open > close) open = close = 0;
        }

        return ans;
    }
}
"""

# C++ Code
"""
//Method 1
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isValid(const string& s, int i, int open) {
        if (i == s.length()) return open == 0;
        if (s[i] == '(') open++;
        else {
            open--;
            if (open < 0) return false;
        }
        return isValid(s, i + 1, open);
    }

    int longestValidParentheses(string s) {
        int ans = 0;

        // Check every possible valid parentheses substring
        for (int i = 0; i < s.length() - 1; i++) {
            for (int j = i + 1; j < s.length(); j++) {
                if (isValid(s.substr(i, j - i + 1), 0, 0)) {
                    ans = max(ans, j - i + 1);
                }
            }
        }

        return ans;
    }
};

//Method 2
#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int ans = 0;
        stack<int> st;
        st.push(-1); // Initially add -1 to handle edge cases

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(') {
                st.push(i);
            } else {
                st.pop();
                if (st.empty()) {
                    st.push(i);
                } else {
                    ans = max(ans, i - st.top()); // Valid substring between st.top() and i
                }
            }
        }

        return ans;
    }
};

//Method 3
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int ans = 0, open = 0, close = 0;

        // Left to right traversal
        for (char c : s) {
            if (c == '(') open++;
            else close++;

            if (open == close) ans = max(ans, 2 * open);
            else if (close > open) open = close = 0;
        }

        // Right to left traversal
        open = close = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] == '(') open++;
            else close++;

            if (open == close) ans = max(ans, 2 * open);
            else if (open > close) open = close = 0;
        }

        return ans;
    }
};
"""