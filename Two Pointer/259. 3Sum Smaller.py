"""
1st sort the array for better traversing and checking.

if the sum of three numbers is less than the target, then any number smaller than our current "right" pointer will also result in a sum less than the target.
    Sort the array.
    Iterate through the array with index i, treating nums[i] as the first element of our triplet.
    Set two pointers for the remaining portion of the array: left = i + 1 and right = n - 1.
    Check the sum: * If nums[i] + nums[left] + nums[right] < target:
    * Since the array is sorted, every element between left and right would also satisfy the condition when paired with nums[i] and nums[left].
    * We add right - left to our total count.
    * Move the left pointer forward to try a larger sum.
        Otherwise, the sum is too large:
            Move the right pointer backward to decrease the sum.

Time : O(n^2), space : O(1)
"""

class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < target:
                    # If nums[i] + nums[left] + nums[right] < target,
                    # then all elements between left and right also work
                    # as the third element.
                    count += (right - left)
                    left += 1
                else:
                    # Sum is too high, need a smaller value from the right
                    right -= 1
                    
        return count
        
