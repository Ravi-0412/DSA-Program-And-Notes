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

# Java
"""
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_val = 0
        ans = -1
        
        for num in nums:
            if num < sum_val:
                ans = num + sum_val
            sum_val += num
            
        return ans
"""

# Method 2: Optimising space to o(1)
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sum_val = 0
        ans = -1
        
        for num in nums:
            if num < sum_val:
                ans = num + sum_val
            sum_val += num
            
        return ans

# Method 2: Going backward

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        _sum = sum(nums)
        n = len(nums)
        for i in range(n - 1, 1, -1):
            _sum -= nums[i]
            if _sum > nums[i]:
                return _sum + nums[i]
        return -1
