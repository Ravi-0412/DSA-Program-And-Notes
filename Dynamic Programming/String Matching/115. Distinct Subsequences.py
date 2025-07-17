# Method 1: 

# in string matching you will come across only two cases i.e 'matched' and 'not matched' always 
# for base case in string matching algo, base cases will be when :
# 1) when 2nd string becomes empty(2nd index becomes zero) 2) when first string becomes empty(1st index becomes=0) and  

# easy only just slight modifiction in lcs
# modification: 1) in case of char matches then we have two choices either include that char into the ans or 
# search for same char at different index in 's'
# 2) in case doesn't matches then search for char in 's' at different index i.e doesn't decr the index of 't' 
# as we have to find the no of subsequences that's it

# Note: instead of using indexes we can also do by slicing like i used to do seeing the Q.
# and in case of slicing use dictionary to memoise the solution.

# time: O(2^m *2^n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n= len(s), len(t)
        return self.helper(m, n, s, t)
    
    def helper(self,m,n,s,t):
        if n== 0:  # it means we have found a match of all char in 't'
            return 1
        if m==0: # n!= 0 and m==0 means matched not found
            return 0
        matched,unMatched= 0,0
        if s[m-1]== t[n-1]:
            matched= self.helper(m-1, n-1, s, t) + self.helper(m-1, n, s, t)    #if you don't want to include the current matched one in ans.  
                                                                # so finding the another occur of same char at different index in given string 's'
        else:  # search for same char of 't' in 's' at different index
            unMatched= self.helper(m-1, n, s, t)
        return matched+ unMatched 

# Java Code 
"""
class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        return helper(m, n, s, t);
    }

    public int helper(int m, int n, String s, String t) {
        if (n == 0)  // it means we have found a match of all char in 't'
            return 1;
        if (m == 0)  // n != 0 and m == 0 means match not found
            return 0;

        int matched = 0, unMatched = 0;

        if (s.charAt(m - 1) == t.charAt(n - 1)) {
            matched = helper(m - 1, n - 1, s, t) + helper(m - 1, n, s, t);  // include or skip current matched char
        } else {
            unMatched = helper(m - 1, n, s, t);  // search for same char of 't' in 's' at different index
        }

        return matched + unMatched;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size(), n = t.size();
        return helper(m, n, s, t);
    }

    int helper(int m, int n, const string& s, const string& t) {
        if (n == 0)  // it means we have found a match of all char in 't'
            return 1;
        if (m == 0)  // n != 0 and m == 0 means match not found
            return 0;

        int matched = 0, unMatched = 0;

        if (s[m - 1] == t[n - 1]) {
            matched = helper(m - 1, n - 1, s, t) + helper(m - 1, n, s, t);  // include or skip current matched char
        } else {
            unMatched = helper(m - 1, n, s, t);  // search for same char of 't' in 's' at different index
        }

        return matched + unMatched;
    }
};
"""

# method 2:
# Shorter way of writing Method 1
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n= len(s), len(t)
        return self.helper(m, n, s, t)
    
    def helper(self,m,n,s,t):
        if n== 0:
            return 1
        if m==0:
            return 0
        if s[m-1]== t[n-1]:
            return self.helper(m-1, n-1, s, t) + self.helper(m-1, n, s, t)    #if you don't want to include the current matched one in ans. 
                                                                # so finding the another occur of same char at different index in given string 's'
        # search for same char of 't' in 's' at different index
        return self.helper(m-1, n, s, t)

# Java Code 
"""
class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        return helper(m, n, s, t);
    }

    public int helper(int m, int n, String s, String t) {
        if (n == 0)
            return 1;  // it means we have found a match of all char in 't'
        if (m == 0)
            return 0;  // n != 0 and m == 0 means match not found

        if (s.charAt(m - 1) == t.charAt(n - 1)) {
            return helper(m - 1, n - 1, s, t) + helper(m - 1, n, s, t);  
            // if you don't want to include the current matched one in ans.
            // so finding another occur of same char at different index in given string 's'
        }

        // search for same char of 't' in 's' at different index
        return helper(m - 1, n, s, t);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length(), n = t.length();
        return helper(m, n, s, t);
    }

    int helper(int m, int n, const string& s, const string& t) {
        if (n == 0)
            return 1;  // it means we have found a match of all char in 't'
        if (m == 0)
            return 0;  // n != 0 and m == 0 means match not found

        if (s[m - 1] == t[n - 1]) {
            return helper(m - 1, n - 1, s, t) + helper(m - 1, n, s, t);  
            // if you don't want to include the current matched one in ans.
            // so finding another occur of same char at different index in given string 's'
        }

        // search for same char of 't' in 's' at different index
        return helper(m - 1, n, s, t);
    }
};
"""

