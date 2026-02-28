"""
i) Sorting the array allows us to use two directional pointers.
ii) We maintain a variable to store the "best" (closest) sum found so far.
iii) 
    If the current sum is less than the target, we need a larger sum to potentially get closer.
    If the current sum is greater than the target, we need a smaller sum.
    If the current sum equals the target, we return immediately as the distance is zero.

Time : O(n^2), space : O(1)
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        # Initialize with the first possible triplet sum
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # Optimization: Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, n - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if the new sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers to get closer to the target
                if current_sum < target:
                    l += 1
                else:
                    r -= 1
                    
        return closest_sum
