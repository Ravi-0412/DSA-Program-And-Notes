# Basic:

# this will not give correct ans in all cases when val of array element < 1
# will give less number of count than the actual one

# this totaly same as subset sum just replaced False -> 0 and True ->1
# but this will not work in case val of ele = 0  
class Solution:
    def perfectSum(self, arr, sum):
        N = len(arr)
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

# Java Code 
"""
public class Solution {
    public int NoOfSubsets(int N, int[] arr, int sum) {
        return helper(N, arr, sum);
    }

    // no need of this helper function
    private int helper(int n, int[] arr, int sum) {
        if (sum == 0)
            return 1;
        if (n == 0)  // means n== 0 and sum != 0
            return 0;
        if (arr[n - 1] > sum)
            return helper(n - 1, arr, sum);
        else
            return helper(n - 1, arr, sum - arr[n - 1]) + helper(n - 1, arr, sum);
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int NoOfSubsets(int N, std::vector<int>& arr, int sum) {
        return helper(N, arr, sum);
    }

private:
    // no need of this helper function
    int helper(int n, const std::vector<int>& arr, int sum) {
        if (sum == 0)
            return 1;
        if (n == 0)  // means n== 0 and sum != 0
            return 0;
        if (arr[n - 1] > sum)
            return helper(n - 1, arr, sum);
        else
            return helper(n - 1, arr, sum - arr[n - 1]) + helper(n - 1, arr, sum);
    }
};
"""

# Method 1: 
# Recursion
# correct one that will work in all cases

# Note vvi:  to find all the ans just write the base case when you reach the last ele instead when sum == 0.

class Solution:
    def perfectSum(self, arr, target):
        return self.helper(len(arr), arr, target)

    def helper(self, n, arr, target):
        if n == 1:
            if target == 0 and arr[0] == 0:
                return 2  # include or exclude 0
            if target == 0 or target == arr[0]:
                return 1
            return 0

        take = 0
        if arr[n - 1] <= target:
            take = self.helper(n - 1, arr, target - arr[n - 1])
        notTake = self.helper(n - 1, arr, target)

        return take + notTake

# Java Code 
"""
class Solution {
    public int perfectSum(int[] arr, int target) {
        return helper(arr.length, arr, target);
    }

    public int helper(int n, int[] arr, int target) {
        if (n == 1) {
            if (target == 0 && arr[0] == 0)
                return 2;  // include or exclude 0
            if (target == 0 || target == arr[0])
                return 1;
            return 0;
        }

        int take = 0;
        if (arr[n - 1] <= target)
            take = helper(n - 1, arr, target - arr[n - 1]);
        int notTake = helper(n - 1, arr, target);

        return take + notTake;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int perfectSum(vector<int>& arr, int target) {
        return helper(arr.size(), arr, target);
    }

    int helper(int n, const vector<int>& arr, int target) {
        if (n == 1) {
            if (target == 0 && arr[0] == 0)
                return 2;  // include or exclude 0
            if (target == 0 || target == arr[0])
                return 1;
            return 0;
        }

        int take = 0;
        if (arr[n - 1] <= target)
            take = helper(n - 1, arr, target - arr[n - 1]);
        int notTake = helper(n - 1, arr, target);

        return take + notTake;
    }
};
"""


# Method 2:
# Memoisation
    
class Solution:
    def perfectSum(self, arr, target):
        N = len(arr)
        dp = [[-1 for _ in range(target + 1)] for _ in range(N + 1)]
        return self.helper(N, arr, target, dp)
    
    def helper(self, n, arr, target, dp):
        if n == 1:
            if target == 0 and arr[0] == 0:   # either take the 1st ele or not both will be our ans
                return 2  # include or exclude 0
            if target == 0 or target == arr[0]:  # in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1
            return 0
        
        if dp[n][target] != -1:
            return dp[n][target]

        take = 0
        if arr[n - 1] <= target:
            take = self.helper(n - 1, arr, target - arr[n - 1], dp)
        notTake = self.helper(n - 1, arr, target, dp)

        dp[n][target] = take + notTake
        return dp[n][target]
