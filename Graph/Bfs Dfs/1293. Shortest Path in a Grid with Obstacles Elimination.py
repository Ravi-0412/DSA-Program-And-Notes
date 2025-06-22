# Method 1: 

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

# Java Code 
"""
import java.util.*;

public class Solution {
    public int shortestPath(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        if (m == 1 && n == 1) return 0;

        // Directions :(up, down, left, right)
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        // BFS queue: (row, col, obstacles_eliminated, steps_taken)
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, 0, 0});
        // Visited set to track (row, col, obstacles_eliminated)
        Set<String> visited = new HashSet<>();
        visited.add("0,0,0");  // Start at (0, 0) with 0 obstacles eliminated

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int i = curr[0], j = curr[1], eliminated = curr[2], steps = curr[3];

            for (int[] dir : directions) {
                int ni = i + dir[0], nj = j + dir[1];
                if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                    if (ni == m - 1 && nj == n - 1)
                        return steps + 1;

                    int newEliminated = eliminated + grid[ni][nj];
                    String state = ni + "," + nj + "," + newEliminated;

                    if (newEliminated <= k && !visited.contains(state)) {
                        visited.add(state);
                        queue.offer(new int[]{ni, nj, newEliminated, steps + 1});
                    }
                }
            }
        }

        return -1;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <string>

class Solution {
public:
    int shortestPath(std::vector<std::vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        if (m == 1 && n == 1) return 0;

        // Directions :(up, down, left, right)
        std::vector<std::pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        // BFS queue: (row, col, obstacles_eliminated, steps_taken)
        std::queue<std::tuple<int, int, int, int>> queue;
        queue.emplace(0, 0, 0, 0);
        // Visited set to track (row, col, obstacles_eliminated)
        std::unordered_set<std::string> visited;
        visited.insert("0,0,0");  // Start at (0, 0) with 0 obstacles eliminated

        while (!queue.empty()) {
            auto [i, j, eliminated, steps] = queue.front();
            queue.pop();

            for (auto [di, dj] : directions) {
                int ni = i + di, nj = j + dj;
                if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
                    if (ni == m - 1 && nj == n - 1)
                        return steps + 1;

                    int newEliminated = eliminated + grid[ni][nj];
                    std::string state = std::to_string(ni) + "," + std::to_string(nj) + "," + std::to_string(newEliminated);

                    if (newEliminated <= k && !visited.count(state)) {
                        visited.insert(state);
                        queue.emplace(ni, nj, newEliminated, steps + 1);
                    }
                }
            }
        }

        return -1;
    }
};
"""
# Method 2: 
# DFS

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

# Java Code 
"""
import java.util.*;

public class Solution {
    int[][] grid;
    int m, n, k;
    int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    Set<String> visited;

    public int shortestPath(int[][] grid, int k) {
        this.grid = grid;
        this.k = k;
        m = grid.length;
        n = grid[0].length;
        visited = new HashSet<>();

        int ans = dfs(0, 0, 0);
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    private int dfs(int i, int j, int obstacles) {
        if (i == m - 1 && j == n - 1)
            return 0;
        if (i < 0 || i >= m || j < 0 || j >= n || obstacles > k)
            return Integer.MAX_VALUE;

        String state = i + "," + j + "," + obstacles;
        if (visited.contains(state))
            return Integer.MAX_VALUE;

        visited.add(state);
        int ans = Integer.MAX_VALUE;

        for (int[] dir : directions) {
            int ni = i + dir[0], nj = j + dir[1];
            int newObstacles = grid[ni][nj] == 1 ? obstacles + 1 : obstacles;
            int path = dfs(ni, nj, newObstacles);
            if (path != Integer.MAX_VALUE)
                ans = Math.min(ans, 1 + path);
        }

        visited.remove(state);
        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
#include <set>
#include <string>
#include <climits>

class Solution {
    std::vector<std::vector<int>> grid;
    int m, n, k;
    std::set<std::string> visited;
    std::vector<std::pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

public:
    int shortestPath(std::vector<std::vector<int>>& inputGrid, int maxK) {
        grid = inputGrid;
        k = maxK;
        m = grid.size();
        n = grid[0].size();
        int ans = dfs(0, 0, 0);
        return ans == INT_MAX ? -1 : ans;
    }

private:
    int dfs(int i, int j, int obstacles) {
        if (i == m - 1 && j == n - 1)
            return 0;
        if (i < 0 || i >= m || j < 0 || j >= n || obstacles > k)
            return INT_MAX;

        std::string state = std::to_string(i) + "," + std::to_string(j) + "," + std::to_string(obstacles);
        if (visited.count(state))
            return INT_MAX;

        visited.insert(state);
        int ans = INT_MAX;

        for (auto [di, dj] : directions) {
            int ni = i + di, nj = j + dj;
            int newObstacles = (ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 1) ? obstacles + 1 : obstacles;
            int path = dfs(ni, nj, newObstacles);
            if (path != INT_MAX)
                ans = std::min(ans, 1 + path);
        }

        visited.erase(state);
        return ans;
    }
};
"""
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

