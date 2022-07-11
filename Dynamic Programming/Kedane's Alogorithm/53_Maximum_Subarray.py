# brute force: O(n^2)
# correct only but giving TLE

def maxSubArray(self, nums: List[int]) -> int:
    max_sum, n= -inf, len(nums)
    # finding ṭhe sum of all the possible subarrays
    for i in range(n):
        curr_sum= 0
        for j in range(i,n):  # this will handle the case of single ele also
            curr_sum+= nums[j]
            max_sum= max(max_sum,curr_sum)
    return max_sum


# 2nd method: 
# Time: O(n)
# logic: To calculate sum(0,i), 
# you have 2 choices: either adding sum(0,i-1) to a[i], or not. 
# If sum(0,i-1) is negative, adding it to a[i] will only make a 
# smaller sum, so we add only if it's non-negative.
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
            # curr_sum is negative then make curr_sum= 0 then add the element
            if curr_sum <0:
                curr_sum= 0
            curr_sum+= n 
            # if even all no is negative then max_sum will store the
            # least negative no(in step: curr_sum+= n) and at last it will return that number
            
            # update the max_sum
            max_sum= max(max_sum, curr_sum)
        return max_sum


# method 4: By DP
# exactly same approach as method 1.
# just instead of storing into variable we stored the max_ending_here in an array 'dp'
def maxSubArray(self, nums: List[int]) -> int:
        n, max_sum= len(nums), nums[0]
        dp= [0]*(n)  # dp[i] will store the max_sum of any subarray till nums[:i]
        dp[0]= nums[0]
        for i in range(1,n):
            dp[i]= nums[i] + (dp[i-1] if dp[i-1]>0 else 0)
            max_sum= max(max_sum, dp[i])
        return max_sum


# this i did as revision time on 11/07/2021
# just same logic as method 3 and 4 even 2 is same only
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum, max_sum= 0, -9999999999
        for num in nums:
            if curr_sum< 0 and curr_sum< num:  # if curr sum is negative and less than current ele then make curr_sum= curr_element as thsi will only lead to max_sum
                curr_sum= num 
            else: 
                curr_sum+= num
            max_sum= max(curr_sum, max_sum) 
        return max_sum


