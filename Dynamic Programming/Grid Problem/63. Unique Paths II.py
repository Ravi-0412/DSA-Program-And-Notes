# Recursive:
# Note: Always do like this only(False condition + out of bound cases all together first then base cases).
# write the code for normal Q(without obstacle) just treat 'obstacle' in invalid base case in any Q .
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.helper(0,0,obstacleGrid)
    
    def helper(self,r,c,grid):
        if r>= len(grid) or c>= len(grid[0]) or grid[r][c]==1:  # write all the false cases together like we used to do in graph
                                                                # this help you to avoid a lot of checking condition further
            return 0
        if r== len(grid)- 1 and c== len(grid[0])-1 :  #if reaches the end point 
            return 1
        return self.helper(r+1,c,grid) + self.helper(r,c+1,grid)

# Java Code 
"""
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        return helper(0, 0, obstacleGrid);
    }

    private int helper(int r, int c, int[][] grid) {
        if (r >= grid.length || c >= grid[0].length || grid[r][c] == 1)  // write all the false cases together like we used to do in graph
                                                                          // this help you to avoid a lot of checking condition further
            return 0;
        if (r == grid.length - 1 && c == grid[0].length - 1)  // if reaches the end point
            return 1;
        return helper(r + 1, c, grid) + helper(r, c + 1, grid);
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int uniquePathsWithObstacles(std::vector<std::vector<int>>& obstacleGrid) {
        return helper(0, 0, obstacleGrid);
    }

private:
    int helper(int r, int c, const std::vector<std::vector<int>>& grid) {
        if (r >= grid.size() || c >= grid[0].size() || grid[r][c] == 1)  // write all the false cases together like we used to do in graph
                                                                          // this help you to avoid a lot of checking condition further
            return 0;
        if (r == grid.size() - 1 && c == grid[0].size() - 1)  // if reaches the end point
            return 1;
        return helper(r + 1, c, grid) + helper(r, c + 1, grid);
    }
};
"""

# memoisation:
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]== 1:   # if there is obstacle at destination
            return 0
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        dp= [[-1 for j in range(n)] for i in range(m)]
        return self.helper(0,0,obstacleGrid,dp)
    
    def helper(self,r,c,grid,dp):
        if r>= len(grid) or c>= len(grid[0]) or grid[r][c]==1:  # write all the false cases together like we used to do in graph
                                                                # this help you to avoid a lot of checking condition further
            return 0
        if r== len(grid)-1 and c== len(grid[0])-1 :  #if reaches the end point 
            return 1
        if dp[r][c]!= -1:
            return dp[r][c]
        dp[r][c]= self.helper(r+1,c,grid,dp) + self.helper(r,c+1,grid,dp)
        return dp[r][c]

# Java Code 
"""
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if (obstacleGrid[obstacleGrid.length - 1][obstacleGrid[0].length - 1] == 1)  // if there is obstacle at destination
            return 0;
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];
        for (int[] row : dp)
            java.util.Arrays.fill(row, -1);
        return helper(0, 0, obstacleGrid, dp);
    }

    private int helper(int r, int c, int[][] grid, int[][] dp) {
        if (r >= grid.length || c >= grid[0].length || grid[r][c] == 1)  // write all the false cases together like we used to do in graph
                                                                          // this help you to avoid a lot of checking condition further
            return 0;
        if (r == grid.length - 1 && c == grid[0].length - 1)  // if reaches the end point
            return 1;
        if (dp[r][c] != -1)
            return dp[r][c];
        dp[r][c] = helper(r + 1, c, grid, dp) + helper(r, c + 1, grid, dp);
        return dp[r][c];
    }
}
"""

