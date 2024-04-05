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

# Method 1: 

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n= len(stones)
        return self.minDifference(stones, n)

    def minDifference(self,arr,n):
        total= sum(arr)
        possible_subset_sum= self.isSubsetSum(n,arr,total) 
        # possible_subset_sum will contain the array with possible_sum till total
        subset_to_check= (total)//2+1   # we have to check till middle only 
        possibe_till_half= []   # this will store the number for which subset sum 
                                                # is possible till middle of total(except 1st index) 
        # print(possibe_till_half)
        for i in range(subset_to_check):
            if possible_subset_sum[i]== True:
                possibe_till_half.append(i)
        min_diff= 999999999
        # print(possibe_till_half)
        for num in possibe_till_half:
            min_diff= min(min_diff, total-2*num)
        return min_diff
    
    def isSubsetSum (self,N, arr, sum):
        # 1st initialse the matrix properly
        dp= [[-1 for j in range(sum+1) ] for i in range(N+1)]
        for i in range(N+1):
            for j in range(sum+1):
                if i==0:
                    dp[i][j]= False
                if j==0:
                    dp[i][j]= True
        # now just same as 0/1 Knapsack           
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]> j:
                    dp[i][j]= dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
        return dp[N]  # this will contain the possible subset sum for numbers till total(boolean array)
                  # since we are returning the last row and last row will give the ans for all possible subset sum till total

# method 2: question reduces to find closest sum (sum of numbers) to (SUM/2).
# for finding closest sum to sum(arr)/2. we can do like.

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
        return abs(total- 2*dp[n][mid])    # ans will be equal to this one.   (some maths done in notes).
    
