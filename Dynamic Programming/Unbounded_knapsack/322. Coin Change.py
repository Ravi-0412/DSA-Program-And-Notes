# logic: totally same as Q no: "518. Coin Change II", except return value in base case
# method 1: By recursion(TLE)

# logic: when we take any coin then we will add '+1' .
# For ans we will take minimum of possible cases.


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
            return min(1+ self.MinCoins(coins,amount-coins[n-1],n) ,self.MinCoins(coins,amount,n-1))
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
            dp[n][amount]= min(1 + self.MinCoins(coins,amount-coins[n-1],n, dp) ,self.MinCoins(coins,amount,n-1, dp))
        else:
            dp[n][amount]= self.MinCoins(coins, amount, n-1, dp)
        return dp[n][amount]


# Other way
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
