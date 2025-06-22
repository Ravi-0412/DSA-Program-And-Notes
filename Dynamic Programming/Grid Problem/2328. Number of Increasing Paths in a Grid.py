# method 1:
# Recursion + memoisation

# How do we calculate for 1D?
# Ans: from every index find the "length of  longest strictly increasing subarray" and add those length to get the final ans.

# E.g: arr= [1,2,3,4,3]

# Let's try to pick each element/index as our starting point and find the answer.
# 1 -> [1,2,3,4] = 4, 2 -> [2,3,4] = 3, 3-> [3,4] = 2, [4] = 1, [3] = 1. 
# Summing these individual values will produce the answer. But what do these individual results essentially mean?

# Let's look at [1,2,3,4] = 4, this means starting from 1 we have a total of 4 increasing sequences/paths. 
# [1,2,3,4], [1,2,3], [1,2], [1]. We are calculating the same for each starting point.

# Note: The 2D version is similar as it forms a DAG and hence are no cycles in the graph/path.

# In same way we are doing for 2D.

# Note: Just same as '329. Longest Increasing Path in a Matrix'
# Isme number chahiye isliye adjacent wale ka 'sum le lo ' and '1' add karke 
# return kar do .

# time : O(4*m *n) .At each recursion at max you have 4 directions thus O(1) further calls and we have a total of m*n states for the DP.
# SPACE: o(m * n)

# Note: It's strictly increasing so we don't need visited array.

from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        
        # Initialize dp with -1 to mark uncomputed cells
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            total = 1  # path that starts and ends at (i, j)
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    total += dfs(ni, nj)
                    total %= mod
            dp[i][j] = total
            return dp[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dfs(i, j)) % mod
        return ans

# Java Code 
"""
public class Solution {
    int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};  // up, down,left, right
    int mod = 1_000_000_007;
    int[][] grid;
    int[][] dp;

    public int countPaths(int[][] grid) {
        this.grid = grid;
        int m = grid.length, n = grid[0].length;
        dp = new int[m][n];

        for (int[] row : dp)
            java.util.Arrays.fill(row, -1);

        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans = (ans + dfs(i, j)) % mod;
            }
        }
        return ans;
    }

    private int dfs(int i, int j) {
        if (dp[i][j] != -1)
            return dp[i][j];

        long sum = 0;
        for (int[] dir : directions) {
            int ni = i + dir[0], nj = j + dir[1];
            if (ni >= 0 && ni < grid.length && nj >= 0 && nj < grid[0].length && grid[ni][nj] > grid[i][j]) {
                sum = (sum + dfs(ni, nj)) % mod;
            }
        }

        return dp[i][j] = (int)((1 + sum) % mod);
    }
}
"""

# C++ Code 
"""
class Solution {
    const int mod = 1e9 + 7;
    std::vector<std::vector<int>> grid;
    std::vector<std::vector<int>> dp;
    std::vector<std::pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};  // up, down, left, right

public:
    int countPaths(std::vector<std::vector<int>>& inputGrid) {
        grid = inputGrid;
        int m = grid.size(), n = grid[0].size();
        dp = std::vector<std::vector<int>>(m, std::vector<int>(n, -1));

        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ans = (ans + dfs(i, j)) % mod;
            }
        }
        return ans;
    }

private:
    int dfs(int i, int j) {
        if (dp[i][j] != -1)
            return dp[i][j];

        long sum = 0;
        for (auto [dr, dc] : directions) {
            int ni = i + dr, nj = j + dc;
            if (ni >= 0 && ni < grid.size() && nj >= 0 && nj < grid[0].size() && grid[ni][nj] > grid[i][j]) {
                sum = (sum + dfs(ni, nj)) % mod;
            }
        }

        return dp[i][j] = (1 + sum) % mod;
    }
};
"""
# Method 2: 
# Tabulation

from typing import List

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right

        dp = [[1] * n for _ in range(m)]  # base case: each cell contributes at least 1 path (itself)

        # Sort all cells by value to process in increasing order
        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda x: grid[x[0]][x[1]])

        for i, j in cells:
            for dr, dc in directions:
                ni, nj = i + dr, j + dc
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < grid[i][j]:
                    dp[i][j] = (dp[i][j] + dp[ni][nj]) % mod

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = (ans + dp[i][j]) % mod

        return ans

# Java Code 
"""
class Solution {
    public int countPaths(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int mod = 1_000_000_007;
        int[][] dp = new int[m][n];

        // Base case: each cell contributes at least 1 path (itself)
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                dp[i][j] = 1;

        // Sort all cells by value to process in increasing order
        List<int[]> cells = new ArrayList<>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                cells.add(new int[] {i, j});
        cells.sort((a, b) -> grid[a[0]][a[1]] - grid[b[0]][b[1]]);

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int[] cell : cells) {
            int i = cell[0], j = cell[1];
            for (int[] dir : directions) {
                int ni = i + dir[0], nj = j + dir[1];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] < grid[i][j]) {
                    dp[i][j] = (dp[i][j] + dp[ni][nj]) % mod;
                }
            }
        }

        int ans = 0;
        for (int[] row : dp)
            for (int val : row)
                ans = (ans + val) % mod;

        return ans;
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
    int countPaths(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int mod = 1e9 + 7;
        vector<vector<int>> dp(m, vector<int>(n, 1));  // base case: each cell contributes at least 1 path

        vector<pair<int, int>> cells;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                cells.emplace_back(i, j);

        sort(cells.begin(), cells.end(), [&](auto& a, auto& b) {
            return grid[a.first][a.second] < grid[b.first][b.second];
        });

        vector<pair<int, int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}};

        for (auto [i, j] : cells) {
            for (auto [dr, dc] : directions) {
                int ni = i + dr, nj = j + dc;
                if (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] < grid[i][j]) {
                    dp[i][j] = (dp[i][j] + dp[ni][nj]) % mod;
                }
            }
        }

        int ans = 0;
        for (auto& row : dp)
            for (int val : row)
                ans = (ans + val) % mod;

        return ans;
    }
};
"""