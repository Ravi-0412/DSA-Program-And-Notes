# Logic: we if we consider any ele say 'nums[i]' as starting ele then max number we can include in 
# arr say nums[j] = nums[i] + (n - 1)

# Since we want only unique values so store in set to get unique values 
# And after that sort to find the max number we can include.

# Observation: more the length of arr, less we will need to replace.
# So Q reduces to "get the length of the longest subarray whose difference between min and max elements is N - 1".

# Note: The brute force way is to pick each A[i] as the start of the subarray and 
# count the number of elements that are <= A[i] + N - 1, which takes O(N^2) time.

# Since the array is already sorted, we can use sliding window so that we only traverse the entire array once.

# suppose we are able to include ele before index 'j' consider starting number as 'nums[i]' then,
# 'no of unique ele considering 'i' as starting ele = 'j - i'.
# So total replacement = n - no_unique_ele = n - (j - i).

# Time : O(n*logn)

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)  # initial length
        nums = sorted(set(nums))
        m = len(nums)  # length after sorting unique values
        j = 0
        ans = n  # any big not possible ans
        for i in range(m):
            start, end = nums[i] , nums[i] + (n - 1)
            while j < m and nums[j] <= end:
                j += 1
            uniqueEle = j- i
            ans = min(ans , n - uniqueEle)  
        return ans


# Method 2: Using Binary search
# Since we are finding the last ele nums[j] for each nums[i] in sorted array(after getting unique ele)

# For finding the index 'j' we can use binary search
# Because we have to find 1st index such that nums[j] > nums[i] + (n-1).

import bisect
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)  # initial length
        nums = sorted(set(nums))
        m = len(nums)  # length after sorting unique values
        ans = n  # any big not possible ans
        for i in range(m):
            start, end = nums[i] , nums[i] + (n - 1)
            j = bisect.bisect_right(nums, end)   
            uniqueEle = j- i
            ans = min(ans , n - uniqueEle)  
        return ans