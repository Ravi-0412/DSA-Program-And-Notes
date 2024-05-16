# Recursive approach 
# correct only but giving TLE

class Solution:
    def matrixMultiplication(self, N, arr):
        i,j= 1, N-1  # we can only subdivide before 'n-1' so took j= 'n-1'. can put braces from first matrix to 'one before last matrix)
        return self.MCM(arr,i,j)  # calculating the minimum multiplication from 'i'th matrix to 'j'th matrix.
    def MCM(self,arr,start,end):
        if start>= end:  # only one matrix remaining. "==" will also work.
            return 0
        mn= 99999999999
        for k in range(start,end):
            # start matrix se leke 'k' matrix tak + (k + 1) se leke 'j-1' tak
            # (start , k) matrix tak jo result matrix milega uska dimension hoga: arr[start-1]*arr[k]
            # (k + 1, end) matrix tak jo result matrix milega uska dimension hoga: arr[k] * arr[end]
            # no of multiplication hoga dono ka: arr[start-1]*arr[k] * arr[end] i.e just conside above sub-matrix as separate matrix .
            # And is dono ka resultant matrix ka jo dimension hoga: arr[start-1] * arr[end] .
            tempAns= self.MCM(arr,start,k) + self.MCM(arr,k+1,end) + arr[start-1]*arr[k]*arr[end]   # will store all possible ans
            mn= min(mn,tempAns)   # take minimum of all ans.
        return mn

# method 2: memoization
# time: O(n^3)
class Solution:
    def matrixMultiplication(self, N, arr):
        i,j= 1, N-1
        dp= [[-1 for j in range(N)] for i in range(N)]  # range of 'i' and 'j' is 'n' i.e from '1' to 'n-1' but indexing will start from '0' only so took size= n
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
# Note: In MCM type Q, go from first valid input to first invalid input (both inclusive) or vice versa.
# both looping variable should go till first function call after initialisng the base case.
class Solution:
    def matrixMultiplication(self, N, arr):
        dp= [[0 for j in range(N)] for i in range(N)]   # automatically get initialised with base for 'dp[i][i]= 0' 
                                                        # when both 'i' and 'j' will be equal
        for start in range(N-2,0,-1):  # from last valid one to first valid one. n-2 to '1'.
            for end in range(start+1,N):  # 'end' must be always right of 'start' so started with 'start+1'. as for valid one 'end' must be greater than 'start' and first invlaid one= 'n-1'.
                # now just copy paste the recurrence
                mn= 99999999999 
                for k in range(start,end):
                    tempAns= dp[start][k] + dp[k+1][end] + arr[start-1]*arr[k]*arr[end]
                    mn= min(mn,tempAns)
                dp[start][end]= mn
        return dp[1][N-1]   # we have called the recursive function for this variable value. so simply return that
