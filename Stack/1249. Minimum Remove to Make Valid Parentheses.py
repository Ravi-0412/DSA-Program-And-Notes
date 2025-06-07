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
import java.util.Stack;

class Solution {
    public String minRemoveToMakeValid(String s) {
        StringBuilder result = new StringBuilder(s);
        Stack<Integer> stack = new Stack<>();

        // First pass: Mark invalid parentheses
        for (int i = 0; i < result.length(); i++) {
            if (result.charAt(i) == '(') {
                stack.push(i);
            } else if (result.charAt(i) == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else {
                    result.setCharAt(i, '*'); // Mark invalid ')'
                }
            }
        }

        // Second pass: Remove remaining '(' with no matching pair
        while (!stack.isEmpty()) {
            result.setCharAt(stack.pop(), '*'); // Mark invalid '('
        }

        // Remove all marked characters
        return result.toString().replace("*", "");
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
    string minRemoveToMakeValid(string s) {
        string result = s;
        stack<int> st;

        // First pass: Mark invalid parentheses
        for (int i = 0; i < result.size(); i++) {
            if (result[i] == '(') {
                st.push(i);
            } else if (result[i] == ')') {
                if (!st.empty()) {
                    st.pop();
                } else {
                    result[i] = '*'; // Mark invalid ')'
                }
            }
        }

        // Second pass: Remove remaining '(' with no matching pair
        while (!st.empty()) {
            result[st.top()] = '*'; // Mark invalid '('
            st.pop();
        }

        // Remove all marked characters
        result.erase(remove(result.begin(), result.end(), '*'), result.end());

        return result;
    }
};
"""
