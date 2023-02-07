# time= space= O(n)
# Intuition behind 'stack' and other arrays is very good.
# undertand this from solution link in the sheet 

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index= {}  # will store the last_index of each char in the string
        visited= set()  # will tell whether curr char has been added to stack already or not.
        stack= []       # at last we will get ans in stack.

        # first storing the last index of each char
        for i in range(len(s)):
            last_index[s[i]]= i
        
        # now getting the ans
        for i in range(len(s)):
            # if s[i] already in stack then simply skip.
            if s[i] not in visited:
                while stack and stack[-1] > s[i] and last_index[stack[-1]] > i:  # keep poping from stack.
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)