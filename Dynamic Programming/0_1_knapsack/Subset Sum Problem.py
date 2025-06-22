# method 1: Recursion
class Solution:
    def isSubsetSum (self, N, arr, sum):
        return self.helper(N, arr, sum)
    def helper(self, n, arr, sum):
        if sum== 0:
            return True
        if n== 0:  # means n== 0 and sum != 0
            return False
        if arr[n-1] > sum:
            # Means we can't consider this ele. only one choice
            return self.helper(n-1,arr,sum)
        # Means we can consider this ele but we have choices i.e 1) Take it 2) Not take it.
        return self.helper(n-1,arr,sum- arr[n-1]) or self.helper(n-1,arr,sum)

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
        if (arr[n - 1] > sum)
            // Means we can't consider this ele. only one choice
            return helper(n - 1, arr, sum);
        // Means we can consider this ele but we have choices i.e 1) Take it 2) Not take it.
        return helper(n - 1, arr, sum - arr[n - 1]) || helper(n - 1, arr, sum);
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
        if (arr[n - 1] > sum)
            // Means we can't consider this ele. only one choice
            return helper(n - 1, arr, sum);
        // Means we can consider this ele but we have choices i.e 1) Take it 2) Not take it.
        return helper(n - 1, arr, sum - arr[n - 1]) || helper(n - 1, arr, sum);
    }
};
"""

# Other better way
# do by this methd only for this type of question

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

# Java Code
"""
public class Solution {
    public boolean isSubsetSum(int N, int[] arr, int sum) {
        // 1st initialse the matrix properly
        boolean[][] dp = new boolean[N + 1][sum + 1];

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= sum; j++) {
                if (i == 0)
                    dp[i][j] = false;
                if (j == 0)
                    dp[i][j] = true;
            }
        }

        // now just same as 0/1 Knapsack
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= sum; j++) {
                if (arr[i - 1] > j)
                    dp[i][j] = dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] || dp[i - 1][j];
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
    bool isSubsetSum(int N, std::vector<int>& arr, int sum) {
        // 1st initialse the matrix properly
        std::vector<std::vector<bool>> dp(N + 1, std::vector<bool>(sum + 1, false));

        for (int i = 0; i <= N; ++i) {
            for (int j = 0; j <= sum; ++j) {
                if (i == 0)
                    dp[i][j] = false;
                if (j == 0)
                    dp[i][j] = true;
            }
        }

        // now just same as 0/1 Knapsack
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= sum; ++j) {
                if (arr[i - 1] > j)
                    dp[i][j] = dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] || dp[i - 1][j];
            }
        }

        return dp[N][sum];
    }
};
"""
# Other way of initialsing the base case.
# dp[0][0] = should be 'True' and in above one 2nd if is making it automatically 'True' that's why above one is working.
# i.e sum = 0 is possible with no ele.

class Solution:
    def isSubsetSum (self, N, arr, sum):
        # 1st initialse the matrix properly
        dp= [[-1 for i in range(sum+1) ] for i in range(N+1)]
        for i in range(N+1):
            dp[i][0] = 1
        for i in range(sum+1):
            dp[0][i] = 0
        dp[0][0] = 1
        # now just same as 0/1 Knapsack           
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1]> j:
                    dp[i][j]= dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
        return dp[N][sum]   

# Java Code
"""
public class Solution {
    public boolean isSubsetSum(int N, int[] arr, int sum) {
        // 1st initialse the matrix properly
        int[][] dp = new int[N + 1][sum + 1];
        for (int i = 0; i <= N; i++) {
            dp[i][0] = 1;
        }
        for (int i = 0; i <= sum; i++) {
            dp[0][i] = 0;
        }
        dp[0][0] = 1;

        // now just same as 0/1 Knapsack
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= sum; j++) {
                if (arr[i - 1] > j)
                    dp[i][j] = dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] == 1 || dp[i - 1][j] == 1 ? 1 : 0;
            }
        }

        return dp[N][sum] == 1;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    bool isSubsetSum(int N, std::vector<int>& arr, int sum) {
        // 1st initialse the matrix properly
        std::vector<std::vector<int>> dp(N + 1, std::vector<int>(sum + 1, -1));
        for (int i = 0; i <= N; ++i)
            dp[i][0] = 1;
        for (int i = 0; i <= sum; ++i)
            dp[0][i] = 0;
        dp[0][0] = 1;

        // now just same as 0/1 Knapsack
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= sum; ++j) {
                if (arr[i - 1] > j)
                    dp[i][j] = dp[i - 1][j];
                else
                    dp[i][j] = (dp[i - 1][j - arr[i - 1]] || dp[i - 1][j]) ? 1 : 0;
            }
        }

        return dp[N][sum] == 1;
    }
};
"""

# method 4: optimising space complexity to O(n)
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

