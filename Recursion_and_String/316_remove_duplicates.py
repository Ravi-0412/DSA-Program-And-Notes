# method 1: 

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        LastIndex= [0]*26  # will store the last index occurences of the char
        # LastIndex will tell whether to delete that char from ans or not
        for i in range(len(s)):
            LastIndex[ord(s[i]) - ord('a')]= i    # for 'a' index= 0, for 'b' index= 1 and so on
        stack= []
        for i in range(len(s)):
            curr= ord(s[i]) - ord('a')  # will help in checking the last index
            if s[i] in stack:  # if curr char is already in stack then skip and do nothing
                continue
            # otherwise check if stack_top > curr_char and if it is then check whether they are occuring again after curr_char or not
            # repeat this till stack become empty 
            # if stack_top is occuring again after curr_char then we can pop the stack_top and consider its final occurences
            while stack and ord(stack[-1]) > ord(s[i]) and LastIndex[ord(stack[-1]) - ord('a')] > i:
                stack.pop()
            stack.append(s[i])
        # now stack will contain the ans but we have to return in form of string'
        # so store in form of string and return, that will be the final ans
        ans= ""
        for i in range(len(stack)):
            ans+= stack[i]
        return ans
            


