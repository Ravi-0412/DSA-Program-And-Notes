# Method 1: 
# Recursion + Memsoisation

# Logic: Indirectly we have to find: The number of subsets with given diff. Here diff= 'Target'.
# How?
# We only have two operations allowed '+' and '-' and we want their result = target 
# so indirectly we are dividing array into two parts while calculating result i.e 
# 1) all containing positive number & 2) all containing negative numbers
#  And taking 'difference' of both to check if it is equal to target.

# So Q reduces to :"find the number of subsets with given diff. Here diff= 'Target'.

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # 1. Edge Case: If target is unreachable or (total+target) is odd, 
        # it's impossible to partition the sum into two integers.
        if abs(target) > total or (total + target) % 2 != 0:
            return 0
            
        s1 = (total + target) // 2
        n = len(nums)
        
        # dp[index][current_sum]
        dp = [[-1 for _ in range(s1 + 1)] for _ in range(n)]
        
        return self.helper(n - 1, nums, s1, dp)
    
    def helper(self, ind, arr, target_sum, dp):
        # Base Case: When we are at the first element (index 0)
        if ind == 0:
            # If target_sum is 0 and arr[0] is 0, we can either include it or exclude it.
            # Both results in a sum of 0, so there are 2 ways.
            if target_sum == 0 and arr[0] == 0: return 2
            # If target_sum matches the element OR target_sum is 0 (we exclude the element),
            # there is exactly 1 way to get the sum.
            if target_sum == 0 or target_sum == arr[0]: return 1
            return 0
            
        if dp[ind][target_sum] != -1:
            return dp[ind][target_sum]
            
        # Recursive Step
        # Choice 1: Exclude the element
        exclude = self.helper(ind - 1, arr, target_sum, dp)
        
        # Choice 2: Include the element (only if it fits in the target_sum)
        include = 0
        if arr[ind] <= target_sum:
            include = self.helper(ind - 1, arr, target_sum - arr[ind], dp)
            
        dp[ind][target_sum] = include + exclude
        return dp[ind][target_sum]

# Java Code 
"""
public class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int total = 0, n = nums.length;
        for (int num : nums) total += num;

        if ((total + target) % 2 != 0)  // if odd then no such subsets possible
            return 0;

        int s1 = (total + target) / 2;  // by solving mathematically(see the notes)
        int[][] dp = new int[n][s1 + 1];  // no need to go till 'N+1' as we are starting from 'N-1'
        for (int[] row : dp)
            java.util.Arrays.fill(row, -1);

        return helper(n - 1, nums, s1, dp);
    }

    private int helper(int ind, int[] arr, int sum, int[][] dp) {
        if (ind == 0) {
            if (sum == 0 && arr[0] == 0)
                return 2;
            if (sum == 0 || sum == arr[0])  // in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1;
            else
                return 0;
        }

        if (dp[ind][sum] != -1)
            return dp[ind][sum];

        if (arr[ind] > sum)
            dp[ind][sum] = helper(ind - 1, arr, sum, dp);
        else  // arr[ind] <= sum
            dp[ind][sum] = helper(ind - 1, arr, sum - arr[ind], dp) + helper(ind - 1, arr, sum, dp);

        return dp[ind][sum];  // return the last ele
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int findTargetSumWays(std::vector<int>& nums, int target) {
        int total = 0, n = nums.size();
        for (int num : nums) total += num;

        if ((total + target) % 2 != 0)  // if odd then no such subsets possible
            return 0;

        int s1 = (total + target) / 2;  // by solving mathematically(see the notes)
        std::vector<std::vector<int>> dp(n, std::vector<int>(s1 + 1, -1));  // no need to go till 'N+1' as we are starting from 'N-1'
        return helper(n - 1, nums, s1, dp);
    }

private:
    int helper(int ind, const std::vector<int>& arr, int sum, std::vector<std::vector<int>>& dp) {
        if (ind == 0) {
            if (sum == 0 && arr[0] == 0)
                return 2;
            if (sum == 0 || sum == arr[0])  // in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1;
            else
                return 0;
        }

        if (dp[ind][sum] != -1)
            return dp[ind][sum];

        if (arr[ind] > sum)
            dp[ind][sum] = helper(ind - 1, arr, sum, dp);
        else  // arr[ind] <= sum
            dp[ind][sum] = helper(ind - 1, arr, sum - arr[ind], dp) + helper(ind - 1, arr, sum, dp);

        return dp[ind][sum];  // return the last ele
    }
};
"""

