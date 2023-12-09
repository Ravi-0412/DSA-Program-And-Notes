# Just similar logic to : "713. Subarray Product Less Than K".
# Logic: Traverse the array and keep updating the frequency of cur number.
# After updating the frequency slide the window from left till frequency[cur_num] > k. 
# Then update the ans.
# Time : O(n)

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i, j = 0, 0
        ans = 0
        freq = collections.defaultdict(int)
        while j < n:
            freq[nums[j]] += 1
            while i < j and freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1
            ans= max(ans, j - i + 1)
            j += 1
        return ans