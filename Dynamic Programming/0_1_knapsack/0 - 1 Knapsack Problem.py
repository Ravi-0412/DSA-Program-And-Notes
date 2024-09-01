
# In other words, given two integer arrays val[0..n-1] and wt[0..n-1] 
# which represent values and weights associated with n items respectively.
#  Also given an integer W which represents knapsack capacity, 
# find out the maximum value subset of val[] such that sum of the weights of 
# this subset is smaller than or equal to W. 
# Note: You cannot break an item, either pick the complete item or don’t pick it (0-1) property

# method1: by recursion
# just like subsequence and subset. basically we are finding this only from the value array

# Logic: For every ele we have two choice : 1) include that or 2) Not include that
# we can only include if sufficient weight in bag is available.

# Time Complexity: O(2^n), no extra space but recursion  O(n)
def knapSack(N, W, val, wt):  # max profit you can get with 'n' items having available bag size = w
    if N==0 or W==0:
        return 0
    if wt[N-1]<= W: # we have two choices either to take this item or not
        return max(val[N-1]+ knapSack(N-1,W- wt[N-1],val,wt), knapSack(N-1,W,val, wt))
    else:  # only one option i.e we can't take this ele. Move to next ele.
        return knapSack(N-1,W,val, wt) 

N = 3
W = 3
values = [1,2,3]
weight = [4,5,6]
print(knapSack(N,W,values,weight))


# submitted on gfg
# time complexity: O(N*W)
# method: By memoization
# 2 variable changing so 2d dp and for size see the range of both the variable from base case to max value it can go
# n:  can go from 0(base case) to n and same for w so it will (n+1)*(w+1)
class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp=[[-1 for j in range(W+1)] for i in range(n+1)]  # initialising the answer matrix  
        return self.helper(W,wt,val,n,dp)
    def helper(self,W,wt,val,n,dp):
        if W==0 or n==0:  # if bag is full or there is no item to place
            return 0
        if dp[n][W]!= -1:  # means value for that function is already calculated
            return dp[n][W]
        if wt[n-1]>W:   # we are checking from last so will comapre with weight of last ele with available bag size ans so on
            dp[n][W]= self.helper(W, wt, val,n-1,dp)
        if wt[n-1]<= W:    # if weight of that item is less than or equal to the available bag size
            dp[n][W]= max((val[n-1]+ self.helper(W-wt[n-1],wt,val,n-1,dp)), self.helper(W, wt, val,n-1,dp))
        return dp[n][W]   # we started the Recursive call from (n,w) so return dp[n][w]


# another method: Tabulation (By Bottom up approach)
# just write the base case and then replace by for loop and inside for loop just copy paste the code of recursion and replace function call by DP value
class Solution:
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        dp= [[0 for j in range(W+1)] for i in range(n+1)]  # already base case is filled for this Q after initialising with zero
        # start filing from dp[1,1] to last
        for i in range(1,n+1):  # n= no of total objects, i= object till 'i' we are considering
            for j in range(1,W+1):  # W= no of total bags, j: bags we are considering at present
                if wt[i-1]<= j:
                    dp[i][j]= max(val[i-1]+ dp[i-1][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[n][W]  # we started the Recursive call from (n,w) so return dp[n][w]


# Better one
# Logic: for each element we have two choice : 1) NotTake and 2) take
# and we can only take 'nth' element 'if wt[n-1] <= W:'.
# ans = max(notTake, take)

# Note: Always try to do this type of question by this approach only (notTake & take).
class Solution:
    def knapSack(self,W, wt, val):
        n = len(wt)
        dp = [[-1 for j in range(W+1)] for i in range(n+1)]  # initialising the answer matrix  
        return self.helper(W,wt,val,n,dp)
        
    def helper(self,W,wt,val,n,dp):
        if W==0 or n==0:  # if bag is full or there is no item to place
            return 0
        if dp[n][W]!= -1:  # means value for that function is already calculated
            return dp[n][W]
        notTake = self.helper(W, wt, val, n-1, dp)
        take = 0
        if wt[n-1] <= W:
            take =  val[n-1] + self.helper(W - wt[n-1], wt, val, n-1, dp)
        dp[n][W] = max(take, notTake)
        return dp[n][W] 