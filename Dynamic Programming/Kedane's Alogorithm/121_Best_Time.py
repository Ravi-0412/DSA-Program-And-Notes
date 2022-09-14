# 1st method: Brute force O(n^2)

# 2nd method using double pointer
def maxProfit(self, prices: List[int]) -> int:
        # you are allowed to buy and sell only one time
        # using two pointer approach
        # left pointer will tell buying day and right pointer will tell the selling day
        left, right, profit, n= 0, 1, 0, len(prices)
        # We always want our left pointer to be minimum
        while right< n:
            if prices[left] >= prices[right]:
                # then make the left point to right
                left= right
            else:  # prices[right]> prices[left]
                # then only incr the right pointer by 1 as we are geeting profit
                profit= max(profit, prices[right]- prices[left])
            # right will always increment by 1
            right= right+1
        return profit 


# 3rd method: just like we buy and sell the stock in normal days
# greedy approach
# time: O(n), space= O(1)
def maxProfit(self, prices: List[int]) -> int:
        ans, profit_if_sold_today, least_so_far= 0, 0, prices[0]
        for i in range(len(prices)):
            # first check if prices[i] is least_so_far # we will get the max profit by subtracting least_So_far only
            least_so_far= min(least_so_far, prices[i])
            # now calculate the profit_if_sold_today and update the ans
            profit_if_sold_today= prices[i]- least_so_far  # we will get the max profit by subtracting least_So_far only
            # now update the ans
            ans= max(ans, profit_if_sold_today)
        return ans


# this i did at revision time(12/07/2022)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max, max_profit, least_so_far= 0, 0, prices[0]
        # least_so_far will always store the minimum price among all till now
        for num in prices:
            if num< least_so_far:  # if curr price is less than min till now then store make curr ele as least_so_far
                least_so_far= num
                curr_max= 0   # and update curr_max = 0 as buying day will this only for max profit
            else:
                curr_max= num- least_so_far  # calculate the curr_max
            max_profit= max(curr_max, max_profit)  # update the max_profit always
        return max_profit




