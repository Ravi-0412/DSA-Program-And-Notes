# this will not give correct ans in all cases when val of array element < 1.
# will give less number of count than the actual one

# method 1: 
class Solution:
    def isSubsetSum(self, N, arr, sum): 
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


# correct one that will work in all cases
# can also do by bottom up approach by initialising the dp matrix with these base condition
class Solution:
    def NoOfSubsets1(self, N, arr, sum): 
        dp= [[-1 for i in range(sum+1)] for i in range(N)]  # no need to go till 'N+1' as we are starting from  'N-1' 
        return self.helper(N-1, arr, sum, dp)
    
    def helper(self, ind, arr, sum, dp):
        if ind== 0:
            if sum== 0 and arr[0]== 0:
                return 2
            if sum==0 or sum== arr[0]: # in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1
            else:
                return 0
        if dp[ind][sum] != -1: 
            return dp[ind][sum]
        if arr[ind]> sum:
            dp[ind][sum]= self.helper(ind -1, arr, sum, dp)
        else:   # arr[ind] <= sum
            dp[ind][sum]= self.helper(ind -1, arr, sum- arr[ind], dp) +  self.helper(ind -1, arr, sum, dp)
        return dp[ind][sum]

# arr= [1,2,3,3]
# arr= [0, 0, 0, 1]
# arr= [1,1,1,1]
# arr= [1,1,2,3]
# ob= Solution()
# print(ob.NoOfSubsets1(4,arr,6))   
# print(ob.NoOfSubsets1(4,arr,4))
# print(ob.NoOfSubsets1(4,arr,1))


# method 3: by aditya verma method and what i used to do also in GATE and while solving Q
# working in all cases
class Solution:
    def NoOfSubsets2(self, N, arr, sum):
        dp= [[-1 for i in range(sum+1)] for i in range(N +1)]   
        ans=  self.helper(N, arr, sum, dp)
        return ans
    
    def helper(self, n, arr, sum, dp):
        if n== 1:
            if sum== 0 and arr[0]== 0:
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

# arr= [0, 0, 0, 1]
arr= [0,0,1]
ob= Solution()
# print(ob.NoOfSubsets2(4,arr,1))
print(ob.NoOfSubsets2(3,arr,1))