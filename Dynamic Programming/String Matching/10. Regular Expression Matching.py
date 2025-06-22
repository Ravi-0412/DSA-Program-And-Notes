# Basic: 

# only difference from "44. Wildcard Matching" is the meaning of "*".
# in "44. Wildcard Matching", "*" can match to any sequence of char , doesn't depend on the pre char before "* but in this Q
# "*" can 1) either match to zero char or 2) one or more char when characters in string is same char as char before "*" in pattern. 
# just like we write the regular expression.

# 'a*' means: ["", a, aa, aaa, aaaa, ....], this can match to zero or more a 
# simlarly '.*' means: ["", ., .., ..., & so on] . 
# Given: ".*" means "zero or more (*) of any character (.)".

# for understanding better draw tree of pattern comparing with sring.


# Method 1: 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n= len(s), len(p)
        return self.helper(m, n, s, p)
    
    def helper(self, m, n, s, p):
        if n== 0:
            return m== 0
        if m== 0: # n!= 0
            # then remaining char of 'p' must be either : 1) s[0]*. Since matches '0' or more prev char  or 2) .* 
            # Other than these two all combination will be invalid.
            for i in range(n-1, -1, -1):
                if i== n-1 and p[i]!= "*":
                    # Last char must be '*'.
                    return False
                elif p[i]!= (s[0] or '.'):
                    return False
            return True 

        if s[m-1]== p[n-1] or p[n-1]== '.':  # decr both indexes by '1'
            if self.helper(m-1, n-1, s, p):
                return True
        elif p[n-1]== '*':
            if n-2>= 0 and (s[m-1]== p[n-2] or p[n-2]=='.') :  
                if self.helper(m, n-1, s, p) or self.helper(m-1, n, s, p):
                    return True
        return False

<<<<<<< HEAD
# Java Code 
"""
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        return helper(m, n, s, p);
    }

    private boolean helper(int m, int n, String s, String p) {
        if (n == 0)
            return m == 0;

        if (m == 0) {  // n != 0
            // then remaining char of 'p' must be either : 1) s[0]*. Since matches '0' or more prev char  or 2) .*
            // Other than these two all combinations will be invalid.
            for (int i = n - 1; i >= 0; i--) {
                if (i == n - 1 && p.charAt(i) != '*')
                    return false;  // Last char must be '*'
                if (i % 2 == 1) continue;  // pattern characters at odd indices
                if (i == 0 || (p.charAt(i) != s.charAt(0) && p.charAt(i) != '.'))
                    return false;
            }
            return true;
        }

        if (s.charAt(m - 1) == p.charAt(n - 1) || p.charAt(n - 1) == '.') {
            return helper(m - 1, n - 1, s, p);
        } else if (p.charAt(n - 1) == '*') {
            if (n - 2 >= 0 && (s.charAt(m - 1) == p.charAt(n - 2) || p.charAt(n - 2) == '.')) {
                return helper(m, n - 1, s, p) || helper(m - 1, n, s, p);
            }
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
        int m = s.length(), n = p.length();
        return helper(m, n, s, p);
    }

private:
    bool helper(int m, int n, const string& s, const string& p) {
        if (n == 0)
            return m == 0;

        if (m == 0) {  // n != 0
            // then remaining char of 'p' must be either : 1) s[0]*. Since matches '0' or more prev char  or 2) .*
            // Other than these two all combinations will be invalid.
            for (int i = n - 1; i >= 0; --i) {
                if (i == n - 1 && p[i] != '*')
                    return false;  // Last char must be '*'
                if (i % 2 == 1) continue;
                if (i == 0 || (p[i] != s[0] && p[i] != '.'))
                    return false;
            }
            return true;
        }

        if (s[m - 1] == p[n - 1] || p[n - 1] == '.') {
            return helper(m - 1, n - 1, s, p);
        } else if (p[n - 1] == '*') {
            if (n - 2 >= 0 && (s[m - 1] == p[n - 2] || p[n - 2] == '.')) {
                return helper(m, n - 1, s, p) || helper(m - 1, n, s, p);
            }
        }

        return false;
    }
};
"""
# Memoised this later 

