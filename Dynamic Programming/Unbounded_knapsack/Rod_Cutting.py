# logic: here length will behave as 'weight' and total length as 'capacity'
# other everything is same as unbounded Knapsack
# method 1: memoization
class Solution:
    def cutRod(self, price, n):
        wt= [i+1 for i in range(n)]   # length array, not given so we have to make itself acc to Q
        dp=[[-1 for j in range(n + 1)] for i in range(n +1)]  # initialising the answer matrix  
        return self.helper(n, n, price, wt, dp)    # here available bag size will be also equal to 'n' comapring with unbounded 0/1 knapsack
        # everything is excatly same as unbounded 0/1 knapsack
        
    def helper(self,N,W,val,wt,dp):
        if N==0 or W==0:
            return 0
        if dp[N][W]!= -1:
            return dp[N][W]
        if wt[N-1]<= W:
            dp[N][W]= max(val[N-1]+ self.helper(N,W- wt[N-1],val,wt,dp), self.helper(N-1,W,val, wt,dp))
        else:
            dp[N][W]= self.helper(N-1,W,val, wt,dp)
        return dp[N][W]



# method 2:By bottom up approach
class Solution:
    def cutRod(self, price, n):
        length= [i for i in range(1,n+1)]
        return self.knapSack(n,n,price,length)
    def knapSack(self, N, W, val, wt):
        dp= [[0 for i in range(W+1)] for i in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,W+1):
                if wt[i-1]<= j:
                    dp[i][j]= max(val[i-1]+ dp[i][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[N][W]


