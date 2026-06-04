
# Understanding the question : SA valid parenthesis is (), ((())) , ()(), ()(()) and so on as such.
# We need to find if the given string is a valid parenthesis, but here's the catch - the "*" - that can act both as ( and ) accoring to the requirement. 

# We will solve this using 2 approaches - Greedy and Recursion. 
# The recursion solution is mostly like a brute force, but the greedy is a 0(n) solution. However, we will see the optimal solution first this time,as it is more intuitive than the recursion solution .


# method 1: 
# By Recursion(TLE)
# time: O(3^n)
# when remove the condition for '*'. it will become the recursive sol for  '(' and ')' only.)
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # count the no of open paranthesis
        return self.check(s, 0, openCount)  # '0': start index from where we have to check.
    
    def check(self, s, ind, openCount):
        if openCount< 0:
            return False
        if ind== len(s):
            return openCount== 0
        if s[ind]== '(':
            openCount+= 1
        elif s[ind]== ')':
            if openCount <=0: return False
            openCount-= 1
        elif s[ind]== '*':  # we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
                            # and if anu of them return True then return True.
            return self.check(s, ind+1, openCount +1) or self.check(s, ind+1, openCount -1) or self.check(s, ind+1, openCount)
        return self.check(s, ind+1, openCount)    # if only either '(' or ')' comes at current index.


# Java
"""
class Solution {
    public boolean checkValidString(String s) {
        int openCount = 0;  // count the no of open parenthesis
        return check(s, 0, openCount);  // '0': start index from where we have to check.
    }

    public boolean check(String s, int ind, int openCount) {
        if (openCount < 0) return false;

        if (ind == s.length()) return openCount == 0;

        char ch = s.charAt(ind);

        if (ch == '(') {
            openCount += 1;
        } else if (ch == ')') {
            if (openCount <= 0) return false;
            openCount -= 1;
        } else if (ch == '*') {
            // we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
            // and if any of them return True then return True.
            return check(s, ind + 1, openCount + 1) ||
                   check(s, ind + 1, openCount - 1) ||
                   check(s, ind + 1, openCount);
        }

        return check(s, ind + 1, openCount);  // if only either '(' or ')' comes at current index.
    }
}
"""

# C++
"""
#include <string>
using namespace std;

class Solution {
public:
    bool checkValidString(string s) {
        int openCount = 0;  // count the no of open parenthesis
        return check(s, 0, openCount);  // '0': start index from where we have to check.
    }

    bool check(const string& s, int ind, int openCount) {
        if (openCount < 0) return false;

        if (ind == s.length()) return openCount == 0;

        char ch = s[ind];

        if (ch == '(') {
            openCount += 1;
        } else if (ch == ')') {
            if (openCount <= 0) return false;
            openCount -= 1;
        } else if (ch == '*') {
            // we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
            // and if any of them return True then return True.
            return check(s, ind + 1, openCount + 1) ||
                   check(s, ind + 1, openCount - 1) ||
                   check(s, ind + 1, openCount);
        }

        return check(s, ind + 1, openCount);  // if only either '(' or ')' comes at current index.
    }
};
"""

# Method 2 :
# optimising the above solution
# time= space= O(n^2) 
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # count the no of open paranthesis
        dp= [[-1 for i in range(len(s) +1)]for i in range(len(s) +1)]
        return self.check(s, 0, openCount, dp)  # '0': start index from where we have to check.
    
    def check(self, s, ind, openCount, dp):
        if openCount< 0:
            return False
        if ind== len(s):
            return openCount== 0
        if dp[ind][openCount] != -1:
            return dp[ind][openCount]
        if s[ind]== '(':
            dp[ind][openCount]= self.check(s, ind+1, openCount +1, dp)
        elif s[ind]== ')':
            if openCount <=0:
                return False
            dp[ind][openCount]= self.check(s, ind+1, openCount -1, dp)
        elif s[ind]== '*':  # we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
                          # and if anu of them return True then return True.
            dp[ind][openCount]= self.check(s, ind+1, openCount +1, dp) or self.check(s, ind+1, openCount -1, dp) or self.check(s, ind+1, openCount, dp)
        return dp[ind][openCount]
    
