# Logic:Just exactly same as "546. Remove Boxes".

# What we have to do?
# Ans: Hmko same given string 's' generate karna h with condition:
# "EK abr me hm sirf same char generate kar sakte h but kitna bhi kar sakte h". New one will overwrite the pre generated one.
# Finally hmko 'min no of turn find karna h jo chahiye given string ko generate karne ke liye'.

# Note : max ans can be len(s) when all char will be distinct.

# Did this very tough Q myself only but still need to visualise properly 'for loop' part recursive call i.e how working.

# Time: O(n^3) , space : O(n^2)

class Solution:
    def strangePrinter(self, s: str) -> int:

        def dfs(i, j):
            if i > j:
                return 0
            # Choices:
            # 1) we will try to print all the same char at once.
            while i + 1 <= j and s[i + 1] == s[i]:
                i += 1
            ans = 1 + dfs(i + 1, j)
            # 2) if same char is there then we will print the same char till that index 'm'. Keep this in left side.
            for m in range(i + 1, j + 1):
                if s[m] == s[i]:
                    ans = min(ans,  dfs(i + 1, m), dfs(m + 1 , j))
                    # ans = min(ans,  dfs(i + 1, m - 1 ) + dfs(m , j))   # this also working but above one is more logical
            return ans
        n = len(s)
        i , j = 0, n -1 
        return dfs(i, j)


# Regex to combine the same letter in python:
# 1 ) s = re.sub(r'(.)\1*', r'\1', s)
# 2) s = ''.join(a for a, b in zip(s, '#' + s) if a != b)
# 3) s = [key for key, group in itertools.groupby(s)] 


# Have to understand the regex properly.
https://leetcode.com/problems/strange-printer/solutions/106794/one-suggestion-for-all-solutions/