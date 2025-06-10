# checking valid paranthesis if it contains only two types of string i.e: '(' and ')'.

# In this type of question, try to do by taking count of '(' rather than pushing and poping.

class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # will count the no of open paranthesis
        for i  in range(len(s)):
            if s[i]== '(':
                openCount+= 1
            else:
                openCount-= 1
            if openCount < 0:   # '(' is less than ')'.
                return False
        return openCount== 0

# can do the same logic by Recursion also.
def isValid(self, i, s, open):
        if open < 0:
            return False
        if i== len(s):
            return open== 0
        if s[i]== '(':
            open+= 1
        else:
            open-= 1
            
        return self.isValid(i+1, s, open)


# actual Q
# method 1: by Recursion(TLE)
# time: O(3^n)
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # count the no of open paranthesis
        return self.check(s, 0, openCount)  # '0': start index from where we have to check.
    
    def check(self, s, ind, openCount):
        if openCount < 0:
            return False
        if ind== len(s):
            return openCount== 0
        if s[ind]== '(':
            return self.check(s, ind+1, openCount +1)
        elif s[ind]== ')':
            if openCount <=0:
                return False
            return self.check(s, ind+1, openCount -1)
        elif s[ind]== '*':  # we have three choices either treat this as 1) '('  2) ')' or 3) empty string. 
                          # and if anu of them return True then return True.
            return self.check(s, ind+1, openCount +1) or self.check(s, ind+1, openCount -1) or self.check(s, ind+1, openCount)

# OR 
# in both of the solution(above and this one, remove the condition for '*'. it will become the recursive sol for  '(' and ')' only.)
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

# optimising the above solution
# time= space= O(n^2) 
class Solution:
    def checkValidString(self, s: str) -> bool:
        openCount= 0  # count the no of open paranthesis
        dp= [[-1 for i in range(len(s) +1)]for i in range(len(s) +1)]
        return self.check(s, 0, openCount, dp)  # '0': start index from where we have to check.
    
    # @lru_cache(None)   # or simply write this one line to memoise. but not a good way. 
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
    

# METHOD 2: optimising the above one to O(n)
# time= O(n), space= O(1)
class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin, openMax= 0, 0   # max and min no of ')' that can be accomodated.
        for i in range(len(s)):
            if s[i]== '(':
                openMinv += 1
                openMaxv += 1
            elif s[i]== ')':
                openMin -= 1
                openMax -= 1
            elif s[i]== '*':
                openMin -= 1    # 'if '*' behaves as ')'. means one '(' is accomodated by '*'.
                openMax += 1    # 'if '*' behaves as '('. means one more matching of '(' is increased.

            if openMax < 0:
                return False
            openMin= max(openMin, 0)    # openMin can't be negative.(if negative make= 0)
        return openMin== 0    # we are not waiting for anymore ')'.


# Note: read solutions in sheet and also few comments under that.


