# Just same as 'unbounded knapsack'.

# method 1: Recursive

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
        if coins[n-1] > amount:
            # Only one option don't take
            return self.MinCoins(coins, amount, n-1)
        # else coins[n-1] <= amount:
        # we have two choice either take the cur one or not
        return self.MinCoins(coins, amount-coins[n-1], n) + self.MinCoins(coins, amount, n-1)
    

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
        not_take = self.MinCoins(coins, amount, n-1)
        take = 0
        if coins[n-1] <= amount:
            take = self.MinCoins(coins, amount-coins[n-1], n)
        return take + not_take
    


# method 2: Memoization
# logic:  # just exactly same as ' count no of subsets with a given sum'
# just write the logic of unbounded kanpsack.

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N= len(coins)
        dp= [[-1 for i in range(amount +1)] for i in range(N +1)]   
        return self.MinCoins(N, coins, amount, dp)
    
    def MinCoins(self, n, arr, sum, dp):
        if sum== 0:  # we have to find the ways so first check 'if sum==0'
            return 1
        if n== 0:   # means sum!= 0 and n==0
            return 0
        if dp[n][sum] != -1: 
            return dp[n][sum]
        if arr[n -1] > sum:
            dp[n][sum]= self.MinCoins(n -1, arr, sum, dp)
        else:   # arr[n -1] <= sum
            dp[n][sum]= self.MinCoins(n, arr, sum- arr[n-1], dp) + self.MinCoins(n -1, arr, sum, dp)
        return dp[n][sum]


# method 3: Bottom up Approach
class Solution:
    def change(self, sum: int, arr: List[int]) -> int:
        N= len(arr)

        # 1st initialse the matrix properly, just like 'no of subsets with a given sum'
        dp= [[0 for i in range(sum+1) ] for i in range(N+1)]
        for i in range(N+1):
            for j in range(sum+1):
                if j==0:
                    dp[i][j]= 1
        # exactyle same as "count the no of subsets with a given sum" . only change the included condition(like unbouded knapsack)       
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]> j: 
                    dp[i][j]= dp[i-1][j]
                else: # ways possible including this ele(unbounded one) + ways possible without including it
                    dp[i][j]= dp[i][j-arr[i-1]] + dp[i-1][j]
        return dp[N][sum]



# Similar Q: 
# 1) 322. Coin Change
# https://github.com/Ravi-0412/DSA-Program-And-Notes/blob/main/Dynamic%20Programming/Unbounded_knapsack/322.%20Coin%20Change.py