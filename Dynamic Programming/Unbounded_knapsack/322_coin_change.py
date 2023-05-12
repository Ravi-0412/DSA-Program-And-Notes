# logic: totally same as Q no: "518. Coin Change II", except return value in base case
# method 1: By recursion
# correct only but showing time limit exceeded

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        minimum= self.MinCoins(coins,amount,n)
        if minimum== float('inf'):    # it means that amount is not possible so return -1.
            return -1
        return minimum
    
    def MinCoins(self,coins,amount,n):
        if amount== 0:
            return 0
        if n== 0:   # retuen a very large val which will indicate sum amount is not possible
            return float('inf')
        if coins[n-1]<= amount:
            return min((1+ self.MinCoins(coins,amount-coins[n-1],n)) ,self.MinCoins(coins,amount,n-1))
        return self.MinCoins(coins,amount,n-1)   # if coins[n-1] > amount


# method 2: memoization
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
        elif coins[n-1] <= amount:
            dp[n][amount]= min((1 + self.MinCoins(coins,amount-coins[n-1],n, dp)) ,self.MinCoins(coins,amount,n-1, dp))
        else:
            dp[n][amount]= self.MinCoins(coins, amount, n-1, dp)
        return dp[n][amount]


# other way: just change in base case
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        dp= [[-1 for j in range(amount +1)] for i in range(n +1)]
        minimum= self.MinCoins(coins,amount,n, dp)
        if minimum== float('inf'):    # it means that amount is not possible so return -1.
            return -1
        return minimum
    
    def MinCoins(self,coins,amount,n, dp):
        if n== 1:  # now we are left with some amount and one coin in our hand 
            return float('inf') if amount % coins[0] != 0 else amount// coins[0]   # if amount is divisible by the weight of available coin return that 
                                                                               # else not possible to form that amount so return very large value
        # now everything is same as before
        if dp[n][amount] != -1:
            return dp[n][amount]
        elif coins[n-1] <= amount:
            dp[n][amount]= min((1 + self.MinCoins(coins,amount-coins[n-1],n, dp)) ,self.MinCoins(coins,amount,n-1, dp))
        else:
            dp[n][amount]= self.MinCoins(coins, amount, n-1, dp)
        return dp[n][amount]
