# Logic: whenever there is backspace then we have to remove the last seen char 
# i.e Last In First Out. So we can use stack.

# time = space = O(m + n)

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

# My mistake

# While condition in case of if 's[i] == '#' or t[j] == '#' is wrong.
# e.g: s = aab#a### . this will make s = aa
# But s = "" 

# Why giving wrong ans because we are checking consecutive '#' for cancellation in while loop.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m , n  = len(s) , len(t)
        i , j = m - 1, n - 1
        while i >= 0 or j >= 0:
            if s[i] != '#' and t[j] != '#':
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            elif s[i] == '#':
                cnt = 0
                while i >= 0 and s[i] == '#':
                    cnt += 1
                    i -= 1
                i -= cnt
            elif t[j] == '#':
                cnt = 0
                while j >= 0 and t[j] == '#':
                    cnt += 1
                    j -= 1
                j -= cnt
        print(i, j)
        # return 1
        return s[: i + 1] == t[: j + 1]


# Correcting above solution

# Above mistake can be handled using a counter.
# We need counter of '#' and till count is > 0, we can cancel and when count == 0 
# We can't cancel and then we will return the cur char at index.

# time = O(m + n)
# space = O(1)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        m , n  = len(s) , len(t)

        def getChar(x, k):
            c , cnt = "", 0
            while k >= 0 and not c:
                if x[k] == '#':
                    cnt += 1
                elif cnt == 0:
                    # Can't erase more so assign c= x[i]
                    c = x[k]
                    # return c, k -1   # Can't cancel more so we can return from here also directly. No need to go futher.
                else: 
                    # Means char other than '#'
                    cnt -= 1
                k -= 1
            return c, k  # 

        i , j = m - 1, n - 1
        while i >= 0 or j >= 0:
            c1 = c2 = ""  # will store the char after erasing if '#' is there.
            if i >= 0:
                c1, i = getChar(s, i)
            if j >= 0 :
                c2, j = getChar(t, j)
            if c1 != c2:
                return False
        return True
            
        