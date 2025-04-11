
# Approach: Front partitioning
# logic: you can only partition at any index if string till that index is palindrome.
# in this we only need to pass one parameter, for checking palindrome at each index.

# method 1: Recursion
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


# method 2: Memoization(Accepted)
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

# Java
"""
import java.util.*;

public class Solution {
    public int minCut(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return helper(s, 0, dp) - 1;
    }

    private int helper(String s, int i, int[] dp) {
        if (i == s.length()) {
            return 0;
        }
        if (dp[i] != -1) {
            return dp[i];
        }

        int minCost = Integer.MAX_VALUE;
        for (int j = i; j < s.length(); j++) {
            String temp = s.substring(i, j + 1);
            if (isPalindrome(temp)) {
                int smallAns = 1 + helper(s, j + 1, dp);
                minCost = Math.min(minCost, smallAns);
            }
        }

        dp[i] = minCost;
        return dp[i];
    }

    private boolean isPalindrome(String str) {
        int l = 0, r = str.length() - 1;
        while (l < r) {
            if (str.charAt(l++) != str.charAt(r--)) return false;
        }
        return true;
    }
}
"""

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

# Java
"""
public class Solution {
    public int minCut(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];

        for (int i = n - 1; i >= 0; i--) {
            int minCost = Integer.MAX_VALUE;
            for (int j = i; j < n; j++) {
                if (isPalindrome(s, i, j)) {
                    int smallAns = 1 + dp[j + 1];
                    minCost = Math.min(minCost, smallAns);
                }
            }
            dp[i] = minCost;
        }

        return dp[0] - 1;
    }

    private boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) {
                return false;
            }
        }
        return true;
    }
}
"""
