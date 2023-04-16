# note: Ans for this will always >= ans of Q "53. Maximum Subarray" since we can join ele in circular also here.
# ans=  total sum - min(subarray)
# But after this ans we will get may not formed form the continous subrray so in this case our ans= maxSum= "53. Maximum Subarray"
# if coninous then ans= total sum - min(subarray)
# So finally our ans= max(maxSum, sum(nums)- minSum).

# so we have to keep track of both 'minSum' and 'maxSum'.

# Note: More deeply what we are doing :
# ans = max( Non circular max sum + circular max sum ) where 'maxSum'= Non circular max sum and 'sum(nums)- minSum'= circular max sum. 
# Also first and last ele of 'minSum' must be '-ve' otherwise those would be part of ans only.
# Corner case in above one: 
# Just one to pay attention:
# If all numbers are negative, maxSum = max(A) and minSum = sum(A).
# In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
# According to the deacription, We need to return the max(A), instead of sum of am empty subarray.
# So we return the maxSum to handle this corner case.

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
