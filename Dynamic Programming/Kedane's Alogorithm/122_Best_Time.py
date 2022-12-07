# just the same way we can earn max profit in stocks by holding and selling one stock at a time
# just buy the stock and sell if price increase and if are sure that price will be decrease on next day just sit idle. 
# Time: O(n)

# unlimited no of transactions are allowed
def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        for i in range(1, len(prices)):
            if prices[i]> prices[i-1]:  # prices has increased so sell the last day purchased stock today.
                profit+= prices[i]- prices[i-1]
        return profit

# shorter way of writing above code
def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        for i in range(1, len(prices)):
            profit+= max((prices[i]- prices[i-1]), 0)
        return profit

# same logic
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit= 0
        for i in range(1,len(prices)):
            max_profit+= prices[i]- prices[i-1] if prices[i]- prices[i-1] >0 else 0
        return max_profit


# now by DP
# since we can hold max one stock at a time, so to know stock has been bought already we need one variable to check 
# for every ele we have two choices in each case if 1) buying allowed(buy or not buy)  2) buying not allowed(sell or not sell)

# Recursive way. Time: O(2^n), space: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(prices, 0, True)   # 2nd parameter is ind, 3rd telling buying is allowed or not
        # without index we can also do by using slicing one ele each time and for base case ccheck whether prices is empty or not

    def helper(self, prices, ind, buy):
        if ind== len(prices):
            return 0
        profit= 0
        # if buying is allowed then we have two choices. 1)buy 2) don't buy
        # while buying you are investing so add with '-ve' and make buy= False 
        if buy:
            profit= max(-prices[ind] + self.helper(prices, ind+1, False), 0+ self.helper(prices, ind+1, True))
        # if buying is not allowed then we have two choices. 1)sell today 2) dont sell today 
        else:
            profit= max(prices[ind] + self.helper(prices, ind+1, True), 0+ self.helper(prices, ind+1, False))
        return profit

# By memoization. time: O(n*2)= space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp= [[-1 for j in range(2)] for i in range(len(prices))]
        return self.helper(prices, 0, True, dp)   # 2nd parameter is ind, 3rd telling buying is allowed or not
        # without index we can also do by using slicing one ele each time and for base case ccheck whether prices is empty or not

    def helper(self, prices, ind, buy, dp):
        if ind== len(prices):
            return 0
        profit= 0
        if dp[ind][buy]!= -1:
            return dp[ind][buy]
        # if buying is allowed then we have two choices. 1)buy 2) don't buy
        # while buying you are investing so add with '-ve' and make buy= False 
        if buy:
            profit= max(-prices[ind] + self.helper(prices, ind+1, False,dp), 0+ self.helper(prices, ind+1, True,dp))
        # if buying is not allowed then we have two choices. 1)sell today 2) dont sell today 
        else:
            profit= max(prices[ind] + self.helper(prices, ind+1, True,dp), 0+ self.helper(prices, ind+1, False,dp))
        dp[ind][buy]= profit
        return dp[ind][buy]

# other way that will work always and easy nothing to think
# range of variable changing is: for ind, from '0' to 'n' and for buy-> 2 values.
# so make 2d array with size acc ro this only and update the ans when you get. this will cover also the base case
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp= [[-1 for j in range(2)] for i in range(len(prices) +1)]
        return self.helper(prices, 0, True, dp)   # 2nd parameter is ind, 3rd telling buying is allowed or not
        # without index we can also do by using slicing one ele each time and for base case ccheck whether prices is empty or not

    def helper(self, prices, ind, buy, dp):
        if ind== len(prices):
            dp[ind][buy]= 0
            return dp[ind][buy]
        profit= 0
        if dp[ind][buy]!= -1:
            return dp[ind][buy]
        # if buying is allowed then we have two choices. 1)buy 2) don't buy
        # while buying you are investing so add with '-ve' and make buy= False 
        if buy:
            profit= max(-prices[ind] + self.helper(prices, ind+1, False,dp), 0+ self.helper(prices, ind+1, True,dp))
        # if buying is not allowed then we have two choices. 1)sell today 2) dont sell today 
        else:
            profit= max(prices[ind] + self.helper(prices, ind+1, True,dp), 0+ self.helper(prices, ind+1, False,dp))
        dp[ind][buy]= profit
        return dp[ind][buy]


# Top Down
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        dp= [[0 for j in range(2)] for i in range(n +1)]
        # for easier just write the variable name in loop same as variable changing in recursive call
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                # now just copy paste the recursive code and replace recursive call by dp seeing the variable value inside the recursive call.
                profit= 0 
                if buy:
                    profit= max(-prices[ind] + dp[ind+1][0], 0+ dp[ind+1][1])
                else:
                    profit= max(prices[ind] + dp[ind+1][1], 0+ dp[ind+1][0])
                dp[ind][buy]= profit
        return dp[0][1]  # you have called the function for (0,1) so at last return that

# optimising space: 
# for calculating the value in curr row we are dependent only on pre row values and each row there is only two ele.
# space: O(4), 2 col 1D array for pre and curr that's it
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        pre= [0 for i in range(2)]
        for ind in range(n-1,-1,-1):
            curr= [0 for i in range(2)]
            for buy in range(2):
                profit= 0 
                if buy:
                    profit= max(-prices[ind] + pre[0], 0+ pre[1])
                else:
                    profit= max(prices[ind] + pre[1], 0+ pre[0])
                curr[buy]= profit
            pre= curr.copy()
        return pre[1]  

# further optimise space to four variable since we only need four variable to calculate the ans

# most optimised and easier is the top methods that i did