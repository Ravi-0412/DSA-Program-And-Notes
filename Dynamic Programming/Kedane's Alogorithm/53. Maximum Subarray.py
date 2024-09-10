# brute force: O(n^2)
# correct only but giving TLE

def maxSubArray(self, nums: List[int]) -> int:
    max_sum, n= -inf, len(nums)
    # finding ṭhe sum of all the possible subarrays starting from each index 
    for i in range(n):
        curr_sum= 0
        for j in range(i,n):  # this will handle the case of single ele also
            curr_sum+= nums[j]
            max_sum= max(max_sum,curr_sum)
    return max_sum


# logic: har ele ke pass 2 choice, either curr_sum me include ho jaye ya khud curr_sum ban jaye. that's it.

# 2nd method: Kedane's Algo
# Time: O(n)
# logic: To calculate sum(0,i), 
# you have 2 choices: either adding sum(0,i-1) to a[i], or not. 
# If sum(0,i-1) is negative , adding a[i] to curSum will curSum samller only no matter whether arr[i] is +ve or -ve.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum= nums[0], 0
        for n in nums:
            # curr_sum is negative then make curr_sum= curr_ele
            if curr_sum <0: # adding the 'n' in curSum will decrease the value of curSum so better start curSum from here only.
                curr_sum= n
            else: # otherwise add the curr ele to the curr_sum
                curr_sum+= n
            # update the max_sum
            max_sum= max(max_sum, curr_sum)
        return max_sum


# short of above

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum= nums[0], 0
        for n in nums:
            curr_sum= max(curr_sum + n, n)
            max_sum= max(max_sum, curr_sum)
        return max_sum

# method 4: By DP
# exactly same approach as method 2.
# just instead of storing into variable we stored the max_ending_here in an array 'dp'
def maxSubArray(self, nums: List[int]) -> int:
        n, max_sum= len(nums), nums[0]
        dp= [0]*(n)  # dp[i] will store the max_sum of any subarray till nums[:i]
        dp[0]= nums[0]
        for i in range(1,n):
            dp[i]= nums[i] + (dp[i-1] if dp[i-1]>0 else 0)
            max_sum= max(max_sum, dp[i])
        return max_sum


# Note: If we want to fidn the "Smallest sum contiguous subarray". (GFG Q)
# https://practice.geeksforgeeks.org/problems/smallest-sum-contiguous-subarray/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

# we can apply the excatly similar logic as above
class Solution:
    def smallestSumSubarray(self, A, N):
        total= sum(A)
        curSum= A[0]
        minSum= A[0]
        for i in range(1, N):
            if curSum > 0:  # we have to decrease 'curSum'.
                curSum= A[i]
            else:
                curSum+= A[i]
            minSum= min(minSum, curSum)
        return minSum


# shortcut of above
class Solution:
    def smallestSumSubarray(self, A, N):
        total= sum(A)
        curSum= A[0]
        minSum= A[0]
        for i in range(1, N):
            curSum= min(curSum + A[i], A[i])
            minSum= min(minSum, curSum)
        return minSum


# Try by divide & conquer later
