# Method 1: 

# Logic: Have to find path as far as from any of the thieves.

# Combination of: "286 walls and gates " + "778. Swim in Rising Water".

# 1) find the minimum distance of all grid from any of the thieves using multisource bfs.
# 2) find the minimum distance using similar approach as "778. Swim in Rising Water".

# understand and visualise properly.

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        # First find the minimum distance of each cell from any of the thieves using multisource bfs

        def calMinimumDist():
            q = deque()
            min_dist = {}
            for r in range(n):
                for c in range(n):
                    if grid[r][c] == 1:
                        q.append([r, c, 0])     # [i, j, distance_from_any_thieves]
                        min_dist[(r, c )] = 0
            
            while q:
                r, c , dist = q.popleft()
                for dr, dc in directions:
                    if 0 <= (r + dr) < n and 0 <= (c + dc) < n and (r + dr, c + dc) not in min_dist:
                        r1, c1 = r + dr, c + dc
                        min_dist[(r1, c1)] = dist + 1
                        q.append([r1, c1, dist + 1])
            return min_dist
        
        min_dist = calMinimumDist()

        # Now find the minimum distance to go from (0, 0) to (n - 1, n - 1)
        # Just similar as : "778. Swim in Rising Water".
        # Only difference here while adding we will take the minimum and 
        # out of all those minimum we will take maximum. so we will use maxHeap instead of minHeap.

        # in "778. Swim in Rising Water", while adding we were taking maximum and out of all those
        # maximum, we will take minimum for ans. so we wil use 'minHeap'

        visited = set()
        visited.add((0, 0))
        maxHeap = [[-1* min_dist[(0, 0)], 0, 0]]   # [min_dist, r, c]
        while maxHeap:
            dist, r, c = heapq.heappop(maxHeap)
            dist = -1* dist
            if r == n-1 and c == n-1:
                return dist
            for dr, dc in directions:
                if 0 <= (r + dr) < n and 0 <= (c + dc) < n and (r + dr, c + dc) not in visited:
                    r1, c1 = r + dr, c + dc
                    min_distance_to_reach_grid = min(dist, min_dist[(r1, c1)])
                    heapq.heappush(maxHeap, [-1* min_distance_to_reach_grid, r1, c1])
                    visited.add((r1, c1))

# Java Code 
"""
import java.util.*;

class Solution {
    int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
    int n;

    public int maximumSafenessFactor(List<List<Integer>> gridList) {
        int[][] grid = new int[gridList.size()][];
        for (int i = 0; i < gridList.size(); i++) {
            grid[i] = gridList.get(i).stream().mapToInt(Integer::intValue).toArray();
        }

        n = grid.length;

        // First find the minimum distance of each cell from any of the thieves using multisource bfs
        int[][] minDist = calMinimumDist(grid);

        // Now find the minimum distance to go from (0, 0) to (n - 1, n - 1)
        // Just similar as : "778. Swim in Rising Water".
        // Only difference here while adding we will take the minimum and 
        // out of all those minimum we will take maximum. so we will use maxHeap instead of minHeap.

        // in "778. Swim in Rising Water", while adding we were taking maximum and out of all those
        // maximum, we will take minimum for ans. so we wil use 'minHeap'

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);
        boolean[][] visited = new boolean[n][n];

        maxHeap.offer(new int[]{minDist[0][0], 0, 0});
        visited[0][0] = true;

        while (!maxHeap.isEmpty()) {
            int[] curr = maxHeap.poll();
            int dist = curr[0], r = curr[1], c = curr[2];

            if (r == n - 1 && c == n - 1) return dist;

            for (int[] d : directions) {
                int nr = r + d[0], nc = c + d[1];
                if (0 <= nr && nr < n && 0 <= nc && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    int newDist = Math.min(dist, minDist[nr][nc]);
                    maxHeap.offer(new int[]{newDist, nr, nc});
                }
            }
        }

        return 0;
    }

    public int[][] calMinimumDist(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int[][] dist = new int[n][n];
        for (int[] row : dist) Arrays.fill(row, -1);

        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    q.offer(new int[]{r, c, 0});
                    dist[r][c] = 0;
                }
            }
        }

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int r = curr[0], c = curr[1], d = curr[2];

            for (int[] dir : directions) {
                int nr = r + dir[0], nc = c + dir[1];
                if (0 <= nr && nr < n && 0 <= nc && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = d + 1;
                    q.offer(new int[]{nr, nc, d + 1});
                }
            }
        }

        return dist;
    }
}


"""

# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
    int n;
    vector<vector<int>> directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        n = grid.size();

        // First find the minimum distance of each cell from any of the thieves using multisource bfs
        vector<vector<int>> minDist = calMinimumDist(grid);

        // Now find the minimum distance to go from (0, 0) to (n - 1, n - 1)
        // Just similar as : "778. Swim in Rising Water".
        // Only difference here while adding we will take the minimum and 
        // out of all those minimum we will take maximum. so we will use maxHeap instead of minHeap.

        // in "778. Swim in Rising Water", while adding we were taking maximum and out of all those
        // maximum, we will take minimum for ans. so we wil use 'minHeap'

        priority_queue<tuple<int, int, int>> maxHeap;
        vector<vector<bool>> visited(n, vector<bool>(n, false));

        maxHeap.push({minDist[0][0], 0, 0});
        visited[0][0] = true;

        while (!maxHeap.empty()) {
            auto [dist, r, c] = maxHeap.top();
            maxHeap.pop();

            if (r == n - 1 && c == n - 1) return dist;

            for (auto& dir : directions) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    int newDist = min(dist, minDist[nr][nc]);
                    maxHeap.push({newDist, nr, nc});
                }
            }
        }

        return 0;
    }

    vector<vector<int>> calMinimumDist(vector<vector<int>>& grid) {
        vector<vector<int>> dist(n, vector<int>(n, -1));
        queue<tuple<int, int, int>> q;

        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) {
                    dist[r][c] = 0;
                    q.push({r, c, 0});
                }
            }
        }

        while (!q.empty()) {
            auto [r, c, d] = q.front();
            q.pop();

            for (auto& dir : directions) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && dist[nr][nc] == -1) {
                    dist[nr][nc] = d + 1;
                    q.push({nr, nc, d + 1});
                }
            }
        }

        return dist;
    }
};


"""