# logic: for n<= 1= 1 only.
# for n>= 2, it is sum of cartesian product of catalan number from '0' to 'n-1' when each number from '0' to 'n-1' is chosen on eby one.
# see the progtam for more clarity.

# (catalan for 1st 'i'th number) * (catalan for 1st 'n-i-1' number), when we choose 'i' from '0' to 'n-1'.
# subproblem is getting generated like this.


# method 1: 
# recursive way
class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        if n<= 1:
            return 1
        ans= 0
        for i in range(n):
            ans+= self.findCatalan(i) * self.findCatalan(n-i -1)   # (catalan for 1st 'i'th number) * (catalan for 1st 'n-i-1' number)
        return ans

# using DP 
class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        dp= [0]*(n+1)
        dp[0]= dp[1]= 1
        
        for j in range(2, n +1):   # start after base case
            ans= 0
            for i in range(j):    # we have to consider number before 'j' only.
                ans+= dp[i]* dp[j-i-1] 
            dp[j]= ans
        return dp[n]

# if you start 2nd loop from n=1 instead of '0' then we have to change code like this.
class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        dp= [0]*(n+1)
        dp[0]= dp[1]= 1
        
        for j in range(2, n +1):
            ans= 0
            for i in range(1, j+1):
                ans+= dp[i-1]* dp[j-i] 
            dp[j]= ans
        return dp[n]


# my mistake : i was not taking sum 
class Solution:
    #Function to find the nth catalan number.
    def findCatalan(self,n):
        if n<= 1:
            return 1
        for i in range(n):
            return self.findCatalan(i) * self.findCatalan(n-i -1)