# Method 1: Sorting  + Binary search
# Just sort and check number if that can be our ans.

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        start , end = 0 , nums[-1]   # ans can be outside 'nums' so will have to cover full range. so start = 0
        while start <= end:
            mid = start + (end - start) // 2
            ind = bisect.bisect_left(nums, mid)   # find index of 'mid' in sorted array
            if mid == n - ind:
                return mid
            if mid > n - ind :
                end = mid - 1
            else:
                start = mid + 1
        return - 1
    
# Method 2: 
# Optimise this by making range from '0' to len(nums) - 1.
# because We have to return X where X elements are greater than or equal to X. 
# So the answer would be at most the length of array. 



# method 3: using counting sort
# VVI: We have to return X where X elements are greater than or equal to X. 
# So the answer would be at most the length of array. 
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0]* (n + 1)  # count[i]: will store number of element >= i
                              # last index will store count when ele > n.
        for num in nums:
            if num > n :
                count[n] += 1
            else:
                count[num] += 1
        ans = 0
        for i in range(len(count) - 1, -1, -1):
            ans += count[i]
            if ans == i :
                # no of element >= i is equal to 'i'
                return i
        return -1


