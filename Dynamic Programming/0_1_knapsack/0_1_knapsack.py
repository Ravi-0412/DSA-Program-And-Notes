# method1: by recursion
def knapSack(N, W, val, wt):
    if N==0 or W==0:
        return 0
    if wt[N-1]<= W:
        return max(val[N-1]+ knapSack(N-1,W- wt[N-1],val,wt), knapSack(N-1,W,val, wt))
    else:
        return knapSack(N-1,W,val, wt) 

N = 3
W = 3
values = [1,2,3]
weight = [4,5,6]
print(knapSack(N,W,values,weight))


# submitted on gfg
# time complexity: O(N*W)
# method: By memoization
class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp=[[-1 for j in range(W+1)] for i in range(n+1)]  # initialising the answer matrix  
        ans= self.helper(W,wt,val,n,dp)
        print(dp)
        return ans
    def helper(self,W,wt,val,n,dp):
        if W==0 or n==0:  # if bag is full or there is no item to place
            return 0
        if dp[n][W]!= -1:  # means value for that function is already calculated
            return dp[n][W]
        if wt[n-1]>W:   # we are checking from last so will comapre with weight of last ele with available bag size ans so on
            dp[n][W]= self.helper(W, wt, val,n-1,dp)
        if wt[n-1]<= W:    # if weight of that item is less than or equal to the available bag size
            dp[n][W]= max((val[n-1]+ self.helper(W-wt[n-1],wt,val,n-1,dp)), self.helper(W, wt, val,n-1,dp))
        return dp[n][W]   # last ele of dp matrix will give the ans


# another method: (By Bottom up approach)
class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp= [[0 for j in range(W+1)]for i in range(n+1)]
        # start filing from dp[1,1] to last
        for i in range(1,n+1):  # n= no of total objects, i= object till 'i' we are considering
            for j in range(1,W+1):  # W= no of total bags, j: bags we are considering at present
                if wt[i-1]<= j:
                    dp[i][j]= max(val[i-1]+ dp[i-1][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[n][W]  # return the last grid value(bottom most one)



