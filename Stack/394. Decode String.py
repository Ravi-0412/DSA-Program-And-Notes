# when you see this type of problem involving nested brackets call with this type of logic then use stack.

# using one stack.
# just like solve 'postfix and infix' evalauation.

# logic: before every '[', there will be a number.
# time: will depend on 'num' before every bracket but will be linear time only.

class Solution:
    def decodeString(self, s: str) -> str:
        stack= []
        for i in range(len(s)):
            if s[i]!= ']':   # push everything into stack until you see ']'.
                stack.append(s[i])
            else:   # means we have seen ']' .
                # first find the string . So start poping till we find '[' .
                temp= ""
                while stack[-1] != '[':
                    temp= stack.pop() + temp
                stack.pop()
                # before every '[', there will be a number but this can be of more than one digit.
                # find the number. better than multiplying by 10.
                num= ""
                while stack and stack[-1].isdigit():  # checking stack empty in case it doesn't any number then stack will be empty.
                    num= stack.pop() + num
                # now multiply 'temp' with 'num' to get the string till one of '[' and put into stack. num will be a string.
                temp= temp*int(num)
                stack.append(temp)
        return "".join(stack)


# Method 2:
# Better one. Just similar logic as "772. Basic Calculator III".

# We need to keep track of number and string before '['.
# So when you see '[' then append string and num before '[' into stack.
# And start from scratch .

# When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
# push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
# the enclosed string k times.
    
class Solution(object):
    def decodeString(self, s):
        stack = []
        current_string = ""
        k = 0
        
        for char in s:
            if char == "[" :
                # Just finished parsing this k, save current string and k for when we pop
                stack.append((current_string, k))
                # Reset current_string and k for this new frame
                current_string = ""
                k = 0
            elif char == "]":
                # We have completed this frame, get the last current_string and k from when the frame 
                # opened, which is the k we need to duplicate the current current_string by
                last_string, last_k = stack.pop(-1)
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                current_string += char
        
        return current_string


# Similar Question:
# 856. Score of Parentheses