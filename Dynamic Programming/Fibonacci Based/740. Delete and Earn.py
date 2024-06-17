# Logic: we can convert this problem into: " 198. House Robber"
# for this just take only distinct ele and sort.

# then we only need to check with next index 'i+1' if that has value = nums[i] + 1 or not.
# if has then skip or take that.

# Note: We can take all the occurence of any ele if we take that.
# for this store the frequency also if you take then points = freq[nums[i]] * nums[i].

# Time; O(n*logn) 

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)

        @lru_cache(None)
        def solve(i):
            if i >= n:
                return 0 
            notTake = solve(i + 1)
            take = freq[nums[i]] * nums[i] 
            take += solve(i + 1) if i + 1 < n  and nums[i + 1] != nums[i] + 1 else solve(i + 2)
            return max(take, notTake)

        return solve(0)