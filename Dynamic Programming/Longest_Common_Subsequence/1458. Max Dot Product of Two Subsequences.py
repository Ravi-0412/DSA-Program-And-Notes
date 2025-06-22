# Method 1:
# Recursion + Memoisation

"""
Choices at each step:
For each pair (i, j):

1) Pick both elements:

1.1) Take nums1[i] * nums2[j], and recursively compute the max dot product of the rest:
nums1[i] * nums2[j] + solve(i+1, j+1)

1.2) If solve(i+1, j+1) is negative, we skip it (i.e., use max(solve(i+1, j+1), 0)) to make sure we never reduce the score by continuing.

2) Skip nums1[i] and try from i+1

3) Skip nums2[j] and try from j+1


dp[i][j] = max(
    nums1[i] * nums2[j] + max(solve(i + 1, j + 1), 0),
    solve(i + 1, j),
    solve(i, j + 1)
)


Base Case:
If either array is exhausted (i == n or j == m), return -inf because we need non-empty subsequences.

Time: O(n * m)

"""

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * m for _ in range(n)]
        
        def solve(i, j):
            if i == n or j == m:
                return float('-inf')
            
            if dp[i][j] != float('-inf'):
                return dp[i][j]
            
            dp[i][j] = max(
                nums1[i] * nums2[j] + max(solve(i + 1, j + 1), 0),
                solve(i + 1, j),  
                solve(i, j + 1), 
            )
            
            return dp[i][j]
        
        return solve(0, 0)
        
# Java Code 
"""
class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length;
        Integer[][] dp = new Integer[n][m];

        return solve(0, 0, nums1, nums2, dp);
    }

    private int solve(int i, int j, int[] nums1, int[] nums2, Integer[][] dp) {
        if (i == nums1.length || j == nums2.length) return Integer.MIN_VALUE;

        if (dp[i][j] != null) return dp[i][j];

        int use = nums1[i] * nums2[j] + Math.max(0, solve(i + 1, j + 1, nums1, nums2, dp));
        int skip1 = solve(i + 1, j, nums1, nums2, dp);
        int skip2 = solve(i, j + 1, nums1, nums2, dp);

        dp[i][j] = Math.max(use, Math.max(skip1, skip2));
        return dp[i][j];
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size(), m = nums2.size();
        vector<vector<int>> dp(n, vector<int>(m, INT_MIN));
        return solve(0, 0, nums1, nums2, dp);
    }

private:
    int solve(int i, int j, const vector<int>& nums1, const vector<int>& nums2, vector<vector<int>>& dp) {
        if (i == nums1.size() || j == nums2.size()) return INT_MIN;

        if (dp[i][j] != INT_MIN) return dp[i][j];

        int use = nums1[i] * nums2[j] + max(0, solve(i + 1, j + 1, nums1, nums2, dp));
        int skip1 = solve(i + 1, j, nums1, nums2, dp);
        int skip2 = solve(i, j + 1, nums1, nums2, dp);

        return dp[i][j] = max({use, skip1, skip2});
    }
};
"""
