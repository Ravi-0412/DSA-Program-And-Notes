# Method 1: 

# just same as pre Q: 122
# here we can only buy and sell if transaction is allowed, otherwise simply return zero
# so for checking the remaining txn we will need one more parameter.
# Time : O(2^N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper(prices, 0, 1,  2)  # 2nd para: ind, 3rd: buying is allowed or not, 4th: no of transactions allowed
    
    def helper(self, prices, ind, buy, txn):
        if txn== 0 or ind == len(prices): 
            return 0
        if buy:
            return max(-prices[ind] + self.helper(prices, ind+1, 0, txn ), 0+ self.helper(prices, ind+1, 1, txn))
        else:
            return max(prices[ind] + self.helper(prices, ind+1, 1, txn-1), 0+ self.helper(prices, ind+1, 0, txn))

# Method 2:
"""
if buy:
            # Path A: Buy today + Path B: Don't buy today
            res = max(-prices[ind] + self.helper(prices, ind + 1, 0, txn, memo), 
                      0 + self.helper(prices, ind + 1, 1, txn, memo))
        else:
            # Path A: Sell today (completes txn) + Path B: Don't sell today
            res = max(prices[ind] + self.helper(prices, ind + 1, 1, txn - 1, memo), 
                      0 + self.helper(prices, ind + 1, 0, txn, memo))
        
        # Save the result in memo before returning
        memo[state] = res

Q) 'res' is under if-else then how are we using outside that ?
In Python, unlike some other languages (like Java or C++), variables defined inside an 
if-else block are not local to that block. They are local to the function.

Total complexity: O(N * 2 * 3)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memo stores: (ind, buy, txn) -> max_profit
        memo = {}
        return self.helper(prices, 0, 1, 2, memo)
    
    def helper(self, prices, ind, buy, txn, memo):
        # Base Cases
        if txn == 0 or ind == len(prices): 
            return 0
        
        # Check if we have already solved this exact state
        state = (ind, buy, txn)
        if state in memo:
            return memo[state]
        
        if buy:
            # Path A: Buy today + Path B: Don't buy today
            res = max(-prices[ind] + self.helper(prices, ind + 1, 0, txn, memo), 
                      0 + self.helper(prices, ind + 1, 1, txn, memo))
        else:
            # Path A: Sell today (completes txn) + Path B: Don't sell today
            res = max(prices[ind] + self.helper(prices, ind + 1, 1, txn - 1, memo), 
                      0 + self.helper(prices, ind + 1, 0, txn, memo))
        
        # Save the result in memo before returning
        memo[state] = res
        return res

# Memoisation using python inbuilt function

from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None) # Automatically memoizes the function
        def helper(ind, buy, txn):
            if txn == 0 or ind == len(prices): 
                return 0
            if buy:
                return max(-prices[ind] + helper(ind + 1, 0, txn), 
                           helper(ind + 1, 1, txn))
            else:
                return max(prices[ind] + helper(ind + 1, 1, txn - 1), 
                           helper(ind + 1, 0, txn))
        
        return helper(0, 1, 2)

# method 3: 
# Tabulation

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # 3D Table: dp[n+1][2][3]
        # Initialized with 0, which covers your base cases:
        # 1. if ind == len(prices) -> return 0
        # 2. if txn == 0 -> return 0
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]

        # Start from the last day and move backwards (just like recursion)
        for ind in range(n - 1, -1, -1):
            for buy in range(2):
                # txn 0 is already 0 from initialization, so we start from 1
                for txn in range(1, 3): 
                    
                    if buy:
                        # Corresponds to: max(-prices[ind] + helper(ind+1, 0, txn), 0 + helper(ind+1, 1, txn))
                        dp[ind][buy][txn] = max(-prices[ind] + dp[ind+1][0][txn], 
                                                0 + dp[ind+1][1][txn])
                    else:
                        # Corresponds to: max(prices[ind] + helper(ind+1, 1, txn-1), 0 + helper(ind+1, 0, txn))
                        dp[ind][buy][txn] = max(prices[ind] + dp[ind+1][1][txn-1], 
                                                0 + dp[ind+1][0][txn])
                                                
        # We want the answer starting from day 0, with buying allowed, and 2 transactions left
        return dp[0][1][2]

# method 4:
# Space optimised
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        # 'after' represents the dp[ind+1] layer
        after = [[0 for _ in range(3)] for _ in range(2)]
        
        for ind in range(n - 1, -1, -1):
            # 'curr' represents the dp[ind] layer we are currently filling
            curr = [[0 for _ in range(3)] for _ in range(2)]
            
            for buy in range(2):
                for txn in range(1, 3):
                    if buy:
                        curr[buy][txn] = max(-prices[ind] + after[0][txn], 
                                             after[1][txn])
                    else:
                        curr[buy][txn] = max(prices[ind] + after[1][txn-1], 
                                             after[0][txn])
            # Move curr to after for the next day iteration
            after = curr
            
        return after[1][2]

# Follow ups: 
# did all other things in Q: 188. totally same
# just replace k->2 


