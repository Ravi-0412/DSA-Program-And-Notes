# 1st method: 
# Brute force O(n^2)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        # Try buying on each day i
        for i in range(n):
            # Try selling on each future day j > i
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

# Java Code
"""
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int max_profit = 0;

        // Try buying on each day i
        for (int i = 0; i < n; i++) {
            // Try selling on each future day j > i
            for (int j = i + 1; j < n; j++) {
                int profit = prices[j] - prices[i];
                if (profit > max_profit) {
                    max_profit = profit;
                }
            }
        }
        return max_profit;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int max_profit = 0;

        // Try buying on each day i
        for (int i = 0; i < n; ++i) {
            // Try selling on each future day j > i
            for (int j = i + 1; j < n; ++j) {
                int profit = prices[j] - prices[i];
                if (profit > max_profit) {
                    max_profit = profit;
                }
            }
        }
        return max_profit;
    }
};
"""

# 2nd method: 
# just like we buy and sell the stock in normal days
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

# Java Code
"""
class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0;
        int profit_if_sold_today = 0;
        int least_so_far = prices[0];

        for (int i = 0; i < prices.length; i++) {
            // check if prices[i] is the new least_so_far
            least_so_far = Math.min(least_so_far, prices[i]);  // will buy the stock on this day

            // calculate profit_if_sold_today based on least_so_far
            profit_if_sold_today = prices[i] - least_so_far;

            // update ans with the maximum profit seen so far
            ans = Math.max(ans, profit_if_sold_today);
        }
        return ans;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int profit_if_sold_today = 0;
        int least_so_far = prices[0];

        for (int i = 0; i < prices.size(); ++i) {
            // check if prices[i] is the new least_so_far
            least_so_far = min(least_so_far, prices[i]);  // will buy the stock on this day

            // calculate profit_if_sold_today based on least_so_far
            profit_if_sold_today = prices[i] - least_so_far;

            // update ans with the maximum profit seen so far
            ans = max(ans, profit_if_sold_today);
        }
        return ans;
    }
};
"""

# 3rd: 
# very better and very easy
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

# Java Code
"""
class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;
        int least_so_far = prices[0]; // least_so_far will always store the minimum price among all till now

        for (int num : prices) {
            least_so_far = Math.min(least_so_far, num);
            max_profit = Math.max(max_profit, num - least_so_far); // keep updating the ans
        }

        return max_profit;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int least_so_far = prices[0]; // least_so_far will always store the minimum price among all till now

        for (int num : prices) {
            least_so_far = min(least_so_far, num);
            max_profit = max(max_profit, num - least_so_far); // keep updating the ans
        }

        return max_profit;
    }
};
"""