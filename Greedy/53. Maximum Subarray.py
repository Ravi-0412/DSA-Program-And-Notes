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

# 2nd method: 
# Time: O(n)
# logic: To calculate sum(0,i), 
# you have 2 choices: either adding sum(0,i-1) to a[i], or not. 
# If sum(0,i-1) is negative , adding it to a[i] will only make a 
# smaller sum, so we add only if it is positive 
def maxSubArraySum(self,arr,N):
        max_so_far, max_ending_here= arr[0], arr[0]
        # max_ending here will give the max_sum till that index(after conidering all the ele max_sum possible till that index)
        # max_so_far will store the actual ans
        # if the max_ending_here value become less after adding any ele, then max_so_far will get updated as max_so_far store only the max_sum of any subarry till now
        # otherwise max_so_far and max_ending_here will be same
        for i in range(1, N):
            # either each element will continue(add their val) to the max_ending_here  till now
            # or will become max_ending_here itself. this will happen when arr[i] will be greater than max_ending here
            max_ending_here= max(max_ending_here + arr[i], arr[i]) 
            # now update the max_so_far
            max_so_far=      max(max_so_far, max_ending_here)
        return max_so_far

# method 3: Kedane's Algo
# time: O(n)
def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum= nums[0], 0
        for n in nums:
            # curr_sum is negative then make curr_sum= curr_ele
            if curr_sum <0:
                curr_sum= n
            else: # otherwise add the curr ele to the curr_sum
                curr_sum+= n
            # update the max_sum
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



