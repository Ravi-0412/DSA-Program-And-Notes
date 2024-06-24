# Just same thing as Q: 122. only added one para 'txn' in function that's it
# here we can only buy and sell if transaction is allowed, otherwise simply return zero.
# so for checking the remaining txn we will need one more para

# method 1: recursive
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:     
        return self.helper(prices, 0, k, 1)  # 2nd para: ind, 3rd: no of transactions allowed, 4th: buying is allowed or not, 
    
    def helper(self, prices, ind, txn, buy):
        if txn== 0: return 0
        if ind== len(prices): return 0
        if buy:
            return max(-prices[ind] + self.helper(prices, ind+1, txn, 0 ), 0+ self.helper(prices, ind+1, txn, 1))
        return max(prices[ind] + self.helper(prices, ind+1, txn-1, 1), 0+ self.helper(prices, ind+1, txn, 0))

# method 2: memoization
# range of k: will be k+1 i.e k,k-1....0    
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int: 
        n= len(prices)
        dp= [[[-1 for m in range(2)] for j in range(k+1)] for i in range(n+1)]     
        return self.helper(prices, 0, k, 1, dp)  # 2nd para: ind, 3rd: buying is allowed or not, 4th: no of transactions allowed
    
    def helper(self, prices, ind, txn, buy, dp):
        if txn== 0:
            dp[ind][txn][buy]= 0
            return dp[ind][txn][buy]
        if ind== len(prices):
            dp[ind][txn][buy]= 0
            return dp[ind][txn][buy]
        if dp[ind][txn][buy] != -1:
            return dp[ind][txn][buy]
        if buy:
            dp[ind][txn][buy]= max(-prices[ind] + self.helper(prices, ind+1, txn, 0, dp), 0+ self.helper(prices, ind+1, txn, 1, dp))
        else:
            dp[ind][txn][buy]=  max(prices[ind] + self.helper(prices, ind+1, txn-1, 1, dp), 0+ self.helper(prices, ind+1, txn, 0, dp))
        return dp[ind][txn][buy]

# Tabulation
# time= space= O(N*k*2)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int: 
        n= len(prices)
        dp= [[[0 for m in range(2)] for j in range(k+1)] for i in range(n+1)]  # automatically got initialised to base case
        for ind in range(n-1, -1, -1):
            for txn in range(1, k+1):
                for buy in range(2):
                    if buy:
                        dp[ind][txn][buy]= max(-prices[ind] + dp[ind+1][txn][0], 0+ dp[ind+1][txn][1])
                    else:
                        dp[ind][txn][buy]= max(prices[ind] + dp[ind+1][txn-1][1], 0+ dp[ind+1][txn][0])     
        return dp[0][k][1]  # return that proper variable for which you have called the recursive function


# space can be optimised to O(K*2)*2 as curr row value is dependent on pre row.
# And for optimising space, just make pre and curr array with dimension 1 less than the dp.(since we are calculating row wise so no need to include row in making array).
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int: 
        n= len(prices)
        pre= [[0 for m in range(2)] for j in range(k+1)]  # automatically got initialised to base case
        for ind in range(n-1, -1, -1):
            curr= [[0 for m in range(2)] for j in range(k+1)]
            for txn in range(1, k+1):
                for buy in range(2):
                    if buy:
                        curr[txn][buy]= max(-prices[ind] + pre[txn][0], 0+ pre[txn][1])
                    else:
                        curr[txn][buy]= max(prices[ind] + pre[txn-1][1], 0+ pre[txn][0])
            pre= curr.copy()     
        return pre[k][1]


# another way of doing and optimising space.
# no need to pass the variable buy in parameter.
# just count the no of buy and sell like: 0,1,2,3....(on day 0, we can buy and on next day we can sell i.e buy,sell,buy,sell.....)
# so if count of txn reaches 2*k then means we can't perform any transaction so simpy retrun 0.
# and if count is even means we can buy only and if count is odd means we can sell only that's it.
# space: O(N*k)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:     
        return self.helper(prices, 0, k, 0)  # 2nd para: ind,3rd: total sell and buy allowed(k), 3rd: count of transactions
    
    def helper(self, prices, ind, txn, cnt):
        if cnt== 2*txn or ind== len(prices): return 0
        if cnt%2==0:  # means we can buy only
            return max(-prices[ind] + self.helper(prices, ind+1, txn, cnt +1), 0+ self.helper(prices, ind+1, txn, cnt))
        else: # means we can sell only
            return max(prices[ind] + self.helper(prices, ind+1, txn, cnt +1), 0+ self.helper(prices, ind+1, txn, cnt))


