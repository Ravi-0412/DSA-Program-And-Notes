# Logic: whenever there is backspace then we have to remove the last seen char 
# i.e Last In First Out. So we can use stack.

# time = space = O(n)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        for i in range(len(s)):
            if s[i] == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(s[i])
        
        stack_t = []
        for i in range(len(t)):
            if t[i] == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(t[i])
        return "".join(stack_s) == "".join(stack_t)



# Method 2: Do by Two pointer approach in space = O(1)