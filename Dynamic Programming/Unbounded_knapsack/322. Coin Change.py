# Method 1 : 

# totally same as Q no: "518. Coin Change II", except return value in base case.

# logic: when we take any coin then we will add '+1' .
# For ans we will take minimum of possible cases.

# Logic: For every coin we have two choice either take or not take.
# And we can only take any coin 'if coins[n-1] <= amount'.
# Ans will be minimum(take, notTake) => return this at last

# Note: Wh returning directly is working in above method?
# Reason: because if case of when we can take current coin 'if coins[n-1] <= amount' we are 
# taking both the case i.e when we take it or when we don't take it, covering both cases.
# otherwise not take this coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        minimum = self.MinCoins(coins,amount,n)
        if minimum == float('inf'):    # it means that amount is not possible so return -1.
            return -1
        return minimum
    
    def MinCoins(self,coins,amount,n):
        if amount == 0:
            return 0
        if n== 0:   # return a very large val which will indicate sum amount is not possible
            return float('inf')
        take , notTake = float('inf'), float('inf')
        if coins[n-1] <= amount:
            take = min(take, 1 + self.MinCoins(coins,amount-coins[n-1], n))   # not taking minimum will give wrong ans.
        notTake = min(notTake, self.MinCoins(coins, amount, n-1))
        return min(take, notTake)


# Java Code 
"""
public class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int minimum = minCoins(coins, amount, n);
        if (minimum == Integer.MAX_VALUE)  // it means that amount is not possible so return -1.
            return -1;
        return minimum;
    }

    public int minCoins(int[] coins, int amount, int n) {
        if (amount == 0)
            return 0;
        if (n == 0)   // return a very large val which will indicate sum amount is not possible
            return Integer.MAX_VALUE;

        int take = Integer.MAX_VALUE, notTake = Integer.MAX_VALUE;
        if (coins[n - 1] <= amount) {
            int res = minCoins(coins, amount - coins[n - 1], n);
            if (res != Integer.MAX_VALUE)
                take = Math.min(take, 1 + res);  // not taking minimum will give wrong ans.
        }
        notTake = Math.min(notTake, minCoins(coins, amount, n - 1));

        return Math.min(take, notTake);
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
        int n = coins.size();
        int minimum = minCoins(coins, amount, n);
        if (minimum == INT_MAX)  // it means that amount is not possible so return -1.
            return -1;
        return minimum;
    }

    int minCoins(const std::vector<int>& coins, int amount, int n) {
        if (amount == 0)
            return 0;
        if (n == 0)   // return a very large val which will indicate sum amount is not possible
            return INT_MAX;

        int take = INT_MAX, notTake = INT_MAX;
        if (coins[n - 1] <= amount) {
            int res = minCoins(coins, amount - coins[n - 1], n);
            if (res != INT_MAX)
                take = std::min(take, 1 + res);  // not taking minimum will give wrong ans.
        }
        notTake = std::min(notTake, minCoins(coins, amount, n - 1));

        return std::min(take, notTake);
    }
};
"""

# Method 2: 
# Memoisation
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        dp= [[-1 for j in range(amount +1)] for i in range(n +1)]
        minimum= self.MinCoins(coins,amount,n, dp)
        if minimum== float('inf'):    # it means that amount is not possible so return -1.
            return -1
        return minimum

    def MinCoins(self,coins,amount,n, dp):
        if amount== 0:
            return 0
        if n== 0:   # retuen a very large val which will indicate sum amount is not possible
            return float('inf')
        if dp[n][amount] != -1:
            return dp[n][amount]
        take , notTake = float('inf'), float('inf')
        if coins[n-1] <= amount:
            take = min(take, 1 + self.MinCoins(coins,amount-coins[n-1], n, dp))
        notTake = min(notTake, self.MinCoins(coins, amount, n-1, dp))
        dp[n][amount] =  min(take, notTake)
        return dp[n][amount]



