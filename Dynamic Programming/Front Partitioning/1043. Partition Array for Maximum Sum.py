# method 1: Recursive
# logic: har index ke liye max_sum find karo, har subarray ka.

# Note: Recursion me jyada dimag nhi lagao and socho nhi bs jo karna h wo likh do that's it. 
# Nhi to recursion me kabhi bhi confidence nhi aayega pure life.

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n= len(arr)
        return self.helper(arr, 0, k, n)
    
# ye denote kar rha max_sum of subarray starting from index 'i' to 'n-1'.
    def helper(self, arr, i, k ,n):  
        if i== n:
            return 0
       ans, max_ele = 0, 0
        # Iterate over the next k elements or until the end of the array
        for j in range(i, min(i+k, n)):
            max_ele = max(max_ele, arr[j])
            # Calculate the current sum considering the maximum value in the partition
            curSum = (j - i + 1) * max_ele + self.helper(arr, j+1, k, n)   # max_till_now + max_sum from remaining indices.
            ans = max(ans, curSum)
        return ans

# method 2: Memoization
# Time:  O(NK)
# Space: O(N)
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n= len(arr)
        dp= [-1 for i in range(n+1)]
        return self.helper(arr, 0, k, n, dp)
    
    def helper(self, arr, i, k ,n, dp):
        if i== n:
            return 0
        if dp[i]!= -1:
            return dp[i]
        ans, max_ele = 0, 0
        for j in range(i, min(i+k, n)):
            max_ele = max(max_ele, arr[j])
            curSum = (j - i + 1) * max_ele + self.helper(arr, j+1, k, n, dp)
            ans = max(ans, curSum)
            dp[i]= ans
        return ans

# Tabulation
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n= len(arr)
        dp = [0 for i in range(n+1)]
        for i in range(n-1, -1, -1):
            ans, max_ele = 0, 0
            for j in range(i, min(i+k, n)):
                max_ele = max(max_ele, arr[j])
                curSum = (j - i + 1) * max_ele + dp[j + 1] 
                ans = max(ans, curSum)
                dp[i] = ans
        return ans



