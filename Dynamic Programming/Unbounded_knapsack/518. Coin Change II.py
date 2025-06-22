# method 1: 
# Just same as 'unbounded knapsack'.
# Recursive

# Logic: At each step we have choice to not_take and we can only take if 'coins[n-1] <= amount'.
# Just combining the above three function call into two function call.
# Return sum of take + not_take.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n= len(coins)
        return self.MinCoins(coins,amount,n)

    def MinCoins(self,coins,amount,n):
        if amount== 0:
            # No need to check further simply return
            return 1
        if n== 0:
            # amount != 0 but n == 0 means there is no possible way
            return 0
<<<<<<< HEAD
        if coins[n-1] > amount:
            # Only one option don't take
            return self.MinCoins(coins, amount, n-1)
        # else coins[n-1] <= amount:
        # we have two choice either take the cur one or not
        return self.MinCoins(coins, amount-coins[n-1], n) + self.MinCoins(coins, amount, n-1)

# Java Code 
"""
public class Solution {
    public int change(int amount, int[] coins) {
        int n = coins.length;
        return minCoins(coins, amount, n);
    }

    public int minCoins(int[] coins, int amount, int n) {
        if (amount == 0)
            // No need to check further simply return
            return 1;
        if (n == 0)
            // amount != 0 but n == 0 means there is no possible way
            return 0;
        if (coins[n - 1] > amount)
            // Only one option don't take
            return minCoins(coins, amount, n - 1);
        // else coins[n - 1] <= amount:
        // we have two choices: either take the cur one or not
        return minCoins(coins, amount - coins[n - 1], n) + minCoins(coins, amount, n - 1);
    }
}
"""
# C++ Code
"""
class Solution {
public:
    int change(int amount, std::vector<int>& coins) {
        int n = coins.size();
        return minCoins(coins, amount, n);
    }

private:
    int minCoins(const std::vector<int>& coins, int amount, int n) {
        if (amount == 0)
            // No need to check further simply return
            return 1;
        if (n == 0)
            // amount != 0 but n == 0 means there is no possible way
            return 0;
        if (coins[n - 1] > amount)
            // Only one option don't take
            return minCoins(coins, amount, n - 1);
        // else coins[n - 1] <= amount:
        // we have two choices: either take the cur one or not
        return minCoins(coins, amount - coins[n - 1], n) + minCoins(coins, amount, n - 1);
    }
};
"""

# Other way to write
# Better one

# Logic: At each step we have choice to not_take and we can only take if 'coins[n-1] <= amount'.

# Just combining the above three function call into two function call.

# Return sum of take + not_take.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n= len(coins)
        return self.MinCoins(coins,amount,n)

    def MinCoins(self,coins,amount,n):
        if amount== 0:
            return 1
        if n== 0:
            return 0
=======
>>>>>>> a40de18 (verified Binary Search and DP)
        not_take = self.MinCoins(coins, amount, n-1)
        take = 0
        # else coins[n-1] <= amount:
        # we have two choice either take the cur one or not
        if coins[n-1] <= amount:
            take = self.MinCoins(coins, amount-coins[n-1], n)
        return take + not_take
    
# Java Code 
"""
public class Solution {
    public int change(int amount, int[] coins) {
        int n = coins.length;
        return minCoins(coins, amount, n);
    }

<<<<<<< HEAD
    public int minCoins(int[] coins, int amount, int n) {
        if (amount == 0)
            return 1;
        if (n == 0)
            return 0;

        int notTake = minCoins(coins, amount, n - 1);
        int take = 0;
        if (coins[n - 1] <= amount)
            take = minCoins(coins, amount - coins[n - 1], n);

        return take + notTake;
    }
}
"""
# C++ Code
"""
class Solution {
public:
    int change(int amount, std::vector<int>& coins) {
        int n = coins.size();
        return minCoins(coins, amount, n);
    }

private:
    int minCoins(const std::vector<int>& coins, int amount, int n) {
        if (amount == 0)
            return 1;
        if (n == 0)
            return 0;

        int notTake = minCoins(coins, amount, n - 1);
        int take = 0;
        if (coins[n - 1] <= amount)
            take = minCoins(coins, amount - coins[n - 1], n);

        return take + notTake;
    }
};
"""

# method 2: Memoization
# logic:  # just exactly same as ' count no of subsets with a given sum'
# just write the logic of unbounded kanpsack.

=======
# method 2:
>>>>>>> a40de18 (verified Binary Search and DP)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for j in range(amount + 1)] for i in range(n + 1)]
        return self.MinCoins(coins, amount, n, dp)

    def MinCoins(self, coins, amount, n, dp):
        if amount == 0:
            # No need to check further simply return
            return 1
        if n == 0:
            # amount != 0 but n == 0 means there is no possible way
            return 0
        if dp[n][amount] != -1:
            return dp[n][amount]
        not_take = self.MinCoins(coins, amount, n - 1, dp)
        take = 0
        # else coins[n-1] <= amount:
        # we have two choice either take the cur one or not
        if coins[n - 1] <= amount:
            take = self.MinCoins(coins, amount - coins[n - 1], n, dp)
        dp[n][amount] = take + not_take
        return dp[n][amount]

