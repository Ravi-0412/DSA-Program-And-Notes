# just the same way we can earn max profit in stocks by holding and selling one stock at a time
# buy the stock on first day when price starts decreasing and sell the stock when on the last day(of increasing price) 
# before start decreasing again. And repeat the same for max price
# Time: O(n)

def maxProfit(self, prices: List[int]) -> int:
        # here multiple transactions are allowed i.e
        # you can buy and sell when prices will decrease and sell when price stop increases
        profit= 0
        for i in range(1, len(prices)):
            # if next day price is more then add the diff to the profit else do nothing
            if prices[i]> prices[i-1]:
                profit+= prices[i]- prices[i-1]
            # At last return the profit
        return profit

# shorter way of writing above code
def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        for i in range(1, len(prices)):
            profit+= max((prices[i]- prices[i-1]), 0)
        return profit