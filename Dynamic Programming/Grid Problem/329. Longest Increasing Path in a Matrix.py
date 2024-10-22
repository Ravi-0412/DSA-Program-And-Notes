# mistakes: was doing correct only but was missing out of order cases of row and col(<0)

# here no need to mark cell visited as it will only take the increasing one only,
# so no chance of loop or viisting the same call again in same function call.

# Logic: Jis bhi cell pe h ,uska adjacent cells ka maximum find karo and 
# '1' karke return kar do. '1' for current cell.
# Note: Maximum chahiye isliye sbka maximum le rhe h and current cell ka value ko add kar rhe h.

# time: O(m * n * 4 ^ (m * n))
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans= 1  # each grid will contibute so automatically it will be '1'.
        # checking ans from every cell.
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans= max(ans, self.dfs(r, c,-1, matrix))   # taking '-1' as pre: smaller value than all the possible values in the matrix
        return ans
    
    def dfs(self, r, c, pre, mat):
        # if out of order then simply return '0'.
        if r< 0 or r >= len(mat) or c< 0 or c >= len(mat[0]) or mat[r][c] <= pre:
            return 0
        maxLength = 0  # iske aake ka maxLength find karke '1' add kar do
        directions= [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        for dr, dc in directions:
            row, col= r + dr, c+ dc        
            # count+= 1 + self.dfs(row, col, mat[row][col], mat)   # it adding the pre count values also that why getting error
            maxLength = max(maxLength, self.dfs(row, col, mat[r][c], mat))     # incr count by 1 and call the next function.
        return 1 + maxLength

# memoisation
# time complexity = O(m * n)  (average)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ans= 1  # each grid will contibute so automatically it will be '1'.
        dp= [[-1 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        # checking ans from every cell.
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans= max(ans, self.dfs(r, c,-1, matrix, dp))   # taking '-1' as pre: smaller value than all the possible values in the matrix
        return ans
    def dfs(self, r, c, pre, mat, dp):
        # if out of order then simply return '0'.
        if r< 0 or r >= len(mat) or c< 0 or c >= len(mat[0]) or mat[r][c] <= pre:
            return 0
        if dp[r][c]!= -1:
            return dp[r][c]
        maxLength = 0  # iske aake ka maxLength find karke '1' add kar do
        directions= [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        for dr, dc in directions:
            row, col= r + dr, c+ dc        
            # count+= 1 + self.dfs(row, col, mat[row][col], mat)   # it adding the pre count values also that why getting error
            maxLength = max(maxLength, self.dfs(row, col, mat[r][c], mat))     # incr count by 1 and call the next function.
        dp[r][c]= 1 + maxLength
        return dp[r][c]

# Java
"""

class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0; // Handle edge case for empty matrix
        }

        int rows = matrix.length;
        int cols = matrix[0].length;
        int[][] dp = new int[rows][cols]; // Memoization table
        int ans = 1; // At least 1 since each cell contributes at least itself

        // Check for the longest increasing path from every cell
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                ans = Math.max(ans, dfs(r, c, -1, matrix, dp)); // Start DFS from each cell
            }
        }

        return ans;
    }

    private int dfs(int r, int c, int pre, int[][] mat, int[][] dp) {
        // Check boundaries and if the current cell is greater than the previous cell
        if (r < 0 || r >= mat.length || c < 0 || c >= mat[0].length || mat[r][c] <= pre) {
            return 0;
        }

        // Return the cached result if already computed
        if (dp[r][c] != 0) {
            return dp[r][c];
        }

        int maxLength = 0; // To find the maximum length from this cell
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // Up, down, left, right

        for (int[] dir : directions) {
            int row = r + dir[0];
            int col = c + dir[1];
            // Recursively calculate the length from the next cell
            maxLength = Math.max(maxLength, dfs(row, col, mat[r][c], mat, dp));
        }

        // Store the result in the dp table, adding 1 for the current cell
        dp[r][c] = 1 + maxLength;
        return dp[r][c];
    }
}
"""
    
# Related Q:
# 1) 2328. Number of Increasing Paths in a Grid
# Isme number chahiye isliye adjacent wale ka 'sum le lo ' and '1' add karke 
# return kar do .




# we can also use bfs.

# top down approach will be very tough.
