# just totally same as Q no: 122 just a very change when we sell the stock.
# if we sell next we can do purchase on 'i+2'th day, So just call the function for 'i+2' in case of sell.
#  simply copy pasted the code of that only.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(prices, 0, 1)   # 2nd parameter is ind, 3rd telling buying is allowed or not

    def helper(self, prices, ind, buy):
        if ind>= len(prices):
            return 0
        if buy:
            return max(-prices[ind] + self.helper(prices, ind+1, 0), 0+ self.helper(prices, ind+1, 1))
        # if we sell we can't buy next day for write 'ind+2' instead of 'ind+1'. this is the only change
        else:
            return max(prices[ind] + self.helper(prices, ind+2, 1), 0+ self.helper(prices, ind+1, 0))

# memoization
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp= [[-1 for j in range(2)] for i in range(len(prices))]
        return self.helper(prices, 0, 1, dp)   # 2nd parameter is ind, 3rd telling buying is allowed or not

    def helper(self, prices, ind, buy, dp):
        if ind>= len(prices):
            return 0
        if dp[ind][buy]!= -1:
            return dp[ind][buy]
        if buy:
            dp[ind][buy]= max(-prices[ind] + self.helper(prices, ind+1, 0,dp), 0+ self.helper(prices, ind+1, 1,dp))
        # if we sell we can't buy next day for write 'ind+2' instead of 'ind+1'. this is the only change
        else:
            dp[ind][buy]= max(prices[ind] + self.helper(prices, ind+2, 1,dp), 0+ self.helper(prices, ind+1, 0,dp))
        return dp[ind][buy]

# Top Down
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n= len(prices)
        dp= [[0 for j in range(2)] for i in range(n +2)]  # (n+2) because we need in case we sell otherwise it will out of bound for 'n-1'
        # for easier just write the variable name in loop same as variable changing in recursive call
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    dp[ind][buy]= max(-prices[ind] + dp[ind+1][0], 0+ dp[ind+1][1])
                else:
                    dp[ind][buy]= max(prices[ind] + dp[ind+2][1], 0+ dp[ind+1][0])
        return dp[0][1]  # you have called the function for (0,1) so at last return that

