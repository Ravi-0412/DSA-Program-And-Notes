# Basic: 

#There will be only two possibility i.e '101' and '010' so Q reduces to
# find the number of distinct subsequences of '101' and '010' in string and add them.
# Which is same as Question: "115. Distinct Subsequences".


# Method 1: 
# Recursive

class Solution:
    def numberOfWays(self, s: str) -> int:
        return self.countPattern(s, "010") + self.countPattern(s, "101")

    def countPattern(self, s, t):
        def helper(m, n):
            if n == 0:
                return 1
            if m == 0:
                return 0
            if s[m - 1] == t[n - 1]:
                return helper(m - 1, n - 1) + helper(m - 1, n)
            else:
                return helper(m - 1, n)
        return helper(len(s), len(t))


# Method 2:
# Memoisation

class Solution:
    def numberOfWays(self, s: str) -> int:
        return self.countPattern(s, "010") + self.countPattern(s, "101")

    def countPattern(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        return self.helper(m, n, s, t, dp)

    def helper(self, m, n, s, t, dp):
        if n == 0:
            return 1
        if m == 0:
            return 0
        if dp[m][n] != -1:
            return dp[m][n]
        
        if s[m - 1] == t[n - 1]:
            dp[m][n] = self.helper(m - 1, n - 1, s, t, dp) + self.helper(m - 1, n, s, t, dp)
        else:
            dp[m][n] = self.helper(m - 1, n, s, t, dp)
        
        return dp[m][n]

# Method 3:
# Tabulation

class Solution:
    def numberOfWays(self, s: str) -> int:
        return self.countPattern(s, "010") + self.countPattern(s, "101")

    def countPattern(self, s, t):
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]

# Method 4:
# Optimising sapce to : O(n)
class Solution:
    def numberOfWays(self, s: str) -> int:
        return self.countPattern(s, "010") + self.countPattern(s, "101")

    def countPattern(self, s, t):
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for c in s:
            for j in range(len(t), 0, -1):
                if c == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[len(t)]
