# method 1: Recursion
class Solution:
    def isSubsetSum (self, N, arr, sum):
        return self.helper(N, arr, sum)
    def helper(self, n, arr, sum):
        if sum== 0:
            return True
        if n== 0:  # means n== 0 and sum != 0
            return False
        if arr[n-1]> sum:
            return self.helper(n-1,arr,sum)
        else:
            return self.helper(n-1,arr,sum- arr[n-1]) or self.helper(n-1,arr,sum)


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

# method 4: optimising space complexity to O(n)

# another way(from here striver's video)
# method 1: By recursion, time: O(2^n), space= O(n)
class Solution:
    def isSubsetSum(self, N, arr, target):
        return self.helper(N-1, arr, target)  # means considering the ele till index 'n-1' is there sum possible = target
    
    def helper(self, ind, arr, sum):  # ind means index
        ans= False
        if sum== 0:  # we got the required target so return True
            return True
        if ind== 0:  # means we are considering the 1st ele(ele at index zero) 
                    # so it will be True if the value of 1st ele(ele at index zero) will be equal to the remaining sum otherwise will be False
            return arr[0]== sum
        # we have two choices for each ele either we can take that in our ans or we can't take
        # case 1: if we not take
        if arr[ind]> sum:
            temp= self.helper(ind -1, arr, sum)
            ans= ans or temp
        # case 2: if we  take
        else:   # arr[ind] <= sum
            temp= self.helper(ind -1, arr, sum- arr[ind]) or self.helper(ind -1, arr, sum)
            ans= ans or temp
        return ans

# method 2: by memoization
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


# method 3: Bottom up approach

class Solution:
    def isSubsetSum(self, N, arr, sum): 
        dp= [[0 for i in range(sum+1)] for i in range(N)]  # no need to go till 'N+1' as we are starting from  'N-1'
        # just convert the base cases into initialisation 
        for i in range(N):
            dp[i][0]= True
        dp[0][arr[0]]= True
        # we have two choices for each ele either we can take that in our ans or we can't take
        for ind in range(1, N):
            for target in range(1, sum +1):
            # case 1: if we not take
                if arr[ind]> target:
                    dp[ind][target]= dp[ind -1][target]
                # case 2: if we  take
                else:   # arr[ind] <= sum
                    dp[ind][target]= dp[ind - 1][target- arr[ind]] or dp[ind - 1][target]
        return dp[N -1][sum]  # return the last ele of dp



# for optimizing space complexity watch striver dp series from start and then try again