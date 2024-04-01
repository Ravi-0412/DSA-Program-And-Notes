# Logic: We need to keep track of three things : 'last' ele we have added, minimum value till now, 
# how many elements left to add with current index.

# For every element we have two choice i.e either include that or not include that.
# And our ans will be equal to above two choice.

class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        @lru_cache(None)
        def dp(ind, last, mn, left):
            if left == 0:
                return mn
            if ind == n:
                return 0
            return dp(ind + 1, nums[ind], min(mn, nums[ind] - last), left - 1) + dp(ind + 1, last, mn, left)

        return dp(0, -float('inf'), float('inf'), k) % (10**9 + 7)
        # 1) Passing last as '-float('inf')' to handle case when no element is included till now.
        # This will make difference very large and will included from ans automatically. 