=======
>>>>>>> a40de18 (verified Binary Search and DP)

# Method 2: 
# base case when i>= len(s) and j is not out of bond will get handled by the case when we don't use the "*" and return false simply.
# take this and check.1) s= a, p= a*b*c(or .*) and let i out of bound by matching with "*" and j still at '0' 
# we will get true by taking the path "don't use '*' "

# if no "*" then will get handled by "return 'False' "

# simle thing keep in mind: if "*" comes then we have two choice 1) either skip it simply(incr 'j' by 2) or
# 2) use "*" again and again if there is match. if not match then simply return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(0, 0, s, p)
    
    def dfs(self, i, j, s, p):
        if j>= len(p):  # then 'i' must be also out of bound
            return i>= len(s)
        # check if char is matching and store them in variable instead of using 'if' condition again and again
        match= i< len(s) and (s[i]== p[j] or p[j]=='.')   # in this there will be match 
        # check if p[j+1]== "*"
        if (j+1) < len(p) and p[j+1]== "*":
            return (self.dfs(i, j+2, s, p) or                 # don't use '*'
                   (match and self.dfs(i+1, j, s, p)))   # if match then use "*" further again and again
        if match:  # same as wildcard
            return self.dfs(i+1, j+1, s, p)
        # in all other cases return False
        return False

<<<<<<< HEAD
# Brute force of above one but got submitted.
# here handled the base case of "i>= len(s)" clearly 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(0, 0, s, p)
    
    def dfs(self, i, j, s, p):
        if j>= len(p):  # then 'i' must be also out of bound
            return i>= len(s)
        # if i>= len(s) then only chance if we can get True if there is alternate '*' and
        # we have to skip the "*" and for that 'j+1' < len(s).
        if i>= len(s):  
            return j+1 < len(p) and p[j+1]== "*" and self.dfs(i, j+2, s, p)
        # check if char is matching and store them in variable instead of using 'if' condition again and again
        match= i< len(s) and (s[i]== p[j] or p[j]=='.')   # in this there will be match 
        # check if p[j+1]== "*"
        if (j+1) < len(p) and p[j+1]== "*":
            return (self.dfs(i, j+2, s, p) or                 # don't use '*'
                   (match and self.dfs(i+1, j, s, p)))   # if match then use "*" further again and again
        if match:  # same as wildcard
            return self.dfs(i+1, j+1, s, p)
        # in all other cases return False
        return False