# Method 3: 
# memoization
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n= len(s), len(t)
        dp= [[-1 for j in range(n+1)] for i in range(m+1)]
        return self.helper(m, n, s, t, dp)
    
    def helper(self,m,n,s,t,dp):
        if n== 0:
            return 1
        if m==0:
            return 0
        if dp[m][n]!= -1:
            return dp[m][n]
        if s[m-1]== t[n-1]:
            dp[m][n]= self.helper(m-1, n-1, s, t,dp) + self.helper(m-1, n, s, t,dp)    
        else:
            dp[m][n]= self.helper(m-1, n, s, t, dp)
        return dp[m][n]


# Java Code 
"""
class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            java.util.Arrays.fill(dp[i], -1);
        }

        return helper(m, n, s, t, dp);
    }

    private int helper(int m, int n, String s, String t, int[][] dp) {
        if (n == 0)
            return 1;
        if (m == 0)
            return 0;
        if (dp[m][n] != -1)
            return dp[m][n];

        if (s.charAt(m - 1) == t.charAt(n - 1))
            dp[m][n] = helper(m - 1, n - 1, s, t, dp) + helper(m - 1, n, s, t, dp); // include and exclude
        else
            dp[m][n] = helper(m - 1, n, s, t, dp);

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
    int numDistinct(string s, string t) {
        int m = s.length(), n = t.length();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return helper(m, n, s, t, dp);
    }

private:
    int helper(int m, int n, const string& s, const string& t, vector<vector<int>>& dp) {
        if (n == 0)
            return 1;
        if (m == 0)
            return 0;
        if (dp[m][n] != -1)
            return dp[m][n];

        if (s[m - 1] == t[n - 1])
            dp[m][n] = helper(m - 1, n - 1, s, t, dp) + helper(m - 1, n, s, t, dp); // include and exclude
        else
            dp[m][n] = helper(m - 1, n, s, t, dp); 

        return dp[m][n];
    }
};
"""
# Method 4:
# Tabulation
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n= len(s), len(t)
        dp= [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):   # i was doing from 1 to 'm+1'. null to null is also a match
            dp[i][0]= 1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]== t[j-1]:
                    dp[i][j]= dp[i-1][j-1] + dp[i-1][j]   
                else:
                    dp[i][j]= dp[i-1][j] 
        return dp[m][n]

# Java Code 
"""
class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        int[][] dp = new int[m + 1][n + 1];

        // i was doing from 1 to 'm+1'. null to null is also a match
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j];
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
    int numDistinct(string s, string t) {
        int m = s.size(), n = t.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        // i was doing from 1 to 'm+1'. null to null is also a match
        for (int i = 0; i <= m; ++i) {
            dp[i][0] = 1;
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (s[i - 1] == t[j - 1])
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j];
            }
        }

        return dp[m][n];
    }
};
"""
# method 5:
# optimise space to O(n)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1  # Empty t can always be formed
        
        for c in s:
            for j in range(len(t), 0, -1):  # Reverse to avoid overwriting
                if c == t[j - 1]:
                    dp[j] += dp[j - 1]
        
        return dp[len(t)]

# Java Code 
"""
class Solution {
    public int numDistinct(String s, String t) {
        int[] dp = new int[t.length() + 1];
        dp[0] = 1;  // Empty t can always be formed

        for (char c : s.toCharArray()) {
            for (int j = t.length(); j > 0; j--) {  // Reverse to avoid overwriting
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
    int numDistinct(string s, string t) {
        vector<int> dp(t.size() + 1, 0);
        dp[0] = 1;  // Empty t can always be formed

        for (char c : s) {
            for (int j = t.size(); j > 0; --j) {  // Reverse to avoid overwriting
                if (c == t[j - 1]) {
                    dp[j] += dp[j - 1];
                }
            }
        }

        return dp[t.size()];
    }
};
"""

# Related Q:
# 1) 2222. Number of Ways to Select Buildings.
# Ans: There will be only two possibility i.e '101' and '010' so Q reduces to
# find the number of distinct subsequences of '101' and '010' in string and add them.
