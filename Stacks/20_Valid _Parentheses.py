# method 1: simplest solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack= [0] # initialising stack with '0' to check at last
        n= len(s)
        for i in range(n):
            # push if any opening bracket comes
            if s[i]== '(' or s[i]== '{' or s[i]== '[':
                stack.append(s[i])
            # pop if any closing bracket come of same type
            # if closing bracket is not of  same type then 'invalid'
            else:
                if s[i]== ')':
                    if stack[-1]== '(':
                        stack.pop()
                    else:
                        return False
                if s[i]== '}':
                    if stack[-1]== '{':
                        stack.pop()
                    else:
                        return False
                if s[i]== ']':
                    if stack[-1]== '[':
                        stack.pop()
                    else:
                        return False
        return stack[-1]== 0  # means no extra char remaining in stack 


# method 2: concise one
#User function Template for python3
class Solution:
    def valid(self, s): 
        stack= [0] # initialising to check whether stack is empty or not 
        # logic: push closing braces of the current braces after seeing the opening braces
        # and when you encouter the closed parenthesis check the ele on top of stack
        # if same as current char then continue the loop
        # at last check for empty stack
        for i in range(len(s)):
            if s[i]== '(':
                stack.append(')')
            elif s[i]== '{':
                stack.append('}')
            elif s[i]== '[':
                stack.append(']')
            elif stack.pop()!= s[i]: # if stack is empty or current char
                                                    # is not equal to ele on top of the stack
                                                    # then it means not valid
                return False
        return stack== [0]   # after traversing all the string if stack is empty
                            # then valid otherwise not


# method 3: using dictionary
# just sam3 logic as method 2
def valid(self, s): 
    stack= [0] 
    # use the dictionary and map the valid parenthesis
    hashmap= {'(': ')', '{': '}', '[': ']'}
    for c in s:
        # if opening braces come then push
        if c in hashmap:
            stack.append(c)
        else: # if closing brace comes then map the ele on top of the stack after poping
              # if not equal to the current character then false
            if hashmap[stack.pop()]!= c: return False
    # at last check for stack content ,if like before then
    # true otherwise false
    return stack== [0]

