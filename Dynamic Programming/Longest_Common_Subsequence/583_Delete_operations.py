"""
Note vvi: if only deletion is allowed , then for making both string same .  Make both equal to lcs.
Because lcs will be the maximum length of string that we can get by using delete operation only to make both string same.

so ans will be equal to the cost of onverting both strings to longest common subsequence
"""

# Time : O(N^2)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        x,y= len(word1), len(word2)
        lcs_length= self.lcs(x,y,word1,word2)
	    # 1st make the 1st string equal to lcs itself
	    # for this we have to delete extra character except lcs
        no_deletion1= x- lcs_length
        # 1st make the 1st string equal to lcs itself
	    # for this we have to delete extra character except lcs
        no_deletion2= y- lcs_length
        # after this length of both string will become equal and will be left with LCS only
        # so finally both string will become equal
        return no_deletion1 + no_deletion2
        
    def lcs(self,x,y,s1,s2):
        dp= [[0 for j in range(y+1)] for i in range(x+1)]
        for i in range(1,x+1):
            for j in range(1,y+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j]= 1+ dp[i-1][j-1]
                else:
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
        return dp[x][y]

# Java Code 
"""
class Solution {
    public int minDistance(String word1, String word2) {
        int x = word1.length(), y = word2.length();
        int lcs_length = lcs(x, y, word1, word2);

        // 1st make the 1st string equal to lcs itself
        // for this we have to delete extra character except lcs
        int no_deletion1 = x - lcs_length;

        // 1st make the 1st string equal to lcs itself
        // for this we have to delete extra character except lcs
        int no_deletion2 = y - lcs_length;

        // after this length of both string will become equal and will be left with LCS only
        // so finally both string will become equal
        return no_deletion1 + no_deletion2;
    }

    private int lcs(int x, int y, String s1, String s2) {
        int[][] dp = new int[x + 1][y + 1];
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1.charAt(i - 1) == s2.charAt(j - 1))
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[x][y];
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int x = word1.size(), y = word2.size();
        int lcs_length = lcs(x, y, word1, word2);

        // 1st make the 1st string equal to lcs itself
        // for this we have to delete extra character except lcs
        int no_deletion1 = x - lcs_length;

        // 1st make the 1st string equal to lcs itself
        // for this we have to delete extra character except lcs
        int no_deletion2 = y - lcs_length;

        // after this length of both string will become equal and will be left with LCS only
        // so finally both string will become equal
        return no_deletion1 + no_deletion2;
    }

private:
    int lcs(int x, int y, const string& s1, const string& s2) {
        vector<vector<int>> dp(x + 1, vector<int>(y + 1, 0));
        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (s1[i - 1] == s2[j - 1])
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[x][y];
    }
};
"""

"""
case 2:
if only insertion operations would have been allowed then 
for making both string equal , make both equal to "shortest common supersequences"
so, we will have to find the shortest common supersequences and we will 
have to insert the char in both the strings to make its length equal to shortest supersequences
total addition= (len(supersequences)- len(s1)) + (len(supersequences)- len(s2))


case 3: if both insertion and deletion is allowed then total no of  operation will equal to 1st case only i.e if only deletion will be allowed
steps: 1st make the 1st string equal to lcs, for this delete and  
no of delete_operation= len(s1)- lcs_lenth
now make the string 1 equal to string 2 by adding the extra char of string 2 other than lcs
so ono of insertion_operation= len(s2)- lcs_length
finally total_operation= delete_operation + insertion_operation  === 1st case only


Method 2:
Note: Indirectly making both equal to lcs only. But did after a long time so forgot about lcs and came with method.
Logic : 1) when 1st char of both will be same then ans= f(s1[1: ] , s2[1 :]) as there is no need to delete any char in this case.
2) if 1st char of both is not equal then we have two choices i.e a) delete 1st char in 's1' or b ) delete 1st char in 's2'.
why not deleting both because later char can become same like 'LCS' so minimum we will get in this case only.

Base case: when any of string becomes empty then in this case only way to make them equal is to make both empty.
 we have to delete the length of other string to make both of them equal 

Logic is similar to 'lcs' but opposite.

Time: O(n^2)
"""

class Solution:
    @lru_cache(None)
    def minDistance(self, word1: str, word2: str) -> int:     
        if not word1 or not word2:
            return max(len(word1), len(word2))
        ans = 0
        if word1[0] == word2[0]:
            ans = self.minDistance(word1[1 : ], word2[1: ])
        else:
            ans = 1 + min(self.minDistance(word1[1 : ], word2), self.minDistance(word1, word2[1: ]))
        return ans
    
