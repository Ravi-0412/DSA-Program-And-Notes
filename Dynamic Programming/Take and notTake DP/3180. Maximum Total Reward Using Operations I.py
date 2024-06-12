# For each element we have two choice: take or notTake.
# for checking if we can take that elememnt we will have to keep track of total_sum till_now also.

# Note vvi: answer will never be above 4000.
# 1 <= rewardValues[i] <= 2000

# Proof:
# Lets say the last element we picked is X.
# The max possible value of reward before that is X-1.
# This implies max possible reward is X + (X-1) = 2*X-1.
# Since max value of X is 2000, so the max value of reward is 3999.

# Even ans will be less than : 2*max(nums)
# so take dimension of total_sum till : 2*max(nums) only not even 4000 is required.

# But giving tle in Python bu getting excepted in c++ and java.

class Solution:
    def maxTotalReward(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def solve(cur, total):
            if cur == n or total >= max(nums):
                return total
            if dp[cur][total] != -1:
                return dp[cur][total]
            take = 0
            notTake = solve(cur + 1, total)
            if nums[cur] > total:
                take = solve(cur + 1, total + nums[cur])
            dp[cur][total] = max(take, notTake)
            return max(take, notTake)
        
        dp = [[-1 for j in range(nums[-1] *2)] for i in range(n)]
        return solve(0, 0)

# java
"""
public class Solution {
    public int maxTotalReward(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int[][] dp = new int[n][nums[n - 1] * 2];
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        return solve(nums, 0, 0, dp);
    }

    private int solve(int[] nums, int cur, int total, int[][] dp) {
        if (cur == nums.length || total >= nums[nums.length - 1]) {
            return total;
        }
        if (dp[cur][total] != -1) {
            return dp[cur][total];
        }
        int take = 0;
        int notTake = solve(nums, cur + 1, total, dp);
        if (nums[cur] > total) {
            take = solve(nums, cur + 1, total + nums[cur], dp);
        }
        dp[cur][total] = Math.max(take, notTake);
        return dp[cur][total];
    }
}
"""