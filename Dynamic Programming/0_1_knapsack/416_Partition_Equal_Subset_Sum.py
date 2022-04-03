# find the sum of the aarray, if sum is odd then no partition possible
# if sum is even then may be possible
# and for finding this, apply eaxctly the subset method on sum/2
# time: space= O(n*(sum/2))
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum= 0
        for num in nums:
            list_sum+= num
        if list_sum %2!= 0:
            return False
        sum_to_check= list_sum//2
        return self.isSubsetSum(len(nums),nums,sum_to_check)   

    def isSubsetSum (self, N, arr, sum):
        # 1st initialse the matrix properly
        dp= [[-1 for i in range(sum+1) ] for i in range(N+1)]
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
        return dp[N][sum]



# another method to reduce space complexity, by using 1D array for ans
# but i am not getting it
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total= sum(nums)
        print(total)
        if total & 1== 1:
            return False
        print(total)
        # initialse in the same way as we do for 1st row in subset
        dp= [False for i in range(total//2+1)]
        dp[0]= True
        total= total//2
        print(dp)
        # start checking from last and we if we reach index 0 for total==0
        # then means possible otherwise not
        for num in nums:
            for i in range(total,0,-1):
                if i>= num:
                    dp[i]= dp[i] | dp[i-num]
                    
        return dp[total]