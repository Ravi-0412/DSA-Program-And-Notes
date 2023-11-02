# Note: we only need to care about max(nums1) & min(nums2)

# Approach:
# Reducing: our ans will be equal to minimum difference between two consecutive elements 
# when they are in sorted order because for getting minimum, value must be close in both the partition.
# for this we need to sort the array and check.
# How?
# suppose 'nums[i] - nums[i-1]' gives the minimum value among all consecutive pairs.
# Then we can partition array like : put elements till 'i-1' into 1st (max one) and put elements from 'i' till last into 2nd one (min one).
# After that value of partition will be same as : nums[i] - nums[i-1].

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans= float('inf')
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i-1])   # nums[i] will go to 1st and nums[i-1] will go to 2nd.
        return ans
