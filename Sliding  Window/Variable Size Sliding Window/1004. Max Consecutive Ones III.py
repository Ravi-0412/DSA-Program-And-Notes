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

# Java
"""
class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int i = 0, j = 0;
        int count = 0;  // number of zeros in the current window
        int ans = 0;

        while (j < n) {
            if (nums[j] == 0) {
                count++;
            }

            while (i <= j && count > k) {
                if (nums[i] == 0) {
                    count--;
                }
                i++;
            }

            ans = Math.max(ans, j - i + 1);
            j++;
        }

        return ans;
    }
}
"""

# Follow up: Find all the indices of the 0s that were flipped to 1 in order to get the longest subarray of consecutive 1s.

from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = 0
        zero_count = 0
        max_len = 0
        best_left = 0

        for right in range(n):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            if right - left + 1 > max_len:
                max_len = right - left + 1
                best_left = left

        # Collect the indices of zeros that were flipped in the best window
        flipped_indices = [
            i for i in range(best_left, best_left + max_len) if nums[i] == 0
        ]
        return flipped_indices


# Note vvi: Whenever you have to find the 'largest subarray length of a single consecutive ele'
# where you can change other ele then apply this logic only.

# Related Q: 
# 1)  "1493. Longest Subarray of 1's After Deleting One Element",
# 2)  "2024. Maximize the Confusion of an Exam"
