# method 2: Memoization
# logic:  # just exactly same as ' count no of subsets with a given sum'
        # just write the logic of unbounded kanpsack when we include any else:
        # here we don't need to make the weight array like 'cutting rod problem' 
        # acc to the q we will increase/ decrease the no of variable
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        N= len(coins)
        dp= [[-1 for i in range(amount +1)] for i in range(N +1)]   
        return self.helper(N, coins, amount, dp)
    def helper(self, n, arr, sum, dp):
        if sum== 0:  # we have to find the ways so first check 'if sum==0'
            return 1
        if n== 0:   # means sum!= 0 and n==0
            return 0
        if dp[n][sum] != -1: 
            return dp[n][sum]
        if arr[n -1]> sum:
            dp[n][sum]= self.helper(n -1, arr, sum, dp)
        else:   # arr[n -1] <= sum
            dp[n][sum]= self.helper(n, arr, sum- arr[n-1], dp) + self.helper(n -1, arr, sum, dp)
        return dp[n][sum]


# method 2: Bottom up Approach
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
        