# C++ Code 
"""
class Solution {
public:
    int uniquePathsWithObstacles(std::vector<std::vector<int>>& obstacleGrid) {
        if (obstacleGrid.back().back() == 1)  // if there is obstacle at destination
            return 0;
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        std::vector<std::vector<int>> dp(m, std::vector<int>(n, -1));
        return helper(0, 0, obstacleGrid, dp);
    }

private:
    int helper(int r, int c, const std::vector<std::vector<int>>& grid, std::vector<std::vector<int>>& dp) {
        if (r >= grid.size() || c >= grid[0].size() || grid[r][c] == 1)  // write all the false cases together like we used to do in graph
                                                                          // this help you to avoid a lot of checking condition further
            return 0;
        if (r == grid.size() - 1 && c == grid[0].size() - 1)  // if reaches the end point
            return 1;
        if (dp[r][c] != -1)
            return dp[r][c];
        dp[r][c] = helper(r + 1, c, grid, dp) + helper(r, c + 1, grid, dp);
        return dp[r][c];
    }
};
"""
# tabulation: Bottom up
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        dp= [[0 for j in range(n)] for i in range(m)]
        # initialise with proper base cases
        # first we have to check at (m-1,n-1) then only we can initialise the base case further
        if obstacleGrid[m-1][n-1]!= 1:
            dp[m-1][n-1]= 1

        # initialisng the last row.after reaching the last row,paths will depend on the value of curr_row and next_col 
        # i.e dp[m-1][i-1] if no obstacle at that cell.
        for i in range(n-2,-1,-1):
            if obstacleGrid[m-1][i]!= 1:
                dp[m-1][i]= dp[m-1][i+1]

        # initialisng the last col. after reaching the last col, 
        # paths will depend on the curr col and next_row val if no obstacle at that cell
        for i in range(m-2,-1,-1):
            if obstacleGrid[i][n-1]!= 1:
                dp[i][n-1]= dp[i+1][n-1]
        
        # now run loop as usual and keep updating if no obstacles is there.
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j]!= 1:  # if not obstacle
                    dp[i][j]= dp[i+1][j] + dp[i][j+1]
        return dp[0][0]


# Java Code 
"""
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];

        // initialise with proper base cases
        // first we have to check at (m-1,n-1) then only we can initialise the base case further
        if (obstacleGrid[m - 1][n - 1] != 1)
            dp[m - 1][n - 1] = 1;

        // initialisng the last row.after reaching the last row,paths will depend on the value of curr_row and next_col 
        // i.e dp[m-1][i-1] if no obstacle at that cell.
        for (int i = n - 2; i >= 0; i--) {
            if (obstacleGrid[m - 1][i] != 1)
                dp[m - 1][i] = dp[m - 1][i + 1];
        }

        // initialisng the last col. after reaching the last col, 
        // paths will depend on the curr col and next_row val if no obstacle at that cell
        for (int i = m - 2; i >= 0; i--) {
            if (obstacleGrid[i][n - 1] != 1)
                dp[i][n - 1] = dp[i + 1][n - 1];
        }

        // now run loop as usual and keep updating if no obstacles is there.
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                if (obstacleGrid[i][j] != 1)
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1];
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
    int uniquePathsWithObstacles(std::vector<std::vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        std::vector<std::vector<int>> dp(m, std::vector<int>(n, 0));

        // initialise with proper base cases
        // first we have to check at (m-1,n-1) then only we can initialise the base case further
        if (obstacleGrid[m - 1][n - 1] != 1)
            dp[m - 1][n - 1] = 1;

        // initialisng the last row.after reaching the last row,paths will depend on the value of curr_row and next_col 
        // i.e dp[m-1][i-1] if no obstacle at that cell.
        for (int i = n - 2; i >= 0; --i) {
            if (obstacleGrid[m - 1][i] != 1)
                dp[m - 1][i] = dp[m - 1][i + 1];
        }

        // initialisng the last col. after reaching the last col, 
        // paths will depend on the curr col and next_row val if no obstacle at that cell
        for (int i = m - 2; i >= 0; --i) {
            if (obstacleGrid[i][n - 1] != 1)
                dp[i][n - 1] = dp[i + 1][n - 1];
        }

        // now run loop as usual and keep updating if no obstacles is there.
        for (int i = m - 2; i >= 0; --i) {
            for (int j = n - 2; j >= 0; --j) {
                if (obstacleGrid[i][j] != 1)
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1];
            }
        }

        return dp[0][0];
    }
};
"""

# optimising space complexity to O(n).
# Find ans row wise from last row




