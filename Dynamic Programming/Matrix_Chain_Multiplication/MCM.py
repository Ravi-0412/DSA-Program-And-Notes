# Recursive approach 
# correct only but giving TLE
def matrixMultiplication(self, N, arr):
        i,j= 1, N-1
        mn= 99999999 # any larger value to compare and store the minimum result
        return self.MCM(arr,i,j,mn)
def MCM(self,arr,start,end,mn):
    if start>= end:
        return 0
    for k in range(start,end):
        tempAns= self.MCM(arr,start,k,mn) + self.MCM(arr,k+1,end,mn) + arr[start-1]*arr[k]*arr[end]
        mn= min(mn,tempAns)
    return mn


# Bottom up :Memoization approach
def matrixMultiplication(self, N, arr):
        i,j= 1, N-1
        dp= [[-1 for j in range(N)] for i in range(N)]
        mn= 99999999999   # any very large  # will store the minimum ans
        return self.MCM(arr,i,j,dp,mn)
    def MCM(self,arr,start,end,ans,mn):
        if start>= end:
            return 0
        if ans[start][end]!= -1:
            return ans[start][end]
        for k in range(start,end):
            tempAns= self.MCM(arr,start,k,ans,mn) + self.MCM(arr,k+1,end,ans,mn) + arr[start-1]*arr[k]*arr[end]
            mn= min(mn,tempAns)
            ans[start][end]= mn
        return mn