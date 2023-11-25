# Time : O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost  # ho handle the corner case for 1st move so that no need to call for index '0' and index '1' separately.
        n = len(cost)
        
        @lru_cache(None)
        def solve(ind):
            if ind >= n:
                return 0
            return cost[ind] + min(solve(ind + 1) , solve(ind + 2))

        return solve(0)


# Note: How above method will take care of not_take case i.e skip case?
# Ans: When we are at index 'i' and if we include ans of 'i+2' (called 'i + 2') then we have skipped 'i+1'.