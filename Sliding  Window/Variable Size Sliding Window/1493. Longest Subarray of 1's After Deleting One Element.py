
# Method 1:

# Totally above logic only but here for prefix we are shifting '1' to right and
#  for suffix we are shifting '1' to left because we have to delete exactly one ele.
# so by shifting, it will mean that we have already deleted that ele.

# Therefore here no need to calculate ans by 'prefixSum[i -1] + suffixSum[i + 1]',
#  we can get directly by max(prefixSum[i] + suffixSum[i])
# Because after shifting 'i-1' -> i , i<-'i+1' from both left and right both will point to 'i' only.

# Time : O(n)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum= [0] * n # prefix[i]: denotes max number of consecutive '1' we can get starting from index 'i' to indices i-1, i-2,....0.
        for i in range(1, n):
            if nums[i -1] == 1:
                prefixSum[i] = prefixSum[i - 1] + 1
        suffixSum= [0] * n  # suffix[i]: denotes max number of consecutive '1' we can get starting from index 'i' to indices i+1, i+2,....n-1.
        for i in range(n-2, -1, -1):
            if nums[i + 1] == 1:
                suffixSum[i] = suffixSum[i + 1] + 1
        ans = 0
        for i in range(n):
            ans = max(ans, prefixSum[i] + suffixSum[i])
        return ans


# Method 3: Exactly same as "1004. Max Consecutive Ones III".
# Only difference is: 
# 1) Here k = 1, 2) we have to delete exactly one ele so our ans = max(length_valid_subarray -1)
# 3) since we have to delete exactly one ele then valid subarray must be >= 1, so 'i' < 'j' here.

# Time: O(n), space : O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n= len(nums)
        i, j= 0, 0
        count = 0
        ans = 0
        while j < n:
            if nums[j] == 0:
                count += 1
            while i < j and count > 1:
                if nums[i] == 0:
                    count -= 1
                i += 1
            ans = max(ans, j- i)   # (length - 1)
            j += 1
        return ans

