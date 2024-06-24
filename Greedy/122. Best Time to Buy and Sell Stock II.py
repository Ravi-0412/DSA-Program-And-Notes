# just the same way we can earn max profit in stocks by holding and selling one stock at a time.
# just buy the stock and sell if price increase and if are sure that price will be decrease on next day just sit idle today &
# buy next day.
# greed approach as we can do in stock market trading. 
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

# java
"""
public class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1]) {  // prices have increased so sell the last day purchased stock today
                profit += prices[i] - prices[i - 1];
            }
        }
        return profit;
    }
}
"""