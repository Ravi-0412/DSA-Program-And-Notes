class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 1
        ans = 1
        while j < n:
            if nums[j] != nums[j -1]:
                ans += j -i + 1   
            else:
                ans += 1
                i = j    # For next window we need to check from 'j'
            j += 1
        return ans
        