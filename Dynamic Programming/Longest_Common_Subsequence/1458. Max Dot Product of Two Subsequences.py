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
        