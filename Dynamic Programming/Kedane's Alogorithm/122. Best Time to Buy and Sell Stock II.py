# just the same way we can earn max profit in stocks by holding and selling one stock at a time
# just buy the stock and sell if price increase & again purchase on day you sell and keep on adding the profit.
# and if we are sure that price will be decrease on next day just sit idle i.e profit= 0 here.

# Note: "you can buy it then immediately sell it on the same day" because of this statement,
# These logic are working because we are selling on curDay if price increases and again purchasing on same day.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        purchased = prices[0]
        for i in range(len(prices)) :
            if prices[i] > purchased:
                # Sell
                ans += prices[i] - purchased
                purchased = prices[i] # and again buy on same day
            else:
                purchased = prices[i]   # Purchase at lower price
        return ans

# combining if & else
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        purchased = prices[0]
        for i in range(len(prices)) :
            if prices[i] > purchased:
                ans += prices[i] - purchased
            purchased = prices[i]
        return ans
    
# Method 2: 
# When we will see what exactly we are doing above is : finding the sum of diff between 'i' and 'i-1' element.

# One good example: [5, 4,3,2,1,10]. In this profit will only get added for (6th - 5th) day & that's also the ans.
# So checking only the adjacent will give the correct ans.
# Time: O(n)

# unlimited no of transactions are allowed
def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:  # prices has increased so sell the last day purchased stock today.
                profit+= prices[i]- prices[i-1]
        return profit

# shorter way of writing above code
def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            profit+= max((prices[i]- prices[i-1]), 0)
        return profit


# Method 3:

# now by DP.
# How to think about DP?
# Ans: on every day we have two choices i.e either 1) buy or 2) sell.
# 1) Buy: if buy is allowed (if stock is not purchased before)
# In this we have two choices: i) We can buy on this day ii) We don't buy on this day
# 2) Not buy: (means only sell is allowed).
# In this also we have two choices: i) we sell on this day ii) we don't sell on this day. 

# Note vvi: since we can hold max one stock at a time, so to know stock has been bought already, we need one variable to check. 

# we also have to keep track of 'last bought date' to calculate the profit but no need of extra varible.
# To handle this we can subtract the price of day on which we will buy and call the further function.

# Note vvi: Here in recursive function, we are not buying and selling on same but still will give correct ans.

# e.g: [1, 7, 9]. This function will call give the ans like : 'buy on day1 and sell on day3' which is eqivalent to 
# 'buy on day1 & sell on day2' + 'buy on day2 and sell on day3' because value are increasing.
# same for e.g: [1, 7, 9, 12]. will give ans according to 'buy on day1 & sell on day4' which is eqivalent to purchasing and selling on next day.

# Note vvi: Keep this method in mind, this is basic of lot of similar q like this.

# Recursive way. Time: O(2^n), space: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(prices, 0, True)   # 2nd parameter is ind, 3rd telling buying is allowed or not
        # without index we can also do by using slicing one ele each time and for base case ccheck whether prices is empty or not

    def helper(self, prices, ind, buy):
        if ind== len(prices):
            return 0
        # if buying is allowed then we have two choices. 1)buy 2) don't buy
        # while buying you are investing so add with '-ve' and make buy= False 
        if buy:
            return max(-prices[ind] + self.helper(prices, ind+1, False), 0+ self.helper(prices, ind+1, True))
        # if buying is not allowed (only sell is allowed) then we have two choices. 1)sell today 2) dont sell today 
        else:
            return max(prices[ind] + self.helper(prices, ind+1, True), 0+ self.helper(prices, ind+1, False))

# shorter and concise
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(prices, 0, True)   

    def helper(self, prices, ind, buy):
        if ind== len(prices):
            return 0
        if buy:
            return max(-prices[ind] + self.helper(prices, ind+1, False), 0+ self.helper(prices, ind+1, True))
        return max(prices[ind] + self.helper(prices, ind+1, True), 0+ self.helper(prices, ind+1, False))

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
# range of variable changing including base case is: for ind, from '0' to 'n' and for buy-> 2 values.
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


# java
# memoisation
"""
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        
        // Initialize dp array with -1 (equivalent to -1 in the Python solution)
        for (int i = 0; i < n; i++) {
            dp[i][0] = -1;
            dp[i][1] = -1;
        }
        
        return helper(prices, 0, 1, dp);
    }

    private int helper(int[] prices, int ind, int buy, int[][] dp) {
        if (ind == prices.length) {
            return 0;
        }

        if (dp[ind][buy] != -1) {
            return dp[ind][buy];
        }

        int profit = 0;
        if (buy == 1) {
            profit = Math.max(-prices[ind] + helper(prices, ind + 1, 0, dp), 
                              helper(prices, ind + 1, 1, dp));
        } else {
            profit = Math.max(prices[ind] + helper(prices, ind + 1, 1, dp), 
                              helper(prices, ind + 1, 0, dp));
        }

        dp[ind][buy] = profit;
        return profit;
    }
}
"""

# further optimise space to four variable since we only need four variable to calculate the ans

# Note vvi: This approach is used in a lot of questions with slight variation.

# Related Q: 
# 1) 123. Best Time to Buy and Sell Stock III
# 2) 188. Best Time to Buy and Sell Stock IV
# 3) 309. Best Time to Buy and Sell Stock with Cooldown
# 4) 309. Best Time to Buy and Sell Stock with Cooldown
# 5) 714. Best Time to Buy and Sell Stock with Transaction Fee