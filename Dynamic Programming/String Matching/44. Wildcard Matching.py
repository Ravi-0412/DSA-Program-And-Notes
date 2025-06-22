# Method 1: 
# By Recursion

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        return self.helper(m, n, s, p)
    
    def helper(self, m, n, s, p):
        if n== 0:     # simplest one
            return m== 0
        
        # if 1st string get exhausted
        # then if all remainig char in 'p' is all "*" then return True else False
        if m==0:  
            for i in range(n-1,-1,-1):
                if p[i]!= '*':
                    return False
            return True
        
        if s[m-1]== p[n-1] or p[n-1]== '?':  # incr both indexes by '1'
            if self.helper(m-1, n-1, s, p):
                return True
        # when p[n-1]=="*", we have two choices 1)matching zero char with "*", move in pattern without keeping string index same
        # or match one or more char with "*", decr string index and keep pattern index same.
        elif p[n-1]== '*':  
            if self.helper(m, n-1, s, p) or self.helper(m-1, n, s, p):
                return True
        return False

# Java Code 
"""
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        return helper(m, n, s, p);
    }

    private boolean helper(int m, int n, String s, String p) {
        if (n == 0)  // simplest one
            return m == 0;

        // if 1st string gets exhausted
        // then if all remaining char in 'p' is "*", return true; else false
        if (m == 0) {
            for (int i = n - 1; i >= 0; i--) {
                if (p.charAt(i) != '*')
                    return false;
            }
            return true;
        }

        if (s.charAt(m - 1) == p.charAt(n - 1) || p.charAt(n - 1) == '?') {
            // match or '?': increment both
            if (helper(m - 1, n - 1, s, p))
                return true;
        } else if (p.charAt(n - 1) == '*') {
            // two choices:
            // 1) match zero chars (move pattern only)
            // 2) match one or more (move input only)
            if (helper(m, n - 1, s, p) || helper(m - 1, n, s, p))
                return true;
        }

        return false;
    }
}
"""
# C++ Code 
"""
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        return helper(m, n, s, p);
    }

private:
    bool helper(int m, int n, const string& s, const string& p) {
        if (n == 0)  // simplest one
            return m == 0;

        // if 1st string gets exhausted
        // then if all remaining char in 'p' is "*", return true; else false
        if (m == 0) {
            for (int i = n - 1; i >= 0; --i) {
                if (p[i] != '*')
                    return false;
            }
            return true;
        }

        if (s[m - 1] == p[n - 1] || p[n - 1] == '?') {
            // match or '?': increment both
            if (helper(m - 1, n - 1, s, p))
                return true;
        } else if (p[n - 1] == '*') {
            // two choices:
            // 1) match zero chars (move pattern only)
            // 2) match one or more (move input only)
            if (helper(m, n - 1, s, p) || helper(m - 1, n, s, p))
                return true;
        }

        return false;
    }
};
"""

# method 2: 
# memoisation
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        dp= [[-1 for j in range(n+1)] for i in range(m+1)]
        return self.helper(m, n, s, p,dp)
    
    def helper(self, m, n, s, p, dp):
        if n== 0:     # simplest one
            return m== 0
        # if 1st string get exhausted
        # then if all remainig char in 'p' is all "*" then return True else False
        if m==0:
            for i in range(n-1,-1,-1):
                if p[i]!= '*':
                    return False
            return True
        if dp[m][n]!= -1:
            return dp[m][n]
        if s[m-1]== p[n-1] or p[n-1]== '?':
            dp[m][n]= self.helper(m-1, n-1, s, p, dp)
        elif p[n-1]== '*':
            dp[m][n]= self.helper(m, n-1, s, p, dp) or self.helper(m-1, n, s, p, dp)
        else: # in all other cases simply return False
            dp[m][n]= False
        return dp[m][n] 

# Java Code 
"""
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        int[][] dp = new int[m + 1][n + 1];
        // initialize dp with -1
        for (int i = 0; i <= m; i++) {
            java.util.Arrays.fill(dp[i], -1);
        }
        return helper(m, n, s, p, dp);
    }

    private boolean helper(int m, int n, String s, String p, int[][] dp) {
        if (n == 0) // simplest one
            return m == 0;

        // if 1st string gets exhausted
        // then if all remaining chars in 'p' are '*', return True, else False
        if (m == 0) {
            for (int i = n - 1; i >= 0; i--) {
                if (p.charAt(i) != '*') return false;
            }
            return true;
        }

        if (dp[m][n] != -1)
            return dp[m][n] == 1;

        if (s.charAt(m - 1) == p.charAt(n - 1) || p.charAt(n - 1) == '?') {
            dp[m][n] = helper(m - 1, n - 1, s, p, dp) ? 1 : 0;
        } else if (p.charAt(n - 1) == '*') {
            dp[m][n] = (helper(m, n - 1, s, p, dp) || helper(m - 1, n, s, p, dp)) ? 1 : 0;
        } else {
            dp[m][n] = 0; // all other cases
        }

        return dp[m][n] == 1;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return helper(m, n, s, p, dp);
    }

private:
    bool helper(int m, int n, const string& s, const string& p, vector<vector<int>>& dp) {
        if (n == 0) // simplest one
            return m == 0;

        // if 1st string gets exhausted
        // then if all remaining chars in 'p' are '*', return True, else False
        if (m == 0) {
            for (int i = n - 1; i >= 0; i--) {
                if (p[i] != '*') return false;
            }
            return true;
        }

        if (dp[m][n] != -1)
            return dp[m][n] == 1;

        if (s[m - 1] == p[n - 1] || p[n - 1] == '?') {
            dp[m][n] = helper(m - 1, n - 1, s, p, dp) ? 1 : 0;
        } else if (p[n - 1] == '*') {
            dp[m][n] = (helper(m, n - 1, s, p, dp) || helper(m - 1, n, s, p, dp)) ? 1 : 0;
        } else {
            dp[m][n] = 0; // all other cases
        }

        return dp[m][n] == 1;
    }
};
"""
# method 3:
# Tabulation
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        dp= [[-1 for j in range(n+1)] for i in range(m+1)]
        # initailise with base cases
        dp[0][0]= True   # if n== 0 and m== 0
        for i in range(1,m+1):  # if n==0 and m!= 0 i.e 1st column
            dp[i][0]= False
        for i in range(1,n+1):  # if m==0
            flag= True
            for j in range(i-1,-1,-1):
                if p[j]!= '*':
                    flag= False
            dp[0][i]= flag
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1]== p[j-1] or p[j-1]== '?':
                    dp[i][j]= dp[i-1][j-1] 
                elif p[j-1]== '*':
                    dp[i][j]= dp[i][j-1] or dp[i-1][j] 
                else: # in all other cases simply return False
                    dp[i][j]= False
        return dp[m][n]


