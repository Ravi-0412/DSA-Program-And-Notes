# Method 1 :
"""
Logic: sort the prices from most to least expensive. In each group of 3, pay for the first two; the third is free, 
because it's never more expensive than the two paid with it. 
Grouping the most expensive candies together makes each free candy as expensive as possible, so you save the most.

Time : O(n*logn)
"""

class Solution:
    def minimumCost(self, cost: list[int]) -> int:
        n = len(cost)
        cost.sort(reverse = True)          # most expensive first, so the free candies are as expensive as possible
        minCost = 0
        for ind in range(n):
            if (ind + 1) % 3 == 0:         # 3rd, 6th, 9th … candy (1-based position) → free
                continue
            minCost += cost[ind]           # 1st and 2nd of each group → pay
        return minCost

  # Shorter one
"""
[2::3] means: start at index 2 and take every 3rd element after that.
"""
  class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        most_expensive_first = sorted(cost, reverse=True)
        free_candies = most_expensive_first[2::3]          # 3rd, 6th, 9th … → the free ones
        return sum(cost) - sum(free_candies)

# Optimization:
"""
counting sort, O(n + 100)
cost[i] ≤ 100, so you can count how many candies have each price instead of sorting.
"""

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        count_of = [0] * 101                               # count_of[price] = how many candies cost that much
        for price in cost:
            count_of[price] += 1

        total, position = 0, 0                             # position = index in descending order
        for price in range(100, 0, -1):                    # most expensive first
            for _ in range(count_of[price]):
                if position % 3 != 2:                      # every 3rd candy is free
                    total += price
                position += 1
        return total
