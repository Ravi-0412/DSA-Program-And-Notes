# Note: i understood the wrong meaning of exactly 2 and exactly 3 are equal.
# i was thinking even [1,2,1] is good subarray because has exactly 2 (1) but it is not.
# Because 1's are not contiguous.

# same for exactly 3 are equal.

# Note : all ele should be contiguous for good subarray.
# And there shouldn't be any extra element.
# This means whenever see any consition following after that we have to split.

# So just check the partition and keep splitting.

# Time : O(n)

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def solve(i):
            if i >= n:
                return True
            # check if there is exactly 2 and exactly 3 ele is equal
            if i + 1 < n and nums[i] == nums[i + 1]:
                if solve(i + 2):
                    return True
                # check for exactly three
                if i + 2 < n and nums[i + 1] == nums[i + 2]:
                    if solve(i + 3):
                        return True
            # check for 3 consecutive ele
            if i + 2 < n and   nums[i + 1] == nums[i] + 1 and  nums[i + 2] == nums[i + 1] + 1:
                if solve(i + 3):
                    return True
            return False

        n = len(nums)
        return solve(0)



