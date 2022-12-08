# Recursive approach 
# correct only but giving TLE

class Solution:
    def matrixMultiplication(self, N, arr):
        i,j= 1, N-1  # we can only subdivide before 'n-1' so took j= 'n-1'
        return self.MCM(arr,i,j)
    def MCM(self,arr,start,end):
        if start== end:
            return 0
        mn= 99999999999
        for k in range(start,end):
            tempAns= self.MCM(arr,start,k) + self.MCM(arr,k+1,end) + arr[start-1]*arr[k]*arr[end]
            mn= min(mn,tempAns)
        return mn

# method 2: memoization
# time: O(n^3)
class Solution:
    def matrixMultiplication(self, N, arr):
        i,j= 1, N-1
        dp= [[-1 for j in range(N)] for i in range(N)]  # range of 'i' and 'j' is 'n' i.e from '0' to 'n-1'
        return self.MCM(arr,i,j,dp)
    def MCM(self,arr,start,end,dp):
        if start>= end:
            # dp[start][end]= 0
            # return dp[start][end]
            return 0  # or simply this only
        if dp[start][end]!= -1:
            return dp[start][end]
        mn= 99999999999
        for k in range(start,end):
            tempAns= self.MCM(arr,start,k,dp) + self.MCM(arr,k+1,end,dp) + arr[start-1]*arr[k]*arr[end]
            mn= min(mn,tempAns)
            dp[start][end]= mn
        return dp[start][end]


# Tabulation:
class Solution:
    def matrixMultiplication(self, N, arr):
        dp= [[0 for j in range(N)] for i in range(N)]   # automatically get initialised with base for 'dp[i][i]= 0' 
                                                        # when both 'i' and 'j' will be equal
        for start in range(N-1,0,-1):  # will go from 'n-1' to '1' 
            for end in range(start+1,N):  # 'end' must be always right of 'start' so started with 'start+1'. as for valid one 'end' must be greater than 'start'
                # now just copy paste the recurrence
                mn= 99999999999 
                for k in range(start,end):
                    tempAns= dp[start][k] + dp[k+1][end] + arr[start-1]*arr[k]*arr[end]
                    mn= min(mn,tempAns)
                dp[start][end]= mn
        return dp[1][N-1]   # we have called the recursive function for this variable value. so simply return that
