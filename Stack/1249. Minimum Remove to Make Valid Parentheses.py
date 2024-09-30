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

# Java
"""
class Solution {
    public String minRemoveToMakeValid(String s) {
        // Convert the input string to a char array (mutable).
        char[] list_s = s.toCharArray();
        // Stack to keep track of indices of '(' characters.
        Stack<Integer> stack = new Stack<>();
        
        // First pass: Remove invalid ')' characters.
        for (int i = 0; i < list_s.length; i++) {
            if (list_s[i] == '(') {
                stack.push(i); // Push index of '(' onto the stack.
            } else if (list_s[i] == ')') {
                // If there's a matching '(' for this ')', pop the stack.
                if (!stack.isEmpty()) {
                    stack.pop();
                } else {
                    // If no matching '(', mark this ')' for removal by setting it to '\0'.
                    list_s[i] = '\0';
                }
            }
        }
        
        // Second pass: Remove any unmatched '(' characters remaining in the stack.
        while (!stack.isEmpty()) {
            list_s[stack.pop()] = '\0'; // Mark unmatched '(' for removal.
        }
        
        // Build the final valid string by ignoring marked characters ('\0').
        StringBuilder result = new StringBuilder();
        for (char c : list_s) {
            if (c != '\0') {
                result.append(c);
            }
        }
        
        return result.toString(); // Return the valid string.
    }
}
"""
