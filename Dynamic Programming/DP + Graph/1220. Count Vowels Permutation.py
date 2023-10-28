# we can create a directed graph where an edge between characters
# first and second imply that it is permissible to write second immediately after first. 

# Note: Hence, the question converts to, Given a directed graph, how many paths of length n are there?

# dp[n][char] denotes the number of directed paths of length n which end at a particular vertex char.
# But for calculating this we need to know last_char included before before cur char i.e
# we can take add this 'char' only after the char 'char' can comes.

# 'a'. 'a' can come after 'e','i','u'.
# 'e'. 'e' can come after 'a', 'i'.
# 'i'. 'i' can come after 'e', 'o'.
# 'o'. 'o' can come after 'i'
# 'u'. 'u' can come after 'i', 'o'.

# We can use the dp[n-1][last_char] to calculate dp[n][char] i.e
#  if we can find the number of paths of length n-1 ending at these vertices, then we can append char at the end of every path .

# Time : O(n), space = O(n*5)
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # index => a : 0, e : 1, i : 2, o: 3, u: 4    
        dp = [[0 for c in range(5)] for i in range(n + 1)]
        # dp[i][j] : will denote the no of string of length 'i' ending at char 'j'.
        for i in range(5):
            dp[1][i] = 1
        mod = 10**9 + 7
        for i in range(2, n + 1):
            # find the string of length '2' to 'n' ending at different chair using prev calculated one
            # 1) for 'a'. 'a' can come after 'e','i','u'.
            dp[i][0] = (dp[i -1][1] + dp[i-1][2] + dp[i-1][4]) % mod
            # 2) for 'e'. 'e' can come after 'a', 'i'.
            dp[i][1] = (dp[i -1][0] + dp[i -1][2]) % mod
            # 3) for 'i'. 'i' can come after 'e', 'o'.
            dp[i][2] = (dp[i -1][1] + dp[i -1][3]) % mod
            # 4) for 'o'. 'o' can come after 'i'
            dp[i][3] = (dp[i -1][2]) % mod
            # 5) for 'u'. 'u' can come after 'i', 'o'.
            dp[i][4] = (dp[i -1][2] + dp[i -1][3]) % mod
        
        # Now add ans for length 'n' ending at all char
        ans = 0
        for i in range(5):
            ans = (ans + dp[n][i]) % mod
        return ans
    

# Optimising space
# Since for current index , it depends only on last one.
# so we can use '5' variable to '5' char. It will store ans calculated for all '5' char till now.

# Time = O(n), space = O(5)

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        mod = 10 ** 9 + 7
        
        for j in range(2, n + 1):
            a2 = (e + i + u) % mod
            e2 = (a + i) % mod
            i2 = (e + o) % mod
            o2 = i 
            u2 = (o + i) % mod
            a , e, i, o , u = a2, e2, i2, o2, u2
        return (a + e + i + o + u) % mod