# Java Code 
"""
public class Solution {
    public int NoOfSubsets2(int N, int[] arr, int sum) {
        int[][] dp = new int[N + 1][sum + 1];
        for (int i = 0; i <= N; i++)
            java.util.Arrays.fill(dp[i], -1);
        return helper(N, arr, sum, dp);
    }

    private int helper(int n, int[] arr, int sum, int[][] dp) {
        if (n == 1) {
            if (sum == 0 && arr[0] == 0)  // either take the 1st ele or not both will be our ans
                return 2;
            if (sum == 0 || sum == arr[0])  // in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1;
            else
                return 0;
        }
        if (dp[n][sum] != -1)
            return dp[n][sum];

        if (arr[n - 1] > sum)
            dp[n][sum] = helper(n - 1, arr, sum, dp);
        else
            dp[n][sum] = helper(n - 1, arr, sum - arr[n - 1], dp) + helper(n - 1, arr, sum, dp);

        return dp[n][sum];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int NoOfSubsets2(int N, std::vector<int>& arr, int sum) {
        std::vector<std::vector<int>> dp(N + 1, std::vector<int>(sum + 1, -1));
        return helper(N, arr, sum, dp);
    }

private:
    int helper(int n, const std::vector<int>& arr, int sum, std::vector<std::vector<int>>& dp) {
        if (n == 1) {
            if (sum == 0 && arr[0] == 0)  // either take the 1st ele or not both will be our ans
                return 2;
            if (sum == 0 || sum == arr[0])  // in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1;
            else
                return 0;
        }

        if (dp[n][sum] != -1)
            return dp[n][sum];

        if (arr[n - 1] > sum)
            dp[n][sum] = helper(n - 1, arr, sum, dp);
        else
            dp[n][sum] = helper(n - 1, arr, sum - arr[n - 1], dp) + helper(n - 1, arr, sum, dp);

        return dp[n][sum];
    }
};
"""


# Method 3:
# Tabulation

class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        # Base case initialization
        # For any i, sum = 0 → count = 1 (empty subset)
        for i in range(n + 1):
            dp[i][0] = 1
        
        # Handle first element separately
        if arr[0] == 0:
            dp[1][0] = 2  # empty subset + subset with zero
        elif arr[0] <= target:
            dp[1][arr[0]] = 1
        
        # Fill the dp table
        for i in range(2, n + 1):
            for t in range(target + 1):
                take = 0
                if arr[i - 1] <= t:
                    take = dp[i - 1][t - arr[i - 1]]
                notTake = dp[i - 1][t]
                dp[i][t] = take + notTake
        
        return dp[n][target]

# Java Code 
"""
class Solution {
    public int perfectSum(int[] arr, int target) {
        int n = arr.length;
        int[][] dp = new int[n + 1][target + 1];

        // Base case initialization
        // For any i, sum = 0 → count = 1 (empty subset)
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }

        // Handle first element separately
        if (arr[0] == 0) {
            dp[1][0] = 2;  // empty subset + subset with zero
        } else if (arr[0] <= target) {
            dp[1][arr[0]] = 1;
        }

        // Fill the dp table
        for (int i = 2; i <= n; i++) {
            for (int t = 0; t <= target; t++) {
                int take = 0;
                if (arr[i - 1] <= t) {
                    take = dp[i - 1][t - arr[i - 1]];
                }
                int notTake = dp[i - 1][t];
                dp[i][t] = take + notTake;
            }
        }

        return dp[n][target];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int perfectSum(vector<int>& arr, int target) {
        int n = arr.size();
        vector<vector<int>> dp(n + 1, vector<int>(target + 1, 0));

        // Base case initialization
        // For any i, sum = 0 → count = 1 (empty subset)
        for (int i = 0; i <= n; i++) {
            dp[i][0] = 1;
        }

        // Handle first element separately
        if (arr[0] == 0) {
            dp[1][0] = 2;  // empty subset + subset with zero
        } else if (arr[0] <= target) {
            dp[1][arr[0]] = 1;
        }

        // Fill the dp table
        for (int i = 2; i <= n; i++) {
            for (int t = 0; t <= target; t++) {
                int take = 0;
                if (arr[i - 1] <= t) {
                    take = dp[i - 1][t - arr[i - 1]];
                }
                int notTake = dp[i - 1][t];
                dp[i][t] = take + notTake;
            }
        }

        return dp[n][target];
    }
};

"""