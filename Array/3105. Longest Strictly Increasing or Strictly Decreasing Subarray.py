# Method 1:
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = inc = dec = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1  # ↗️ Case
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1  # ↘️ Case
                inc = 1
            else:
                inc = dec = 1  # 🟡 Case
            max_len = max(max_len, inc, dec)  # Update ans
        return max_len

# Method 2:
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n, ans, inc, dec=len(nums), 1, 1, 1
        for i in range(1, n):
            A=nums[i] > nums[i-1]   # A = 1 if condition follows, else 0
            B=nums[i] < nums[i-1]   # B = 1 if condition follows, else 0
            inc=A*inc+1
            dec=B*dec+1
            ans=max(ans, dec, inc)
        return ans
