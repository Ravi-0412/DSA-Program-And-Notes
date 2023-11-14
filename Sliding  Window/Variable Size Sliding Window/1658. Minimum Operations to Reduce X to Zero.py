# Observation: After removing combination of ele from start and end with sum = 'x' (if exist),
# We will be left with an subarray whose sum will be 'sum(nums) - x'.

# So now our q reduces to : "Find the length of longest subarray whose sum = "sum(nums) - x"
# for minimum no of operations say 'maxLen'.

# Then ans = n - maxLen if subarray exist else -1.

# Note: constarint of ele is +ve. So no need to use map.

# Time = O(n) , space = O(1)

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        maxLen = -1  # any min value that can't be ans
        i, j = 0, 0
        curSum = 0
        target = sum(nums) - x
        while j < n:
            curSum += nums[j]
            while i <= j and curSum > target:
                curSum -= nums[i]
                i += 1
            if curSum == target:
                maxLen = max(maxLen , j - i + 1)
            j += 1
        return -1 if maxLen == -1 else n - maxLen
