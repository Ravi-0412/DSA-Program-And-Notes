# only thing in this to handle the case when it starts with '0'.
# in case if '0' comes after any number that will get handled by the range (1 to 26).
# other things are just as we used to do in front partitioning like at every index check for greater index if that can be included in our ans.

class Solution:
    def numDecodings(self, s: str) -> int:
        n= len(s)
        return self.helper(s, 0, n)
    
    def helper(self, s, i, n):
        if i== n:  # means we have found one of the ways
            return 1
        if int(s[i])== 0:  # if starts with '0' then simply return 0
            return 0
        count= 0
        for k in range(i+1, n+1):
            if 1<= int(s[i:k])<= 26:
                count+= self.helper(s, k,n)
        return count


# memoisation
class Solution:
    def numDecodings(self, s: str) -> int:
        n= len(s)
        dp= [-1 for i in range(n+1)]
        return self.helper(s, 0, n, dp)
    
    def helper(self, s, i, n, dp):
        if i== n:
            return 1
        if int(s[i])== 0:
            return 0
        if dp[i]!= -1:
            return dp[i]
        count= 0
        for k in range(i+1, n+1):
            if 1<= int(s[i:k])<= 26:
                count+= self.helper(s, k,n, dp)
        dp[i]= count
        return dp[i]

# Java
"""
class Solution {
    public int numDecodings(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, -1);
        return helper(s, 0, n, dp);
    }

    private int helper(String s, int i, int n, int[] dp) {
        if (i == n) {
            return 1;
        }
        if (s.charAt(i) == '0') {
            return 0;
        }
        if (dp[i] != -1) {
            return dp[i];
        }
        int count = 0;
        for (int k = i + 1; k <= n; k++) {
            if (1 <= Integer.parseInt(s.substring(i, k)) && Integer.parseInt(s.substring(i, k)) <= 26) {
                count += helper(s, k, n, dp);
            }
        }
        dp[i] = count;
        return dp[i];
    }
}

"""