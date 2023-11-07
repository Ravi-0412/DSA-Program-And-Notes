# method 1: Brute force

# Iterate towards i+1, j+1 for the lower digonal element and put them in a set. 
# Similarly iterate i-1, j-1 for the upper left diagonal element and put then in another set.
# Take absolute difference of the both the size of the sets as ans of each cell.

# time: O((m*n) * min(m, n))

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n= len(grid), len(grid[0])
        def solve(row, col):
            r, c= row -1, col -1
            top_left= set()
            while r >= 0 and c >= 0:
                top_left.add(grid[r][c])
                r-= 1
                c-= 1
            
            bottom_right= set()
            r, c= row + 1, col + 1
            while r < m and c < n:
                bottom_right.add(grid[r][c])
                r+= 1
                c+= 1
            return abs(len(top_left) - len(bottom_right))
        
        ans= [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                ans[i][j]= solve(i, j)
        return ans


# method 2: optimised one
# ty to do in O(m*n)
# links in sheet