# Java Code 
"""
class Solution {
    public boolean isMatch(String s, String p) {
        return dfs(0, 0, s, p);
    }

    private boolean dfs(int i, int j, String s, String p) {
        if (j >= p.length())  // then 'i' must also be out of bound
            return i >= s.length();

        // check if char is matching and store in variable instead of using 'if' again and again
        boolean match = i < s.length() && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.');

        // check if p[j+1] == "*"
        if ((j + 1) < p.length() && p.charAt(j + 1) == '*') {
            return dfs(i, j + 2, s, p) ||  // don't use '*'
                   (match && dfs(i + 1, j, s, p));  // if match then use '*' further again and again
        }

        if (match)  // same as wildcard
            return dfs(i + 1, j + 1, s, p);

        // in all other cases return False
        return false;
    }
}
// Brute force of the above one but got submitted.
// here handled the base case of "i >= len(s)" clearly
class Solution {
    public boolean isMatch(String s, String p) {
        return dfs(0, 0, s, p);
    }

    private boolean dfs(int i, int j, String s, String p) {
        if (j >= p.length())  // then 'i' must be also out of bound
            return i >= s.length();

        // if i >= len(s) then only chance we can get True is if there is alternate '*' 
        // and we have to skip the '*' and for that j+1 < len(p)
        if (i >= s.length())
            return (j + 1) < p.length() && p.charAt(j + 1) == '*' && dfs(i, j + 2, s, p);

        // check if char is matching and store in variable instead of using 'if' again and again
        boolean match = s.charAt(i) == p.charAt(j) || p.charAt(j) == '.';

        // check if p[j+1] == "*"
        if ((j + 1) < p.length() && p.charAt(j + 1) == '*') {
            return dfs(i, j + 2, s, p) ||  // don't use '*'
                   (match && dfs(i + 1, j, s, p));  // if match then use '*' further again and again
        }

        if (match)  // same as wildcard
            return dfs(i + 1, j + 1, s, p);

        // in all other cases return False
        return false;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    bool isMatch(string s, string p) {
        return dfs(0, 0, s, p);
    }

private:
    bool dfs(int i, int j, const string& s, const string& p) {
        if (j >= p.size())  // then 'i' must also be out of bound
            return i >= s.size();

        // check if char is matching and store in variable instead of using 'if' again and again
        bool match = i < s.size() && (s[i] == p[j] || p[j] == '.');

        // check if p[j+1] == "*"
        if ((j + 1) < p.size() && p[j + 1] == '*') {
            return dfs(i, j + 2, s, p) ||  // don't use '*'
                   (match && dfs(i + 1, j, s, p));  // if match then use '*' further again and again
        }

        if (match)  // same as wildcard
            return dfs(i + 1, j + 1, s, p);

        // in all other cases return False
        return false;
    }
};
// Brute force of the above one but got submitted.
// here handled the base case of "i >= len(s)" clearly
class Solution {
public:
    bool isMatch(string s, string p) {
        return dfs(0, 0, s, p);
    }

private:
    bool dfs(int i, int j, const string& s, const string& p) {
        if (j >= p.size())  // then 'i' must also be out of bound
            return i >= s.size();

        // if i >= len(s) then only chance we can get True is if there is alternate '*' 
        // and we have to skip the '*' and for that j+1 < len(p)
        if (i >= s.size())
            return (j + 1) < p.size() && p[j + 1] == '*' && dfs(i, j + 2, s, p);

        // check if char is matching and store in variable instead of using 'if' again and again
        bool match = (s[i] == p[j] || p[j] == '.');

        // check if p[j+1] == "*"
        if ((j + 1) < p.size() && p[j + 1] == '*') {
            return dfs(i, j + 2, s, p) ||  // don't use '*'
                   (match && dfs(i + 1, j, s, p));  // if match then use '*' further again and again
        }

        if (match)  // same as wildcard
            return dfs(i + 1, j + 1, s, p);

        // in all other cases return False
        return false;
    }
};
"""
=======
# Method 3: 
>>>>>>> a40de18 (verified Binary Search and DP)
# memoised one
# time: O(m*n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp= [[-1 for j in range(len(p)+1)] for i in range(len(s)+1)]
        return self.dfs(0, 0, s, p, dp)
    
    def dfs(self, i, j, s, p, dp):
        if j>= len(p):  # then 'i' must be also out of bound
            return i>= len(s)
        # if i>= len(s) then only chance if we can get True if there is alternate '*' and
        # we have to skip the "*" and for that 'j+1' < len(s).
        if i>= len(s):  
            return j+1 < len(p) and p[j+1]== "*" and self.dfs(i, j+2, s, p, dp)
        if dp[i][j]!= -1:
            return dp[i][j]
        # check if char is matching and store them in variable instead of using 'if' condition again and again
        match= i< len(s) and (s[i]== p[j] or p[j]=='.')   # in this there will be match 
        # check if p[j+1]== "*"
        if (j+1) < len(p) and p[j+1]== "*":
            dp[i][j]= (self.dfs(i, j+2, s, p, dp) or                 # don't use '*'
                   (match and self.dfs(i+1, j, s, p, dp)))   # if match then use "*" further again and again
            return dp[i][j]
        if match:  # same as wildcard
            dp[i][j]= self.dfs(i+1, j+1, s, p, dp)
            return dp[i][j]
        dp[i][j]= False
        return dp[i][j]
