# method 1: Recursion(String matching)
"""
logic: if matched then nothing to do , just move forward in both the words
if not matched then we have three choices i.e insert, delete or replace

The time complexity of above solution is exponential. In worst case, we may end up doing O(3^m) operations.
 The worst case happens when none of characters of two strings match. 
Auxiliary Space: O(1), because no extra space is utilized.

in worst case no of total operations can be O(n)) when none of the string matches . in this case
just replace all char in word2 by char in word1.
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n= len(word1), len(word2)
        return self.helper(m, n, word1, word2)  # this means min operations required to convert word1[0...m-1] to word2[0....n-1]
    
    def helper(self,m,n,s,t):
        if n == 0:
             # only way to make word1= word2 is to delete all the char remaining in word1 which is equal to m
            return m
        if m ==0: # means n!= 0 and m==0 
            # only way to make word1= word2 is to insert all the remaining ele of word2 which is equal to n
            return n
        if s[m-1] == t[n-1]: # matched then nothing to do , zero cost
            return self.helper(m-1, n-1, s, t)
        """
        if not matched then we have three option:
        1) insert the same char of word2 in word1,
        in this case no need to move ahead in word1, only move ahead in word2 
        because curr char of word 1 can be be the next char of word2.
        2) delete the char in word1 and move ahead in word1 being at same position in word2.
        3) replace the char in word1 by char of word2, in this case move ahead in word1 and word2 both.
        """
        return  1+ min(self.helper(m, n-1, s, t), self.helper(m-1, n, s, t), self.helper(m-1, n-1, s, t))

<<<<<<< HEAD
# Java Code
"""
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        // this means min operations required to convert word1[0...m-1] to word2[0....n-1]
        return helper(m, n, word1, word2);
    }

    private int helper(int m, int n, String s, String t) {
        if (n == 0)
            // only way to make word1 = word2 is to delete all the char remaining in word1 which is equal to m
            return m;
        if (m == 0)
            // only way to make word1 = word2 is to insert all the remaining ele of word2 which is equal to n
            return n;
        if (s.charAt(m - 1) == t.charAt(n - 1))
            // matched then nothing to do , zero cost
            return helper(m - 1, n - 1, s, t);

        /*
        if not matched then we have three option:
        1) insert the same char of word2 in word1,
        in this case no need to move ahead in word1, only move ahead in word2
        because curr char of word 1 can be the next char of word2.
        2) delete the char in word1 and move ahead in word1 being at same position in word2.
        3) replace the char in word1 by char of word2, in this case move ahead in word1 and word2 both.
        */
        return 1 + Math.min(helper(m, n - 1, s, t), Math.min(helper(m - 1, n, s, t), helper(m - 1, n - 1, s, t)));
    }
}
"""
# C++ Code 
"""
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        // this means min operations required to convert word1[0...m-1] to word2[0....n-1]
        return helper(m, n, word1, word2);
    }

private:
    int helper(int m, int n, const string& s, const string& t) {
        if (n == 0)
            // only way to make word1 = word2 is to delete all the char remaining in word1 which is equal to m
            return m;
        if (m == 0)
            // only way to make word1 = word2 is to insert all the remaining ele of word2 which is equal to n
            return n;
        if (s[m - 1] == t[n - 1])
            // matched then nothing to do , zero cost
            return helper(m - 1, n - 1, s, t);

        /*
        if not matched then we have three option:
        1) insert the same char of word2 in word1,
        in this case no need to move ahead in word1, only move ahead in word2
        because curr char of word 1 can be the next char of word2.
        2) delete the char in word1 and move ahead in word1 being at same position in word2.
        3) replace the char in word1 by char of word2, in this case move ahead in word1 and word2 both.
        */
        return 1 + min({
            helper(m, n - 1, s, t),       // insert
            helper(m - 1, n, s, t),       // delete
            helper(m - 1, n - 1, s, t)    // replace
        });
    }
};
"""

# method 2: memoization
=======
# method 2: 
# memoisation
>>>>>>> a40de18 (verified Binary Search and DP)
# Time Complexity: O(m*n) 
# Auxiliary Space: O(m*n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n= len(word1), len(word2)
        dp= [[-1 for j in range(n+1)] for i in range(m+1)]
        return self.helper(m, n, word1, word2,dp)
    
    def helper(self,m,n,s,t,dp):
        if n== 0:
             # only way to make word1= word2 is to delete all the char remaining in word1 which is equal to m
            return m
        if m==0: # means n!= 0 and m==0 
            # only way to make word1= word2 is to insert all the remaining ele of word2 which is equal to n
            return n
        if dp[m][n]!= -1:
            return dp[m][n]
        if s[m-1]== t[n-1]: # matched then nothing to do , zero cost
            dp[m][n]= self.helper(m-1, n-1, s, t,dp)
        # if not matched then we have three option either insert the same char of word2 in word1, in this case no need of move ahead in word1 only move ahead in word2
        # or delete the char in word1 and move ahead in word1 being at same position in word2
        # or replace the char in word1 by char of word2, in this case move ahead in word1 and word2 both
        else:
            dp[m][n]= 1+ min(self.helper(m, n-1, s, t), self.helper(m-1, n, s, t), self.helper(m-1, n-1, s, t)) 
        return dp[m][n]

<<<<<<< HEAD

# Java Code
"""
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];

        // Initialize dp with -1
        for (int i = 0; i <= m; i++)
            java.util.Arrays.fill(dp[i], -1);

        return helper(m, n, word1, word2, dp);
    }

    private int helper(int m, int n, String s, String t, int[][] dp) {
        if (n == 0)
            // only way to make word1 = word2 is to delete all the char remaining in word1 which is equal to m
            return m;
        if (m == 0)  // means n != 0 and m == 0
            // only way to make word1 = word2 is to insert all the remaining ele of word2 which is equal to n
            return n;
        if (dp[m][n] != -1)
            return dp[m][n];
        if (s.charAt(m - 1) == t.charAt(n - 1))  // matched then nothing to do , zero cost
            dp[m][n] = helper(m - 1, n - 1, s, t, dp);
        // if not matched then we have three option:
        // 1) insert the same char of word2 in word1 — move ahead in word2 only
        // 2) delete the char in word1 — move ahead in word1 only
        // 3) replace the char in word1 by char of word2 — move ahead in both
        else
            dp[m][n] = 1 + Math.min(helper(m, n - 1, s, t, dp),
                            Math.min(helper(m - 1, n, s, t, dp),
                                     helper(m - 1, n - 1, s, t, dp)));
        return dp[m][n];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length(), n = word2.length();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, -1));
        return helper(m, n, word1, word2, dp);
    }

