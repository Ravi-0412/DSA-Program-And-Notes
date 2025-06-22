# Method 1:
# Recursion
# Approach: Front partitioning
# logic: you can only partition at any index if string till that index is palindrome.
# in this we only need to pass one parameter, for checking palindrome at each index.


class Solution:
    def minCut(self, s: str) -> int:
        n, i= len(s), 0
        ans= self.helper(s, i) -1  # since even after end index our function is doing partition and adding '+1'. so we have to subtract that '1'.
        return ans
    
    def helper(self, s, i):
        if i== len(s):
            return 0
        mincost= 9999
        for j in range(i, len(s)):
            temp= s[i: j+1]   # keep on adding one string at a time and if it is palindrom then partition after that index.
            if temp== temp[::-1]:
                smallAns= 1 + self.helper(s, j+1)
                mincost= min(mincost, smallAns)
        return mincost

# Java Code 
"""
class Solution {
    public int minCut(String s) {
        int n = s.length();
        int i = 0;
        int ans = helper(s, i) - 1;  // since even after end index our function is doing partition and adding '+1'. so we have to subtract that '1'.
        return ans;
    }

    private int helper(String s, int i) {
        if (i == s.length()) {
            return 0;
        }

        int mincost = 9999;
        for (int j = i; j < s.length(); j++) {
            String temp = s.substring(i, j + 1);  // keep on adding one string at a time and if it is palindrom then partition after that index.
            if (temp.equals(new StringBuilder(temp).reverse().toString())) {
                int smallAns = 1 + helper(s, j + 1);
                mincost = Math.min(mincost, smallAns);
            }
        }

        return mincost;
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
    int minCut(string s) {
        int n = s.length();
        int i = 0;
        int ans = helper(s, i) - 1;  // since even after end index our function is doing partition and adding '+1'. so we have to subtract that '1'.
        return ans;
    }

    int helper(string& s, int i) {
        if (i == s.length()) {
            return 0;
        }

        int mincost = 9999;
        for (int j = i; j < s.length(); ++j) {
            string temp = s.substr(i, j - i + 1);  // keep on adding one string at a time and if it is palindrom then partition after that index.
            string rev = temp;
            reverse(rev.begin(), rev.end());
            if (temp == rev) {
                int smallAns = 1 + helper(s, j + 1);
                mincost = min(mincost, smallAns);
            }
        }

        return mincost;
    }
};
"""


# method 2: 
# Memoization(Accepted)
# for time complexity: see the no of variable changing(say m) and no of 'for' loop (say p)
# time= O(n*r1*r2*....).  r1, r2,....: are size of variable changing in function as well as inside the for loop.

# here : time: O(n^2) as both the variable changing in function as well as variable inside the for loop is O(n)
class Solution:
    def minCut(self, s: str) -> int:
        n, i= len(s), 0
        dp = [-1 for i in range(n+1)]   # 'i' going from '0' to 'n'(base case)
        ans = self.helper(s, i, dp) - 1  # since even after end index our function is doing partition and adding '+1'. so we have to subtract that '1'.
        return ans
    
    def helper(self, s, i, dp):
        if i== len(s):
            return 0
        if dp[i]!= -1:
            return dp[i]
        mincost= 9999
        for j in range(i, len(s)):
            temp= s[i: j+1]   # keep on adding one string at a time and if it is palindrom then partition after that index.
            if temp== temp[::-1]:
                smallAns= 1 + self.helper(s, j+1, dp)
                mincost= min(mincost, smallAns)
        dp[i] = mincost
        return dp[i]

# Java Code 
"""
class Solution {
    public int minCut(String s) {
        int n = s.length(), i = 0;
        int[] dp = new int[n + 1];   // 'i' going from '0' to 'n'(base case)
        for (int k = 0; k <= n; k++) dp[k] = -1;
        int ans = helper(s, i, dp) - 1;  // since even after end index our function is doing partition and adding '+1'. so we have to subtract that '1'.
        return ans;
    }

    private int helper(String s, int i, int[] dp) {
        if (i == s.length()) return 0;
        if (dp[i] != -1) return dp[i];
        int mincost = 9999;
        for (int j = i; j < s.length(); j++) {
            String temp = s.substring(i, j + 1);  // keep on adding one string at a time and if it is palindrom then partition after that index.
            if (temp.equals(new StringBuilder(temp).reverse().toString())) {
                int smallAns = 1 + helper(s, j + 1, dp);
                mincost = Math.min(mincost, smallAns);
            }
        }
        dp[i] = mincost;
        return dp[i];
    }
}
"""
# C++ Code 
"""
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minCut(string s) {
        int n = s.length(), i = 0;
        vector<int> dp(n + 1, -1);   // 'i' going from '0' to 'n'(base case)
        int ans = helper(s, i, dp) - 1;  // since even after end index our function is doing partition and adding '+1'. so we have to subtract that '1'.
        return ans;
    }

    int helper(string& s, int i, vector<int>& dp) {
        if (i == s.length()) return 0;
        if (dp[i] != -1) return dp[i];
        int mincost = 9999;
        for (int j = i; j < s.length(); ++j) {
            string temp = s.substr(i, j - i + 1);  // keep on adding one string at a time and if it is palindrom then partition after that index.
            string rev = temp;
            reverse(rev.begin(), rev.end());
            if (temp == rev) {
                int smallAns = 1 + helper(s, j + 1, dp);
                mincost = min(mincost, smallAns);
            }
        }
        dp[i] = mincost;
        return dp[i];
    }
};
"""

# method 3: 
# Tabulation
class Solution:
    def minCut(self, s: str) -> int:
        n, i= len(s), 0
        dp = [0 for i in range(n+1)]
        for i in range(n-1, -1, -1):
            mincost= 9999
            for j in range(i, len(s)):
                temp= s[i: j+1]   # keep on adding one string at a time and if it is palindrom then partition after that index.
                if temp== temp[::-1]:
                    smallAns= 1 + dp[j+1]
                    mincost= min(mincost, smallAns)
            dp[i]= mincost
        return dp[0] - 1

# Java Code 
"""
class Solution {
    public int minCut(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];

        for (int i = n - 1; i >= 0; i--) {
            int mincost = 9999;
            for (int j = i; j < n; j++) {
                String temp = s.substring(i, j + 1);   // keep on adding one string at a time and if it is palindrom then partition after that index.
                if (temp.equals(new StringBuilder(temp).reverse().toString())) {
                    int smallAns = 1 + dp[j + 1];
                    mincost = Math.min(mincost, smallAns);
                }
            }
            dp[i] = mincost;
        }

        return dp[0] - 1;
    }
}
"""
# C++ Code 
"""
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> dp(n + 1, 0);

        for (int i = n - 1; i >= 0; --i) {
            int mincost = 9999;
            for (int j = i; j < n; ++j) {
                string temp = s.substr(i, j - i + 1);  // keep on adding one string at a time and if it is palindrom then partition after that index.
                string rev = temp;
                reverse(rev.begin(), rev.end());
                if (temp == rev) {
                    int smallAns = 1 + dp[j + 1];
                    mincost = min(mincost, smallAns);
                }
            }
            dp[i] = mincost;
        }

        return dp[0] - 1;
    }
};
"""
