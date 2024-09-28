# Time = space = O(m*n)

# Consider each cell as apex and see of how much height of pyramid  we can form.
# For reverse grid: 
# for this cell , above cell must be '1' &  (left, right) of pre cell should also form a pyramid 
# if we go top down i.e from (0, 0) to (m, n).
# Recurrence relation,
# f(i, j) = 1 + min(f(i - 1, j-1), f(i- 1, j+1)) if grid[i][j] = 1 else 0.
# where f(i, j) is the height of largest pyramid, whose apex is at i,j.

# height 'h' will contribue 'h-1' to the ans because the cell that will come below/above apex will also contribute to the ans.

# Explanation in note, page : 182

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
        # Will count no of reverse pyramid in given 'grid'.
        def count(grid):
            ans = 0
            # apex can't be in 0th row
            for i in range(1, m):
                # apex can't be in last column
                for j in range(1, n-1):  
                    if grid[i][j] and grid[i-1][j]:
                        # find the height of pyramid that we can get if (i, j) is apex
                        grid[i][j] = min(grid[i-1][j-1] , grid[i-1][j + 1]) + 1  # min height from (left, right) + 1
                        ans += grid[i][j] - 1   # pyramid of height 'h' will contribute 'h-1' to the ans.
            return ans

        m , n = len(grid) , len(grid[0])
        reversed_grid = []
        for i in range(m -1, -1, -1):
            reversed_grid.append(grid[i].copy())   # deep copy
        ans =  count(grid)  # will count the ans for reverse pyramid
        ans += count(reversed_grid)  # will count the ans for simple pyramid
        return ans

# Java
"""
class Solution {
    public int countPyramids(int[][] grid) {
        int[][] inverseGrid = inverse(grid);
         return helper(grid) + helper(inverseGrid);
    }
    
    public int helper(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int ans = 0;
        for(int i = 1; i < m; i++) {
            for(int j = 1; j < n - 1; j ++) {
                if(grid[i][j] > 0) {
                    grid[i][j] = Math.min(Math.min(grid[i-1][j], grid[i-1][j-1]), grid[i-1][j + 1]) + 1;
                    ans += grid[i][j] - 1;
                }
            }
        }
        return ans;
    }
    
    public int[][] inverse(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] g = new int[m][n];
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                g[i][j] = grid[m - i- 1][j];
            }
        }
        return g;
    }
}
"""

# Note: in java if you will do like this then won't work.
"""
After updating the grid for one type of pyramid (regular or inverted), you are modifying the grid itself. 
This alteration affects subsequent computations, leading to an incorrect answer.
"""

"""
public int countPyramids(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        // Create a reversed grid for counting inverted pyramids
        int[][] reversedGrid = new int[m][n];
        for (int i = 0; i < m; i++) {
            reversedGrid[i] = grid[m - 1 - i].clone();
        }

        // Count regular pyramids
        int ans = count(grid, m, n);
        // Count inverted pyramids
        ans += count(reversedGrid, m, n);

        return ans;
    }
}
"""

# if you want to do 'using' clone the you have to use two separate 2-D arrays like below.
# But correct one is better one as that saves one extra 2-D array.
"""
public int countPyramids(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        
        // Create a deep copy of the grid for counting inverted pyramids
        int[][] reversedGrid = new int[m][n];
        for (int i = 0; i < m; i++) {
            reversedGrid[i] = grid[m - 1 - i].clone();
        }

        // Create another deep copy of the original grid to preserve it
        int[][] originalGrid = new int[m][n];
        for (int i = 0; i < m; i++) {
            originalGrid[i] = grid[i].clone();
        }

        // Count regular pyramids using the original grid
        int ans = count(originalGrid, m, n);
        // Count inverted pyramids using the reversed grid
        ans += count(reversedGrid, m, n);

        return ans;
    }
"""

# Do by prefix Sum method later and other approaches. link in sheet
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/solutions/1606479/easy-prefix-sum-accepted-intuition-comment-without-dp/