# Java Code 
"""
public class Solution {
    // Define the four possible movement directions: down, up, right, and left
    int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int[][] grid;
    int n, m;
    boolean[][] visited;
    Integer[][][][] dp;

    public int shortestPath(int[][] grid, int k) {
        this.grid = grid;
        this.n = grid.length;
        this.m = grid[0].length;

        // Memoization table dp[k][i][j][dir], for each k (remaining eliminations), position (i, j), and direction
        dp = new Integer[k + 1][n][m][4];

        // To track visited cells
        visited = new boolean[n][m];

        // Start DFS from (0, 0) with no obstacles eliminated (start with obstacles = 0)
        int res = dfs(0, 0, 0, 0, k);

        // If the result is infinite, there is no valid path
        return res == Integer.MAX_VALUE ? -1 : res;
    }

    private int dfs(int i, int j, int obstacles, int dir, int k) {
        // If we've reached the bottom-right corner, return 0 (no more steps needed)
        if (i == n - 1 && j == m - 1)
            return 0;

        // If we've exceeded the number of allowed eliminations, return infinity
        if (obstacles > k)
            return Integer.MAX_VALUE;

        // If we've already calculated this state, return the memoized result
        if (dp[obstacles][i][j][dir] != null)
            return dp[obstacles][i][j][dir];

        // Mark the current cell as visited
        visited[i][j] = true;
        int ans = Integer.MAX_VALUE;

        for (int d = 0; d < 4; d++) {
            int ni = i + directions[d][0];
            int nj = j + directions[d][1];

            // Check if the new coordinates are within bounds and if the cell is not visited
            if (ni >= 0 && ni < n && nj >= 0 && nj < m && !visited[ni][nj]) {
                // If moving to an obstacle, increase the obstacle elimination count
                int newObs = obstacles + grid[ni][nj];
                // Recursively call DFS for the next cell and calculate the minimum steps
                int next = dfs(ni, nj, newObs, d, k);
                if (next != Integer.MAX_VALUE)
                    ans = Math.min(ans, 1 + next);
            }
        }

        // Unmark the current cell (backtrack)
        visited[i][j] = false;

        // Memoize the result for the current state
        dp[obstacles][i][j][dir] = ans;
        return ans;
    }
}
"""

# C++ Code 
"""
class Solution {
    // Define the four possible movement directions: down, up, right, and left
    std::vector<std::pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    std::vector<std::vector<int>> grid;
    std::vector<std::vector<bool>> visited;
    std::vector<std::vector<std::vector<std::vector<int>>>> dp;
    int n, m;

public:
    int shortestPath(std::vector<std::vector<int>>& inputGrid, int k) {
        grid = inputGrid;
        n = grid.size();
        m = grid[0].size();

        // Memoization table dp[k][i][j][dir], for each k (remaining eliminations), position (i, j), and direction
        dp = std::vector(k + 1, std::vector(n, std::vector(m, std::vector<int>(4, -1))));

        // To track visited cells
        visited.assign(n, std::vector<bool>(m, false));

        // Start DFS from (0, 0) with no obstacles eliminated (start with obstacles = 0)
        int res = dfs(0, 0, 0, 0, k);

        // If the result is infinite, there is no valid path
        return res == INT_MAX ? -1 : res;
    }

private:
    int dfs(int i, int j, int obstacles, int dir, int k) {
        // If we've reached the bottom-right corner, return 0 (no more steps needed)
        if (i == n - 1 && j == m - 1)
            return 0;

        // If we've exceeded the number of allowed eliminations, return infinity
        if (obstacles > k)
            return INT_MAX;

        // If we've already calculated this state, return the memoized result
        if (dp[obstacles][i][j][dir] != -1)
            return dp[obstacles][i][j][dir];

        // Mark the current cell as visited
        visited[i][j] = true;
        int ans = INT_MAX;

        for (int d = 0; d < 4; ++d) {
            int ni = i + directions[d].first;
            int nj = j + directions[d].second;

            // Check if the new coordinates are within bounds and if the cell is not visited
            if (ni >= 0 && ni < n && nj >= 0 && nj < m && !visited[ni][nj]) {
                // If moving to an obstacle, increase the obstacle elimination count
                int newObs = obstacles + grid[ni][nj];
                // Recursively call DFS for the next cell and calculate the minimum steps
                int next = dfs(ni, nj, newObs, d, k);
                if (next != INT_MAX)
                    ans = std::min(ans, 1 + next);
            }
        }

        // Unmark the current cell (backtrack)
        visited[i][j] = false;

        // Memoize the result for the current state
        return dp[obstacles][i][j][dir] = ans;
    }
};
"""