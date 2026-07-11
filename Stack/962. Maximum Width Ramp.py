"""
Time = space = O(1)
"""

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        # Step 1: Forward Pass - Build a monotonic decreasing stack of indices
        # We only add an index if its value is strictly smaller than the current stack top.
        # Why? Any larger value to the right would yield a shorter ramp than an earlier, smaller value.
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
                
        max_width = 0
        
        # Step 2: Backward Pass - Scan from right to left to maximize the width span (j - i)
        for j in range(n - 1, -1, -1):
            # While the stack is not empty and the current element forms a valid ramp
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)
                
            # Early termination optimization: If the stack is empty, 
            # we have exhausted all possible optimal left boundaries.
            if not stack:
                break
                
        return max_width
