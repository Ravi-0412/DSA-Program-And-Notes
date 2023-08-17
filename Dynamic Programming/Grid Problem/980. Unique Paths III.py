# Just normal way we do
# time: O(m*n) as problem will overlap also and we can use dp to memoise.

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m ,n = len(grid), len(grid[0])
        self.walkableCell = 1   # including the starting cell . without self it's not acting as global varibale
        start_x, start_y = None, None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    self.walkableCell += 1
                if grid[i][j] == 1:
                    start_x, start_y = i, j

        directions =[[0, 1], [0, -1], [-1, 0],[1, 0]]

        def dfs(r, c):
            if r >= m or r < 0 or c >= n or c < 0 or grid[r][c] == -1:
                return 0
            if grid[r][c] == 2:
                return self.walkableCell == 0
            ans = 0
            temp = grid[r][c]
            grid[r][c] = -1   # marking visited
            self.walkableCell -= 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                ans += dfs(nr, nc)
            self.walkableCell += 1
            grid[r][c] = temp
            return ans

        return dfs(start_x, start_y)