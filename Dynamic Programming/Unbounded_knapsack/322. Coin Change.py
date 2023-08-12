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



# My mistake:
# 2nd case 'coins[ind] <= amount' will also run everytime but we have to run only one cases not both.
# That's why geting 'recursion depth increases'.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def solve(ind , amount):
            if amount == 0:
                return 0
            if ind == len(coins):
                return float('inf')
            ans = float('inf')
            if coins[ind] > amount:
            # Only one option don't take
                ans = solve(ind + 1, amount)
            # else coins[ind] <= amount:
            # we have two choice either take the cur one or not
            ans = min(ans , 1 + solve(ind, amount- coins[ind]) , solve(ind + 1 , amount))   # this will run always...
            return ans

        ans = solve(0 , amount)
        return ans if ans != float('inf') else -1
    

# Above method correct one
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def solve(ind , amount):
            if amount == 0:
                return 0
            if ind == len(coins):
                return float('inf')
            ans = float('inf')
            if coins[ind] > amount:
            # Only one option don't take
                ans = solve(ind + 1, amount)
                # return ans
            if coins[ind] <= amount:
            # we have two choice either take the cur one or not
                ans = min(ans , 1 + solve(ind, amount- coins[ind]) , solve(ind + 1 , amount))
            return ans

        ans = solve(0 , amount)
        return ans if ans != float('inf') else -1


# Note vvi : Why returning directly (method :1) is working.
# Since here only one case will execute and after that our ans will follow that path only so we can return direct also.
