# Recursion + memoisation

# Note: Same Q as "518. Coin Change II" but here order also matter.

# Logic vvi: Kisi bhi element ke bad koi bhi ele aa sakta h kabhi bhi.
# So there is always a possibility to choose next number even after reaching last index.
# So if we take 'index' as parameter in function call then, it will give TLE. (my mistake).

# So we have to avoid function call while taking any number only.
# So before taking any number just check 'if nums[i] <= target'.



class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def solve(target):
            if target == 0:
                return 1
            ans = 0
            for i in range(len(nums)):
                if nums[i] <= target:
                    ans += solve(target - nums[i])
            return ans

        return solve(target)



# Note vvi:
# 1) If ALL numbers are negative, then the solution would be the same if you switch signs for numbers and target simultaneously. 

# 2) However, there is no guaranteed finite solution if positive and negative numbers are mixed, e.g. nums=[1,-1, 2] target = 0
# in this case , we can put one restriction that : "each number can only be used up to k times".