# Method 2:
# Tabulation

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total, n = sum(nums), len(nums)
        if (total + target) & 1:  # if odd then no such subsets possible
            return 0
        s1 = (total + target) // 2
        if s1 < 0:
            return 0
        
        dp = [[0 for _ in range(s1 + 1)] for _ in range(n)]
        
        # Base case initialization for ind == 0
        if nums[0] == 0:
            dp[0][0] = 2  # either take or not take zero
        else:
            dp[0][0] = 1  # only one way to make sum=0 by not taking
        
        if nums[0] != 0 and nums[0] <= s1:
            dp[0][nums[0]] = 1
        
        # Fill dp for remaining indices
        for ind in range(1, n):
            for sum_ in range(s1 + 1):
                notTake = dp[ind - 1][sum_]
                take = 0
                if nums[ind] <= sum_:
                    take = dp[ind - 1][sum_ - nums[ind]]
                dp[ind][sum_] = take + notTake
        
        return dp[n - 1][s1]

# Java Code
"""
class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        int total = 0, n = nums.length;
        for (int num : nums) total += num;

        if ((total + target) % 2 != 0) return 0;  // if odd then no such subsets possible
        int s1 = (total + target) / 2;
        if (s1 < 0) return 0;

        int[][] dp = new int[n][s1 + 1];

        // Base case initialization for ind == 0
        if (nums[0] == 0) {
            dp[0][0] = 2;  // either take or not take zero
        } else {
            dp[0][0] = 1;  // only one way to make sum=0 by not taking
        }

        if (nums[0] != 0 && nums[0] <= s1) {
            dp[0][nums[0]] = 1;
        }

        // Fill dp for remaining indices
        for (int ind = 1; ind < n; ind++) {
            for (int sum = 0; sum <= s1; sum++) {
                int notTake = dp[ind - 1][sum];
                int take = 0;
                if (nums[ind] <= sum) {
                    take = dp[ind - 1][sum - nums[ind]];
                }
                dp[ind][sum] = take + notTake;
            }
        }

        return dp[n - 1][s1];
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int total = 0, n = nums.size();
        for (int num : nums) total += num;

        if ((total + target) % 2 != 0) return 0;  // if odd then no such subsets possible
        int s1 = (total + target) / 2;
        if (s1 < 0) return 0;

        vector<vector<int>> dp(n, vector<int>(s1 + 1, 0));

        // Base case initialization for ind == 0
        if (nums[0] == 0) {
            dp[0][0] = 2;  // either take or not take zero
        } else {
            dp[0][0] = 1;  // only one way to make sum=0 by not taking
        }

        if (nums[0] != 0 && nums[0] <= s1) {
            dp[0][nums[0]] = 1;
        }

        // Fill dp for remaining indices
        for (int ind = 1; ind < n; ++ind) {
            for (int sum = 0; sum <= s1; ++sum) {
                int notTake = dp[ind - 1][sum];
                int take = 0;
                if (nums[ind] <= sum) {
                    take = dp[ind - 1][sum - nums[ind]];
                }
                dp[ind][sum] = take + notTake;
            }
        }

        return dp[n - 1][s1];
    }
};
"""

# Short way : Tabulation
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2 != 0: return 0
        s1 = (total + target) // 2
        
        # dp[i][j] = number of ways to get sum 'j' using first 'i' elements
        dp = [[0] * (s1 + 1) for _ in range(len(nums) + 1)]
        
        # Base Case: 1 way to get sum 0 (by choosing an empty set)
        dp[0][0] = 1
        
        for i in range(1, len(nums) + 1):
            for j in range(s1 + 1):
                # Exclude current element
                dp[i][j] = dp[i-1][j]
                # Include current element (if it fits)
                if nums[i-1] <= j:
                    dp[i][j] += dp[i-1][j - nums[i-1]]
                    
        return dp[len(nums)][s1]
