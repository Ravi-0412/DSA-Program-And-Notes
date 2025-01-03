# time: O(n), space: O(1)

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        curSum, ans = 0, 0
        for i in range(n-1):
            curSum += nums[i]
            ans += curSum >= (total - curSum)
        return ans
