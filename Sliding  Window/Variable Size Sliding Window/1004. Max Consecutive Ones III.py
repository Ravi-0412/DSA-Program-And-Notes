# Logic: Q reduces to "find the max length of subarray such that number of zero in that subarray can be at most 'k' ".
# i.e Find the longest subarray with at most K zeros.
# Then our ans = max(length_valid_subarray)

# Time = O(n), space : O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n= len(nums)
        i, j= 0, 0
        count = 0  # will store the number of '0' in every subarray.
        ans = 0
        while j < n:
            if nums[j] == 0:
                count += 1
            # ans can be '0' also when 'k'= 0 and all ele is '0' only like [0,0,0,0] 
            # in that case we may have to go till 'j' to get length = 0.
            while i <= j and count > k:   
                if nums[i] == 0:
                    count -= 1
                i += 1
            ans = max(ans, j- i + 1)
            j += 1
        return ans
    

# Note vvi: Whenever you have to find the 'largest subarray length of a single consecutive ele'
# where you can change other ele then apply this logic only.

# Related Q: 
# 1)  "1493. Longest Subarray of 1's After Deleting One Element",
# 2)  "2024. Maximize the Confusion of an Exam"