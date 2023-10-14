# Time : O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost  # ho handle the corner case for 1st move
        n = len(cost)
        
        @lru_cache(None)
        def solve(ind):
            if ind >= n:
                return 0
            return cost[ind] + min(solve(ind + 1) , solve(ind + 2))

        return solve(0)