# Method 1: 
# Recursion 
# Time : O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost  # ho handle the corner case for 1st move so that no need to call for index '0' and index '1' separately.
        n = len(cost)
        
        def solve(ind):
            if ind >= n:
                return 0
            return cost[ind] + min(solve(ind + 1) , solve(ind + 2))

        return solve(0)

# Java
"""
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] newCost = new int[cost.length + 1];
        newCost[0] = 0;  // to handle the corner case for 1st move so that no need to call for index '0' and index '1' separately.
        System.arraycopy(cost, 0, newCost, 1, cost.length);
        return solve(0, newCost);
    }

    private int solve(int ind, int[] cost) {
        int n = cost.length;
        if (ind >= n) {
            return 0;
        }
        return cost[ind] + Math.min(solve(ind + 1, cost), solve(ind + 2, cost));
    }
}
"""

# C++
"""
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        cost.insert(cost.begin(), 0);  // to handle the corner case for 1st move so that no need to call for index '0' and index '1' separately.
        return solve(0, cost);
    }

private:
    int solve(int ind, vector<int>& cost) {
        int n = cost.size();
        if (ind >= n) {
            return 0;
        }
        return cost[ind] + min(solve(ind + 1, cost), solve(ind + 2, cost));
    }
};
"""

# Method  2: 
# Memoization 
# Time = space = O(n)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        n = len(cost)
        dp = [-1] * n

        def solve(ind):
            if ind >= n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            dp[ind] = cost[ind] + min(solve(ind + 1), solve(ind + 2))
            return dp[ind]

        return solve(0)

# Java
"""
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] newCost = new int[cost.length + 1];
        newCost[0] = 0;
        System.arraycopy(cost, 0, newCost, 1, cost.length);
        int[] dp = new int[newCost.length];
        Arrays.fill(dp, -1);
        return solve(0, newCost, dp);
    }

    private int solve(int ind, int[] cost, int[] dp) {
        int n = cost.length;
        if (ind >= n) {
            return 0;
        }
        if (dp[ind] != -1) {
            return dp[ind];
        }
        dp[ind] = cost[ind] + Math.min(solve(ind + 1, cost, dp), solve(ind + 2, cost, dp));
        return dp[ind];
    }
}

"""

# C++
"""
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        cost.insert(cost.begin(), 0);
        int n = cost.size();
        vector<int> dp(n, -1);
        return solve(0, cost, dp);
    }

private:
    int solve(int ind, vector<int>& cost, vector<int>& dp) {
        int n = cost.size();
        if (ind >= n) {
            return 0;
        }
        if (dp[ind] != -1) {
            return dp[ind];
        }
        dp[ind] = cost[ind] + min(solve(ind + 1, cost, dp), solve(ind + 2, cost, dp));
        return dp[ind];
    }
};
"""


# Method  3:
# Tabulation

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        n = len(cost)
        dp = [0] * (n + 1)

        # Base cases
        dp[n] = 0  # Cost beyond the last step is 0
        dp[n - 1] = cost[n - 1]

        for ind in range(n - 2, -1, -1):
            dp[ind] = cost[ind] + min(dp[ind + 1], dp[ind + 2])

        return dp[0]

# Java
"""
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int[] newCost = new int[cost.length + 1];
        newCost[0] = 0;
        System.arraycopy(cost, 0, newCost, 1, cost.length);
        int n = newCost.length;
        int[] dp = new int[n + 1];

        // Base cases
        dp[n] = 0;  // Cost beyond the last step is 0
        dp[n - 1] = newCost[n - 1];

        for (int ind = n - 2; ind >= 0; ind--) {
            dp[ind] = newCost[ind] + Math.min(dp[ind + 1], dp[ind + 2]);
        }

        return dp[0];
    }
}
"""

# C++
"""
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        cost.insert(cost.begin(), 0);
        int n = cost.size();
        vector<int> dp(n + 1, 0);

        // Base cases
        dp[n] = 0;  // Cost beyond the last step is 0
        dp[n - 1] = cost[n - 1];

        for (int ind = n - 2; ind >= 0; ind--) {
            dp[ind] = cost[ind] + min(dp[ind + 1], dp[ind + 2]);
        }

        return dp[0];
    }
};
"""

# Extension: 

# Note: How above method will take care of not_take case i.e skip case?
# Ans: When we are at index 'i' and if we include ans of 'i+2' (called 'i + 2') then we have skipped 'i+1'.

# If say you can jump upto 'k' then we have to take minimum of next 'k' index after adding the cost of cur_index.




# Related Q: 
# 1) 2944. Minimum Number of Coins for Fruits
