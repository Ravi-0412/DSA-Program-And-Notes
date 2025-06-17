# method1: 
# Recursive way
# just same logic as 'frog jump' only difference in base case
# just reverse th Q, you are starting robing from house no 'n'

# logic: At every home you have two option either rob the current house or don't rob.
# if we rob then move to two house ahead(non-adj) else move to just next house.

# vvi:one good way to think: 
# just you have to "find subsequences such that no element are  adjacent and whose sum is maximum".
# using the technique of included and not included.

# time: O(2^n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(len(nums),nums)
    
    # will give the max profit when 'n' houses are left to rob from start.
    def helper(self,n,nums):
        if n<=0:   # means no house left to rob
            return 0
        maxProfit= max(nums[n-1]+ self.helper(n-2,nums), self.helper(n-1,nums))  # when you rob the current house or when you don't rob.
        return maxProfit
    
# Java 
"""
class Solution {
    public int rob(int[] nums) {
        return helper(nums.length, nums);
    }

    // will give the max profit when 'n' houses are left to rob from start.
    private int helper(int n, int[] nums) {
        if (n <= 0) {  // means no house left to rob
            return 0;
        }
        int maxProfit = Math.max(nums[n - 1] + helper(n - 2, nums), helper(n - 1, nums));  // when you rob the current house or when you don't rob.
        return maxProfit;
    }
}
"""

# C++
"""
class Solution {
public:
    int rob(vector<int>& nums) {
        return helper(nums.size(), nums);
    }

    // will give the max profit when 'n' houses are left to rob from start.
    int helper(int n, vector<int>& nums) {
        if (n <= 0) {  // means no house left to rob
            return 0;
        }
        int maxProfit = max(nums[n - 1] + helper(n - 2, nums), helper(n - 1, nums));  // when you rob the current house or when you don't rob.
        return maxProfit;
    }
};
"""

# method 2: 
# memoization
# time = space =  0(n) 
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp= [-1]*(len(nums) + 1)
        return self.helper(len(nums),nums,dp)
    
    def helper(self,n,nums,dp):
        if n<=0:
            return 0
        if dp[n]!= -1:
            return dp[n]
        dp[n]= max(nums[n-1]+ self.helper(n-2,nums,dp), self.helper(n-1,nums,dp))
        return dp[n]

# Java
"""
class Solution {
    public int rob(int[] nums) {
        int[] dp = new int[nums.length + 1];
        Arrays.fill(dp, -1);
        return helper(nums.length, nums, dp);
    }

    private int helper(int n, int[] nums, int[] dp) {
        if (n <= 0) {
            return 0;
        }
        if (dp[n] != -1) {
            return dp[n];
        }
        dp[n] = Math.max(nums[n - 1] + helper(n - 2, nums, dp), helper(n - 1, nums, dp));
        return dp[n];
    }
}
"""

# C++
"""
class Solution {
public:
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size() + 1, -1);
        return helper(nums.size(), nums, dp);
    }

    int helper(int n, vector<int>& nums, vector<int>& dp) {
        if (n <= 0) {
            return 0;
        }
        if (dp[n] != -1) {
            return dp[n];
        }
        dp[n] = max(nums[n - 1] + helper(n - 2, nums, dp), helper(n - 1, nums, dp));
        return dp[n];
    }
};
"""

# Method 3:
# Tabulation: 
#time : o(n), space : o(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp= [0]*(n +1)   
        dp[1]= nums[0]   # if we start from '1'then we will need dp[-1] which will give error.
        for i in range(2,n+1):
            dp[i]= max(nums[i-1]+ dp[i-2], dp[i-1])   # when you rob the current house or when you rob the next house
        return dp[n]


# Java
"""
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 1];
        dp[1] = nums[0];  // if we start from '1' then we will need dp[-1] which will give error.

        for (int i = 2; i <= n; i++) {
            dp[i] = Math.max(nums[i - 1] + dp[i - 2], dp[i - 1]);  // when you rob the current house or when you rob the next house
        }

        return dp[n];
    }
}
"""


# C++ 
"""
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 1];
        dp[1] = nums[0];  // if we start from '1' then we will need dp[-1] which will give error.

        for (int i = 2; i <= n; i++) {
            dp[i] = Math.max(nums[i - 1] + dp[i - 2], dp[i - 1]);  // when you rob the current house or when you rob the next house
        }

        return dp[n];
    }
}
"""


# Method 4:
# optimising space complexity
# time:= O(n), space: O(1)

# logic to optimise space to O(1) from O(n) or to O(n) from O(n^2).

# Replace:  dp[i-2]= non_adj, dp[i-1]= adj
# non_adj= 0  # will tell the max_profit till pre non-adj house. Same meaniing as dp[i-2]
# adj= nums[0]  # will tell the profit till pre adj_house. Same meaning as dp[i-1].
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n + 1];
        dp[1] = nums[0];  // if we start from '1' then we will need dp[-1] which will give error.

        for (int i = 2; i <= n; i++) {
            dp[i] = Math.max(nums[i - 1] + dp[i - 2], dp[i - 1]);  // when you rob the current house or when you rob the next house
        }

        return dp[n];
    }
}


# Java
"""
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int nonAdj = 0;     // initially it will be zero.
        int adj = nums[0];  // initially it will be nums[0].
        int ans = nums[0];  // in case only one ele is present and also this will be the minimum profit

        for (int i = 2; i <= n; i++) {
            ans = Math.max(ans, nums[i - 1] + nonAdj);  // when you rob the current house
            ans = Math.max(ans, adj);  // or when you rob the next house
            int temp = adj;
            adj = ans;
            nonAdj = temp;  // update adj and non_adj.
        }

        return ans;
    }
}
"""

# C++
"""
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        int nonAdj = 0;     // initially it will be zero.
        int adj = nums[0];  // initially it will be nums[0].
        int ans = nums[0];  // in case only one ele is present and also this will be the minimum profit

        for (int i = 2; i <= n; i++) {
            ans = max(ans, nums[i - 1] + nonAdj);  // when you rob the current house
            ans = max(ans, adj);  // or when you rob the next house
            int temp = adj;
            adj = ans;
            nonAdj = temp;  // update adj and non_adj.
        }

        return ans;
    }
};
"""