private:
    int helper(int m, int n, const string& s, const string& t, vector<vector<int>>& dp) {
        if (n == 0)
            // only way to make word1 = word2 is to delete all the char remaining in word1 which is equal to m
            return m;
        if (m == 0)  // means n != 0 and m == 0
            // only way to make word1 = word2 is to insert all the remaining ele of word2 which is equal to n
            return n;
        if (dp[m][n] != -1)
            return dp[m][n];
        if (s[m - 1] == t[n - 1])  // matched then nothing to do , zero cost
            dp[m][n] = helper(m - 1, n - 1, s, t, dp);
        // if not matched then we have three option:
        // 1) insert the same char of word2 in word1 — move ahead in word2 only
        // 2) delete the char in word1 — move ahead in word1 only
        // 3) replace the char in word1 by char of word2 — move ahead in both
        else
            dp[m][n] = 1 + min({helper(m, n - 1, s, t, dp),
                                helper(m - 1, n, s, t, dp),
                                helper(m - 1, n - 1, s, t, dp)});
        return dp[m][n];
    }
};
"""
=======
>>>>>>> a40de18 (verified Binary Search and DP)

# Method 3: 
# Tabulation
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n= len(word1), len(word2)
        dp= [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i==0:
                    dp[i][j]= j
                if j== 0:
                    dp[i][j]= i
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]== word2[j-1]:
                    dp[i][j]= dp[i-1][j-1]   
                else:
                    dp[i][j]= 1+ min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) 
        return dp[m][n]

<<<<<<< HEAD

# Java Code
"""
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[][] dp = new int[m + 1][n + 1];

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0)
                    dp[i][j] = j;
                if (j == 0)
                    dp[i][j] = i;
            }
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = 1 + Math.min(dp[i][j - 1],
                                    Math.min(dp[i - 1][j], dp[i - 1][j - 1]));
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
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0)
                    dp[i][j] = j;
                if (j == 0)
                    dp[i][j] = i;
            }
        }

        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1])
                    dp[i][j] = dp[i - 1][j - 1];
                else
                    dp[i][j] = 1 + min({dp[i][j - 1],
                                        dp[i - 1][j],
                                        dp[i - 1][j - 1]});
            }
        }

        return dp[m][n];
    }
};
"""
=======
>>>>>>> a40de18 (verified Binary Search and DP)

# method 4: 
# optimised space complexity to O(n)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n= len(word1), len(word2)
        pre= [0 for j in range(n+1)]
        for i in range(n+1):
            pre[i]= i
            
        for i in range(1,m+1):
            curr= [0 for j in range(n+1)]
            curr[0]= i  # since we are starting from 1 so for zero index we have to write manually (from base case)
            for j in range(1,n+1):
                if word1[i-1]== word2[j-1]:
                    curr[j]= pre[j-1]   
                else:
                    curr[j]= 1+ min(curr[j-1], pre[j], pre[j-1]) 
            pre= curr.copy()
        return pre[n]

<<<<<<< HEAD
# Java Code
"""
class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        int[] pre = new int[n + 1];

        for (int j = 0; j <= n; j++) {
            pre[j] = j;
        }

        for (int i = 1; i <= m; i++) {
            int[] curr = new int[n + 1];
            curr[0] = i;  // since we are starting from 1, we set index 0 manually (from base case)

            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    curr[j] = pre[j - 1];
                } else {
                    curr[j] = 1 + Math.min(curr[j - 1],
                                  Math.min(pre[j], pre[j - 1]));
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
#include <algorithm>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<int> pre(n + 1, 0);

        for (int j = 0; j <= n; ++j) {
            pre[j] = j;
        }

        for (int i = 1; i <= m; ++i) {
            vector<int> curr(n + 1, 0);
            curr[0] = i;  // since we are starting from 1, set index 0 manually (from base case)

            for (int j = 1; j <= n; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    curr[j] = pre[j - 1];
                } else {
                    curr[j] = 1 + min({curr[j - 1], pre[j], pre[j - 1]});
                }
            }

            pre = curr;
        }

        return pre[n];
    }
};
"""
=======
>>>>>>> a40de18 (verified Binary Search and DP)

