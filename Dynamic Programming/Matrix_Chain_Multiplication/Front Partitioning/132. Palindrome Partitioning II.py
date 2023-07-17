# mIne method : easy only

# Logic: if given string is palindrome simply return '0'
# else Try partition it at all index and take minimum of all.


# Recursion
# time :O(2^n)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        def solve(i):
            if i == len(s):
                return 0
            if s[i: ] == s[i :][::-1]:
                return 0
            ans = float('inf')
            for j in range(i, n):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    ans = min(ans, 1 + solve(j + 1))
            return ans

        return solve(0)
    
# Recursion  + memoisation
# tIme: O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        def solve(i):
            if i == len(s):
                return 0
            if s[i: ] == s[i :][::-1]:
                return 0
            if dp[i] != -1:
                return dp[i]
            ans = float('inf')
            for j in range(i, n):
                if s[i : j + 1] == s[i : j + 1][::-1]:
                    ans = min(ans, 1 + solve(j + 1))
            dp[i] = ans
            return ans
        dp = [-1 for i in range(len(s))]
        return solve(0)

# but TLE all the three methods.

# method 1: 
class Solution:
    def minCut(self, s: str) -> int:
        n= len(s)
        i, j= 0, n-1
        return self.helper(s, i, j)
    
    def helper(self, s, i, j):
        if i== j:  # if equal means single char so no need to cut anymore
            return 0
        s1= s[i: j+1]
        if s1== s1[::-1]: # if string between 'i' to 'j' is already palindrome
            return 0
        # if not palindrome try to partition it at all possible index
        mn= 9999
        for k in range(i, j):
            SmallAns= self.helper(s, i, k) + self.helper(s, k+1, j) + 1
            mn= min(mn, SmallAns)
        return mn
        

# method 2: memoization 
# this also giving TLE
class Solution:
    def minCut(self, s: str) -> int:
        n= len(s)
        i, j= 0, n-1
        dp= [[-1 for j in range(n)] for i in range(n)]
        return self.helper(s, i, j, dp)
    
    def helper(self, s, i, j, dp):
        if i== j:  # if equal means single char so no need to cut anymore
            return 0
        s1= s[i: j+1]  
        if s1== s1[::-1]:  # if string between 'i' to 'j' is already palindrome
            return 0
        if dp[i][j]!= -1:
            return dp[i][j]
        mn= 9999   # maximum no of partition can be 'n-1' when all ele are distinct
        for k in range(i, j):
            SmallAns= self.helper(s, i, k, dp) + self.helper(s, k+1, j, dp) + 1
            mn= min(mn, SmallAns)
            dp[i][j]= mn
        return dp[i][j]


# method 3: Tabulation
class Solution:
    def minCut(self, s: str) -> int:
        n= len(s)
        i, j= 0, n-1
        dp= [[0 for j in range(n)] for i in range(n)]   # automatically initialised with base case
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                s1= s[i: j+1]
                if s1== s1[::-1]:
                    dp[i][j]= 0
                    continue
                mn= 9999999999
                for k in range(i, j):
                    SmallAns= dp[i][k] + dp[k+1][j] + 1
                    mn= min(mn, SmallAns)
                dp[i][j]= mn
        return dp[0][n-1]


# another Approach: Front partitioning
# logic: you can only partition at any index if string till that index is palindrome.
# in this we only need to pass one parameter, for checking palindrome at each index.

# method 1: Recursion
class Solution:
    def minCut(self, s: str) -> int:
        n, i= len(s), 0
        ans= self.helper(s, i) -1  # since even after end index our function is doing partition and adding '+1'. so we have to subtract that '1'.
        return ans
    
    def helper(self, s, i):
        if i== len(s):
            return 0
        mincost= 9999
        for j in range(i, len(s)):
            temp= s[i: j+1]   # keep on adding one string at a time and if it is palindrom then partition after that index.
            if temp== temp[::-1]:
                smallAns= 1 + self.helper(s, j+1)
                mincost= min(mincost, smallAns)
        return mincost


# method 2: Memoization(Accepted)
# for time complexity: see the no of variable changing(say m) and no of 'for' loop (say p)
# time: O(n^(m+p)). actual one will depend on range of changing variables and no of for loops.
# better one: time= O(n*r1*r2*....).  r1, r2,....: are size of variable changing in function as well as inside the for loop.

# here : time: O(n^2) as both the variable changing in function as well as variable inside the for loop is O(n)
class Solution:
    def minCut(self, s: str) -> int:
        n, i= len(s), 0
        dp = [-1 for i in range(n+1)]   # 'i' going from '0' to 'n'(base case)
        ans= self.helper(s, i, dp) -1  # since even after end index our function is doing partition and adding '+1'. so we have to subtract that '1'.
        return ans
    
    def helper(self, s, i, dp):
        if i== len(s):
            return 0
        if dp[i]!= -1:
            return dp[i]
        mincost= 9999
        for j in range(i, len(s)):
            temp= s[i: j+1]   # keep on adding one string at a time and if it is palindrom then partition after that index.
            if temp== temp[::-1]:
                smallAns= 1 + self.helper(s, j+1, dp)
                mincost= min(mincost, smallAns)
                dp[i]= mincost
        return dp[i]


# Tabulation
class Solution:
    def minCut(self, s: str) -> int:
        n, i= len(s), 0
        dp = [0 for i in range(n+1)]
        for i in range(n-1, -1, -1):
            mincost= 9999
            for j in range(i, len(s)):
                temp= s[i: j+1]   # keep on adding one string at a time and if it is palindrom then partition after that index.
                if temp== temp[::-1]:
                    smallAns= 1 + dp[j+1]
                    mincost= min(mincost, smallAns)
            dp[i]= mincost
        return dp[0] -1
