

# submitted on GFG
class Solution:
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

    def minDifference(self,arr,n):
        total= sum(arr)
        possible_subset_sum= self.isSubsetSum(n,arr,total) 
        # possible_subset_sum will contain the array with possible_sum till total
        # print(possible_subset_sum) 
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


# method 2: question reduces to find closest sum (sum of numbers) to (SUM/2).
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


# Related Q: 
# 1) 1049.Last stone weight 2'.