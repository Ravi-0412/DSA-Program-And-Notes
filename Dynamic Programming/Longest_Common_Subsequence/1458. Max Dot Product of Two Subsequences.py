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
