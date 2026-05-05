# Method 1:

# Basic
"""
Q) We need to minimise the maximum value of any element by using the given operation.

The key to this problem is understanding the direction of the "flow":
1) You can move a value from nums[i] to nums[i-1].
2) This means you can move values from the right to the left, but never from left to right.
3) Therefore, if the numbers on the right are large, you can "distribute" them to the left to lower the maximum value. 
However, the numbers on the left are "stuck"—they can only be increased by their neighbors on the right.
"""

# Method 1 :
"""
Using Binary Search

Logic :
we pick a potential maximum value (let's call it mid) and ask: "Is it possible to make every number in the array <= mid?
1) "The Range: The smallest possible maximum is 0 (or nums[0]), and the largest is max(nums).
2) The Check (Greedy): * We process the array from right to left.
  If nums[i] is greater than our target mid, we must move the "excess" (nums[i] - mid) to the left neighbor nums[i-1].
  If we reach the very first element nums[0] and it is still greater than mid, then mid is too small.

Note : Just same way we find the 1st index . 

Time Complexity: O(n * log(max_val}))
"""

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def can_achieve(max_limit):
            # We use a temporary buffer so we don't modify the original nums
            # 'excess' carries the values shifted from right to left
            excess = 0
            for i in range(len(nums) - 1, 0, -1):
                # Calculate how much this current number plus shifted excess 
                # exceeds our allowed max_limit
                current_val = nums[i] + excess
                # Check if the current number (plus any overflow from the right) 
                # exceeds the maximum limit we are testing.
                if current_val > max_limit:
                    # If it's too big, we 'push' the extra amount to the left neighbor (nums[i-1]).
                    # This represents the operation: Decrease nums[i] and Increase nums[i-1].
                    excess = current_val - max_limit
                else:
                    # If the current number is already under or equal to the limit, 
                    # we don't need to push anything to the left.
                    # Importantly: we cannot 'pull' values from the left to the right,
                    # so we reset excess to 0 even if we have 'space' available here.
                    excess = 0
            
            # Finally, check if the first element can absorb the remaining excess
            return nums[0] + excess <= max_limit

        # Binary search range
        low = nums[0]
        high = max(nums)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if can_achieve(mid):
                ans = mid
                high = mid - 1 # Try to find an even smaller maximum
            else:
                low = mid + 1  # mid is too small, need a larger maximum
        
        return ans

  # Method 2:
  """
  Most Optimised One.

  Using Prefix Sum logic

  Q) Way to find the ceil(a / b ) , where a is the sum and b is the count.
  = (a + b - 1) // b

The Intuition to find ceil(a/b) using above formula:
Imagine you are packing $a$ items into boxes of size b. If a is a multiple of b (e.g., 10 / 5), you need exactly 2 boxes. 
Adding b-1 (which is 4) gives you 14. 14 // 5 is still 2. If a is not a multiple (e.g., 11 / 5), you have a remainder. 
You need an extra box. Adding b-1 (4) gives you 15. 15 // 5 is 3.

Now come to this Question:
Logic:
i) Imagine having two number 5 10 . We need to decrease one and increase other, how would we minimize the maximum number among them? 
By Evenly distributing them! We can then take the ceiling of their average (10+5)/2 = 7.5 = 8 .
ii) If there are three numbers, we need to take average of all of them and update our ans if it's bigger than the previously achieved answer, 
same for the whole array.
iii) Take a prefix sum variable, an ans variable, iterate through the array from 1st index, keep finding the ceiling of average until 
current iteration and update the answer as ans = max(ans, ceil(total+i)/(i+1)).
Why ceil value: The total sum of elements in that prefix remains constant or increases (if we move values from i+1 into the prefix). 

Other way : 
For any prefix of the array (from index 0 to i), the total sum of elements in that prefix remains constant or increases (if we move values from i+1 into the prefix). 
However, the best we can possibly do for any prefix is to spread its current total sum as evenly as possible across all its elements.

q) Why does this work?
Because we can only move values to the left, the "bottle-neck" is always a prefix that has a high average. 
No matter how much we shuffle values around at index i, we can never change the fact that the first i+1 spots must hold at least sum(nums[0...i]). 
The best we can do is make them all equal to the average.


  """

import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        running_prefix_sum = 0
        min_possible_max = 0
        
        for index in range(len(nums)):
            running_prefix_sum += nums[index]
            
            # The 'count' is the number of elements in the current prefix.
            # Since index starts at 0, count = index + 1.
            count = index + 1
            
            # We need to find the ceiling of (running_prefix_sum / count).
            # General Ceil Formula: (a + b - 1) // b
            # Here: a = running_prefix_sum, b = count
            # Simplified: (running_prefix_sum + count - 1) // count
            # Which is: (running_prefix_sum + index) // (index + 1)
            
            current_average_ceil = (running_prefix_sum + count - 1) // count
            
            # The answer for the whole array must be at least as large as 
            # the most "crowded" prefix average we have encountered.
            min_possible_max = max(min_possible_max, current_average_ceil)
            
        return min_possible_max


# Follow ups:
"""
Q) If the operation were reversed—meaning you increase nums[i] and decrease nums[i-1]—
Ans: the fundamental logic of the problem shifts from moving values "left" to moving values "right.

# Logic for REVERSED operation (Moving values Left to Right)
suffix_sum = 0
max_of_averages = 0
n = len(nums)

for i in range(n - 1, -1, -1):
    suffix_sum += nums[i]
    count = n - i
    # Ceiling division of suffix average
    current_suffix_avg = (suffix_sum + count - 1) // count
    max_of_averages = max(max_of_averages, current_suffix_avg)

return max_of_averages
"""
