# Observation : 1) element x of an integer array arr of length n is dominant if freq(x) * 2 > n,
# it means arr can have at most one dominant element in that array.

# 2) nums[0, ..., i], and nums[i + 1, ..., n - 1] have the same dominant element if we split at index 'i'.

# observation from these two points: 
# a) Majority ele say 'm' of original array must be dominant in any one of the parts then using '2' point ,
# It confirms that 'm' must be dominant in both the parts.

# so now Q reduces to find the "smallest index at which m is in dominant in both the parts".

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # a) find the majority 'm' 
        m = nums[0]  # Assume majority is 'm'.
        count = 1   # nums[0]
        for i in range(1, n):
            if nums[i] == m:
                count += 1
            else:
                count -= 1
                if count == 0:
                    m = nums[i]
                    count = 1
        
        # Now count the freq of majority ele
        count = 0
        for num in nums:
            if num == m:
                count += 1

        # Now just check at which index majority ele 'm' is in majority in both parts.
        left = 0   # will count the no of majority ele we have seen till now from left that is till index 'i'.
        # we will try split till 'n-2'
        for i in range(n - 1):   
            if nums[i] == m:
                left += 1
            right = count - left
            # Check if in both parts 'm' is in majority.
            # if left > (i + 1) //2 and  right > (n- i -1) //2:
            if left *2 > (i + 1) and right * 2 > (n - i - 1):
                return i
        return -1         # e.g: [3,3,3,3,7,2,2]