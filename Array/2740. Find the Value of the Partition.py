# Note: we only need to care about max(nums1) & min(nums2)

# Approach:

# Sort the array
# Now we can split the array in to part from the point where the two consicutive elemnts have min difference.
# So the lower side array have max value and the next element is the min of the next upper side array section.
# so keep iterating to get the min diff betteen two consicutive elements.

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans= float('inf')
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i-1])   # nums[i] will go to 1st and nums[i-1] will go to 2nd.
        return ans
    