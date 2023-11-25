# Every 'i'th day we have 3 choice:
# 1) Either buy any of the three ticket
# a) if bought '7' days ticket, then no need to buy for next '6' days.
# b) if bought '30' days ticket, then no need to buy for next '29' days
# 2) Use the previous bought ticket

# Time : O(n * days[-1])

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @lru_cache(None)
        def solve(i, day):   
            if i >= len(days) or day >= days[-1] :
                # if have covered all days 
                return 0
            if days[i] <= day:
                # No need to buy ticket , we can use previous one
                return solve(i + 1, day)
            # else buy any three ticket
            choice1 = costs[0] + solve(i + 1, days[i])
            choice2 = costs[1] + solve(i + 1, days[i] + 6)
            choice3 = costs[2] + solve(i + 1, days[i] + 29)
            return min(choice1, choice2, choice3)
            
        return solve(0, 0)   # will give the cost till when we are on 'i'th day and we have pass till day 'day'.


# Method 2:
# reducing time to : O(days[-1])

# dp[i] means up to i-th day the minimum cost of the tickets. 
# The size of the dp array depends on the last travel day, so we don't need an array length to be 365.

# If a 1-day ticket on day i, dp[i] = dp[i - 1] + cost[0]
# If a 7-day ticket ending on day i, dp[i] = min(dp[i - 7], dp[i - 6] ... dp[i - 1]) + cost[1]
# If a 30-day ticket ending on day i, dp[i] = min(dp[i - 30], dp[i - 29] ... dp[i - 1]) + cost[2]

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]
        travelDays = set()
        for day in days:
            travelDays.add(day)
        dp = [0] *(maxDay + 1)
        for day in range(maxDay + 1):
            if day not in travelDays:
                dp[day] = dp[day-1]
                continue
            cost_day = costs[0] + dp[day-1]
            cost_week = costs[1] + dp[max(0, day - 7)]  # if week pass is ending on this day, we can buy new week pass
            cost_month = costs[2] + dp[max(0, day - 30)] # if month pass is ending on this day, we can buy new month pass
            dp[day] = min(cost_day, cost_week, cost_month)
        return dp[-1]


# Try to do this using approach of :
# "746. Min Cost Climbing Stairs" , "2944. Minimum Number of Coins for Fruits".