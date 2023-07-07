# prefix[i]: denotes max number of consecutive '1' we can get starting from index 'i' to indices i-1, i-2,....0.
# suffix[i]: denotes max number of consecutive '1' we can get starting from index 'i' to indices i+1, i+2,....n-1.
# our ans will be max of 'prefix[i- 1] + suffix[i + 1]' if there is '0' at index 'i'
# Note : we can escape 'if' condition while calculating the prefix and suffix because prefixSum and suffixSum is already initialised to '0'.

# Logic: We have to delete one '0' from nums.

# Note: Our ans can be maximum 'n-1' because we have to delete one element.

# Time = space = O(n)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        # if single ele then ans = 0 since we must have to delete one element.
        if n == 1:
            return 0
        # check if only '0' is present in the array
        if max(nums) == 0:
            return 0
        prefixSum, suffixSum = [0]*n, [0]*n
        if nums[0] == 1:
            prefixSum[0] = 1
        if nums[-1] == 1:
            suffixSum[-1] = 1
        # First calculate the prefixSum
        for i in range(1, n):
            if nums[i] == 0:
                prefixSum[i] = 0
            else:
                prefixSum[i] = prefixSum[i - 1] + 1
        # check if only '1' is present in the array'
        if prefixSum[-1] == n:
            return n - 1   # we must have to delete one element.

        # Now calculate the suffixSum
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                suffixSum[i] = 0
            else:
                suffixSum[i] = suffixSum[i + 1] + 1   
        ans = 0
        # No need to check for '1' case 
        for i in range(n):
            if nums[i] == 0:
                if i == 0 :
                    ans = max(ans, suffixSum[i + 1])
                elif i == n- 1:
                    ans = max(ans, prefixSum[i -1])
                else:
                    ans = max(ans, prefixSum[i -1] + suffixSum[i + 1])
        return ans


# Method 2: Very better one.

# Totally above logic only but here for prefix we are shifting '1' to right and for suffix we are shifting '1' to left.
# So here no need to calculate ans by 'prefixSum[i -1] + suffixSum[i + 1]', we can get directly by max(prefixSum[i] + suffixSum[i])
# Because after shifting 'i-1' -> i , i<-'i+1' from both left and right .

# Time : O(n)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        prefixSum= [0] * n
        for i in range(1, n):
            if nums[i -1] == 1:
                prefixSum[i] = prefixSum[i - 1] + 1
        suffixSum= [0] * n
        for i in range(n-2, -1, -1):
            if nums[i + 1] == 1:
                suffixSum[i] = suffixSum[i + 1] + 1
        ans = 0
        for i in range(n):
            ans = max(ans, prefixSum[i] + suffixSum[i])
        return ans


# Method 3: Exactly same as "1004. Max Consecutive Ones III".
# Only difference is: 
# 1) Here k = 1, 2) we have to delete one ele so our ans = max(length_valid_subarray -1)
# 3) k= 1 > 0 so we don't need to take 'i' = j for finding the valid subarray i.e 'i < j' only.

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

