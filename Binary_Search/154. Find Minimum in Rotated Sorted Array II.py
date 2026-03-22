"""
Logic:
1. If nums[mid] > nums[right]: The right side is definitely unsorted. The minimum is to the right. (left = mid + 1)
2. If nums[mid] < nums[right]: The right side is definitely sorted. The minimum is at mid or to the left. (right = mid)
3. If nums[mid] == nums[right]: The Ambiguity. We don't know where the minimum is.
  Solution: We can't discard half, but we can safely discard right. Since nums[mid] is the same as nums[right], 
  even if nums[right] was the minimum, nums[mid] still exists to represent it. So, right -= 1.

Time : O(N), in worst case
Example : nums = [1, 1, 1, 1, 0, 1]
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # Case 1: Minimum must be in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Case 2: Right side is sorted, minimum is at mid or to the left
                right = mid
            else:
                # Case 3: nums[mid] == nums[right]
                # We can't tell which side has the minimum, 
                # but we know nums[right] is redundant.
                right -= 1
                
        return nums[left]
