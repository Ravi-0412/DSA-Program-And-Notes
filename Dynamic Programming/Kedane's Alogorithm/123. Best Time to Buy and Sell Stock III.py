# just same as pre Q: 122
# here we can only buy and sell if transaction is allowed, otherwise simply return zero
# so for checking the remaining txn we will need one more parameter.
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


# did all other things in Q: 188. totally same
# just replace k->2 


