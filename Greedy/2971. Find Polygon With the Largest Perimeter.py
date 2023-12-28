# Logic: Sort the array and check each num[i] if that can be the largest number.
# for this sum till 'i-1' > nums[i].

# For this maintain prefix sum or store sum in a variable.

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] + prefix[i -1]
        ans = -1
        for i in range(2, n):
            if prefix[i -1] > nums[i]:
                ans = max(ans , prefix[i])
        return ans
        