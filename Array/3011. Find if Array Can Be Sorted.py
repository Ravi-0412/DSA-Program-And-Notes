# Logic: 
# 1) We can only swap if no of set bits are same.
# 2) Depending upon no of set bits we can divide array into different subarrays.
# How? 
# Consecutive elements having same no of set bits will form a subarray.
# e.g : nums = [3,16,8,4,2]
# we can divide into : [3] , [16, 8, 4, 2]

# 3) Next subarray smallest ele must be greater than previous subarray maximum ele
# Then we can combined make these two subarray sorted.
# Otherwise we can't make whole array sorted.

# For this we will maintain two arrays min_arr and max_arr for storing minimum and maximum values of all subarrays.
# Then we will use step '3' to check.

# Time: O(n) = space

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        def countSetBit(num):
            count=0
            while num:    
                count+= 1
                num = num & num -1
            return count
        
        n = len(nums)
        min_arr = []
        max_arr = []
        
        i = 0
        while i < n :
            set_bit = countSetBit(nums[i])
            mx = mn = nums[i]
            while i + 1 < n and countSetBit(nums[i + 1]) == set_bit:
                mn = min(mn, nums[i + 1])
                mx = max(mx , nums[i + 1])
                i += 1
            i += 1
            min_arr.append(mn)
            max_arr.append(mx)
        
        for i in range(1, len(min_arr)):
            if min_arr[i] < max_arr[i - 1]:
                return False
        return True