# oppsite way
# from (m-1,n-1) to (0,0)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m,n= len(obstacleGrid), len(obstacleGrid[0])
        dp= [[0 for j in range(n)] for i in range(m)]
        # initialise with proper base cases
        # first we have to check at (m-1,n-1) then only we can initialise the base case further
        if obstacleGrid[m-1][n-1]!= 1:
            dp[m-1][n-1]= 1
        print(dp)
        # initialisng the last row.after reaching the last row,paths will depend on the value of curr_row and pre_col val  
        # and pre row i.e dp[m-1][i-1] if no obstacle at that cell.
        for i in range(n-2,-1,-1):
            if obstacleGrid[m-1][i]!= 1:
                dp[m-1][i]= dp[m-1][i+1]
        print(dp)
        # initialisng the last col. after reaching the last col, paths will depend on the curr col and pre row val( dp[i-1][0]) if no obstacle at that cell
        for i in range(m-2,-1,-1):
            if obstacleGrid[i][n-1]!= 1:
                dp[i][n-1]= dp[i+1][n-1]
        print(dp)  
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if obstacleGrid[i][j]!= 1:  # if not obstacle
                    dp[i][j]= dp[i+1][j] + dp[i][j+1]
        return dp[0][0]


# Java Code 
"""
import java.util.Arrays;

public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length, n = obstacleGrid[0].length;
        int[][] dp = new int[m][n];

        // initialise with proper base cases
        // first we have to check at (m-1,n-1) then only we can initialise the base case further
        if (obstacleGrid[m - 1][n - 1] != 1)
            dp[m - 1][n - 1] = 1;

        printGrid(dp);

        // initialisng the last row.after reaching the last row,paths will depend on the value of curr_row and pre_col val  
        // and pre row i.e dp[m-1][i-1] if no obstacle at that cell.
        for (int i = n - 2; i >= 0; i--) {
            if (obstacleGrid[m - 1][i] != 1)
                dp[m - 1][i] = dp[m - 1][i + 1];
        }

        printGrid(dp);

        // initialisng the last col. after reaching the last col, paths will depend on the curr col and pre row val( dp[i-1][0]) if no obstacle at that cell
        for (int i = m - 2; i >= 0; i--) {
            if (obstacleGrid[i][n - 1] != 1)
                dp[i][n - 1] = dp[i + 1][n - 1];
        }

        printGrid(dp);

        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--) {
                if (obstacleGrid[i][j] != 1)  // if not obstacle
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1];
            }
        }

        return dp[0][0];
    }

    private void printGrid(int[][] grid) {
        for (int[] row : grid)
            System.out.println(Arrays.toString(row));
        System.out.println();
    }
}
"""

# C++ Code 
"""
#include <vector>
#include <iostream>

class Solution {
public:
    int uniquePathsWithObstacles(std::vector<std::vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        std::vector<std::vector<int>> dp(m, std::vector<int>(n, 0));

        // initialise with proper base cases
        // first we have to check at (m-1,n-1) then only we can initialise the base case further
        if (obstacleGrid[m - 1][n - 1] != 1)
            dp[m - 1][n - 1] = 1;

        print(dp);

        // initialisng the last row.after reaching the last row,paths will depend on the value of curr_row and pre_col val  
        // and pre row i.e dp[m-1][i-1] if no obstacle at that cell.
        for (int i = n - 2; i >= 0; --i) {
            if (obstacleGrid[m - 1][i] != 1)
                dp[m - 1][i] = dp[m - 1][i + 1];
        }

        print(dp);

        // initialisng the last col. after reaching the last col, paths will depend on the curr col and pre row val( dp[i-1][0]) if no obstacle at that cell
        for (int i = m - 2; i >= 0; --i) {
            if (obstacleGrid[i][n - 1] != 1)
                dp[i][n - 1] = dp[i + 1][n - 1];
        }

        print(dp);

        for (int i = m - 2; i >= 0; --i) {
            for (int j = n - 2; j >= 0; --j) {
                if (obstacleGrid[i][j] != 1)  // if not obstacle
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1];
            }
        }

        return dp[0][0];
    }

private:
    void print(const std::vector<std::vector<int>>& grid) {
        for (const auto& row : grid) {
            for (int val : row)
                std::cout << val << " ";
            std::cout << "\n";
        }
        std::cout << std::endl;
    }
};
"""