# Logic: 
"""
i) If you can find a subset whose sum is as close as possible to half of the total sum of the array, 
the difference between this subset and the other subset will be minimized.
ii) Mathematically, if the total sum of the array is totalSum, 
you want to find a subset with a sum as close as possible to totalSum // 2.
"""

# submitted on GFG
class Solution:
    def isSubsetSum(self, N, arr, target_sum):
        # Initialize the dp matrix
        dp = [[False for _ in range(target_sum + 1)] for _ in range(N + 1)]
        # Subset sum of 0 is always possible
        for i in range(N + 1):
            dp[i][0] = True
        
        # Fill the dp matrix
        for i in range(1, N + 1):
            for j in range(1, target_sum + 1):
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
        
        return dp[N] # this will contain the possible subset sum for numbers till target_sum(boolean array)
                  # since we are returning the last row and last row will give the ans for all possible subset sum till target_sum
    
    def minDifference(self, arr, n):
        total_sum = sum(arr)
        half_sum = total_sum // 2
        
        # Get possible subset sums till half_sum
        possible_subset_sum = self.isSubsetSum(n, arr, half_sum)
        
        # Find the maximum sum that is possible and <= half_sum
        max_subset_sum = 0
        for i in range(half_sum + 1):
            if possible_subset_sum[i]:
                max_subset_sum = i
        
        # Calculate minimum difference
        min_diff = total_sum - 2 * max_subset_sum
        
        return min_diff

# Method 2: 
# Optimising the space to O(Target_sum) i.e O(sum(arr))
# Logic: 
"""
Above logic only just used element value directly instead of index.
i) Subproblem: We want to know whether it’s possible to form a subset with a sum j using the first i elements of the array.
ii) State Definition: Let dp[j] be a boolean that tells us whether a subset with sum j is possible.
iii) Transition: For each element num in the array, if dp[j - num] is True, then dp[j] should also be True. 
This means if we can form a subset with sum j - num, then by adding num, we can form a subset with sum j.
iv) Initialization: dp[0] = True, since a sum of 0 can always be formed with an empty subset.
"""
class Solution:
    def isSubsetSum(self, arr, target_sum):
        n = len(arr)
        dp = [False] * (target_sum + 1)
        dp[0] = True  # Subset sum of 0 is always possible (empty set)
        
        for num in arr:
            # Traverse backwards to avoid overwriting values that we need to check in the same iteration
            # This ensures that each number is only used once in calculating possible subset sums.
            for j in range(target_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp
    
    def minDifference(self, arr, n):
        total_sum = sum(arr)
        half_sum = total_sum // 2
        
        # Get possible subset sums
        possible_subset_sum = self.isSubsetSum(arr, half_sum)
        
        # Find the maximum sum that is possible and <= half_sum
        max_subset_sum = 0
        for i in range(half_sum + 1):
            if possible_subset_sum[i]:
                max_subset_sum = i
        
        # Calculate minimum difference
        min_diff = total_sum - 2 * max_subset_sum
        
        return min_diff

# Using method 2 logic
class Solution:
    def minDifference(self, arr, n):
        total_sum = sum(arr)  # Calculate the total sum of the array
        half_sum = total_sum // 2  # Target half of the total sum
        
        # dp[i] will be True if a subset with sum i is possible
        dp = [False] * (half_sum + 1)
        dp[0] = True  # Subset sum of 0 is always possible (empty set)
        
        # Fill the dp array
        for num in arr:
            # Traverse backwards to avoid overwriting values that we need to check in the same iteration
            for j in range(half_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        # Find the maximum subset sum that is possible and <= half_sum
        max_subset_sum = 0
        for i in range(half_sum + 1):
            if dp[i]:
                max_subset_sum = i
        
        # Calculate the minimum difference
        min_diff = total_sum - 2 * max_subset_sum
        
        return min_diff
    
# method 3: question reduces to find closest sum (sum of numbers) to (SUM/2).
# for finding closest sum to sum(arr)/2. we can do like.

# Exactly same code as :'1049.Last stone weight 2'.

# submitted on gfg.
class Solution:
    def minDifference(self, arr, n):
	    total= sum(arr)
        mid= total//2   # we have to find the closest sum possible for 'mid_sum'.
        dp= [[0 for j in range(mid +1)] for i in range(n+1)]
        # dp[i][j] : subset sum close to 'j' considering 'i' element.
        for i in range(1, n+1):
            for j in range(1, mid+1):
                if arr[i-1] > j:  # when we have no choice to  include the curr ele.
                    dp[i][j]= dp[i-1][j]
                else:   # when we have choice to include the curr ele or not.
                    dp[i][j]= max(dp[i-1][j], dp[i-1][j- arr[i-1]] + arr[i-1])   # we have to find the closest sum so taking max.
        return abs(total- 2*dp[n][mid])    # ans will be equal to this one.   (some maths done in notes).


# Follow up question:
# Q) Find the sum of both the arrays and return their sum in a list.
# i.e "divide a array into two array such that diferrence of their sum is minimum , and return sum of both the arrays "

"""
class Solution:
    def getProcessTime(self, arr):
        # Call the minDifferencePartition method to get the partitioned sums
        partition_sums = self.minDifferencePartition(arr)
        
        # Convert the result to a list of integers and return
        result = [int(partition_sums[0]), int(partition_sums[1])]
        return result

    # Method to find the two subsets with minimal difference in their sums
    def minDifferencePartition(self, arr):
        n = len(arr)
        total_sum = sum(arr)  # Calculate the total sum of the array
        
        half_sum = total_sum // 2  # Target half of the total sum
        
        # dp[i] will be True if a subset with sum i is possible
        dp = [False] * (half_sum + 1)
        dp[0] = True  # Subset sum of 0 is always possible (empty set)
        
        # Fill the dp array
        for num in arr:
            # Traverse backwards to avoid overwriting values that we need to check in the same iteration
            for j in range(half_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        # Find the maximum sum that is possible and is less than or equal to half_sum
        subset1_sum = 0
        for j in range(half_sum, -1, -1):
            if dp[j]:
                subset1_sum = j
                break
        
        subset2_sum = total_sum - subset1_sum  # The other subset sum is total_sum - subset1_sum
        
        # Return the sums of both subsets
        return [subset1_sum, subset2_sum]
"""

# Related Q: 
# 1) 1049.Last stone weight 2'.
# 2) 2035. Partition Array Into Two Arrays to Minimize Sum Difference   => Try later
# 3) Split array into two subarrays such that difference of their sum is minimum   => Try later
# https://www.geeksforgeeks.org/split-array-into-two-subarrays-such-that-difference-of-their-sum-is-minimum/

