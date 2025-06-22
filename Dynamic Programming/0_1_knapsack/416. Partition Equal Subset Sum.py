# Method 1: 
# Recursion + Memoisation

# Problem reduces to: is there any subset possible which has sum equal to sum(array)//2

# find the sum of the array, if sum is odd then no partition possible
# if sum is even then may be possible
# and for finding this, apply eaxctly the subset method on sum/2
# time: space= O(n*(sum/2))

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum= sum(nums)
        if list_sum %2!= 0:
            return False
        sum_to_check= list_sum//2
        return self.isSubsetSum(len(nums),nums,sum_to_check)   

    def isSubsetSum (self, N, arr, sum):
        # 1st initialse the matrix properly
        dp= [[False for i in range(sum+1) ] for i in range(N+1)]
        for i in range(N+1):
            for j in range(sum+1):
                if j==0:   # sum==0 
                    dp[i][j]= True
                elif i==0:  # sum!= 0 and number of ele= 0.
                    dp[i][j]= False
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
    public boolean canPartition(int[] nums) {
        int list_sum = 0;
        for (int num : nums) list_sum += num;

        if (list_sum % 2 != 0)
            return false;

        int sum_to_check = list_sum / 2;
        return isSubsetSum(nums.length, nums, sum_to_check);
    }

    public boolean isSubsetSum(int N, int[] arr, int sum) {
        // 1st initialse the matrix properly
        boolean[][] dp = new boolean[N + 1][sum + 1];
        for (int i = 0; i <= N; i++) {
            for (int j = 0; j <= sum; j++) {
                if (j == 0)  // sum==0 
                    dp[i][j] = true;
                else if (i == 0)  // sum!= 0 and number of ele= 0.
                    dp[i][j] = false;
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
    bool canPartition(std::vector<int>& nums) {
        int list_sum = 0;
        for (int num : nums) list_sum += num;

        if (list_sum % 2 != 0)
            return false;

        int sum_to_check = list_sum / 2;
        return isSubsetSum(nums.size(), nums, sum_to_check);
    }

    bool isSubsetSum(int N, std::vector<int>& arr, int sum) {
        // 1st initialse the matrix properly
        std::vector<std::vector<bool>> dp(N + 1, std::vector<bool>(sum + 1, false));
        for (int i = 0; i <= N; ++i) {
            for (int j = 0; j <= sum; ++j) {
                if (j == 0)  // sum==0 
                    dp[i][j] = true;
                else if (i == 0)  // sum!= 0 and number of ele= 0.
                    dp[i][j] = false;
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
# Method 2:
# Reducing space complexity to O(n).
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum= sum(nums)
        if list_sum %2!= 0:
            return False
        sum_to_check= list_sum//2
        return self.isSubsetSum(len(nums),nums,sum_to_check)   

    def isSubsetSum (self, N, arr, sum):
        # 1st initialse the matrix properly
        pre= [False for i in range(sum+1)]
        # filling the 1st row i.e for n== 0(when we are not considering any ele)
        pre[0]= True  # sum==0 if possible with '0' ele and all other will be False.
       
        for i in range(1,N+1):
            cur= [False for i in range(sum+1)]
            for j in range(1,sum+1):
                if arr[i-1]> j:
                    cur[j]= pre[j]
                else:
                    cur[j]= pre[j-arr[i-1]] or pre[j]
            pre= cur.copy()
        return cur[sum]

# Java Code 
"""
public class Solution {
    public boolean canPartition(int[] nums) {
        int list_sum = 0;
        for (int num : nums)
            list_sum += num;

        if (list_sum % 2 != 0)
            return false;

        int sum_to_check = list_sum / 2;
        return isSubsetSum(nums.length, nums, sum_to_check);
    }

    public boolean isSubsetSum(int N, int[] arr, int sum) {
        // 1st initialse the matrix properly
        boolean[] pre = new boolean[sum + 1];

        // filling the 1st row i.e for n== 0(when we are not considering any ele)
        pre[0] = true;  // sum==0 if possible with '0' ele and all other will be False.

        for (int i = 1; i <= N; i++) {
            boolean[] cur = new boolean[sum + 1];
            for (int j = 1; j <= sum; j++) {
                if (arr[i - 1] > j) {
                    cur[j] = pre[j];
                } else {
                    cur[j] = pre[j - arr[i - 1]] || pre[j];
                }
            }
            pre = cur.clone();
        }

        return pre[sum];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    bool canPartition(std::vector<int>& nums) {
        int list_sum = 0;
        for (int num : nums)
            list_sum += num;

        if (list_sum % 2 != 0)
            return false;

        int sum_to_check = list_sum / 2;
        return isSubsetSum(nums.size(), nums, sum_to_check);
    }

    bool isSubsetSum(int N, std::vector<int>& arr, int sum) {
        // 1st initialse the matrix properly
        std::vector<bool> pre(sum + 1, false);

        // filling the 1st row i.e for n== 0(when we are not considering any ele)
        pre[0] = true;  // sum==0 if possible with '0' ele and all other will be False.

        for (int i = 1; i <= N; ++i) {
            std::vector<bool> cur(sum + 1, false);
            for (int j = 1; j <= sum; ++j) {
                if (arr[i - 1] > j) {
                    cur[j] = pre[j];
                } else {
                    cur[j] = pre[j - arr[i - 1]] || pre[j];
                }
            }
            pre = cur;
        }

        return pre[sum];
    }
};
"""

# Method 3:
# Tabulation
from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        list_sum = sum(nums)
        if list_sum % 2 != 0:
            return False
        sum_to_check = list_sum // 2
        return self.isSubsetSum(len(nums), nums, sum_to_check)

    def isSubsetSum(self, N, arr, sum):
        # 1st initialise the matrix properly
        dp = [[False for _ in range(sum + 1)] for _ in range(N + 1)]
        
        for i in range(N + 1):
            for j in range(sum + 1):
                if j == 0:   # sum == 0 
                    dp[i][j] = True
                elif i == 0:  # sum != 0 and number of elements = 0
                    dp[i][j] = False
        
        # now just same as 0/1 Knapsack           
        for i in range(1, N + 1):
            for j in range(1, sum + 1):
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
        
        return dp[N][sum]
