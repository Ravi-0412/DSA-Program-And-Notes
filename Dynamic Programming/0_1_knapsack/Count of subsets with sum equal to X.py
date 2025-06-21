# Basic:

# this will not give correct ans in all cases when val of array element < 1
# will give less number of count than the actual one

# this totaly same as subset sum just replaced False -> 0 and True ->1
# but this will not work in case val of ele = 0  
class Solution:
    def perfectSum(self, arr, sum):
        N = len(arr)
        return self.helper(N, arr, sum)
    def helper(self, n, arr, sum):  # no need of this helper function
        if sum== 0:
            return 1
        if n== 0:  # means n== 0 and sum != 0
            return 0
        if arr[n-1] > sum:
            return self.helper(n-1,arr,sum)
        else:
            return self.helper(n-1,arr,sum- arr[n-1]) + self.helper(n-1,arr,sum)


# arr= [1,2,3,3]
# arr= [1,1,1,1]
# arr= [1,1,2,3]
# print(NoOfSubsets(4,arr,6))   
# print(NoOfSubsets(4,arr,4)) 


# Method 1: 
# Recursion
# correct one that will work in all cases

# Note vvi:  to find all the ans just write the base case when you reach the last ele instead when sum == 0.

class Solution:
    def perfectSum(self, arr, target):
        return self.helper(len(arr), arr, target)

    def helper(self, n, arr, target):
        if n == 1:
            if target == 0 and arr[0] == 0:
                return 2  # include or exclude 0
            if target == 0 or target == arr[0]:
                return 1
            return 0

        take = 0
        if arr[n - 1] <= target:
            take = self.helper(n - 1, arr, target - arr[n - 1])
        notTake = self.helper(n - 1, arr, target)

        return take + notTake


# Method 2:
# Memoisation
    
class Solution:
    def perfectSum(self, arr, target):
        N = len(arr)
        dp = [[-1 for _ in range(target + 1)] for _ in range(N + 1)]
        return self.helper(N, arr, target, dp)
    
    def helper(self, n, arr, target, dp):
        if n == 1:
            if target == 0 and arr[0] == 0:   # either take the 1st ele or not both will be our ans
                return 2  # include or exclude 0
            if target == 0 or target == arr[0]:  # in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1
            return 0
        
        if dp[n][target] != -1:
            return dp[n][target]

        take = 0
        if arr[n - 1] <= target:
            take = self.helper(n - 1, arr, target - arr[n - 1], dp)
        notTake = self.helper(n - 1, arr, target, dp)

        dp[n][target] = take + notTake
        return dp[n][target]


# Method 3:
# Tabulation

class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # Base case initialization
        # For any i, sum = 0 → count = 1 (empty subset)
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Handle first element separately
        if arr[0] == 0:
            dp[1][0] = 2  # empty subset + subset with zero
        elif arr[0] <= target:
            dp[1][arr[0]] = 1
        
        # Fill the dp table
        for i in range(2, n + 1):
            for t in range(target + 1):
                take = 0
                if arr[i - 1] <= t:
                    take = dp[i - 1][t - arr[i - 1]]
                notTake = dp[i - 1][t]
                dp[i][t] = take + notTake
        
        return dp[n][target]






