# Method 1:
# Recursion
# Do by this methd only for this type of question

# We always has one choice to notTake and we can only take current ele if 'arr[i] <= sum'

class Solution:
    def isSubsetSum (self, N, arr, sum):
        return self.helper(N, arr, sum)
    def helper(self, n, arr, sum):
        if sum== 0:
            return True
        if n== 0:  # means n== 0 and sum != 0
            return False
        take = False
        if arr[n-1] <= sum:
            take = self.helper(n-1,arr,sum - arr[n -1])
        notTake = self.helper(n-1,arr,sum)
        return take or notTake

# Java Code
"""
public class Solution {
    public boolean isSubsetSum(int N, int[] arr, int sum) {
        return helper(N, arr, sum);
    }

    private boolean helper(int n, int[] arr, int sum) {
        if (sum == 0)
            return true;
        if (n == 0)  // means n== 0 and sum != 0
            return false;

        boolean take = false;
        if (arr[n - 1] <= sum)
            take = helper(n - 1, arr, sum - arr[n - 1]);

        boolean notTake = helper(n - 1, arr, sum);
        return take || notTake;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    bool isSubsetSum(int N, std::vector<int>& arr, int sum) {
        return helper(N, arr, sum);
    }

private:
    bool helper(int n, const std::vector<int>& arr, int sum) {
        if (sum == 0)
            return true;
        if (n == 0)  // means n== 0 and sum != 0
            return false;

        bool take = false;
        if (arr[n - 1] <= sum)
            take = helper(n - 1, arr, sum - arr[n - 1]);

        bool notTake = helper(n - 1, arr, sum);
        return take || notTake;
    }
};
"""

# method 2: 
# memoized method:

class Solution:
    def isSubsetSum(self, arr, sum):
        dp = [[-1] * (sum + 1) for _ in range(N + 1)]
        return self.helper(N, arr, sum, dp)

    def helper(self, n, arr, sum, dp):
        if sum == 0:
            return True
        if n == 0:
            return False
        if dp[n][sum] != -1:
            return dp[n][sum]
        
        take = False
        if arr[n - 1] <= sum:
            take = self.helper(n - 1, arr, sum - arr[n - 1], dp)
        notTake = self.helper(n - 1, arr, sum, dp)
        dp[n][sum] = take or notTake
        return dp[n][sum]

# Java Code
"""
public class Solution {
    public boolean isSubsetSum(int N, int[] arr, int sum) {
        int[][] dp = new int[N + 1][sum + 1];
        for (int[] row : dp)
            java.util.Arrays.fill(row, -1);
        return helper(N, arr, sum, dp);
    }

    private boolean helper(int n, int[] arr, int sum, int[][] dp) {
        if (sum == 0)
            return true;
        if (n == 0)  // means n== 0 and sum != 0
            return false;
        if (dp[n][sum] != -1)
            return dp[n][sum] == 1;

        if (arr[n - 1] > sum)
            dp[n][sum] = helper(n - 1, arr, sum, dp) ? 1 : 0;
        else
            dp[n][sum] = (helper(n - 1, arr, sum - arr[n - 1], dp) || helper(n - 1, arr, sum, dp)) ? 1 : 0;

        return dp[n][sum] == 1;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    bool isSubsetSum(int N, std::vector<int>& arr, int sum) {
        std::vector<std::vector<int>> dp(N + 1, std::vector<int>(sum + 1, -1));
        return helper(N, arr, sum, dp);
    }

private:
    bool helper(int n, const std::vector<int>& arr, int sum, std::vector<std::vector<int>>& dp) {
        if (sum == 0)
            return true;
        if (n == 0)  // means n== 0 and sum != 0
            return false;
        if (dp[n][sum] != -1)
            return dp[n][sum] == 1;

        if (arr[n - 1] > sum)
            dp[n][sum] = helper(n - 1, arr, sum, dp) ? 1 : 0;
        else
            dp[n][sum] = (helper(n - 1, arr, sum - arr[n - 1], dp) || helper(n - 1, arr, sum, dp)) ? 1 : 0;

        return dp[n][sum] == 1;
    }
};
"""

