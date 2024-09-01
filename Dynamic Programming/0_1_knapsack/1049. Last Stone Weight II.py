# Logic: 
"""
Say you have four stones a,b,c,d.
first you smash b against c, you get (b-c)
now you smash (b-c) against a
you get a-(b-c) which is same as (a+c)-(b)
now you smash d against (a+c)-b
you get d-((a+c)-b) which is same as (d+b)-(a+c).
Basically for the given stones we can create two sets,the sum of second set of stones to be subtracted from sum of first one.
ideally we want sum of each set to be sum(stones)/2 so that they cancel each other out.

So to solve the problem we try to 'select a set of stones such that their sum comes as close as possible to sum(stones)/2'.
Clearly this subproblem is analogous to the knapsack problem.

"""

# How to do this?
# we can reduce this further more to ' partition an array into 2 subsets whose difference is minima.
# And we have to find that difference.

# How to find the diff?
# (1) S1 + S2  = S
# (2) S1 - S2 = diff  , s1 >= s2
# ==> solving these two: take s1 = s - s2 from (1) and put in 2nd then 
# diff = S - 2 * S2 
# ==> minimize diff equals to  maximize S2 

# Finally reduces to find: 'Minium sum Partition'.

# So question reduces to find closest sum (sum of numbers) to (SUM/2).
# for finding closest sum to sum(arr)/2. we can do like.

# Using method of 'Minimum sum partition"
# Method 1: 
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)  # Calculate the total sum of all stones
        half_sum = total_sum // 2  # Target half of the total sum
        
        # Initialize the DP array
        dp = [False] * (half_sum + 1)
        dp[0] = True  # Subset sum of 0 is always possible (empty set)
        
        # Fill the DP array
        for stone in stones:
            # Traverse backwards to avoid overwriting values that we need to check in the same iteration
            for j in range(half_sum, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]
        
        # Find the maximum subset sum that is possible and <= half_sum
        max_subset_sum = 0
        for i in range(half_sum + 1):
            if dp[i]:
                max_subset_sum = i
        
        # Calculate the minimum difference
        min_diff = total_sum - 2 * max_subset_sum
        
        return min_diff

# Method 2: 

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total, n= sum(stones), len(stones)
        mid= total//2   # we have to find the closest sum possible for 'mid'.
        dp= [[0 for j in range(mid +1)] for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, mid+1):
                if stones[i-1] > j:  # when we have no choice to  include the curr ele.
                    dp[i][j]= dp[i-1][j]
                else:   # when we have choice to include the curr ele or not.
                    dp[i][j]= max(dp[i-1][j], dp[i-1][j- stones[i-1]] + stones[i-1])   # we have to find the closest sum so taking max.
        return abs(total- 2*dp[n][mid])    # ans will be equal to this one.  

