# Logic: Just same logic as "1047. Remove All Adjacent Duplicates In String".
# only diff: Here we can only remove if no of same element including current char is >= k.
# for this add the count of same char also with character in stack.

# 1) when you see any char check if top of stack has same char,:
# a) if same then:
# a.1) increment the count of top of stack by '1'.
# a.2) After incr check if count == k .
# a.2.1) if == k then pop 
# b) else append current char with number = 1.

# Time = space = O(n)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        n = len(s)
        stack = []  # [[char, count]]
        for i in range(n):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
                if stack[-1][1] == k :
                    stack.pop()
            else:
                stack.append([s[i], 1])
        ans = ""
        for i in range(len(stack)):
            ans += stack[i][1]  * stack[i][0]             
        return ans
        