# java
# Memoisation
"""
public class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        int[][][] dp = new int[n + 1][k + 1][2];
        
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                dp[i][j][0] = -1;
                dp[i][j][1] = -1;
            }
        }
        
        return helper(prices, 0, k, 1, dp);
    }

    private int helper(int[] prices, int ind, int txn, int buy, int[][][] dp) {
        if (txn == 0 || ind == prices.length)  {
            return 0;
        }
        if (dp[ind][txn][buy] != -1) {
            return dp[ind][txn][buy];
        }
        if (buy == 1) {
            dp[ind][txn][buy] = Math.max(-prices[ind] + helper(prices, ind + 1, txn, 0, dp),
                                         helper(prices, ind + 1, txn, 1, dp));
        } else {
            dp[ind][txn][buy] = Math.max(prices[ind] + helper(prices, ind + 1, txn - 1, 1, dp),
                                         helper(prices, ind + 1, txn, 0, dp));
        }
        return dp[ind][txn][buy];
    }
}
"""

# Tabulation
"""
public class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n == 0) {
            return 0;
        }

        int[][][] dp = new int[n + 1][k + 1][2];

        // Initialize the base case where dp[n][x][y] is 0
        for (int i = 0; i <= k; i++) {
            dp[n][i][0] = 0;
            dp[n][i][1] = 0;
        }
        
        for (int ind = n - 1; ind >= 0; ind--) {
            for (int txn = 1; txn <= k; txn++) {
                for (int buy = 0; buy <= 1; buy++) {
                    if (buy == 1) {
                        dp[ind][txn][buy] = Math.max(-prices[ind] + dp[ind + 1][txn][0], dp[ind + 1][txn][1]);
                    } else {
                        dp[ind][txn][buy] = Math.max(prices[ind] + dp[ind + 1][txn - 1][1], dp[ind + 1][txn][0]);
                    }
                }
            }
        }

        return dp[0][k][1];  // Return the result of starting with the ability to buy and k transactions
    }
}
"""

# Tabulation with space optimised

public class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n == 0) {
            return 0;
        }

        int[][] pre = new int[k + 1][2];
        int[][] curr = new int[k + 1][2];

        for (int ind = n - 1; ind >= 0; ind--) {
            for (int txn = 1; txn <= k; txn++) {
                for (int buy = 0; buy <= 1; buy++) {
                    if (buy == 1) {
                        curr[txn][buy] = Math.max(-prices[ind] + pre[txn][0], pre[txn][1]);
                    } else {
                        curr[txn][buy] = Math.max(prices[ind] + pre[txn - 1][1], pre[txn][0]);
                    }
                }
            }
            // Copy current state to previous state for next iteration
            for (int txn = 0; txn <= k; txn++) {
                pre[txn][0] = curr[txn][0];
                pre[txn][1] = curr[txn][1];
            }
        }

        return pre[k][1];  // Return the result of starting with the ability to buy and k transactions
    }
}

# Tabulation without 'buy' variable

"""
public class Solution {
    public int maxProfit(int k, int[] prices) {
        return helper(prices, 0, k, 0);
    }

    private int helper(int[] prices, int ind, int txn, int cnt) {
        if (cnt == 2 * txn || ind == prices.length) {
            return 0;
        }

        if (cnt % 2 == 0) {  // means we can buy only
            return Math.max(-prices[ind] + helper(prices, ind + 1, txn, cnt + 1),
                            helper(prices, ind + 1, txn, cnt));
        } else {  // means we can sell only
            return Math.max(prices[ind] + helper(prices, ind + 1, txn, cnt + 1),
                            helper(prices, ind + 1, txn, cnt));
        }
    }
}
"""