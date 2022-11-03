# method1: Recursive way
# just same logic as 'frog jump' only difference in base case
# just reverse th Q, you are starting robing from house no 'n'

# logic: At every home you have two option either rob the current house or rob the next house
# time: O(2^n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(len(nums),nums)
    
    def helper(self,n,nums):
        if n<=0:  # this you will reach after you have robbed the house no 3(2nd call) or house no 2(1st and 2nd call) so after that there will be no house to rob
            return 0
        if n==1:  # if you have left with only 1st house to rob
            return nums[0]
        maxProfit= max(nums[n-1]+ self.helper(n-2,nums), nums[n-2] + self.helper(n-3,nums))  # when you rob the current house or when you rob the next house
        return maxProfit

# method 2: memoization: Top Down
# time: 0(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp= [-1]*(len(nums))
        return self.helper(len(nums),nums,dp)
    
    def helper(self,n,nums,dp):
        if n<=0:  # this you will reach after you have robbed the house no 3(2nd call) or house no 2(1st and 2nd call) so after that there will be no house to rob
            return 0
        if n==1:  # if you have left with only 1st house to rob
            return nums[0]
        if dp[n-1]!= -1:
            return dp[n-1]
        dp[n-1]= max(nums[n-1]+ self.helper(n-2,nums,dp), nums[n-2] + self.helper(n-3,nums,dp))  # when you are at the nth house after robbing the pre non-adjacent house 
                                                                                            # you can start robing from nth house or (n-1)th house
        return dp[n-1]


# Tabulation: Bottom Up
class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp= [0]*(n+1)
        dp[1]= nums[0]
        for i in range(2,n+1):
            dp[i]= max(nums[i-1]+ dp[i-2], dp[i-1])   # when you rob the current house or when you rob the next house
        return dp[n]


# one good way to think: 
# just you have to find subsequences such that no ele are  adjacent and whose sum is maximum
# using the technique of included and not included
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(len(nums)-1,nums)  # robbing from '0'th house to 'n-1'th house
    
    def helper(self,ind,nums):
        if ind<0: # no house left to rob
            return 0
        if ind==0:  # if you have left with only 1st house to rob
            return nums[0]
        # either you rob the curr house or not rob the curr house
        maxProfit= max(nums[ind]+ self.helper(ind-2,nums), self.helper(ind-1,nums)) 
        return maxProfit


# Tabulation
# time= space= O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp= [0]*n
        dp[0]= nums[0]
        for i in range(1,n):
            # when you include curr ele in profit
            take= nums[i]
            if i>=2:  # to avoid negative index
                take+= dp[i-2]
            notTake= dp[i-1]
            dp[i]= max(take, notTake)
        return dp[n-1]


# optimising space complexity
# time:= O(n), space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        non_adj= 0  # intially it will be zero
        adj= nums[0]  # initially it will be nums[0]
        ans= nums[0]  # in case only one ele is present and also this will be the minimum profit
        for i in range(1,n):
            # when you include curr ele in profit
            take= nums[i]
            if i>=2:  # if you take that ele then add the non_adj
                take+= non_adj
            notTake= adj  # if not take then equate to adj ele
            ans= max(take, notTake)
            adj, non_adj= ans, adj  # curr ele will become 'adj' and adj will become 'non_adj' for next coming ele
        return ans

