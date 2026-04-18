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
# Better one
# No need to take 'pre' in function parameter.
# Time complexity = O(m * n) = space

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        
        # Memoization table: stores the longest path starting from (r, c)
        memo = {} 
        
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        def dfs(r, c):
            # If we've already calculated the path for this cell, return it
            if (r, c) in memo:
                return memo[(r, c)]
            
            # Every cell has a minimum path length of 1 (itself)
            max_len = 1 
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                
                # Check bounds and increasing condition
                if 0 <= new_r < rows and 0 <= new_c < cols and matrix[new_r][new_c] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(new_r, new_c))
            
            # Store the result before returning
            # memo[(r, c)] = max_len + 1   # will give error , output will be one more than expected. 
            # So either take max_len = 0 and then in return add '1'(like above method) while returning. 
            return max_len

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))
        return ans

# Method 4:
# Tabulation
"""
By sorting the cells by value, we guarantee that when we are calculating dp[r][c], 
we have already calculated the dp values for all neighbors that have smaller values than matrix[r][c]. 

Time : O(M*N * log(M * N))

Q) Why not we are able to convert into Tabulation by simply running required no of 'for' loops like other questions ?
-> 
1. The order of computation isn't just i-1, i-2 or known dependent row.
You have to know the order in which to fill the table. This is why we had to sort the cells first in the tabulation approach.

2. If you just use a for loop over rows and cols, you might try to calculate dp[r][c] before its neighbors are ready. 
That is why sorting or Topological Sort is required in tabulation for path problems.
(See below Method 5 for this) 
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        
        rows, cols = len(matrix), len(matrix[0])
        
        # 1. Store all cells as (value, r, c) and sort them.
        # Sorting ensures we process cells from smallest value to largest.
        cells = []
        for r in range(rows):
            for c in range(cols):
                cells.append((matrix[r][c], r, c))
        cells.sort()
        
        # 2. dp[r][c] will store the longest increasing path ENDING at (r, c)
        dp = [[1] * cols for _ in range(rows)]
        
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        
        # 3. Process cells from smallest to largest
        for val, r, c in cells:
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                
                # Check neighbors that are smaller than the current cell.
                # If the neighbor is smaller, the path ending at (new_r, new_c)
                # can be extended to (r, c).
                if 0 <= new_r < rows and 0 <= new_c < cols and matrix[new_r][new_c] < matrix[r][c]:
                    dp[r][c] = max(dp[r][c], 1 + dp[new_r][new_c])
                    
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dp[r][c])
        return ans


# Method 5:
"""
using Topological sort , but how ?
Since we need to find the longest increasing path , it means that path won't contain cycle and it will a directed path only.

How to proceed?
Define Edges: A directed edge exists from Cell A to Cell B if B is an adjacent neighbor and B > A.
Calculate Out-Degrees: For every cell, count how many neighbors are strictly greater than it.
Find the Peaks: Any cell with an out-degree of 0 is a "peak" (it has no higher ground to move to). 
Add all these peaks to a queue.
Layered BFS (The "Peel"): * Remove all current peaks from the queue (Level 1).For each peak, look at its smaller neighbors. 
Since the peak is now "removed," these neighbors have one fewer "greater neighbor" to worry about. 
Decrement their out-degree.If a neighbor's out-degree hits 0, it becomes a "peak" for the next level.
Count Levels: The total number of BFS levels processed before the queue is empty equals the length of the Longest Increasing Path.

Time = space = O(M*N)
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
