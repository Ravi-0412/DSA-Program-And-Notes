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
            # 'k' can be '0' also, in that case we may have to go till 'j' to get length = 0.
            # e.g : [0,0,0,0], k= 0
            while i <= j and count > k:   
                if nums[i] == 0:
                    count -= 1
                i += 1
            ans = max(ans, j- i + 1)
            j += 1
        return ans