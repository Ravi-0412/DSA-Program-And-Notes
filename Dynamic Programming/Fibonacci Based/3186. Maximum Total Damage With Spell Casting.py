# just extension of q: "740. Delete and Earn".
# Here you need to skip 'i+1' or 'i + 2' based on condition.

class Solution:
    def maximumTotalDamage(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)

        @lru_cache(None)
        def solve(i):
            if i >= n:
                return 0 
            notTake = solve(i + 1)
            take = freq[nums[i]] * nums[i]
            # first check if we can take 'i+1' as next or not. 'i+ 1' can have value = nums[i] + 1 or nums[i] + 2
            if (i + 1 < n and nums[i + 1] != nums[i] + 1 and nums[i + 1] != nums[i] + 2)  :
                take += solve(i + 1)
            # if can't take 'i+1', check if we can take 'i+2'. in this we only need to check case 'nums[i + 2] != nums[i] + 2'.
            elif i + 2 < n and nums[i + 2] != nums[i] + 2:
                take += solve(i + 2)
            # if can't take both 'i+1' or 'i +2' then, take 'i +3' skipping 'i+1' and 'i+2'.
            else:
                take += solve(i + 3)
            return max(take, notTake)

        return solve(0)