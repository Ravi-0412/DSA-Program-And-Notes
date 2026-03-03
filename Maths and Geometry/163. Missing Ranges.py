"""
1. The "Virtual" Boundaries: The range is [lower, upper]. To make the logic uniform, 
think of the numbers just outside the bounds (lower - 1 and upper + 1) as our starting and ending points.
2. Linear Scan: We iterate through the numbers in nums. For any two consecutive numbers A and B, 
if B - A > 1, there is a missing range between them.
    The missing range starts at A + 1 and ends at B - 1.
3. Handling Edges: 
    Check the gap between lower and the first element of nums.
    Check the gap between the last element of nums and upper.
4. The "Missing" Rule: A range [start, end] exists only if start <= end.

Time : O(n), space : O(1)
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        
        # We start at lower - 1 so that if 'lower' itself is missing, 
        # the first gap check (nums[0] - prev) will be > 1.
        prev = lower - 1
        
        # We run the loop n + 1 times to include the gap after the last element in case last element is missing 
        for i in range(len(nums) + 1):
            # If we are within the array, use the element. 
            # If we passed the last element, use the 'virtual' upper bound + 1.
            curr = nums[i] if i < len(nums) else upper + 1
            
            # Logic: If there is at least one integer between prev and curr
            if curr - prev > 1:
                # The missing integers are everything from (prev + 1) to (curr - 1)
                res.append([prev + 1, curr - 1])
            
            # Move our standing point to the current number
            prev = curr
            
        return res