# Java Code 
"""
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        Boolean[][] dp = new Boolean[m + 1][n + 1];
        return dfs(0, 0, s, p, dp);
    }

    private boolean dfs(int i, int j, String s, String p, Boolean[][] dp) {
        if (j >= p.length())  // then 'i' must be also out of bound
            return i >= s.length();

        // if i >= len(s) then only chance we can get True if there is alternate '*' and
        // we have to skip the '*' and for that j+1 < len(p)
        if (i >= s.length()) {
            return (j + 1 < p.length()) && p.charAt(j + 1) == '*' && dfs(i, j + 2, s, p, dp);
        }

        if (dp[i][j] != null) return dp[i][j];

        // check if char is matching and store it instead of using 'if' again and again
        boolean match = s.charAt(i) == p.charAt(j) || p.charAt(j) == '.';

        // check if p[j+1] == '*'
        if ((j + 1) < p.length() && p.charAt(j + 1) == '*') {
            return dp[i][j] = dfs(i, j + 2, s, p, dp) || (match && dfs(i + 1, j, s, p, dp));
        }

        if (match) {
            return dp[i][j] = dfs(i + 1, j + 1, s, p, dp);
        }

        return dp[i][j] = false;
    }
}
"""
# C++ Code 
"""
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size(), n = p.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return dfs(0, 0, s, p, dp);
    }

private:
    bool dfs(int i, int j, const string& s, const string& p, vector<vector<int>>& dp) {
        if (j >= p.size())  // then 'i' must be also out of bound
            return i >= s.size();

        // if i >= len(s) then only chance we can get True if there is alternate '*'
        // and we have to skip the '*' and for that j+1 < len(p)
        if (i >= s.size()) {
            return (j + 1 < p.size()) && p[j + 1] == '*' && dfs(i, j + 2, s, p, dp);
        }

        if (dp[i][j] != -1) return dp[i][j];

        // check if char is matching and store in variable
        bool match = s[i] == p[j] || p[j] == '.';

        // check if p[j+1] == '*'
        if ((j + 1) < p.size() && p[j + 1] == '*') {
            return dp[i][j] = dfs(i, j + 2, s, p, dp) || (match && dfs(i + 1, j, s, p, dp));
        }

        if (match) {
            return dp[i][j] = dfs(i + 1, j + 1, s, p, dp);
        }

        return dp[i][j] = false;
    }
};
"""


# Method 4:
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        # dp[i][j] will be True if s[i:] matches p[j:]
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Base case: both strings are empty
        dp[n][m] = True

        # Fill the table in reverse order
        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                # check if char is matching and store them in variable instead of using 'if' condition again and again
                match = i < n and (s[i] == p[j] or p[j] == '.')

                # check if p[j+1] == "*"
                if (j + 1) < m and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])  # don't use '*' OR use '*'
                elif match:  # same as wildcard
                    dp[i][j] = dp[i + 1][j + 1]
                # in all other cases dp[i][j] is already False

        return dp[0][0]


# Method 5: 
# Brute force of method 2 but got submitted.
# here handled the base case of "i>= len(s)" clearly 
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.dfs(0, 0, s, p)
    
    def dfs(self, i, j, s, p):
        if j>= len(p):  # then 'i' must be also out of bound
            return i>= len(s)
        # if i>= len(s) then only chance if we can get True if there is alternate '*' and
        # we have to skip the "*" and for that 'j+1' < len(s).
        if i>= len(s):  
            return j+1 < len(p) and p[j+1]== "*" and self.dfs(i, j+2, s, p)
        # check if char is matching and store them in variable instead of using 'if' condition again and again
        match= i< len(s) and (s[i]== p[j] or p[j]=='.')   # in this there will be match 
        # check if p[j+1]== "*"
        if (j+1) < len(p) and p[j+1]== "*":
            return (self.dfs(i, j+2, s, p) or                 # don't use '*'
                   (match and self.dfs(i+1, j, s, p)))   # if match then use "*" further again and again
        if match:  # same as wildcard
            return self.dfs(i+1, j+1, s, p)
        # in all other cases return False
        return False





