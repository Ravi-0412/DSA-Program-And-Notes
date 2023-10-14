# Note: free painter paid painter ke saath hi use ho sakta h.

# Logic: kis kis paid painter ko use kare taki usi samay free painter ko use karke apna cost minimise kar sake.
# if we use 'i'th paid painter then remaining walls to paint = walls - time[i -1] - 1.
# Reason: '1' will be painted by the paid painter, and 'time[i-1]' walls will be paid by the free painter during that time.

# Note:
# when we paint a wall by the painter1 then we can skip time[i] walls 
# (basically this time[i] no. of walls will be painted by the painter2 with zero cost).

# Note:So we can re-think the problem as select n walls from the given one so that the sum of the times to paint wall:  
# (painted by painter1 i.e paid painter + painted by painter2 i.e free painter + ) > total no. of walls to paint.

# This is similar to the 0/1 Knapsack where the cost is same as weight and our bag size is wall count. 
# But in Knapsack we reduce the bag size by the stone size here we reduce the wall count by the time[i] 
# and additional -1 to reduced currently painted wall.

# Note: Other thought
# There is a sense to use small cost to buy more time

# So we can find that this is a Knapsack problem and instead of value of items(profit),
# we calculate the minimum cost to buy enough time to finish n walls.

class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @lru_cache(None)   # or dp = (n +1) * (n + 1)
        def solve(painter , walls):
            if walls <= 0:
                # means all walls are painted
                return 0
            if painter == 0:
                # means all walls are not painted and there is no paid painter available
                return float('inf')
            notTake = solve(painter -1 , walls)
            Take =  cost[painter -1] +  solve(painter -1, walls - time[painter -1] - 1)
            return min(notTake, Take)

        return solve(n, n)   # cost of painting 'n' walls with help of 'n' paid painters 