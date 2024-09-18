# Just same as normal bfs, onky diff here we need to keep track of 'no of obstacles that we had eliminated till now'
# as well with cell indexes (i, j) .

# time: O(m*n*k) = space 

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        # Directions :(up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # BFS queue: (row, col, obstacles_eliminated, steps_taken)
        queue = deque([(0, 0, 0, 0)])
        # Visited set to track (row, col, obstacles_eliminated)
        visited = set((0, 0, 0))  # Start at (0, 0) with 0 obstacles eliminated
        
        while queue:
            i, j, eliminated, steps = queue.popleft()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    # If we reach the destination
                    if ni == m - 1 and nj == n - 1:
                        return steps + 1
                    new_eliminated = eliminated + grid[ni][nj]  # Increase obstacle count if we encounter one
                    # If within the obstacle elimination limit and we haven't visited with this exact state
                    if new_eliminated <= k and (ni, nj, new_eliminated) not in visited:
                        visited.add((ni, nj, new_eliminated))
                        queue.append((ni, nj, new_eliminated, steps + 1))
        return -1


# My dfs code which is giving wrong ans at 53/55 test case
# Why this is not working?
"""
Because when we memoize using (i, j, obstacles) it will treat same cell (i, j) with the same number of obstacle eliminations (k) 
as identical regardless of how it was approached.
Note: But we can get more better ans (shorter path) from other directions having 'same number of obstacle eliminations (k)'.
So we need to maintain the previous direction also (up, down, left, right) also through we had reached the cell (i, j).

q) But why with bfs it is working with only three parameter (i, j, obstacles_eliminated).
Reason: When BFS reaches a cell, it guarantees that it's reached with the fewest steps possible.
SO once BFS reaches a cell, it never needs to consider coming back to that cell with fewer steps.
But DFS explores paths in a depth-first manner, which means it can explore a long path before realizing that a shorter path was possible.

Correct solution below
"""
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        @lru_cache(None)
        def dfs(i, j, obstacles):
            if i == m - 1 and j == n- 1:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n or obstacles > k or (i, j, obstacles) in visited :
                return float('inf')
            visited.add((i, j, obstacles))
            ans = float('inf')
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1 and (ni, nj, obstacles) not in visited:
                    ans = min(ans, 1 + dfs(ni, nj, obstacles + 1))
                else:
                    ans = min(ans, 1 + dfs(ni, nj, obstacles))
            visited.remove((i, j, obstacles))
            return ans
                
        ans = dfs(0, 0, 0)
        return ans if ans != float('inf') else -1


# Correct solution using 'dfs' using four parameter i.e with direction as well.
# time: O(m*n*k*4) = space 
class Solution:
    def __init__(self):
        # Define the four possible movement directions: down, up, right, and left
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        self.g = grid
        self.n = len(grid)
        self.m = len(grid[0])
        
        # Memoization table dp[k][i][j][dir], for each k (remaining eliminations), position (i, j), and direction
        self.dp = [[[[None for _ in range(4)] for _ in range(self.m)] for _ in range(self.n)] for _ in range(k + 1)]
        
        # To track visited cells
        self.visited = [[False for _ in range(self.m)] for _ in range(self.n)]
        
        # Start DFS from (0, 0) with no obstacles eliminated (start with obstacles = 0)
        res = self.dfs(0, 0, 0, 0, k)
        
        # If the result is infinite, there is no valid path
        if res == float('inf'):
            return -1
        return res
    
    def dfs(self, i: int, j: int, obstacles: int, dir: int, k: int) -> int:
        # If we've reached the bottom-right corner, return 0 (no more steps needed)
        if i == self.n - 1 and j == self.m - 1:
            return 0
        
        # If we've exceeded the number of allowed eliminations, return infinity
        if obstacles > k:
            return float('inf')
        
        # If we've already calculated this state, return the memoized result
        if self.dp[obstacles][i][j][dir] is not None:
            return self.dp[obstacles][i][j][dir]
        
        # Mark the current cell as visited
        self.visited[i][j] = True
        ans = float('inf')
        for i1 in range(4):
            nx, ny = i + self.directions[i1][0], j + self.directions[i1][1]
            
            # Check if the new coordinates are within bounds and if the cell is not visited
            if 0 <= nx < self.n and 0 <= ny < self.m and not self.visited[nx][ny]:
                # If moving to an obstacle, increase the obstacle elimination count
                new_obstacles = obstacles + self.g[nx][ny]
                # Recursively call DFS for the next cell and calculate the minimum steps
                ans = min(ans, 1 + self.dfs(nx, ny, new_obstacles, i1, k))
        
        # Unmark the current cell (backtrack)
        self.visited[i][j] = False
        
        # Memoize the result for the current state
        self.dp[obstacles][i][j][dir] = ans
        
        return ans

        