# Java Code 
"""
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];

        // initialise with base cases
        dp[0][0] = true;  // if n == 0 and m == 0

        for (int i = 1; i <= m; i++)  // if n == 0 and m != 0 i.e. 1st column
            dp[i][0] = false;

        for (int i = 1; i <= n; i++) {  // if m == 0
            boolean flag = true;
            for (int j = i - 1; j >= 0; j--) {
                if (p.charAt(j) != '*') {
                    flag = false;
                    break;
                }
            }
            dp[0][i] = flag;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                } else {
                    // in all other cases simply return false
                    dp[i][j] = false;
                }
            }
        }

        return dp[m][n];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        // initialise with base cases
        dp[0][0] = true;  // if n == 0 and m == 0

        for (int i = 1; i <= m; ++i)  // if n == 0 and m != 0 i.e. 1st column
            dp[i][0] = false;

        for (int i = 1; i <= n; ++i) {  // if m == 0
            bool flag = true;
            for (int j = i - 1; j >= 0; --j) {
                if (p[j] != '*') {
                    flag = false;
                    break;
                }
            }
            dp[0][i] = flag;
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == p[j - 1] || p[j - 1] == '?') {
                    dp[i][j] = dp[i - 1][j - 1];
                } else if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 1] || dp[i - 1][j];
                } else {
                    // in all other cases simply return false
                    dp[i][j] = false;
                }
            }
        }

        return dp[m][n];
    }
};
"""
# method 4:
# space optimised to O(n)
# for base case 0th row means previous and other than zero means curr
# so initialise based on the actual means of row and col 
# we have to initialise 'curr' for every row 
# so after every row make check condition

# and in for loop 'dp[i-1]' means pre and 'dp[i]' means curr 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        # initialising 1st row
        pre= [False for i in range(n +1)]
        pre[0]= True 
        for i in range(1,n+1):  # if m==0
            flag= True
            for j in range(i-1,-1,-1):
                if p[j]!= '*':
                    flag= False
            pre[i]= flag
            
        curr= [False for i in range(n +1)]
        for i in range(1, m+1):
            curr[0]= False  # zeroth col of each row should be False
            for j in range(1, n+1):
                if s[i-1]== p[j-1] or p[j-1]== '?':
                    curr[j]= pre[j-1] 
                elif p[j-1]== '*':
                    curr[j]= curr[j-1] or pre[j] 
                else: # in all other cases simply return False
                    curr[j]= False
            pre= curr.copy()
        return pre[n]


# Java Code 
"""
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        boolean[] pre = new boolean[n + 1]; // initializing 1st row
        pre[0] = true;

        for (int i = 1; i <= n; i++) {  // if m == 0
            boolean flag = true;
            for (int j = i - 1; j >= 0; j--) {
                if (p.charAt(j) != '*') {
                    flag = false;
                    break;
                }
            }
            pre[i] = flag;
        }

        boolean[] curr = new boolean[n + 1];
        for (int i = 1; i <= m; i++) {
            curr[0] = false;  // zeroth col of each row should be False
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == p.charAt(j - 1) || p.charAt(j - 1) == '?') {
                    curr[j] = pre[j - 1];
                } else if (p.charAt(j - 1) == '*') {
                    curr[j] = curr[j - 1] || pre[j];
                } else {
                    // in all other cases simply return False
                    curr[j] = false;
                }
            }
            pre = curr.clone();
        }

        return pre[n];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<bool> pre(n + 1, false); // initializing 1st row
        pre[0] = true;

        for (int i = 1; i <= n; ++i) {  // if m == 0
            bool flag = true;
            for (int j = i - 1; j >= 0; --j) {
                if (p[j] != '*') {
                    flag = false;
                    break;
                }
            }
            pre[i] = flag;
        }

        vector<bool> curr(n + 1, false);
        for (int i = 1; i <= m; ++i) {
            curr[0] = false;  // zeroth col of each row should be False
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == p[j - 1] || p[j - 1] == '?') {
                    curr[j] = pre[j - 1];
                } else if (p[j - 1] == '*') {
                    curr[j] = curr[j - 1] || pre[j];
                } else {
                    // in all other cases simply return False
                    curr[j] = false;
                }
            }
            pre = curr;
        }

        return pre[n];
    }
};
"""