# Logic: 
# Optimize the total sum in two steps:

# 1) Flip all rows that start with zero;
# 2) Flip all columns where the number of zeros is larger than the number of ones;

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
        