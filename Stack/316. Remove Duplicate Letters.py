# Why stack?
# When we will see any character then we will try to remove all the characters before
# which has higher lexicographically order if that char is also occuring ahead.
# For this we need stack.

# Implementation:
# we have to pick the character's if it is not already visited. 
# We'll also make sure, the previously picked character is smaller then the current character
# in order to maintain lexicographically order. 

# time= space= O(n)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index= {}  # will store the last_index of each char in the string
        visited= set()  # will tell whether curr char has been added to stack already or not.
        stack= []       # at last we will get ans in stack. keep track of selected character's.
                        # put the character's only once & maintain the lexicographicall smallest one.

        # first storing the last index of each char so in case of duplicate we can check whether 
        # we can remove stack top char or not for maintaining lexicographicall smallest order.
        for i in range(len(s)):
            last_index[s[i]]= i
        
        # now getting the ans
        for i in range(len(s)):
            # if s[i] already in stack then simply skip.
            if s[i] not in visited:
                # Keep on removing char from stack if : 
                # 1) stack top is greater and 2) stack top char has another occurence also after index 'i'.
                while stack and stack[-1] > s[i] and last_index[stack[-1]] > i:  # keep poping from stack.
                    visited.remove(stack.pop())   # Removing from visited also 
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)


# Related Q:
# 1) 1081. Smallest Subsequence of Distinct Characters
# Exactly same question 

# about 'join' in java
# link: https://www.geeksforgeeks.org/java-string-join-examples/

# Java Code 
"""
import java.util.*;

class Solution {
    public String removeDuplicateLetters(String s) {
        Map<Character, Integer> lastIndex = new HashMap<>(); // Stores last occurrence of each character
        Set<Character> visited = new HashSet<>(); // Tracks characters already added to the stack
        Stack<Character> stack = new Stack<>(); // Stores characters in lexicographically smallest order without duplicates

        // First storing the last index of each character in the string
        for (int i = 0; i < s.length(); i++) {
            lastIndex.put(s.charAt(i), i);
        }

        // Iterate through the string
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            // Skip if already in stack
            if (visited.contains(c)) continue;

            // Keep removing chars from stack if:
            // 1) Stack top is greater than current char
            // 2) The stack top character appears again later
            while (!stack.isEmpty() && stack.peek() > c && lastIndex.get(stack.peek()) > i) {
                visited.remove(stack.pop()); // Remove from visited as well
            }

            stack.push(c);
            visited.add(c);
        }

        // Construct result from stack
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
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char, int> last_index; // Stores the last occurrence of each character in the string
        unordered_set<char> visited; // Tracks characters already added to the stack
        stack<char> st; // Stores characters in lexicographically smallest order without duplicates

        // First storing the last index of each character in the string
        for (int i = 0; i < s.size(); i++) {
            last_index[s[i]] = i;
        }

        // Iterate through the string
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];

            // Skip if already in stack
            if (visited.find(c) != visited.end()) continue;

            // Keep removing chars from stack if:
            // 1) Stack top is greater than current char
            // 2) The stack top character appears again later
            while (!st.empty() && st.top() > c && last_index[st.top()] > i) {
                visited.erase(st.top()); // Remove from visited as well
                st.pop();
            }

            st.push(c);
            visited.insert(c);
        }

        // Construct result from stack
        string result;
        while (!st.empty()) {
            result = st.top() + result;
            st.pop();
        }

        return result;
    }
};
"""