# Recursion + memoisation

# Note: Same Q as "518. Coin Change II" but here order also matter.

# Logic vvi: Kisi bhi element ke bad koi bhi ele aa sakta h kabhi bhi.
# i.e since asking for combination so pre index ele can also come again because here 
# different order of same sets of element is also calculated as ans.

# e.g: nums = [1,2,3], target = 4
# possible ans = (1, 1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 3), (2, 1, 1), (2, 2), (3, 1)

# Take : (1, 2, 1) & (2, 1, 1)
# element at index '0' i.e '1' is coming after ele at index 1' i.e 2.

# So in this we take index as parameter like 'coin change' then we won't be able to consider 
# pre index element again but we have to consider that again.

# Note vvi: In this type of question always use for loop and don't take index as parameter in function call.
# using for loop an element can come after any element. 
# And only call next function checking the condition, this will take us to the proper base case a/c to the q.

# vvi: for base case -> we have to avoid function call while taking any number only.
# So before taking any number just check 'if nums[i] <= target'.
# And for base check if target == 0.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def solve(target):
            if target == 0:
                return 1
            ans = 0
            for i in range(len(nums)):
                if nums[i] <= target:
                    ans += solve(target - nums[i])   # sb possibility ko add karna h.
            return ans

        return solve(target)



# Note vvi:
# 1) If ALL numbers are negative, then the solution would be the same if you switch signs for numbers and target simultaneously. 

# 2) However, there is no guaranteed finite solution if positive and negative numbers are mixed, e.g. nums=[1,-1, 2] target = 0
# in this case , we can put one restriction that : "each number can only be used up to k times".