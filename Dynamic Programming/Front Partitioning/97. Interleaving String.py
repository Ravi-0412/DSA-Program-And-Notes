# Method 1: 

# i was getting how to do but not able to write.
# Recursion me jyada dimag mat lagao bs likh do jo lage kam karega recursively nhi to recursion me kabhi bhi confidence nhi aayeaga.

# logic: just check for char of s3 in s1 or s2 if it present in any of them then incr the pointer of that string.
# there will be two cases either char in s3 can be present in s1 or s2.
# index of s3 will be : i+j since we are forming s3 only from s1 + s2

# if we get continous char from same string then it's fine only as it will get counted 
# as whole one time only(one substring) when switching will happpen, so order will be maintained only.

# Note that the condition |n - m| <=1 always holds true.

# Proof:
# Let's say s1 = "abcde" and s2 = "fgh". We divide s1 into four parts and s2 into two parts. So, x - y = 2.
# s1 = "ab" + "c" + "d" + "e" and s2 = "f" + "gh".
# s3 = "ab" + "f" + "c" + "gh" + "d" + "e".
# The above can rewritten as s3 = "ab" + "f" + "c" + "gh" + "de", 
# which is basically dividing s1 into three parts and s2 into two parts.
#  Two or more contiguous substring parts from same string can be combined into one substring.
#  And hence, the condition |x - y| <=1 holds true.
# recursive:
# time: O(2^(n+m)), At each step, we have two choices i.e take char from s1 or s2.

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2)!= len(s3):
            return False
        return self.helper(0, 0,s1, s2, s3)
    
    # this function will tell considering the char from 'i'th index of s1 and char from 'j'th index in s2,
    # is s3[i+j: ] is a interleavig substring?
    def helper(self, i, j, s1, s2, s3):
        if i== len(s1) and j== len(s2):
            return True
        # checking char at curr index in 's3' is same as either curr index in s1 or s2
        # index of s3 will be always equal to 'i+j' since we are forming s3 from s1 and s2 
        if i < len(s1) and s1[i]== s3[i+j]  and self.helper(i+1, j, s1, s2, s3):
            return True
        if j < len(s2) and s2[j]== s3[i+j]  and self.helper(i, j+1, s1, s2, s3):
            return True
        return False

# Java Code 
"""
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length())
            return false;
        return helper(0, 0, s1, s2, s3);
    }

    // this function will tell considering the char from 'i'th index of s1 and char from 'j'th index in s2,
    // is s3[i+j: ] is a interleaving substring?
    private boolean helper(int i, int j, String s1, String s2, String s3) {
        if (i == s1.length() && j == s2.length())
            return true;

        // checking char at curr index in 's3' is same as either curr index in s1 or s2
        // index of s3 will be always equal to 'i + j' since we are forming s3 from s1 and s2
        if (i < s1.length() && s1.charAt(i) == s3.charAt(i + j) && helper(i + 1, j, s1, s2, s3))
            return true;

        if (j < s2.length() && s2.charAt(j) == s3.charAt(i + j) && helper(i, j + 1, s1, s2, s3))
            return true;

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
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.length() + s2.length() != s3.length())
            return false;
        return helper(0, 0, s1, s2, s3);
    }

    // this function will tell considering the char from 'i'th index of s1 and char from 'j'th index in s2,
    // is s3[i+j: ] is a interleaving substring?
    bool helper(int i, int j, const string& s1, const string& s2, const string& s3) {
        if (i == s1.length() && j == s2.length())
            return true;

        // checking char at curr index in 's3' is same as either curr index in s1 or s2
        // index of s3 will be always equal to 'i + j' since we are forming s3 from s1 and s2
        if (i < s1.length() && s1[i] == s3[i + j] && helper(i + 1, j, s1, s2, s3))
            return true;

        if (j < s2.length() && s2[j] == s3[i + j] && helper(i, j + 1, s1, s2, s3))
            return true;

        return false;
    }
};
"""