# Java Code 
"""
public class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[][] dp = new int[n + 1][amount + 1];
        for (int i = 0; i <= n; i++)
            java.util.Arrays.fill(dp[i], -1);

        int minimum = minCoins(coins, amount, n, dp);
        if (minimum == Integer.MAX_VALUE)    // it means that amount is not possible so return -1.
            return -1;
        return minimum;
    }

    public int minCoins(int[] coins, int amount, int n, int[][] dp) {
        if (amount == 0)
            return 0;
        if (n == 0)   // return a very large val which will indicate sum amount is not possible
            return Integer.MAX_VALUE;
        if (dp[n][amount] != -1)
            return dp[n][amount];

        int take = Integer.MAX_VALUE, notTake = Integer.MAX_VALUE;
        if (coins[n - 1] <= amount) {
            int res = minCoins(coins, amount - coins[n - 1], n, dp);
            if (res != Integer.MAX_VALUE)
                take = Math.min(take, 1 + res);
        }
        notTake = Math.min(notTake, minCoins(coins, amount, n - 1, dp));

        dp[n][amount] = Math.min(take, notTake);
        return dp[n][amount];
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int coinChange(std::vector<int>& coins, int amount) {
        int n = coins.size();
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(amount + 1, -1));
        int minimum = minCoins(coins, amount, n, dp);
        if (minimum == INT_MAX)    // it means that amount is not possible so return -1.
            return -1;
        return minimum;
    }

    int minCoins(const std::vector<int>& coins, int amount, int n, std::vector<std::vector<int>>& dp) {
        if (amount == 0)
            return 0;
        if (n == 0)   // return a very large val which will indicate sum amount is not possible
            return INT_MAX;
        if (dp[n][amount] != -1)
            return dp[n][amount];

        int take = INT_MAX, notTake = INT_MAX;
        if (coins[n - 1] <= amount) {
            int res = minCoins(coins, amount - coins[n - 1], n, dp);
            if (res != INT_MAX)
                take = std::min(take, 1 + res);
        }
        notTake = std::min(notTake, minCoins(coins, amount, n - 1, dp));

        return dp[n][amount] = std::min(take, notTake);
    }
};
"""


# method 3:
# Tabulation

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf') for j in range(amount + 1)] for i in range(n + 1)]

        # base case
        for i in range(n + 1):
            dp[i][0] = 0  # if amount== 0

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                take, notTake = float('inf'), float('inf')
                if coins[i - 1] <= j:
                    take = min(take, 1 + dp[i][j - coins[i - 1]])
                notTake = min(notTake, dp[i - 1][j])
                dp[i][j] = min(take, notTake)

        minimum = dp[n][amount]
        if minimum == float('inf'):  # it means that amount is not possible so return -1.
            return -1
        return minimum

# Java Code 
"""
class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[][] dp = new int[n + 1][amount + 1];

        // initialize dp table with +inf
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= amount; j++) {
                dp[i][j] = Integer.MAX_VALUE / 2;  // avoid overflow
            }
        }

        // base case
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 0;  // if amount == 0
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= amount; j++) {
                int take = Integer.MAX_VALUE / 2, notTake = Integer.MAX_VALUE / 2;
                if (coins[i - 1] <= j) {
                    take = Math.min(take, 1 + dp[i][j - coins[i - 1]]);
                }
                notTake = Math.min(notTake, dp[i - 1][j]);
                dp[i][j] = Math.min(take, notTake);
            }
        }

        int minimum = dp[n][amount];
        if (minimum == Integer.MAX_VALUE / 2) {  // amount not possible
            return -1;
        }
        return minimum;
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector<vector<int>> dp(n + 1, vector<int>(amount + 1, INT_MAX / 2));  // avoid overflow

        // base case
        for (int i = 0; i <= n; ++i) {
            dp[i][0] = 0;  // if amount == 0
        }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= amount; ++j) {
                int take = INT_MAX / 2, notTake = INT_MAX / 2;
                if (coins[i - 1] <= j) {
                    take = min(take, 1 + dp[i][j - coins[i - 1]]);
                }
                notTake = min(notTake, dp[i - 1][j]);
                dp[i][j] = min(take, notTake);
            }
        }

        int minimum = dp[n][amount];
        return (minimum == INT_MAX / 2) ? -1 : minimum;
    }
};
"""