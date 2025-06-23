# Method 1:

# Logic: We need to only care about brackets.
# So we can just check combination of '(' and ')' ignoring alphabetical character.
# When we will see '(' we will push index of '(' into stack  and 
# on ')' if stack is empty then  there is no matching for current ')' 
# so we will make value at index of ')' as empty("").

# At last we will left with all unmatched pair for '(' in form of indexes so we will
# make all value at these indexes also = "".

# Time= space = O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        list_s = list(s)
        stack = []
        for i in range(len(list_s)):
            if list_s[i] == '(':
                stack.append(i)
            elif list_s[i] == ')':
                # pop if stack is not empty. Means we have required pair for this one.
                if stack:
                    stack.pop()
                # For cur char ')' there is no pair. so we have make value at this index = "".
                # Means extra char, so we will remove this.
                else:
                    list_s[i] = ""
        # Now if our stack is not empty then we will have to make all those index value = "".
        # Because these '(' have no matching pair.
        for i in stack:
            list_s[i] = ""
        # Now return the ans as string
        return  "".join(list_s)

# Java Code 
"""
class Solution {
    public String minRemoveToMakeValid(String s) {
        char[] list_s = s.toCharArray();
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < list_s.length; i++) {
            if (list_s[i] == '(') {
                stack.push(i);
            } else if (list_s[i] == ')') {
                // pop if stack is not empty. Means we have required pair for this one.
                if (!stack.isEmpty()) {
                    stack.pop();
                } 
                // For cur char ')' there is no pair. so we have make value at this index = "".
                // Means extra char, so we will remove this.
                else {
                    list_s[i] = '\0';
                }
            }
        }

        // Now if our stack is not empty then we will have to make all those index value = "".
        // Because these '(' have no matching pair.
        while (!stack.isEmpty()) {
            list_s[stack.pop()] = '\0';
        }

        // Now return the ans as string
        StringBuilder result = new StringBuilder();
        for (char c : list_s) {
            if (c != '\0') {
                result.append(c);
            }
        }

        return result.toString();
    }
}
"""

# C++ Code 
"""
#include <string>
#include <stack>

class Solution {
public:
    std::string minRemoveToMakeValid(std::string s) {
        std::stack<int> stack;

        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                stack.push(i);
            } else if (s[i] == ')') {
                // pop if stack is not empty. Means we have required pair for this one.
                if (!stack.empty()) {
                    stack.pop();
                }
                // For cur char ')' there is no pair. so we have make value at this index = "".
                // Means extra char, so we will remove this.
                else {
                    s[i] = '\0';
                }
            }
        }

        // Now if our stack is not empty then we will have to make all those index value = "".
        // Because these '(' have no matching pair.
        while (!stack.empty()) {
            s[stack.top()] = '\0';
            stack.pop();
        }

        // Now return the ans as string
        std::string result;
        for (char c : s) {
            if (c != '\0') {
                result += c;
            }
        }

        return result;
    }
};
"""