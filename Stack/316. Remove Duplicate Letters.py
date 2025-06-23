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

# Java Code 
"""
import java.util.*;

public class Solution {
    public String removeDuplicateLetters(String s) {
        Map<Character, Integer> last_index = new HashMap<>();  // will store the last_index of each char in the string
        Set<Character> visited = new HashSet<>();              // will tell whether curr char has been added to stack already or not.
        Stack<Character> stack = new Stack<>();                // at last we will get ans in stack. keep track of selected character's.
                                                               // put the character's only once & maintain the lexicographically smallest one.

        // first storing the last index of each char so in case of duplicate we can check whether 
        // we can remove stack top char or not for maintaining lexicographically smallest order.
        for (int i = 0; i < s.length(); i++) {
            last_index.put(s.charAt(i), i);
        }

        // now getting the ans
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            // if c already in stack then simply skip.
            if (!visited.contains(c)) {
                // Keep on removing char from stack if : 
                // 1) stack top is greater and 2) stack top char has another occurrence also after index 'i'.
                while (!stack.isEmpty() && stack.peek() > c && last_index.get(stack.peek()) > i) {
                    visited.remove(stack.pop());  // Removing from visited also 
                }
                stack.push(c);
                visited.add(c);
            }
        }

        // Build result
        StringBuilder sb = new StringBuilder();
        for (char ch : stack) {
            sb.append(ch);
        }

        return sb.toString();
    }
}

"""
# C++ Code 
"""
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <stack>
using namespace std;

class Solution {
public:
    string removeDuplicateLetters(string s) {
        unordered_map<char, int> last_index;  // will store the last_index of each char in the string
        unordered_set<char> visited;          // will tell whether curr char has been added to stack already or not.
        stack<char> stack;                    // at last we will get ans in stack. keep track of selected character's.
                                              // put the character's only once & maintain the lexicographically smallest one.

        // first storing the last index of each char so in case of duplicate we can check whether 
        // we can remove stack top char or not for maintaining lexicographically smallest order.
        for (int i = 0; i < s.size(); i++) {
            last_index[s[i]] = i;
        }

        // now getting the ans
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];

            // if c already in stack then simply skip.
            if (visited.find(c) == visited.end()) {
                // Keep on removing char from stack if : 
                // 1) stack top is greater and 2) stack top char has another occurrence also after index 'i'.
                while (!stack.empty() && stack.top() > c && last_index[stack.top()] > i) {
                    visited.erase(stack.top());  // Removing from visited also 
                    stack.pop();
                }
                stack.push(c);
                visited.insert(c);
            }
        }

        // Build result
        string result;
        while (!stack.empty()) {
            result += stack.top();
            stack.pop();
        }
        reverse(result.begin(), result.end());
        return result;
    }
};

"""

# Related Q:
# 1) 1081. Smallest Subsequence of Distinct Characters
# Exactly same question 

# about 'join' in java
# link: https://www.geeksforgeeks.org/java-string-join-examples/
