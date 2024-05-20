# 1st method: Brute force O(n^2)

# 2nd method: Better than all.
# Very Easy and logical.
# logic: Q reduces to.. we have to find the maximum difference between two ele 
# and for getting max_diff first ele should be minimum_as_possible and second ele should be max_As_possible after buying Day

# We only need to change the buyDay if it's value is more than the curDay price.
# Else keep updating the ans.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyDay = 0
        ans= 0
        for i, num in enumerate(prices):
            if num < prices[buyDay]:
                # update the buyDay
                buyDay = i
            else:
                # update the ans.
                ans= max(ans, num - prices[buyDay])
        return ans


# 3rd method:
# Above logic only.
# logic: Keep track of min ele seen till now and check what profit we will get if we will sell the stock today.

# we have to find the minimum diff bw two ele.  
# here every ele has two choice either that can be min_till_now or may not not.
#  if not then update the ans if min then  max_profit will become '0'.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, least_so_far= 0, prices[0]
        # least_so_far will always store the minimum price among all till now
        for num in prices:
            least_so_far= min(least_so_far, num)
            max_profit= max(max_profit, num- least_so_far)   # keep updating the ans
        return max_profit


# java
"""
# Method 2:
class Solution {
    public int maxProfit(int[] prices) {
        int buyDay = 0;
        int ans = 0;
        
        for (int i = 0; i < prices.length; i++) {
            if (prices[i] < prices[buyDay]) {
                // update the buyDay
                buyDay = i;
            } else {
                // update the ans
                ans = Math.max(ans, prices[i] - prices[buyDay]);
            }
        }
        
        return ans;
    }
}


# Method 3:
class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int leastSoFar = prices[0];
        
        // Iterate through the array
        for (int num : prices) {
            // Update leastSoFar to be the minimum price encountered so far
            leastSoFar = Math.min(leastSoFar, num);
            // Calculate the potential profit and update maxProfit
            maxProfit = Math.max(maxProfit, num - leastSoFar);
        }
        return maxProfit;
    }
}
"""