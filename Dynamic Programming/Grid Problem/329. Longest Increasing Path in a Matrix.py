# method 1 : 

# mistakes: was doing correct only but was missing out of order cases of row and col(<0)

# here no need to mark cell visited as it will only take the increasing one only,
# so no chance of loop or viisting the same call again in same function call.

# Logic: Jis bhi cell pe h ,uska adjacent cells ka maximum find karo and 
# '1' karke return kar do. '1' for current cell.
# Note: Maximum chahiye isliye sbka maximum le rhe h and current cell ka value ko add kar rhe h.

# time: O(m * n * 4 ^ (m * n))

# Correct code 

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

# Java Code 
"""
public class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int ans = 1;  // each grid will contibute so automatically it will be '1'.
        // checking ans from every cell.
        for (int r = 0; r < matrix.length; r++) {
            for (int c = 0; c < matrix[0].length; c++) {
                ans = Math.max(ans, dfs(r, c, -1, matrix));  // taking '-1' as pre: smaller value than all the possible values in the matrix
            }
        }
        return ans;
    }

    private int dfs(int r, int c, int pre, int[][] mat) {
        // if out of order then simply return '0'.
        if (r < 0 || r >= mat.length || c < 0 || c >= mat[0].length || mat[r][c] <= pre) {
            return 0;
        }

        int maxLength = 0;  // iske aake ka maxLength find karke '1' add kar do
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};  // up, down, left, right
        for (int[] dir : directions) {
            int row = r + dir[0], col = c + dir[1];
            // count+= 1 + dfs(row, col, mat[row][col], mat)   // it adding the pre count values also that why getting error
            maxLength = Math.max(maxLength, dfs(row, col, mat[r][c], mat));  // incr count by 1 and call the next function.
        }
        return 1 + maxLength;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int longestIncreasingPath(std::vector<std::vector<int>>& matrix) {
        int ans = 1;  // each grid will contibute so automatically it will be '1'.
        // checking ans from every cell.
        for (int r = 0; r < matrix.size(); ++r) {
            for (int c = 0; c < matrix[0].size(); ++c) {
                ans = std::max(ans, dfs(r, c, -1, matrix));  // taking '-1' as pre: smaller value than all the possible values in the matrix
            }
        }
        return ans;
    }

private:
    int dfs(int r, int c, int pre, const std::vector<std::vector<int>>& mat) {
        // if out of order then simply return '0'.
        if (r < 0 || r >= mat.size() || c < 0 || c >= mat[0].size() || mat[r][c] <= pre) {
            return 0;
        }

        int maxLength = 0;  // iske aake ka maxLength find karke '1' add kar do
        std::vector<std::pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};  // up, down, left, right
        for (auto [dr, dc] : directions) {
            int row = r + dr, col = c + dc;
            // count+= 1 + dfs(row, col, mat[row][col], mat)   // it adding the pre count values also that why getting error
            maxLength = std::max(maxLength, dfs(row, col, mat[r][c], mat));  // incr count by 1 and call the next function.
        }
        return 1 + maxLength;
    }
};
"""
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

# Java Code 
"""
public class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        int ans = 1;  // each grid will contibute so automatically it will be '1'.
        int rows = matrix.length, cols = matrix[0].length;
        int[][] dp = new int[rows][cols];
        for (int[] row : dp)
            java.util.Arrays.fill(row, -1);

        // checking ans from every cell.
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                ans = Math.max(ans, dfs(r, c, -1, matrix, dp));  // taking '-1' as pre: smaller value than all the possible values in the matrix
            }
        }
        return ans;
    }

    private int dfs(int r, int c, int pre, int[][] mat, int[][] dp) {
        // if out of order then simply return '0'.
        if (r < 0 || r >= mat.length || c < 0 || c >= mat[0].length || mat[r][c] <= pre)
            return 0;

        if (dp[r][c] != -1)
            return dp[r][c];

        int maxLength = 0;  // iske aake ka maxLength find karke '1' add kar do
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};  // up, down, left, right
        for (int[] dir : directions) {
            int row = r + dir[0], col = c + dir[1];
            // count+= 1 + dfs(row, col, mat[row][col], mat)   // it adding the pre count values also that why getting error
            maxLength = Math.max(maxLength, dfs(row, col, mat[r][c], mat, dp));  // incr count by 1 and call the next function.
        }

        return dp[r][c] = 1 + maxLength;
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int longestIncreasingPath(std::vector<std::vector<int>>& matrix) {
        int ans = 1;  // each grid will contibute so automatically it will be '1'.
        int rows = matrix.size(), cols = matrix[0].size();
        std::vector<std::vector<int>> dp(rows, std::vector<int>(cols, -1));

        // checking ans from every cell.
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                ans = std::max(ans, dfs(r, c, -1, matrix, dp));  // taking '-1' as pre: smaller value than all the possible values in the matrix
            }
        }
        return ans;
    }

private:
    int dfs(int r, int c, int pre, const std::vector<std::vector<int>>& mat, std::vector<std::vector<int>>& dp) {
        // if out of order then simply return '0'.
        if (r < 0 || r >= mat.size() || c < 0 || c >= mat[0].size() || mat[r][c] <= pre)
            return 0;

        if (dp[r][c] != -1)
            return dp[r][c];

        int maxLength = 0;  // iske aake ka maxLength find karke '1' add kar do
        std::vector<std::pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};  // up, down, left, right
        for (auto [dr, dc] : directions) {
            int row = r + dr, col = c + dc;
            // count+= 1 + dfs(row, col, mat[row][col], mat)   // it adding the pre count values also that why getting error
            maxLength = std::max(maxLength, dfs(row, col, mat[r][c], mat, dp));  // incr count by 1 and call the next function.
        }

        return dp[r][c] = 1 + maxLength;
    }
};
"""
    
