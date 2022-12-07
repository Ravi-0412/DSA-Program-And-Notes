# just copy pasted the code of Q: 122 and while selling subtracted the transaction fee that's it.

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.helper(prices, 0, 1, fee)   # 2nd parameter is ind, 3rd telling buying is allowed or not

    def helper(self, prices, ind, buy, fee):
        if ind== len(prices):
            return 0
        if buy:
            return max(-prices[ind] + self.helper(prices, ind+1, 0, fee), 0+ self.helper(prices, ind+1, 1, fee))
        else: # just subtract the transaction fee when you sell, this is teh only change we have to do.
            return max(prices[ind] - fee + self.helper(prices, ind+1, 1, fee), 0+ self.helper(prices, ind+1, 0, fee))
        