# Method 2: 
# memoization
# time= space= O(m*n)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2)!= len(s3):
            return False
        dp= [[-1 for j in range(len(s2) +1)] for i in range(len(s1) + 1)]
        return self.helper(0, 0,s1, s2, s3, dp)
    
    def helper(self, i, j, s1, s2, s3, dp):
        if i== len(s1) and j== len(s2):
            return True
        if dp[i][j]!= -1:
            return dp[i][j]
        # checking char at curr index in 's3' is same as either curr index in s1 or s2
        # index of s3 will be always equal to 'i+j' since we are forming s3 from s1 and s2 
        if i < len(s1) and s1[i]== s3[i+j]  and self.helper(i+1, j, s1, s2, s3, dp):
            dp[i][j]= True
            return True
        if j < len(s2) and s2[j]== s3[i+j]  and self.helper(i, j+1, s1, s2, s3, dp):
            dp[i][j]= True
            return True
        dp[i][j]= False
        return False
   
# Java Code 
"""
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length())
            return false;

        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        for (int i = 0; i <= s1.length(); i++)
            for (int j = 0; j <= s2.length(); j++)
                dp[i][j] = -1;

        return helper(0, 0, s1, s2, s3, dp);
    }

    private boolean helper(int i, int j, String s1, String s2, String s3, int[][] dp) {
        if (i == s1.length() && j == s2.length())
            return true;
        if (dp[i][j] != -1)
            return dp[i][j] == 1;
        // checking char at curr index in 's3' is same as either curr index in s1 or s2
        // index of s3 will be always equal to 'i+j' since we are forming s3 from s1 and s2 
        if (i < s1.length() && s1.charAt(i) == s3.charAt(i + j) && helper(i + 1, j, s1, s2, s3, dp)) {
            dp[i][j] = 1;
            return true;
        }
        if (j < s2.length() && s2.charAt(j) == s3.charAt(i + j) && helper(i, j + 1, s1, s2, s3, dp)) {
            dp[i][j] = 1;
            return true;
        }
        dp[i][j] = 0;
        return false;
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
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.length() + s2.length() != s3.length())
            return false;

        vector<vector<int>> dp(s1.length() + 1, vector<int>(s2.length() + 1, -1));
        return helper(0, 0, s1, s2, s3, dp);
    }

    bool helper(int i, int j, const string& s1, const string& s2, const string& s3, vector<vector<int>>& dp) {
        if (i == s1.length() && j == s2.length())
            return true;
        if (dp[i][j] != -1)
            return dp[i][j];

        // checking char at curr index in 's3' is same as either curr index in s1 or s2
        // index of s3 will be always equal to 'i+j' since we are forming s3 from s1 and s2 
        if (i < s1.length() && s1[i] == s3[i + j] && helper(i + 1, j, s1, s2, s3, dp)) {
            dp[i][j] = 1;
            return true;
        }
        if (j < s2.length() && s2[j] == s3[i + j] && helper(i, j + 1, s1, s2, s3, dp)) {
            dp[i][j] = 1;
            return true;
        }

        dp[i][j] = 0;
        return false;
    }
};
""" 

# Method 3: 
# Tabulation
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True # base case 
        
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True  # Match current character in s1
                elif j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True  # Match current character in s2
        
        return dp[0][0]

# Java Code 
"""
class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s1.length() + s2.length() != s3.length())
            return false;

        boolean[][] dp = new boolean[s1.length() + 1][s2.length() + 1];
        dp[s1.length()][s2.length()] = true; // base case

        for (int i = s1.length(); i >= 0; i--) {
            for (int j = s2.length(); j >= 0; j--) {
                if (i < s1.length() && s1.charAt(i) == s3.charAt(i + j) && dp[i + 1][j]) {
                    dp[i][j] = true;  // Match current character in s1
                } else if (j < s2.length() && s2.charAt(j) == s3.charAt(i + j) && dp[i][j + 1]) {
                    dp[i][j] = true;  // Match current character in s2
                }
            }
        }

        return dp[0][0];
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
    bool isInterleave(string s1, string s2, string s3) {
        if (s1.length() + s2.length() != s3.length())
            return false;

        vector<vector<bool>> dp(s1.length() + 1, vector<bool>(s2.length() + 1, false));
        dp[s1.length()][s2.length()] = true; // base case

        for (int i = s1.length(); i >= 0; --i) {
            for (int j = s2.length(); j >= 0; --j) {
                if (i < s1.length() && s1[i] == s3[i + j] && dp[i + 1][j]) {
                    dp[i][j] = true;  // Match current character in s1
                } else if (j < s2.length() && s2[j] == s3[i + j] && dp[i][j + 1]) {
                    dp[i][j] = true;  // Match current character in s2
                }
            }
        }

        return dp[0][0];
    }
};
"""



