# method 1: Recursive
# logic: har index ke liye max_sum find karo 

# Note: Recursion me jyada dimag and socho nhi bs jo karna h wo likh do that's it. Nhi to recursion me kabhi bhi confidence nhi aayega pure life.

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n= len(arr)
        return self.helper(arr, 0, k, n)
    
# ye denote kar rha max_sum till index 'i'. Function ke meaning anusar hi base case likha jata har Q me.
    def helper(self, arr, i, k ,n):  
        if i== n:
            return 0
        len, max_ele, sum, ans= 0, -inf, 0, -inf
        for j in range(i, min(i+k, n)):
            len+= 1
            max_ele= max(max_ele, arr[j])
            sum= len * max_ele + self.helper(arr, j+1, k, n)   # max_till_now + max_sum from remaining indices.
            ans = max(ans, sum)
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
        len, max_ele, sum, ans= 0, -inf, 0, -inf
        for j in range(i, min(i+k, n)):
            len+= 1
            max_ele= max(max_ele, arr[j])
            sum= len * max_ele + self.helper(arr, j+1, k, n, dp)
            ans = max(ans, sum)
            dp[i]= ans
        return dp[i]

# Tabulation
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n= len(arr)
        dp= [0 for i in range(n+1)]
        for i in range(n-1, -1, -1):
            l, max_ele, sum, ans= 0, -inf, 0, -inf
            for j in range(i, min(i+k, n)):
                l+= 1
                max_ele= max(max_ele, arr[j])
                sum= l * max_ele + dp[j+1]
                ans = max(ans, sum)
                dp[i]= ans
        return dp[0]



