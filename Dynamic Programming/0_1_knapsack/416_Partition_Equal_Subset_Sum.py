# Problem reduces to: is there any subset possible which has sum equal to sum(array)//2

# find the sum of the array, if sum is odd then no partition possible
# if sum is even then may be possible
# and for finding this, apply eaxctly the subset method on sum/2
# time: space= O(n*(sum/2))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum= sum(nums)
        if list_sum %2!= 0:
            return False
        sum_to_check= list_sum//2
        return self.isSubsetSum(len(nums),nums,sum_to_check)   

    def isSubsetSum (self, N, arr, sum):
        # 1st initialse the matrix properly
        dp= [[False for i in range(sum+1) ] for i in range(N+1)]
        for i in range(N+1):
            for j in range(sum+1):
                if j==0:   # sum==0 
                    dp[i][j]= True
                elif i==0:  # sum!= 0 and number of ele= 0.
                    dp[i][j]= False
        # now just same as 0/1 Knapsack           
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]> j:
                    dp[i][j]= dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
        return dp[N][sum]


# Reducing time complexity to O(n).
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum= sum(nums)
        if list_sum %2!= 0:
            return False
        sum_to_check= list_sum//2
        return self.isSubsetSum(len(nums),nums,sum_to_check)   

    def isSubsetSum (self, N, arr, sum):
        # 1st initialse the matrix properly
        pre= [False for i in range(sum+1)]
        # filling the 1st row i.e for n== 0(when we are not considering any ele)
        pre[0]= True  # sum==0 if possible with '0' ele and all other will be False.
       
        for i in range(1,N+1):
            cur= [False for i in range(sum+1)]
            for j in range(1,sum+1):
                if arr[i-1]> j:
                    cur[j]= pre[j]
                else:
                    cur[j]= pre[j-arr[i-1]] or pre[j]
            pre= cur.copy()
        return cur[sum]