# Java Code 
"""
// METHOD 1: Greedy (Left to Right Scan)
class Solution {
    public boolean checkValidString(String s) {
        int openCount = 0; // will count the no of open paranthesis
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                openCount++;
            } else {
                openCount--;
            }
            if (openCount < 0) { // '(' is less than ')'.
                return false;
            }
        }
        return openCount == 0;
    }
}


// METHOD 2: Pure Recursion (TLE)
class Solution {
    public boolean checkValidString(String s) {
        return check(s, 0, 0); // '0': start index from where we have to check.
    }

    private boolean check(String s, int ind, int openCount) {
        if (openCount < 0) return false;
        if (ind == s.length()) return openCount == 0;

        if (s.charAt(ind) == '(') {
            return check(s, ind + 1, openCount + 1);
        } else if (s.charAt(ind) == ')') {
            if (openCount <= 0) return false;
            return check(s, ind + 1, openCount - 1);
        } else if (s.charAt(ind) == '*') { // three choices: treat as '(', ')' or empty
            return check(s, ind + 1, openCount + 1)
                || check(s, ind + 1, openCount - 1)
                || check(s, ind + 1, openCount);
        }
        return check(s, ind + 1, openCount); // if only either '(' or ')' comes at current index
    }
}


// METHOD 3: Recursion with Memoization
class Solution {
    public boolean checkValidString(String s) {
        int[][] dp = new int[s.length() + 1][s.length() + 1];
        for (int[] row : dp) Arrays.fill(row, -1);
        return check(s, 0, 0, dp);
    }

    private boolean check(String s, int ind, int openCount, int[][] dp) {
        if (openCount < 0) return false;
        if (ind == s.length()) return openCount == 0;
        if (dp[ind][openCount] != -1) return dp[ind][openCount] == 1;

        boolean ans = false;
        if (s.charAt(ind) == '(') {
            ans = check(s, ind + 1, openCount + 1, dp);
        } else if (s.charAt(ind) == ')') {
            if (openCount <= 0) return false;
            ans = check(s, ind + 1, openCount - 1, dp);
        } else if (s.charAt(ind) == '*') {
            ans = check(s, ind + 1, openCount + 1, dp)
                || check(s, ind + 1, openCount - 1, dp)
                || check(s, ind + 1, openCount, dp);
        } else {
            ans = check(s, ind + 1, openCount, dp);
        }
        dp[ind][openCount] = ans ? 1 : 0;
        return ans;
    }
}


// METHOD 4: Greedy (Optimized O(n))
class Solution {
    public boolean checkValidString(String s) {
        int openMin = 0, openMax = 0; // max and min no of ')' that can be accomodated
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                openMin += 1;
                openMax += 1;
            } else if (s.charAt(i) == ')') {
                openMin -= 1;
                openMax -= 1;
            } else if (s.charAt(i) == '*') {
                openMin -= 1; // if '*' behaves as ')'
                openMax += 1; // if '*' behaves as '('
            }

            if (openMax < 0) return false;
            openMin = Math.max(openMin, 0); // openMin can't be negative
        }
        return openMin == 0; // we are not waiting for anymore ')'
    }
}

"""

# C++ Code 
"""
// Method 1: Early Return on Imbalance
class Solution {
public:
    bool checkValidString(string s) {
        int openCount = 0;  // will count the no of open parentheses
        for (char ch : s) {
            if (ch == '(') openCount++;
            else openCount--;
            if (openCount < 0) return false;  // '(' is less than ')'
        }
        return openCount == 0;
    }
};

// Method 2: Simple Recursion (TLE)
class RecursiveSolution {
public:
    bool checkValidString(string s) {
        return check(s, 0, 0);
    }

    bool check(const string& s, int index, int openCount) {
        if (openCount < 0) return false;
        if (index == s.size()) return openCount == 0;

        if (s[index] == '(') {
            return check(s, index + 1, openCount + 1);
        } else if (s[index] == ')') {
            return check(s, index + 1, openCount - 1);
        } else if (s[index] == '*') {
            return check(s, index + 1, openCount + 1) ||
                   check(s, index + 1, openCount - 1) ||
                   check(s, index + 1, openCount);
        }
        return false;
    }
};

// Method 3: Recursive with Memoization (DP)
class DPSolution {
public:
    bool checkValidString(string s) {
        int n = s.size();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, -1));
        return check(s, 0, 0, dp);
    }

    bool check(const string& s, int index, int openCount, vector<vector<int>>& dp) {
        if (openCount < 0) return false;
        if (index == s.size()) return openCount == 0;
        if (dp[index][openCount] != -1) return dp[index][openCount];

        bool res = false;
        if (s[index] == '(') {
            res = check(s, index + 1, openCount + 1, dp);
        } else if (s[index] == ')') {
            res = check(s, index + 1, openCount - 1, dp);
        } else if (s[index] == '*') {
            res = check(s, index + 1, openCount + 1, dp) ||
                  check(s, index + 1, openCount - 1, dp) ||
                  check(s, index + 1, openCount, dp);
        }

        dp[index][openCount] = res;
        return res;
    }
};

// Method 4: Greedy O(n) Time
class GreedySolution {
public:
    bool checkValidString(string s) {
        int openMin = 0, openMax = 0;  // max and min no of ')' that can be accommodated
        for (char ch : s) {
            if (ch == '(') {
                openMin++;
                openMax++;
            } else if (ch == ')') {
                openMin--;
                openMax--;
            } else if (ch == '*') {
                openMin--;    // if '*' behaves as ')'
                openMax++;    // if '*' behaves as '('
            }
            if (openMax < 0) return false;
            openMin = max(openMin, 0);  // openMin can't be negative
        }
        return openMin == 0;  // no unmatched '(' left
    }
};

"""