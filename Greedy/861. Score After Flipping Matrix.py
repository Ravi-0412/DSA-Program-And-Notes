# Method 1:

# Logic: 
# Optimize the total sum in two steps:

# 1) Flip all rows that start with zero;
# Why? 
# We want to keep leftmost position '1' for maximum value.
# 2) Flip all columns where the number of zeros is larger than the number of ones;
# why?
# Because for same column, bit value will same(when we convert binary to integer)
# so it's only better to flip if no of '1' > no of '0' so that we can bring more '1' 
# and this will increase the value. 

# Time : O(row * col), space: O(1)

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid) , len(grid[0])

        def flipRow(r):
            for c in range(n):
                grid[r][c] = grid[r][c] ^ 1
        
        def flipCol(c):
            for r in range(m):
                grid[r][c] = grid[r][c] ^ 1

        # flip rows if its first element is = 0
        # so that leftmost bit can become '1' for greater number
        for i in range(m):
            if grid[i][0] == 0:
                flipRow(i)
        
        # flip column from '1' if no of '0' is > no of '1'.
        for c in range(1, n):
            noOfZero = 0
            for r in range(m):
                if grid[r][c] == 0:
                    noOfZero += 1
            # if no of zero > no of '1' in this row then flip the row
            if noOfZero > m - noOfZero:
                flipCol(c)
        # Now find the ans
        ans = 0
        for i in range(m):
            for j in range(n):
                # add value of this 'bit' in binary
                # this will be equal to grid_value* (2**'no of element on right')
                ans += grid[i][j] * (1 << (n - j - 1))
        return ans

# Java
"""
public class Solution {
    public int matrixScore(int[][] grid) {
        int m = grid.length, n = grid[0].length;

        // flip rows if its first element is = 0
        // so that leftmost bit can become '1' for greater number
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                flipRow(grid, i, n);
            }
        }

        // flip column from '1' if no of '0' is > no of '1'.
        for (int c = 1; c < n; c++) {
            int noOfZero = 0;
            for (int r = 0; r < m; r++) {
                if (grid[r][c] == 0) {
                    noOfZero++;
                }
            }
            // if no of zero > no of '1' in this row then flip the row
            if (noOfZero > m - noOfZero) {
                flipCol(grid, c, m);
            }
        }

        // Now find the ans
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // add value of this 'bit' in binary
                // this will be equal to grid_value * (2 ** 'no of element on right')
                ans += grid[i][j] * (1 << (n - j - 1));
            }
        }
        return ans;
    }

    private void flipRow(int[][] grid, int r, int n) {
        for (int c = 0; c < n; c++) {
            grid[r][c] ^= 1;
        }
    }

    private void flipCol(int[][] grid, int c, int m) {
        for (int r = 0; r < m; r++) {
            grid[r][c] ^= 1;
        }
    }
}
"""

# C++
"""
class Solution {
public:
    int matrixScore(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();

        // flip rows if its first element is = 0
        // so that leftmost bit can become '1' for greater number
        for (int i = 0; i < m; i++) {
            if (grid[i][0] == 0) {
                flipRow(grid, i, n);
            }
        }

        // flip column from '1' if no of '0' is > no of '1'.
        for (int c = 1; c < n; c++) {
            int noOfZero = 0;
            for (int r = 0; r < m; r++) {
                if (grid[r][c] == 0) {
                    noOfZero++;
                }
            }
            // if no of zero > no of '1' in this row then flip the row
            if (noOfZero > m - noOfZero) {
                flipCol(grid, c, m);
            }
        }

        // Now find the ans
        int ans = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // add value of this 'bit' in binary
                // this will be equal to grid_value * (2 ** 'no of element on right')
                ans += grid[i][j] * (1 << (n - j - 1));
            }
        }
        return ans;
    }

private:
    void flipRow(vector<vector<int>>& grid, int r, int n) {
        for (int c = 0; c < n; c++) {
            grid[r][c] ^= 1;
        }
    }

    void flipCol(vector<vector<int>>& grid, int c, int m) {
        for (int r = 0; r < m; r++) {
            grid[r][c] ^= 1;
        }
    }
};
"""