# this will not give correct ans in all cases when val of array element < 1
# will give less number of count than the actual one

# this totaly same as subset sum just replaced False ->0 and True ->1
# but this will not work in case val of ele= 0  
class Solution:
    def NoOfSubsets(self, N, arr, sum):
        return self.helper(N, arr, sum)
    def helper(self, n, arr, sum):  # no need of this helper function
        if sum== 0:
            return 1
        if n== 0:  # means n== 0 and sum != 0
            return 0
        if arr[n-1] > sum:
            return self.helper(n-1,arr,sum)
        else:
            return self.helper(n-1,arr,sum- arr[n-1]) + self.helper(n-1,arr,sum)

# memoized the above method
class Solution:
    def NoOfSubsets(self, N, arr, sum): 
        dp= [[-1 for i in range(sum+1)] for i in range(N)]  # no need to go till 'N+1' as we are starting from  'N-1' 
        return self.helper(N-1, arr, sum, dp)
    
    def helper(self, ind, arr, sum, dp):
        if sum== 0:
            return True
        if ind== 0:
            return arr[0]== sum
        if dp[ind][sum] != -1: 
            return dp[ind][sum]
        if arr[ind]> sum:
            dp[ind][sum]= self.helper(ind -1, arr, sum, dp)
        else:   # arr[ind] <= sum
            dp[ind][sum]= self.helper(ind -1, arr, sum- arr[ind], dp) or self.helper(ind -1, arr, sum, dp)
        return dp[ind][sum]

# arr= [1,2,3,3]
# arr= [1,1,1,1]
# arr= [1,1,2,3]
# print(NoOfSubsets(4,arr,6))   
# print(NoOfSubsets(4,arr,4)) 

# Method 3 vvi: correct one that will work in all cases

# Note vvi:  to find all the ans just write the base case when you reach the last ele instead when sum==0.

# can also do by bottom up approach by initialising the dp matrix with these base condition

class Solution:
    def NoOfSubsets2(self, N, arr, sum):
        dp= [[-1 for i in range(sum+1)] for i in range(N +1)]   
        ans=  self.helper(N, arr, sum, dp)
        return ans
    
    def helper(self, n, arr, sum, dp):
        if n== 1:
            if sum== 0 and arr[0]== 0:  # either take the 1st ele or not both will be our ans
                return 2
            if sum==0 or sum== arr[0]: # in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1
            else:
                return 0
        if dp[n][sum]!= -1:
            return dp[n][sum]
        if arr[n-1]> sum:
            dp[n][sum]= self.helper(n-1,arr,sum, dp)
        else:
            dp[n][sum]= self.helper(n-1,arr,sum- arr[n-1], dp) + self.helper(n-1,arr,sum, dp)
        return dp[n][sum]

arr= [0, 0, 0, 1]
# arr= [0,0,1]
ob= Solution()
# print(ob.NoOfSubsets2(4,arr,1))
# print(ob.NoOfSubsets2(3,arr,1))



