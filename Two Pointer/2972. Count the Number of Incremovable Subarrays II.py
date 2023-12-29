# Steps:
# 1) find the index from start and end till where array is strictly increasing say leftPivot and rightPivot.
# 2) Now start from index '0' and go till index 'leftPivot + 1' say 'i' 
# and check number of subarray we can remove we start from index 'i'.
# a) For this we need to find the 1st index say 'j' in right strictly increasing array 
# such that nums[i - 1] < nums[j] . Then only array till 'i-1' from start and array from 'j' to end
# combinedly form a strictly increasing array.

# a.1) for this we can use two pointer as array is sorted so need to traverse again and again for 
# each ele.

# Note: why we doing till 'leftPivot + 1'.
# Because we have to necessarily remove ele after 'leftPivot + 1' till 'rightPivot -1' to make
# remaining array sorted for every ele.
# so no need to check for these indexes we are removing for sure for every ele.
# But we can remove from index 'leftPivot + 1' also.

# time : O(n)

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        leftPivot = 0  # last index from start till array is strictly increasing
        for i in range(1, n):
            if nums[i] <= nums[i -1]:
                break
            leftPivot = i
        if leftPivot == n -1:
            # Array is strictly increasing so we can remove every possible subarray.
            return n*(n + 1) //2
        
        rightPivot = n-1  # last index from end till array is strictly increasing
                          # from index to last array will be in strictly increasing order
        for i in range(n-2, -1, -1):
            if nums[i] >= nums[i +1]:
                break
            rightPivot = i
        
        j = rightPivot
        ans = n - j + 1    # for index '0' adding 1st to avoid corner case
        i = 1
        while i <= leftPivot + 1:
            while j < n and nums[i - 1] >= nums[j]:
                j += 1
            ans += n - j + 1
            i += 1
        return ans