<<<<<<< HEAD
# Java Code 
"""
public class Solution {
    public int change(int amount, int[] coins) {
        int N = coins.length;
        int[][] dp = new int[N + 1][amount + 1];
        for (int i = 0; i <= N; i++) {
            java.util.Arrays.fill(dp[i], -1);
        }
        return minCoins(N, coins, amount, dp);
    }

    public int minCoins(int n, int[] arr, int sum, int[][] dp) {
        if (sum == 0)  // we have to find the ways so first check 'if sum==0'
            return 1;
        if (n == 0)    // means sum!= 0 and n==0
            return 0;
        if (dp[n][sum] != -1)
            return dp[n][sum];
        if (arr[n - 1] > sum)
            dp[n][sum] = minCoins(n - 1, arr, sum, dp);
        else  // arr[n -1] <= sum
            dp[n][sum] = minCoins(n, arr, sum - arr[n - 1], dp) + minCoins(n - 1, arr, sum, dp);
        return dp[n][sum];
    }
}
"""
# C++ Code
"""
class Solution {
public:
    int change(int amount, std::vector<int>& coins) {
        int N = coins.size();
        std::vector<std::vector<int>> dp(N + 1, std::vector<int>(amount + 1, -1));
        return minCoins(N, coins, amount, dp);
    }

    int minCoins(int n, const std::vector<int>& arr, int sum, std::vector<std::vector<int>>& dp) {
        if (sum == 0)  // we have to find the ways so first check 'if sum==0'
            return 1;
        if (n == 0)    // means sum!= 0 and n==0
            return 0;
        if (dp[n][sum] != -1)
            return dp[n][sum];
        if (arr[n - 1] > sum)
            dp[n][sum] = minCoins(n - 1, arr, sum, dp);
        else  // arr[n -1] <= sum
            dp[n][sum] = minCoins(n, arr, sum - arr[n - 1], dp) + minCoins(n - 1, arr, sum, dp);
        return dp[n][sum];
    }
};
"""

# method 3: Bottom up Approach
=======

# Method 3:
# Tabulation
>>>>>>> a40de18 (verified Binary Search and DP)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]

        # base case
        for i in range(n + 1):
            dp[i][0] = 1  # No need to check further simply return

<<<<<<< HEAD
# Java Code 
"""
public class Solution {
    public int change(int sum, int[] arr) {
        int N = arr.length;

        // 1st initialise the matrix properly, just like 'no of subsets with a given sum'
        int[][] dp = new int[N + 1][sum + 1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= sum; j++) {
                if (j == 0)
                    dp[i][j] = 1;
            }
        }

        // exactly same as "count the no of subsets with a given sum"
        // only change the included condition (like unbounded knapsack)
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= sum; j++) {
                if (arr[i - 1] > j)
                    dp[i][j] = dp[i - 1][j];
                else // ways possible including this ele (unbounded one) + ways possible without including it
                    dp[i][j] = dp[i][j - arr[i - 1]] + dp[i - 1][j];
            }
        }

        return dp[N][sum];
    }
}
"""
# C++ Code
"""
class Solution {
public:
    int change(int sum, std::vector<int>& arr) {
        int N = arr.size();

        // 1st initialise the matrix properly, just like 'no of subsets with a given sum'
        std::vector<std::vector<int>> dp(N + 1, std::vector<int>(sum + 1, 0));
        for (int i = 0; i <= N; ++i) {
            for (int j = 0; j <= sum; ++j) {
                if (j == 0)
                    dp[i][j] = 1;
            }
        }

        // exactly same as "count the no of subsets with a given sum"
        // only change the included condition (like unbounded knapsack)
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= sum; ++j) {
                if (arr[i - 1] > j)
                    dp[i][j] = dp[i - 1][j];
                else // ways possible including this ele (unbounded one) + ways possible without including it
                    dp[i][j] = dp[i][j - arr[i - 1]] + dp[i - 1][j];
            }
        }

        return dp[N][sum];
    }
};
"""


# Similar Q: 
# 1) 322. Coin Change
# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Dynamic%20Programming/Unbounded_knapsack/322.%20Coin%20Change.py
=======
        for i in range(1, n + 1):
            for j in range(amount + 1):
                not_take = dp[i - 1][j]
                take = 0
                # else coins[n-1] <= amount:
                # we have two choice either take the cur one or not
                if coins[i - 1] <= j:
                    take = dp[i][j - coins[i - 1]]
                dp[i][j] = take + not_take

        return dp[n][amount]
>>>>>>> a40de18 (verified Binary Search and DP)
