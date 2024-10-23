# Logic:
"""
At each index, find the length of alternating subarray.
Say length = n after adding cur ele 'i; then we will get 'n' new subarray.

e.g: 

[1, 0, 1, 0, 1]
   [0, 1, 0, 1]
      [1, 0, 1]
	     [0, 1]
	        [1]
"""
# Time = O(n), space = O(1)
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        size, ans, i = 1 , 1, 1
        while i < n:
            if nums[i] != nums[i - 1]:
                size += 1
                ans += size
            else:
                size = 1
                ans += size
            i += 1
        return ans
