# method 1: Recursion
# just same as Q n: '62' 
# for every cell minimum path = current cell val + min(path_sum of its left adjacent, path_sum of its upper adjacent)
# if you go bottom-up in recursive.

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        return self.helper(m-1,n-1,grid)  # going from 'm-1,n-1' to '0,0'
    
    def helper(self,row,col,grid):
        # when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if row == 0 and col== 0:
            return grid[row][col]
        if col == 0: # we can only move vertically up
            return grid[row][col] +  self.helper(row-1, col, grid)
        if row == 0:
            return grid[row][col] +  self.helper(row, col-1, grid)
        return grid[row][col] +  min(self.helper(row-1,col,grid), self.helper(row,col-1,grid))
    
# Java Code 
"""
public class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        return helper(m - 1, n - 1, grid);  // going from 'm-1,n-1' to '0,0'
    }

    private int helper(int row, int col, int[][] grid) {
        // when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if (row == 0 && col == 0)
            return grid[row][col];
        if (col == 0) // we can only move vertically up
            return grid[row][col] + helper(row - 1, col, grid);
        if (row == 0)
            return grid[row][col] + helper(row, col - 1, grid);
        return grid[row][col] + Math.min(helper(row - 1, col, grid), helper(row, col - 1, grid));
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int minPathSum(std::vector<std::vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        return helper(m - 1, n - 1, grid);  // going from 'm-1,n-1' to '0,0'
    }

private:
    int helper(int row, int col, const std::vector<std::vector<int>>& grid) {
        // when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if (row == 0 && col == 0)
            return grid[row][col];
        if (col == 0) // we can only move vertically up
            return grid[row][col] + helper(row - 1, col, grid);
        if (row == 0)
            return grid[row][col] + helper(row, col - 1, grid);
        return grid[row][col] + std::min(helper(row - 1, col, grid), helper(row, col - 1, grid));
    }
};
"""

# my mistakes VVI:
"""
if row and col will go out of bound then left or up will be '0' then it will return '0' since we are returning minimum value.

say you are at (0, 3) , from here you can go left and but can't go up.
for from left , you will get : sum from index '3 to 0' in row '0'
And from up you will get '0'.
Now since it is returning minimum , it will return '0' instead of sum from index '3 to 0' in row '0'.

That's why we have to stop before reaching the invalid case. SO did like above one

OR

Better one: return very big value like 'float('inf)' then it will give correct ans.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n= len(grid), len(grid[0])
        return self.helper(m-1,n-1,grid)  # going from 'm-1,n-1' to '0,0'
    
    def helper(self,row,col,grid):
        # when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if row ==0 and col== 0:
            return grid[row][col]
        if row < 0 or col < 0:
            # return 0   # will give wrong ans. less than required
            return float('inf')   # will give correct ans
        return grid[row][col] +  min(self.helper(row-1,col,grid), self.helper(row,col-1,grid))

# Java Code 
"""
public class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        return helper(m - 1, n - 1, grid);  // going from 'm-1,n-1' to '0,0'
    }

    private int helper(int row, int col, int[][] grid) {
        // when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if (row == 0 && col == 0)
            return grid[row][col];
        if (row < 0 || col < 0) {
            // return 0   // will give wrong ans. less than required
            return Integer.MAX_VALUE;   // will give correct ans
        }
        return grid[row][col] + Math.min(helper(row - 1, col, grid), helper(row, col - 1, grid));
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int minPathSum(std::vector<std::vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        return helper(m - 1, n - 1, grid);  // going from 'm-1,n-1' to '0,0'
    }

private:
    int helper(int row, int col, const std::vector<std::vector<int>>& grid) {
        // when you have reached the 0th row, then you have only one choice i.e from curr col move to 0th col by adding all the ele bw that
        if (row == 0 && col == 0)
            return grid[row][col];
        if (row < 0 || col < 0) {
            // return 0   // will give wrong ans. less than required
            return INT_MAX;   // will give correct ans
        }
        return grid[row][col] + std::min(helper(row - 1, col, grid), helper(row, col - 1, grid));
    }
};
"""

# My bottom- up dp solution.
# Just above logic.
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[m-1][n-1] = grid[m-1][n -1]
        # fill the ans for last row
        for c in range(n - 2, -1, -1):
            dp[m- 1][c] = grid[m-1][c] + dp[m-1][c + 1]   # sum of all elements on its right
        # fill the ans for last col 
        for r in range(m - 2, -1, -1):
            dp[r][n-1] = grid[r][n -1] + dp[r + 1][n -1]  # sum of all ele on  its down
        # Now start filling other rows and cols taking help of these values
        for r in range(m - 2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = grid[r][c] +  min(dp[r + 1][c] , dp[r][c + 1])
        return dp[0][0]
    
# Java Code 
"""
public class Solution {
    public int minPathSum(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        dp[m - 1][n - 1] = grid[m - 1][n - 1];

        // fill the ans for last row
        for (int c = n - 2; c >= 0; c--) {
            dp[m - 1][c] = grid[m - 1][c] + dp[m - 1][c + 1];  // sum of all elements on its right
        }

        // fill the ans for last col 
        for (int r = m - 2; r >= 0; r--) {
            dp[r][n - 1] = grid[r][n - 1] + dp[r + 1][n - 1];  // sum of all ele on  its down
        }

        // Now start filling other rows and cols taking help of these values
        for (int r = m - 2; r >= 0; r--) {
            for (int c = n - 2; c >= 0; c--) {
                dp[r][c] = grid[r][c] + Math.min(dp[r + 1][c], dp[r][c + 1]);
            }
        }

        return dp[0][0];
    }
}
"""
# C++ Code 
"""
class Solution {
public:
    int minPathSum(std::vector<std::vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        std::vector<std::vector<int>> dp(m, std::vector<int>(n, 0));
        dp[m - 1][n - 1] = grid[m - 1][n - 1];

        // fill the ans for last row
        for (int c = n - 2; c >= 0; --c) {
            dp[m - 1][c] = grid[m - 1][c] + dp[m - 1][c + 1];
        }

        // fill the ans for last col 
        for (int r = m - 2; r >= 0; --r) {
            dp[r][n - 1] = grid[r][n - 1] + dp[r + 1][n - 1];
        }

        // Now start filling other rows and cols taking help of these values
        for (int r = m - 2; r >= 0; --r) {
            for (int c = n - 2; c >= 0; --c) {
                dp[r][c] = grid[r][c] + std::min(dp[r + 1][c], dp[r][c + 1]);
            }
        }

        return dp[0][0];
    }
};
"""

# similar q asked in interview
# 1) https://www.geeksforgeeks.org/maximum-sum-path-in-a-matrix-from-top-left-to-bottom-right/
# Instead on minimum we have to find maximum

