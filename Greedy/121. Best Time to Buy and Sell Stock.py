# 1st method: Brute force O(n^2)


# 2nd method: just like we buy and sell the stock in normal days
# logic: Q reduces to.. we have to find the maximum difference between two ele 
# and for getting max_diff first ele should be minimum_as_possible and second ele should be max_As_possible
# greedy approach
# time: O(n), space= O(1)
def maxProfit(self, prices: List[int]) -> int:
        ans, profit_if_sold_today, least_so_far= 0, 0, prices[0]
        for i in range(len(prices)):
            # first check if prices[i] is least_so_far # we will get the max profit by subtracting least_So_far only
            least_so_far= min(least_so_far, prices[i])  # will buy the stock on this day
            # now calculate the profit_if_sold_today and update the ans
            profit_if_sold_today= prices[i]- least_so_far  # we will get the max profit by subtracting least_So_far only
            # now update the ans
            ans= max(ans, profit_if_sold_today)
        return ans


# 3rd: very better and very easy
# we have to find the minimum diff bw two ele. And that we will get by purchasing at min_price and selling it on higher price as far as possible. 
# here very ele has two choice either that can be min_till_now or may not not. if not then update the ans if min then  max_profit will become '0'.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, least_so_far= 0, prices[0]
        # least_so_far will always store the minimum price among all till now
        for num in prices:
            least_so_far= min(least_so_far, num)
            max_profit= max(max_profit, num- least_so_far)   # keep updating the ans
        return max_profit


# Java
"""
public class Solution {
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length == 0) {
            return 0;
        }

        int maxProfit = 0;
        int leastSoFar = prices[0];

        for (int price : prices) {
            leastSoFar = Math.min(leastSoFar, price);
            maxProfit = Math.max(maxProfit, price - leastSoFar);
        }

        return maxProfit;
    }
}
"""