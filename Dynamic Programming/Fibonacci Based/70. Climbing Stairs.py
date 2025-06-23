# method 1: recursion

# time: same as finonacci , time space everything
# when you reach the base just return the value as it will be one of the possible ways.

# Pattern: in this type of Q(Fibonacci based), just make sure that function didn't call for negative number.
# i.e write the base condition such that it doesn't reach till negative number and at last return all the function call
# or write the minimal base case and before calling the function & check if it will not lead to call fn with negative number.

# problem with this pattern have difference in base case only according to the Q , other things wil be similar

# logic: 
"""
we have total n stairs, and we start our recursion call from nth stair.
For every stair for a point of time we have 2 options: jump one step or jump two steps and we try or explore all these options for each stair and calculate the total ways
For that we need to return sum of all choices we made.

Now for base case we can think that for every index, we have 2 options either jump one step or jump two steps
and as we are starting from nth stair to 0th stair for our recursion journey, so when we reach at stair 0 we return 1 as 
we find a way.
Also we need to add one more case that at n = 1 stair as we cannot have recursion call func(n-2) at n = 1, that would be an invalid case and we simply return 1 
as there is only one way to come Oth stair from n=1 stair.

so, if(n == 0) or if (n==1) we are returning 1 
we can write this as if(n <= 1) return 1;
"""

"""
# TC - O(2^n)
# SC - The maximum recursion depth is n, so the call stack space is O(n) 
"""


# or you can write like this. Better one
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1: # after reaching here only we can say that steps that we had taken will lead to destination. so it is one of the ways
            return 1  # only difference from fibonacci.. if n== 0 also then it means you have taken one step then only you have reached '0'. so return 1 instead of 'n'
        return self.climbStairs(n-1) + self.climbStairs(n-2)

#CPP
"""
class Solution {
public:
    int climbStairs(int n) {
        // after reaching here only we can say that steps that we had taken will lead to destination. so it is one of the ways
        if (n <= 1)
            return 1;  // only difference from fibonacci.. if n== 0 also then it means you have taken one step then only you have reached '0'. so return 1 instead of 'n'

        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};
"""

#JAVA
"""
public class Solution {
    public int climbStairs(int n) {
        // after reaching here only we can say that steps that we had taken will lead to destination. so it is one of the ways
        if (n <= 1)
            return 1;  // only difference from fibonacci.. if n== 0 also then it means you have taken one step then only you have reached '0'. so return 1 instead of 'n'

        return climbStairs(n - 1) + climbStairs(n - 2);
    }
}

"""

# method2: 
# memoization(Top Down)
# TC: O(n)
# SC: O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        dp= [-1]*(n+1)
        return self.helper(n,dp)
    
    def helper(self,n,dp):
        if n<=1:   
            return 1   
        if dp[n]!= -1:   
            return dp[n]
        dp[n]= self.helper(n-1,dp) + self.helper(n-2,dp)  
        return dp[n]   

#CPP
"""
class Solution {
public:
    int climbStairs(int n) {
        std::vector<int> dp(n + 1, -1);
        return helper(n, dp);
    }

private:
    int helper(int n, std::vector<int>& dp) {
        if (n <= 1)
            return 1;
        if (dp[n] != -1)
            return dp[n];
        dp[n] = helper(n - 1, dp) + helper(n - 2, dp);
        return dp[n];
    }
};

"""

#JAVA
"""
public class Solution {
    public int climbStairs(int n) {
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = -1;
        return helper(n, dp);
    }

    private int helper(int n, int[] dp) {
        if (n <= 1)
            return 1;
        if (dp[n] != -1)
            return dp[n];
        dp[n] = helper(n - 1, dp) + helper(n - 2, dp);
        return dp[n];
    }
}
"""

# method3 : Tabulation(Bottom-up)
# TC - O(n)
# SC - O(n)

#python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

#cpp
"""
class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) return 1;
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; ++i) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
};

"""

#JAVA
"""
class Solution {
    public int climbStairs(int n) {
        if (n <= 1) return 1;
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}

"""