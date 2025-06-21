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
        not_take = self.MinCoins(coins, amount, n-1)
        take = 0
        # else coins[n-1] <= amount:
        # we have two choice either take the cur one or not
        if coins[n-1] <= amount:
            take = self.MinCoins(coins, amount-coins[n-1], n)
        return take + not_take
    

# method 2:
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


# Method 3:
# Tabulation
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for j in range(amount + 1)] for i in range(n + 1)]

        # base case
        for i in range(n + 1):
            dp[i][0] = 1  # No need to check further simply return

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
