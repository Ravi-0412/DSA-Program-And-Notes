# Note: the goal of this problem is to "find a num that makes the sum of moves is minimum".

# Just used the logic: learnt from the Q :"2448. Minimum Cost to Make Array Equal".

# the elements are to be made equal to any of the three measures of central tendency mean / median / mode.
# But which of this should be taken that is the main question we need to figure out?

# Note vvvvi: 1) If the cost for all element is the same, then the minimum cost is when all numbers converge at the median.
# 2) If the cost is not the same, we need to find a weighted median.

# How to find median?
# 1) sort the array
# median = mean of the middle values in case of even 'n' and the middle value itself in case of 'n' is odd.

# Why not mean?
# Example(if we take mean): [1, 97, 98, 99, 100]. In this case, the avg(mean) is 50. 
# However, in this case only one element is to the left of 50 while 4 on its right. 
# In this case, wouldn't it better for the first element to increment and go near the other elements rather than decrement 4 elements.

# time: O(n*logn)
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n= len(nums)
        nums.sort()
        # Find the median
        median = nums[n//2] if n % 2 else (nums[n//2] + nums[n//2 -1]) //2
        # Calculate the moves to make all ele equal to median.
        return sum(abs(num - median) for num in nums)


# Note vvi: when ever you want to equalize values in an array and the absolute value change in each item
# to make it equal we should consider the median value as the final value.


# Related Q
# 296. Best Meeting Point
# 2967. Minimum Cost to Make Array Equalindromic



