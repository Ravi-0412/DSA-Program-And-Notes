# memoized method: Giving TLE but iots correct only

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # dp= [[-1 for i in range(sum+1) ] for i in range(N+1)]
        # if sum==0:
        #     return True
        # if N==0:
        #     return False
        # if dp[N][sum]!= -1:
        #     return dp[N][sum]
        # if arr[N-1]> sum:
        #     dp[N][sum]= self.isSubsetSum(N-1,arr,sum)
        #     return dp[N][sum]
        # else:
        #     dp[N][sum]= self.isSubsetSum(N-1,arr,sum-arr[N-1]) or self.isSubsetSum(N-1,arr,sum)
        #     return dp[N][sum]


# method 2: By top Down Approach
class Solution:
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

