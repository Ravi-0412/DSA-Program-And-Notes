# Just same as normal bfs, onky diff here we need to keep track of 'no of obstacles that we had eliminated till now'
# as well with cell indexes (i, j) .
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
        
