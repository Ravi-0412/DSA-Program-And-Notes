# method 1: By recursion
# correct only but showing time limit exceeded

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        minimum= self.MinCoins(coins,amount,n)
        if minimum== 99999999:
            return -1
        return minimum
    def MinCoins(self,coins,amount,n):
        ans= 0
        if n==0 and (amount==0 or amount!=0):  # when you want to form an amount with zero number of coins
            return 99999999                    # then it is not possible so, initialise it with any greater value
        if n!=0 and amount==0:                 # when you want to form an amont equal to zero with any number
                                               # of coin(no of coin>0), then only possiblity is not include that coin. 
            return 0
        
        if coins[n-1]<= amount:
            tempAns= min((1+ self.MinCoins(coins,amount-coins[n-1],n)) ,self.MinCoins(coins,amount,n-1))
            ans+= tempAns
        else:
            tempAns= self.MinCoins(coins,amount,n-1)
            ans+= tempAns
        return ans

# method 2: memoization
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        dp= [[-1 for j in range(amount +1)] for i in range(n +1)]
        minimum= self.MinCoins(coins,amount,n, dp)
        if minimum== 99999999:  # if equal to the larger val that we gave into the base case , means that amount is not possible so return -1
            return -1
        return minimum
    def MinCoins(self,coins,amount,n, dp):
        if n==0 and amount!=0 :     # not possible to make any amount with no coin available
            return 99999999         # so return any very large val (max till 'maxint -1' as we are already adding '1' when we are including any coin)
        if (n!= 0 or n==0)  and amount==0:  # no coins is needed to form amount = 0
            return 0        # so return 0
        # this is the additional case we have to handle separately in this Q but got submiited without this condition also
        if n== 1:  # now we are left with some amount and one coin in our hand 
            return 99999999 if amount % coins[0] != 0 else amount// coins[0]   # if amount is divisible by the weight of available coin return that 
                                                                               # else not possible to form that amount so return very large value
        # now everything is same as before
        if dp[n][amount] != -1:
            return dp[n][amount]
        elif coins[n-1] <= amount:
            dp[n][amount]= min((1 + self.MinCoins(coins,amount-coins[n-1],n, dp)) ,self.MinCoins(coins,amount,n-1, dp))
        else:
            dp[n][amount]= self.MinCoins(coins, amount, n-1, dp)
        return dp[n][amount]

