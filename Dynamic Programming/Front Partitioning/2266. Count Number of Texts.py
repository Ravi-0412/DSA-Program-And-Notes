# Time: O(n)

class Solution:
    def __init__(self):
        self.mod = 1000000007

    def countTexts(self, pressedKeys: str) -> int:
        key = [0, 0, 3, 3, 3, 3, 3, 4, 3, 4]
        n = len(pressedKeys)
        dp = [-1] * n
        return self.solve(0, pressedKeys, key, dp)
    
    def solve(self, ind: int, s: str, key: list[int], dp: list[int]) -> int:
        if ind == len(s):
            return 1
        if dp[ind] != -1:
            return dp[ind]
        
        count = 0
        num = int(s[ind])
        rep = key[num]
        
        for i in range(rep):
            if ind + i < len(s) and s[ind] == s[ind + i]:
                count += self.solve(ind + 1 + i, s, key, dp)
                count %= self.mod
            else:
                break
        
        dp[ind] = count
        return dp[ind]
    
# Tabulation
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 1000000007
        key = [0, 0, 3, 3, 3, 3, 3, 4, 3, 4]
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[n] = 1
        
        for ind in range(n - 1, -1, -1):
            count = 0
            num = int(pressedKeys[ind])
            rep = key[num]
            for i in range(rep):
                if ind + i < n and pressedKeys[ind] == pressedKeys[ind + i]:
                    count += dp[ind + i + 1]
                    count %= mod
                else:
                    break
            dp[ind] = count
        
        return dp[0]


# java
""""
class Solution {
    int mod = (1000000007);
    public int countTexts(String pressedKeys) {
         int[] key = new int[] {0,0,3,3,3,3,3,4,3,4};
         int n = pressedKeys.length();
         int[] dp = new int[n];
        Arrays.fill(dp,-1);
         return solve(0,pressedKeys,key,dp);
    }
    public int solve(int ind , String s ,int[] key,int[]dp){
        if(ind==s.length()){
            return 1;
        }
        if(dp[ind]!=-1) return dp[ind];
        int count = 0;
        int num = s.charAt(ind)-'0';
        int rep = key[num];
        for(int i =0;i<rep && ind+i<s.length() && s.charAt(ind)==s.charAt(ind+i);i++){
            count += solve(ind+1+i,s,key,dp);
            count %= mod;
        }
        return dp[ind] = count;
    }
}
"""


"""
class Solution {
    int mod = (1000000007);

    public int countTexts(String pressedKeys) {
        int[] key = new int[] { 0, 0, 3, 3, 3, 3, 3, 4, 3, 4 };
        int n = pressedKeys.length();
        int[] dp = new int[n + 1];
        dp[n] = 1;

        for (int ind = n - 1; ind >= 0; ind--) {
            int count = 0;
            int num = pressedKeys.charAt(ind) - '0';
            int rep = key[num];
            for (int i = 0; i < rep && ind + i < pressedKeys.length() && pressedKeys.charAt(ind) == pressedKeys.charAt(ind + i); i++) {
                count += dp[ind+i+1];
                count %= mod;
            }
             dp[ind] = count;
        }
        return dp[0];
    }
}
"""

# Later do in O(1) space.
# Solution in sheet