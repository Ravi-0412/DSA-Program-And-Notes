class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.NoWays(len(coins),coins,amount)
    
    def NoWays(self,N, arr, sum):
        # 1st initialse the matrix properly, just like 'no of subsets with a given sum'
        dp= [[0 for i in range(sum+1) ] for i in range(N+1)]
        for i in range(N+1):
            for j in range(sum+1):
                if j==0:
                    dp[i][j]= 1
        # exactyle same as "count the no of subsets with a given sum" . only change the included condition(like unbouded knapsack)       
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]> j: 
                    dp[i][j]= dp[i-1][j]
                else: # ways possible including this ele(unbounded one) + ways possible without including it
                    dp[i][j]= dp[i][j-arr[i-1]] + dp[i-1][j]
        return dp[N][sum]
        