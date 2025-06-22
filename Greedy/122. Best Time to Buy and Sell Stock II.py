# Method 1 :

# just the same way we can earn max profit in stocks by holding and selling one stock at a time.
# just buy the stock and sell if price increase and if are sure that price will be decrease on next day just sit idle today &
# buy next day.
# greed approach as we can do in stock market trading. 
# unlimited no of transactions are allowed
# Time: O(n)

# method 1: 
def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        for i in range(1, len(prices)):
            if prices[i]> prices[i-1]:  # prices has increased so sell the last day purchased stock today.
                profit+= prices[i]- prices[i-1]
        return profit


# method 2: 
# shorter way of writing above code
def maxProfit(self, prices: List[int]) -> int:
        profit= 0
        for i in range(1, len(prices)):
            profit+= max((prices[i]- prices[i-1]), 0)
        return profit


