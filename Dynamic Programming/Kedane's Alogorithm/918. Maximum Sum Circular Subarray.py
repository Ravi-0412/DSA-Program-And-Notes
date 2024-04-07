# note => Ans for this will always >= ans of part 1:  "53. Maximum Subarray" since we can join ele in circular also here.

# Explanation
# There are two case.
# Case 1. The first is that the subarray take only a middle part, and we know how to find the max subarray sum.
# ans = "53. Maximum Subarray" 
# Case2. The second is that the subarray take a part of head array and a part of tail array.
# We can transfer this case to the part 1.
# The maximum result equals to the total sum minus the minimum subarray sum.

# For case 2: Find the minimum subarray sum and subtract from 'toal sum of array'.

# So the max subarray circular sum equals to
# ans = max( Non circular max sum + circular max sum ) i.e max(the max subarray sum, the total sum - the min subarray sum)

# so we have to keep track of both 'minSum' and 'maxSum'.

# Corner case in above one: 
# Just one to pay attention:
# If all numbers are negative, maxSum = max(A) and minSum = sum(A).
# In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
# According to the description, We need to return the max(A), instead of sum of am empty subarray.
# So we return the maxSum to handle this corner case.

# How we handle next and previous element in circular array?
# Next: the next element of nums[i] is:  nums[(i + 1) % n] 
# the previous element of nums[i] is:    nums[(i - 1 + n) % n].

# time: O(n)
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total= sum(nums)
        curMin= minSum= nums[0]
        curMax= maxSum= nums[0]
        for i in range(1, len(nums)):
            curMin= min(curMin + nums[i], nums[i])
            minSum= min(minSum, curMin)
            curMax= max(curMax + nums[i], nums[i])
            maxSum= max(maxSum, curMax)
        if maxSum > 0:   # means all ele is not 'negative' or atleast one ele is 'positive'.
            return max(maxSum, total- minSum)
        return maxSum  # all ele is negative


# method 2: same logic only but different way of finding 'max sum in circular Subarray'.
# Steps:Invert the sign of all the numbers in original subarray, 
# and find the maximum subarray sum using Kadane algorithm. Then add it with the total sum. 
# (which is similar to [total - minimum subarray sum ]).

# if max_sum_circular_subarrray= total - minimum subarray sum= 0, it means all number is negative
# so return min(nums)= max_sum_non_circular_subarray.
# else return max( Non circular max sum + circular max sum ).

# Code later by yourself(solution in link: 2nd no)

# method 3:
# Try by other method like ' Heap' and deque given in this link later.
# https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/1348545/python-3-solutions-clean-concise-o-1-space/


# 