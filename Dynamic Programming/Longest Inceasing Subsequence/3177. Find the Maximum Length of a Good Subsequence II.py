# 1st do part1 then come to this

# part1 solution

# Method 1: Similar as '300.Longest Increasing subsequence'
# But giving tle in python but got accepted in c++ and java.

# time: O(n*n*k) = O(500*500*25) = O(625 * 10^4) ~ O(10^7)

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def solve(cur, pre, k):
            if cur == n:
                return 0
            if dp[cur][pre + 1][k] != -1:
                return dp[cur][pre + 1][k]
            take = 0
            notTake = solve(cur + 1 , pre, k)   # we always have one choice to not take
            # Now consider all the cases where we can include this
            if pre == - 1 or nums[cur] == nums[pre]:
                # considering these two cases where we can include together because
                # in these two cases 'k' won't change
                take = max(take ,  1 + solve(cur + 1, cur, k))
            elif k > 0 : # nums[cur] == nums[pre]: 
                # in this case we only include if we have sufficient 'k' left 
                # and this case 'k' will decrease
                take = max(take, 1 + solve(cur + 1, cur, k - 1))
            dp[cur][pre + 1][k] = max(take, notTake)
            return max(take, notTake)  # return max of both
        
        dp = [[[-1 for l in range(k + 1)] for j in range(n + 1)] for i in range(n + 1)]

        return solve(0, -1, k)

# java version of above
# Accepted
"""
import java.util.Arrays;

public class Solution {
    private int[][][] dp;
    
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        dp = new int[n + 1][n + 1][k + 1];
        
        // Initialize dp array with -1
        for (int[][] row : dp) {
            for (int[] col : row) {
                Arrays.fill(col, -1);
            }
        }
        
        return solve(nums, 0, -1, k);
    }
    
    private int solve(int[] nums, int cur, int pre, int k) {
        int n = nums.length;
        
        if (cur == n) {
            return 0;
        }
        
        if (dp[cur][pre + 1][k] != -1) {
            return dp[cur][pre + 1][k];
        }
        
        int take = 0;
        int notTake = solve(nums, cur + 1, pre, k);  // we always have one choice to not take
        
        // Now consider all the cases where we can include this
        if (pre == -1 || nums[cur] == nums[pre]) {
            // considering these two cases where we can include together because
            // in these two cases 'k' won't change
            take = Math.max(take, 1 + solve(nums, cur + 1, cur, k));
        } else if (k > 0) {
            // in this case we only include if we have sufficient 'k' left 
            // and this case 'k' will decrease
            take = Math.max(take, 1 + solve(nums, cur + 1, cur, k - 1));
        }
        
        dp[cur][pre + 1][k] = Math.max(take, notTake);
        return dp[cur][pre + 1][k];  // return max of both
    }
}
"""

# But above solution will tle in java also because
# time = O(n*n*n) = O(5* 10^3 * 5* 10^3 * 50) = O(125 * 10^7) > O(10^8)

# so somehow we have to optimise
# Instead of checking with all the used index for current index 
# check only with first index on left/right with each possible value of 'k'.
# And for other element where current ele is equal or even not equal we can maintain 
# and array with size 'k' which will tell what will be maximum value till now if you allow 'j' no of changes.

# Explanation of the Logic:
# 1) Definition of dp[i][j]:
# dp[i][j] represents the longest subsequence that starts from index i and allows up to j changes.

# 2) Two Cases for Computing dp[i][j]:
# Previous Occurrence of the Same Number (nums[i]):
# We maintain a hashmap named prev to track the previous position p of the same number nums[i].
# If there's a previous occurrence of nums[i] at index p, dp[i][j] can be extended from dp[p][j] by adding 1 
# to represent the current occurrence of nums[i].
# Maximum Result So Far for Any Previous Number:
# We maintain an array named max_dp to keep track of the maximum result so far for any previous number.
# max_dp[j - 1] represents the maximum subsequence length with j - 1 changes allowed.
# If j > 0, we can use this value to extend the current subsequence by adding 1 to it.

# 3) Tracking the Largest Result:
# Throughout the iteration, we keep track of the largest dp[i][k] value encountered and return it as the final result.

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1) for _ in range(n)]
        max_dp = [0] * (k + 1)
        prev = {}

        res = 0

        for i in range(n - 1, -1, -1):
            p = prev.get(nums[i], i)
            for j in range(k, -1, -1):
                dp[i][j] = max(1 + (dp[p][j] if i != p else 0),
                               1 + (max_dp[j - 1] if j > 0 else 0))
                max_dp[j] = max(max_dp[j], dp[i][j])
            prev[nums[i]] = i   # only need to store next right index
            res = max(res, dp[i][k])

        return res
    
# java
"""
public class Solution {
    public int maximumLength(int[] nums, int k) {
        int n = nums.length;
        int[][] dp = new int[n][k + 1];
        int[] max_dp = new int[k + 1];
        HashMap<Integer, Integer> prev = new HashMap<>();

        int res = 0;

        for (int i = n - 1; i >= 0; i--) {
            int p = prev.getOrDefault(nums[i], i);
            for (int j = k; j >= 0; j--) {
                dp[i][j] = Math.max(1 + (i != p ? dp[p][j] : 0),
                                    1 + (j > 0 ? max_dp[j - 1] : 0));
                max_dp[j] = Math.max(max_dp[j], dp[i][j]);
            }
            prev.put(nums[i], i);   // only need to store next right index
            res = Math.max(res, dp[i][k]);
        }

        return res;
    }
}

"""