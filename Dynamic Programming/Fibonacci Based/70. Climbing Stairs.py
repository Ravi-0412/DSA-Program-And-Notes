# method 1: recursion
# time: same as finonacci , time space everything
# when you reach the base just return the value as it will be one of the possible ways.

# Pattern: in this type of Q(Fibonacci based), just make sure that function didn't call for negative number.
# i.e write the base condition such that it doesn't reach till negative number and at last return all the function call
# or write the minimal base case and before calling the function & check if it will not lead to call fn with negative number.

# problem with this pattern have difference in base case only according to the Q , other things wil be similar

# logic: at every stair you have two options either take one step or take two step
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:  # for n= 1, 1 choice. for n= 2 two choice(1->1 or 2)
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)  # ways(n)= ways(n-1) + ways(n-2)

# or you can write like this. Better one
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1: # after reaching here only we can say that steps that we had taken will lead to destination. so it is one of the ways
            return 1  # only difference from fibonacci.. if n== 0 also then it means you have taken one step then only you have reached '0'. so return 1 instead of 'n'
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# method2: memoization(Top Down)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp= [-1]*(n+1)
        return self.helper(n,dp)
    
    def helper(self,n,dp):
        if n<=1:   # for base case value= -1 only since we are not updating in that but we will get correct ans
            return 1   
        if dp[n]!= -1:   
            return dp[n]
        dp[n]= self.helper(n-1,dp) + self.helper(n-2,dp)  
        return dp[n]   