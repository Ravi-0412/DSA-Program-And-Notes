# tried a lot with two stack one with 'stack storing num' and one with 'stack storing char'.
# but it is going very complicated for nested brackets.

# when you see this type of problem involving nested brackets cal with this type of logic then use stack.

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
            else:   # means we have seen ']' so start poping till we find '['.
                temp= ""
                while stack[-1]!= '[':
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