# Java
"""
class Solution {
    public boolean checkValidString(String s) {
        int n = s.length();
        int[][] dp = new int[n + 1][n + 1];
        
        // initialize all to -1
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                dp[i][j] = -1;
            }
        }

        int openCount = 0;  // count the no of open parenthesis
        return check(s, 0, openCount, dp);  // '0': start index from where we have to check.
    }

    public boolean check(String s, int ind, int openCount, int[][] dp) {
        if (openCount < 0) return false;
        if (ind == s.length()) return openCount == 0;

        if (dp[ind][openCount] != -1) return dp[ind][openCount] == 1;

        char ch = s.charAt(ind);

        if (ch == '(') {
            dp[ind][openCount] = check(s, ind + 1, openCount + 1, dp) ? 1 : 0;
        } else if (ch == ')') {
            if (openCount <= 0) return false;
            dp[ind][openCount] = check(s, ind + 1, openCount - 1, dp) ? 1 : 0;
        } else if (ch == '*') {
            // we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
            // and if any of them return True then return True.
            boolean res = check(s, ind + 1, openCount + 1, dp) ||
                          check(s, ind + 1, openCount - 1, dp) ||
                          check(s, ind + 1, openCount, dp);
            dp[ind][openCount] = res ? 1 : 0;
        } else {
            dp[ind][openCount] = check(s, ind + 1, openCount, dp) ? 1 : 0;
        }

        return dp[ind][openCount] == 1;
    }
}
"""


# C++
"""
#include <string>
#include <vector>
using namespace std;

class Solution {
public:
    bool checkValidString(string s) {
        int n = s.length();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, -1));
        int openCount = 0;  // count the no of open parenthesis
        return check(s, 0, openCount, dp);  // '0': start index from where we have to check.
    }

    bool check(string& s, int ind, int openCount, vector<vector<int>>& dp) {
        if (openCount < 0) return false;
        if (ind == s.length()) return openCount == 0;

        if (dp[ind][openCount] != -1) return dp[ind][openCount] == 1;

        char ch = s[ind];

        if (ch == '(') {
            dp[ind][openCount] = check(s, ind + 1, openCount + 1, dp) ? 1 : 0;
        } else if (ch == ')') {
            if (openCount <= 0) return false;
            dp[ind][openCount] = check(s, ind + 1, openCount - 1, dp) ? 1 : 0;
        } else if (ch == '*') {
            // we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
            // and if any of them return True then return True.
            bool res = check(s, ind + 1, openCount + 1, dp) ||
                       check(s, ind + 1, openCount - 1, dp) ||
                       check(s, ind + 1, openCount, dp);
            dp[ind][openCount] = res ? 1 : 0;
        } else {
            dp[ind][openCount] = check(s, ind + 1, openCount, dp) ? 1 : 0;
        }

        return dp[ind][openCount] == 1;
    }
};
"""


# Method  3: 
"""
Instead of maintaining a massive tree of numbers, we just maintain these two integers 
(min_open and max_open) as a dynamic interval window: [min_open, max_open].

min_open: The absolute minimum number of open brackets you could have if you were aggressive about closing brackets (treating asterisks * as ) whenever possible).
max_open: The absolute maximum number of open brackets you could have if you were aggressive about opening brackets (treating asterisks * as ( whenever possible).

The Rules of the Window
As we scan each character in the string, our window changes based on simple rules:
1. If char == '(': Both boundaries must increase.
min_open += 1
max_open += 1

2. If char == ')': Both boundaries must decrease.
min_open -= 1
max_open -= 1

3. If char == '*': The wildcard gives choices! It can decrease our minimum (treated as )) or increase our maximum (treated as ().
min_open -= 1
max_open += 1

The Two Vital Course Corrections (The "Greedy" Part)
1. Safety Check 1 (Too Many Closing Brackets): If at any point max_open < 0, it means even if we treated every single asterisk as an open bracket, 
we still don't have enough ( to match the overwhelming amount of ). The string is instantly invalid.
2. Safety Check 2 (Floor Guard): min_open can never realistically drop below 0. 
If min_open becomes negative, it just means we treated too many wildcards as ) early on. 
We simply reset min_open = 0 to assume those extra wildcards were used as empty strings "" instead.


TIME COMPLEXITY ANALYSIS :
-> 0(n) for iterating through the array.

SPACE COMPLEXITY : 
-> O(1) for the stack spaces.
"""


# PYTHON : 


class Solution:
    def checkValidString(self, s: str) -> bool:
        # min_open tracks the minimum possible unmatched '(' we could have
        # max_open tracks the maximum possible unmatched '(' we could have
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            elif char == '*':
                # If '*' is used as ')', min_open decreases
                # If '*' is used as '(', max_open increases
                # (If used as "", min_open/max_open stay steady, which is handled implicitly by the range expansion)
                min_open -= 1
                max_open += 1
                
            # CRITICAL CHECK 1: If max_open drops below 0, there are too many ')'
            # No amount of asterisks can save this string.
            if max_open < 0:
                return False
                
            # CRITICAL CHECK 2: min_open cannot step below zero. 
            # You can't have a negative balance of open brackets. If it dips negative,
            # it just means we shouldn't have counted some '*' as ')' yet. Reset to 0.
            if min_open < 0:
                min_open = 0
                
        # At the end of the string, if 0 falls perfectly inside our possible 
        # range of unmatched open brackets [min_open, max_open], then the string is valid.
        # Since we guard min_open to never go below 0, we just check if min_open reached exactly 0.
        return min_open == 0
