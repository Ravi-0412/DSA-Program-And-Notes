# Time = space = O(m*n)

# Consider each cell as apex and see of how much height of pyramid  we can form.
# for this cell below/above must be '1' and left, right should also form a pyramid.
# Recurrence relation,
# f(i, j) = 1 + min(f(i+1, j-1), f(i+1, j+1))
# where f(i, j) is the height of largest pyramid, whose apex is at i,j.

# height 'h' will contribue 'h-1' to the ans because cell that will come below/above apex will also contribute to the ans.

# Explanation in note, page : 182

class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        
        # Will count no of reverse pyramid in given 'grid'.
        def count(grid):
            ans = 0
            for i in range(1, m):
                for j in range(1, n-1):  # last column can't be apex 
                    if grid[i][j] and grid[i-1][j]:
                        # find the height of pyramid that we can get if (i, j) is apex
                        grid[i][j] = min(grid[i-1][j-1] , grid[i-1][j + 1]) + 1  # min height from (left, right) + 1
                        ans += grid[i][j] - 1   # pyramid of height 'h' will contribute 'h-1' to the ans.
            return ans

        m , n = len(grid) , len(grid[0])
        reversed_grid = []
        for i in range(m -1, -1, -1):
            reversed_grid.append(grid[i][:])
        ans =  count(grid)  # will count the ans for reverse pyramid
        ans += count(reversed_grid)  # will count the ans for simple pyramid
        return ans


# Do by prefix Sum method later and other approaches. link in sheet
# https://leetcode.com/problems/count-fertile-pyramids-in-a-land/solutions/1606479/easy-prefix-sum-accepted-intuition-comment-without-dp/