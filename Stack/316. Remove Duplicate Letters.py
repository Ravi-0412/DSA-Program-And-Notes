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

# Java
# about 'join' in java
# link: https://www.geeksforgeeks.org/java-string-join-examples/
"""
class Solution {
    public String removeDuplicateLetters(String s) {
        int n = s.length();
        Stack<Character> stack = new Stack<>();
        Set<Character>  set = new HashSet<>();
        Map<Character, Integer> lastIndex = new HashMap<>();
        for(int i = 0; i < n; i ++) {
            lastIndex.put(s.charAt(i), i);
        }
        for(int i = 0; i < n; i ++) {
            Character c = s.charAt(i) ;
            if(!set.contains(c)) {
                while(!stack.isEmpty() && stack.peek() > c && lastIndex.get(stack.peek()) > i) {
                    set.remove(stack.pop()) ;
                }
                stack.push(c);
                set.add(c);
            }
        }
        // return String.join(",", stack);   // 'join' works on string not on character
        StringBuilder ans = new StringBuilder();
        for(Character c : stack){
            ans.append(c);
        }
        return ans.toString();
    }
}
"""