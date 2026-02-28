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

# Follow ups:
"""
1. 
Range Target: "What if instead of one target, you were given a range [low,high] and 
asked to find a sum within that range? If none exist, find the closest one to the range boundaries." 

The Logic: This is effectively a search for the "Intersection" of conditions.
    Case A: If any sum exists such that low≤sum≤high, return any such sum (or the one closest to the middle of the range, depending on the interviewer's preference).
    Case B: If no sum falls in the range, the "closest" sum must be either the one closest to low (from the left) or the one closest to high (from the right).

The Pivot: You track two "best" values: closest_to_low and closest_to_high. In your while loop:
    If sum<low, update closest_to_low and move l++.
    If sum>high, update closest_to_high and move r--.
    If low≤sum≤high, you found a winner! Return sum.
"""

class Solution:
    def threeSumRange(self, nums: List[int], low: int, high: int) -> int:
        nums.sort()
        n = len(nums)
        
        # Initialize with infinity so any sum is closer
        closest_to_low = float('-inf')
        closest_to_high = float('inf')
        
        for i in range(n - 2):
            l, r = i + 1, n - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                
                # Case A: Found a sum within the intersection
                if low <= curr_sum <= high:
                    return curr_sum
                
                # Case B: Sum is outside the range
                if curr_sum < low:
                    # Looking for the largest value that is still < low
                    if curr_sum > closest_to_low:
                        closest_to_low = curr_sum
                    l += 1
                else: # curr_sum > high
                    # Looking for the smallest value that is still > high
                    if curr_sum < closest_to_high:
                        closest_to_high = curr_sum
                    r -= 1
        
        # If no sum was in [low, high], compare distances to boundaries
        if abs(low - closest_to_low) <= abs(closest_to_high - high):
            return closest_to_low
        else:
            return closest_to_high

"""
"Given the constraints (N=500), O(n^2) is fine. But if N=10,000, can you optimize the inner loop using binary search for the third element? 
Ans : yes, for every pair (i,j), you calculate the needed_value = target - (nums[i] + nums[j])

But time : O(n^2 * logn)

"""