# Better memoise using indexes using 2d matrix just like lcs.


# vvi : Common mistake that people can make.
# no need to include 'ans' in else case otherwise you will get less than required because of 1st case.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return max(len(word1), len(word2))
        ans = 0
        if word1[0] == word2[0]:
            ans = self.minDistance(word1[1 : ], word2[1: ])
        else:
            ans = min(ans, 1 + self.minDistance(word1[1 : ], word2), 1 +  self.minDistance(word1, word2[1: ]))
        return ans
    

# Java Code 
"""
class Solution {
    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()][word2.length()];
        for (int[] row : dp) {
            java.util.Arrays.fill(row, -1);
        }
        return helper(0, 0, word1, word2, dp);
    }

    private int helper(int i, int j, String word1, String word2, int[][] dp) {
        if (i == word1.length()) return word2.length() - j;
        if (j == word2.length()) return word1.length() - i;

        if (dp[i][j] != -1) return dp[i][j];

        int ans;
        if (word1.charAt(i) == word2.charAt(j)) {
            ans = helper(i + 1, j + 1, word1, word2, dp);
        } else {
            ans = 1 + Math.min(helper(i + 1, j, word1, word2, dp),
                               helper(i, j + 1, word1, word2, dp));
        }
        dp[i][j] = ans;
        return ans;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length(), n = word2.length();
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return helper(0, 0, word1, word2, dp);
    }

private:
    int helper(int i, int j, const string& word1, const string& word2, vector<vector<int>>& dp) {
        if (i == word1.length()) return word2.length() - j;
        if (j == word2.length()) return word1.length() - i;

        if (dp[i][j] != -1) return dp[i][j];

        int ans;
        if (word1[i] == word2[j]) {
            ans = helper(i + 1, j + 1, word1, word2, dp);
        } else {
            ans = 1 + min(helper(i + 1, j, word1, word2, dp),
                          helper(i, j + 1, word1, word2, dp));
        }
        dp[i][j] = ans;
        return ans;
    }
};
"""

# Similar Q 
# 1) "712. Minimum ASCII Delete Sum for Two Strings"

# Exactly same only we need to add the ascii value of characters we are deleting.
class Solution:
    @lru_cache(None)
    def minimumDeleteSum(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            sum = 0
            if word1:
                for c in word1:
                    sum += ord(c)
                    
            if word2:
                for c in word2:
                    sum += ord(c)
            return sum
        ans = 0
        if word1[0] == word2[0]:
            ans = self.minimumDeleteSum(word1[1 : ], word2[1: ])
        else:
            ans = min(ord(word1[0]) + self.minimumDeleteSum(word1[1 : ], word2), ord(word2[0]) + self.minimumDeleteSum(word1, word2[1: ]))
        return ans

# Java Code 
"""
class Solution {
    public int minimumDeleteSum(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        Integer[][] dp = new Integer[m][n];
        return helper(0, 0, word1, word2, dp);
    }

    private int helper(int i, int j, String word1, String word2, Integer[][] dp) {
        if (i == word1.length()) {
            int sum = 0;
            while (j < word2.length()) sum += word2.charAt(j++);
            return sum;
        }
        if (j == word2.length()) {
            int sum = 0;
            while (i < word1.length()) sum += word1.charAt(i++);
            return sum;
        }

        if (dp[i][j] != null) return dp[i][j];

        int ans;
        if (word1.charAt(i) == word2.charAt(j)) {
            ans = helper(i + 1, j + 1, word1, word2, dp);
        } else {
            ans = Math.min(word1.charAt(i) + helper(i + 1, j, word1, word2, dp),
                           word2.charAt(j) + helper(i, j + 1, word1, word2, dp));
        }

        dp[i][j] = ans;
        return ans;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minimumDeleteSum(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m, vector<int>(n, -1));
        return helper(0, 0, word1, word2, dp);
    }

private:
    int helper(int i, int j, const string& word1, const string& word2, vector<vector<int>>& dp) {
        if (i == word1.size()) {
            int sum = 0;
            while (j < word2.size()) sum += word2[j++];
            return sum;
        }
        if (j == word2.size()) {
            int sum = 0;
            while (i < word1.size()) sum += word1[i++];
            return sum;
        }

        if (dp[i][j] != -1) return dp[i][j];

        int ans;
        if (word1[i] == word2[j]) {
            ans = helper(i + 1, j + 1, word1, word2, dp);
        } else {
            ans = min(word1[i] + helper(i + 1, j, word1, word2, dp),
                      word2[j] + helper(i, j + 1, word1, word2, dp));
        }

        dp[i][j] = ans;
        return ans;
    }
};
"""