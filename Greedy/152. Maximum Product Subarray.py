# Method 1: 

"""
logic: negative no is making problem like if product till now is min but next time it can become the ans if next ele will be negative.
that's why maintaining two varaibel to store the curr_max and curr_min till now.
here we are becoming greedy as we can get our ans from both like curr_min and curr_max.

Time : O(n), space : O(1)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans= nums[0]
        curr_max, curr_min= 1, 1  # for multiplication '1' won't effect the ans
        for n in nums:
            temp= curr_max*n  # have to update curr_min acc to prev value only
            # for curr_max: 1) n is +ve and curr_max is +ve 2) n is -ve and curr_min is -ve 3) if for input like: [-1, 8]
            curr_max= max(n* curr_max, n*curr_min, n)
            # for curr_min: 1) n is -ve and curr_max is +ve 2) n is +ve and curr_min is -ve 3) if for input like: [-1, -8]
            curr_min= min(temp, n*curr_min, n)
            ans= max(ans, curr_max)
        return ans

# method 2:
"""
just for learning purpose
the maximum product subarray will always include either the first element or the last element of the array, 
unless there is a zero in the middle (which acts as a boundary).

Why does this work? (The Intuition)
Think of the array as being divided by zeros. In any segment between two zeros:
If there are an even number of negative signs, the product of the whole segment is the maximum.
If there are an odd number of negative signs, you must exclude one negative sign. To get the maximum product, 
you would exclude either the "first" negative sign (leaving a suffix) or the "last" negative sign (leaving a prefix).
By checking both directions, we are guaranteed to find that optimal prefix or suffix.

Time : O(n), space : O(1)
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums[0]
        
        prefix = 1
        suffix = 1
        
        for i in range(n):
            # Calculate prefix from the left
            prefix *= nums[i]
            # Calculate suffix from the right
            suffix *= nums[n - 1 - i]
            
            ans = max(ans, prefix, suffix)
            
            # If we hit a 0, we must reset the product for the next element
            if prefix == 0: prefix = 1
            if suffix == 0: suffix = 1
                
        return ans
        
