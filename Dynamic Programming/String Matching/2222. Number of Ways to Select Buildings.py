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

# Java Code 
"""
class Solution {
    public int numberOfWays(String s) {
        return countPattern(s, "010") + countPattern(s, "101");
    }

    private int countPattern(String s, String t) {
        return helper(s, t, s.length(), t.length());
    }

    private int helper(String s, String t, int m, int n) {
        if (n == 0) return 1;
        if (m == 0) return 0;

        if (s.charAt(m - 1) == t.charAt(n - 1)) {
            return helper(s, t, m - 1, n - 1) + helper(s, t, m - 1, n);
        } else {
            return helper(s, t, m - 1, n);
        }
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int numberOfWays(string s) {
        return countPattern(s, "010") + countPattern(s, "101");
    }

private:
    int countPattern(const string& s, const string& t) {
        return helper(s, t, s.size(), t.size());
    }

    int helper(const string& s, const string& t, int m, int n) {
        if (n == 0) return 1;
        if (m == 0) return 0;

        if (s[m - 1] == t[n - 1]) {
            return helper(s, t, m - 1, n - 1) + helper(s, t, m - 1, n);
        } else {
            return helper(s, t, m - 1, n);
        }
    }
};
"""

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

# Java Code 
"""
class Solution {
    public int numberOfWays(String s) {
        return countPattern(s, "010") + countPattern(s, "101");
    }

    public int countPattern(String s, String t) {
        int m = s.length(), n = t.length();
        int[][] dp = new int[m + 1][n + 1];

        // Fill with -1
        for (int i = 0; i <= m; i++) {
            Arrays.fill(dp[i], -1);
        }

        return helper(m, n, s, t, dp);
    }

    public int helper(int m, int n, String s, String t, int[][] dp) {
        if (n == 0) return 1;
        if (m == 0) return 0;
        if (dp[m][n] != -1) return dp[m][n];

        if (s.charAt(m - 1) == t.charAt(n - 1)) {
            dp[m][n] = helper(m - 1, n - 1, s, t, dp) + helper(m - 1, n, s, t, dp);
        } else {
            dp[m][n] = helper(m - 1, n, s, t, dp);
        }

        return dp[m][n];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int numberOfWays(string s) {
        return countPattern(s, "010") + countPattern(s, "101");
    }

    int countPattern(const string& s, const string& t) {
        int m = s.size(), n = t.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return helper(m, n, s, t, dp);
    }

    int helper(int m, int n, const string& s, const string& t, vector<vector<int>>& dp) {
        if (n == 0) return 1;
        if (m == 0) return 0;
        if (dp[m][n] != -1) return dp[m][n];

        if (s[m - 1] == t[n - 1]) {
            dp[m][n] = helper(m - 1, n - 1, s, t, dp) + helper(m - 1, n, s, t, dp);
        } else {
            dp[m][n] = helper(m - 1, n, s, t, dp);
        }

        return dp[m][n];
    }
};
"""

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

# Java Code 
"""
class Solution {
    public int numberOfWays(String s) {
        return countPattern(s, "010") + countPattern(s, "101");
    }

    public int countPattern(String s, String t) {
        int m = s.length(), n = t.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[m][n];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int numberOfWays(string s) {
        return countPattern(s, "010") + countPattern(s, "101");
    }

    int countPattern(const string& s, const string& t) {
        int m = s.size(), n = t.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i <= m; ++i) {
            dp[i][0] = 1;
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == t[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        return dp[m][n];
    }
};
"""

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

# Java Code 
"""
class Solution {
    public int numberOfWays(String s) {
        return countPattern(s, "010") + countPattern(s, "101");
    }

    public int countPattern(String s, String t) {
        int[] dp = new int[t.length() + 1];
        dp[0] = 1;

        for (char c : s.toCharArray()) {
            for (int j = t.length(); j > 0; j--) {
                if (c == t.charAt(j - 1)) {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return dp[t.length()];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int numberOfWays(string s) {
        return countPattern(s, "010") + countPattern(s, "101");
    }

    int countPattern(const string& s, const string& t) {
        vector<int> dp(t.size() + 1, 0);
        dp[0] = 1;

        for (char c : s) {
            for (int j = t.size(); j > 0; --j) {
                if (c == t[j - 1]) {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return dp[t.size()];
    }
};
"""