# method 3: 
# By Bottom up  Approach
class Solution:
    def isSubsetSum(self, N, arr, sum):
        # Create dp table of size (N+1) x (sum+1)
        dp = [[False] * (sum + 1) for _ in range(N + 1)]

        # Base Case: sum == 0 → True (any n)
        for n in range(N + 1):
            dp[n][0] = True

        # Fill the dp table using bottom-up approach
        for n in range(1, N + 1):
            for s in range(1, sum + 1):
                take = False
                if arr[n - 1] <= s:
                    take = dp[n - 1][s - arr[n - 1]]
                notTake = dp[n - 1][s]
                dp[n][s] = take or notTake
        return dp[N][sum]

# Java Code 
"""
class Solution {
    public boolean isSubsetSum(int N, int[] arr, int sum) {
        // Create dp table of size (N+1) x (sum+1)
        boolean[][] dp = new boolean[N + 1][sum + 1];

        // Base Case: sum == 0 → True (any n)
        for (int n = 0; n <= N; n++) {
            dp[n][0] = true;
        }

        // Fill the dp table using bottom-up approach
        for (int n = 1; n <= N; n++) {
            for (int s = 1; s <= sum; s++) {
                boolean take = false;
                if (arr[n - 1] <= s) {
                    take = dp[n - 1][s - arr[n - 1]];
                }
                boolean notTake = dp[n - 1][s];
                dp[n][s] = take || notTake;
            }
        }

        return dp[N][sum];
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    bool isSubsetSum(int N, vector<int>& arr, int sum) {
        // Create dp table of size (N+1) x (sum+1)
        vector<vector<bool>> dp(N + 1, vector<bool>(sum + 1, false));

        // Base Case: sum == 0 → True (any n)
        for (int n = 0; n <= N; n++) {
            dp[n][0] = true;
        }

        // Fill the dp table using bottom-up approach
        for (int n = 1; n <= N; n++) {
            for (int s = 1; s <= sum; s++) {
                bool take = false;
                if (arr[n - 1] <= s) {
                    take = dp[n - 1][s - arr[n - 1]];
                }
                bool notTake = dp[n - 1][s];
                dp[n][s] = take || notTake;
            }
        }

        return dp[N][sum];
    }
};
"""

# Method 4:  
# optimising space complexity to O(n)
class Solution:
    def isSubsetSum (self, N, arr, sum):
        pre = [0] * (sum + 1)
        pre[0] = 1   # just dp[0][0] = 1
        # now just same as 0/1 Knapsack           
        for i in range(1,N+1):
            cur = [0] * (sum + 1)
            cur[0] = 1   # value of dp[i][0]
            for j in range(1,sum+1):
                if arr[i-1] > j:
                    cur[j]= pre[j]
                else:
                    cur[j]= pre[j-arr[i-1]] or pre[j]
            pre = cur.copy()
        return pre[sum] 

# Java Code
"""
public class Solution {
    public boolean isSubsetSum(int N, int[] arr, int sum) {
        int[] pre = new int[sum + 1];
        pre[0] = 1;   // just dp[0][0] = 1

        // now just same as 0/1 Knapsack
        for (int i = 1; i <= N; i++) {
            int[] cur = new int[sum + 1];
            cur[0] = 1;   // value of dp[i][0]

            for (int j = 1; j <= sum; j++) {
                if (arr[i - 1] > j) {
                    cur[j] = pre[j];
                } else {
                    cur[j] = (pre[j - arr[i - 1]] == 1 || pre[j] == 1) ? 1 : 0;
                }
            }
            pre = cur;
        }

        return pre[sum] == 1;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    bool isSubsetSum(int N, std::vector<int>& arr, int sum) {
        std::vector<int> pre(sum + 1, 0);
        pre[0] = 1;  // just dp[0][0] = 1

        // now just same as 0/1 Knapsack
        for (int i = 1; i <= N; ++i) {
            std::vector<int> cur(sum + 1, 0);
            cur[0] = 1;  // value of dp[i][0]

            for (int j = 1; j <= sum; ++j) {
                if (arr[i - 1] > j) {
                    cur[j] = pre[j];
                } else {
                    cur[j] = pre[j - arr[i - 1]] || pre[j];
                }
            }
            pre = cur;
        }

        return pre[sum] == 1;
    }
};
"""

