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
        total, n= sum(nums), len(nums)
        if (total+ target) & 1:  # if odd then no such subsets possible 
            return 0
        s1 = (total+ target)//2  # by solving mathematically(see the notes)
        dp= [[-1 for i in range(s1 +1)] for i in range(n)]  # no need to go till 'N+1' as we are starting from  'N-1' 
        return self.helper(n-1, nums, s1, dp)
    
    def helper(self, ind, arr, sum, dp):
        if ind== 0:
            if sum== 0 and arr[0]== 0:
                return 2
            if sum==0 or sum== arr[0]: # in actual sum== 0 and arr[0] != 0 or sum== arr[0]
                return 1
            else:
                return 0
        if dp[ind][sum] != -1: 
            return dp[ind][sum]
        if arr[ind]> sum:
            dp[ind][sum]= self.helper(ind -1, arr, sum, dp)
        else:   # arr[ind] <= sum
            dp[ind][sum]= self.helper(ind -1, arr, sum- arr[ind], dp) +  self.helper(ind -1, arr, sum, dp)
        return dp[ind][sum]  # return the last ele

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