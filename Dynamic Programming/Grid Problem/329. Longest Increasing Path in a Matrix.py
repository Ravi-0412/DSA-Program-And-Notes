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

"""
Method 2: 
# memoisation
Time complexity = O(m * n) = space


"""
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

# Method 3:
"""
using Topological sort , but how ?
Since we need to find the longest increasing path , it means that pathwon't contain cycle and it will a directed path only.

How to proceed?
Define Edges: A directed edge exists from Cell A to Cell B if B is an adjacent neighbor and B > A.
Calculate Out-Degrees: For every cell, count how many neighbors are strictly greater than it.
Find the Peaks: Any cell with an out-degree of 0 is a "peak" (it has no higher ground to move to). 
Add all these peaks to a queue.
Layered BFS (The "Peel"): * Remove all current peaks from the queue (Level 1).For each peak, look at its smaller neighbors. 
Since the peak is now "removed," these neighbors have one fewer "greater neighbor" to worry about. 
Decrement their out-degree.If a neighbor's out-degree hits 0, it becomes a "peak" for the next level.
Count Levels: The total number of BFS levels processed before the queue is empty equals the length of the Longest Increasing Path.

Time = space = O(M*N
"""

from collections import deque

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        M, N = len(matrix), len(matrix[0])
        out_degree = [[0] * N for _ in range(M)] # gives number of adjacent cell greater than from cell (i, j)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # 1. Calculate out-degrees
        # A cell points to a neighbor if neighbor > cell
        for r in range(M):
            for c in range(N):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N and matrix[nr][nc] > matrix[r][c]:
                        out_degree[r][c] += 1
        
        # 2. Find all cells that have no neighbors larger than them
        queue = deque([(r, c) for r in range(M) for c in range(N) if out_degree[r][c] == 0])
        
        # BFS, going from bigger value to smaller value
        height = 0
        while queue:
            height += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N and matrix[nr][nc] < matrix[r][c]:
                        out_degree[nr][nc] -= 1
                        if out_degree[nr][nc] == 0:
                            queue.append((nr, nc))
        return height
