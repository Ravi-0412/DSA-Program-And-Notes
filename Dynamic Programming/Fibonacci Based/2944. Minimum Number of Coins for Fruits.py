# Just same logic as '746. Min Cost Climbing Stairs'.
# Just here we need to consider next 'i+1' element.


# Time: O(n^2)

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def solve(i):
            if i > n:
                return 0
            # buy ith fruit and take minimum of next 'ith' fruit.
            ans = float('inf')
            # next 'ith' fruits i.e till index '2*i' free me buy kar sakte h.
            # i.e yahan tak skip kar sakte h .
            # '2*i + 1' pe har hal me hmko buy karna hoga agar pura i.e '2*i' tak skip karte h tb.
            for j in range(i + 1 , 2*i + 2):
                ans = min(ans , solve(j))
            return prices[i - 1] + ans  # 'i'th fruit buy kiye.

        return solve(1)  # using 1 based indexing

# Note: How above method will take care of not_take case i.e skip case?
# Ans: when we are at ith position we are directly calling solve with value of i = j where 
# 'j' can be any value between i+1 to 2*i+1. so when you are calling j = i + 2 that means - not taken i + 1 value.
# If we are calling 'i+4' then ,it means we skipping 'i+1' , 'i+2' , 'i+3'. 
# And so on.


# Try to do in O(n*logn). Solution in sheet.