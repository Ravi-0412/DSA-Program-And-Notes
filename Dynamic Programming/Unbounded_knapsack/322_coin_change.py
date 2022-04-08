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

        