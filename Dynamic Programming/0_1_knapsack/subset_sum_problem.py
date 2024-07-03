# method 1: Recursion
class Solution:
    def isSubsetSum (self, N, arr, sum):
        return self.helper(N, arr, sum)
    def helper(self, n, arr, sum):
        if sum== 0:
            return True
        if n== 0:  # means n== 0 and sum != 0
            return False
        if arr[n-1] > sum:
            # Means we can't consider this ele. only one choice
            return self.helper(n-1,arr,sum)
        # Means we can consider this ele but we have choices i.e 1) Take it 2) Not take it.
        return self.helper(n-1,arr,sum- arr[n-1]) or self.helper(n-1,arr,sum)
    

# Other better way
# do by this methd only for this type of question

# We always has one choice to notTake and we can only take current ele if 'arr[i] <= sum'

class Solution:
    def isSubsetSum (self, N, arr, sum):
        return self.helper(N, arr, sum)
    def helper(self, n, arr, sum):
        if sum== 0:
            return True
        if n== 0:  # means n== 0 and sum != 0
            return False
        take = False
        if arr[n-1] <= sum:
            take = self.helper(n-1,arr,sum - arr[n -1])
        notTake = self.helper(n-1,arr,sum)
        return take or notTake


# memoized method:

class Solution:
    def isSubsetSum (self, N, arr, sum):
        dp= [[-1 for i in range(sum+1)] for i in range(N +1)]   
        ans=  self.helper(N, arr, sum, dp)
        return ans
    
    def helper(self, n, arr, sum, dp):
        if sum== 0:
            return True
        if n== 0:  # means n== 0 and sum != 0
            return False
        if dp[n][sum]!= -1:
            return dp[n][sum]
        if arr[n-1]> sum:
            dp[n][sum]= self.helper(n-1,arr,sum, dp)
        else:
            dp[n][sum]= self.helper(n-1,arr,sum- arr[n-1], dp) or self.helper(n-1,arr,sum, dp)
        return dp[n][sum]


# method 3: By Bottom up  Approach
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

# Other way of initialsing the base case.
# dp[0][0] = should be 'True' and in above one 2nd if is making it automatically 'True' that's why above one is working.
# i.e sum = 0 is possible with no ele.

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # 1st initialse the matrix properly
        dp= [[-1 for i in range(sum+1) ] for i in range(N+1)]
        for i in range(N+1):
            dp[i][0] = 1
        for i in range(sum+1):
            dp[0][i] = 0
        dp[0][0] = 1
        # now just same as 0/1 Knapsack           
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]> j:
                    dp[i][j]= dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
        return dp[N][sum]   

# method 4: optimising space complexity to O(n)
class Solution:
    def isSubsetSum (self, N, arr, sum):
        pre = [0] * (sum + 1)
        pre[0] = 1   # just dp[0][0] = 1
        # now just same as 0/1 Knapsack           
        for i in range(1,N+1):
            cur = [0] * (sum + 1)
            cur[0] = 1   # value of dp[i][0]
            for j in range(1,sum+1):
                if arr[i-1] > j:
                    cur[j]= pre[j]
                else:
                    cur[j]= pre[j-arr[i-1]] or pre[j]
            pre = cur.copy()
        return pre[sum] 

