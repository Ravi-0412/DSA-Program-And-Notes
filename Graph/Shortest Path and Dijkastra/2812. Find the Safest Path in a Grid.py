# Logic: Have to find path as far as from any of the thieves.

# Combination of: "286 walls and gates " + "778. Swim in Rising Water".

# 1) find the minimum distance of all grid from any of the thieves using multisource bfs.
# 2) find the minimum distance using similar approach as "778. Swim in Rising Water".

# understand and visualise properly.
# Try by other approaches also later.

"""
Related Patterns & Interview Strategy:
The "Min-Max" vs "Max-Min" Vocabulary
Maximize the Minimum: (This problem). Use Max-Heap or Binary Search with "Can we do >= X".
Minimize the Maximum: (e.g., LC 1631). Use Min-Heap or Binary Search with "Can we do <= X?".
"""

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

# Method 2:
"""
Using BFS( + Binary Search

"""

from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        """
        Main function to find the maximum safeness factor using:
        1. Multi-source BFS for pre-calculating distances.
        2. Binary Search on the answer for optimization.
        3. Standard BFS for path validation.
        """
        n = len(grid)
        
        # 1. Edge Case: If start or end is occupied by a thief, safeness is 0.
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        # 2. STEP 1: Pre-calculate min distance to any thief for every cell.
        # This is the 'Multi-source BFS' phase.
        dist_to_thief = self._compute_thief_distances(grid, n)
        
        # 3. STEP 2: Binary Search for the optimal safeness factor.
        # We use Template 1 (start <= end) to find the largest valid factor.
        start, end = 0, 2 * n # Max Manhattan distance in n x n grid is roughly 2n.
        max_safe_factor = 0
        
        while start <= end:
            mid_factor = start + (end - start) // 2
            
            # Check if a path exists where every cell is at least 'mid_factor' units from a thief.
            if self._has_valid_path(dist_to_thief, n, mid_factor):
                max_safe_factor = mid_factor  # This factor is valid, try to improve it.
                start = mid_factor + 1
            else:
                end = mid_factor - 1          # This factor is too strict, try lower.
                
        return max_safe_factor

    def _compute_thief_distances(self, grid: list[list[int]], n: int) -> list[list[int]]:
        """
        Uses Multi-source BFS to calculate the shortest distance from 
        each cell to any thief (represented by 1 in the grid).
        """
        dist = [[-1] * n for _ in range(n)]
        queue = deque()
        
        # Initialize queue with all thieves (distance 0).
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        # 4-directional movement: Right, Left, Down, Up.
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            curr_r, curr_c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc
                
                # If neighbor is valid and hasn't been reached yet.
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[curr_r][curr_c] + 1
                    queue.append((nr, nc))
                    
        return dist

    def _has_valid_path(self, dist_matrix: list[list[int]], n: int, threshold: int) -> bool:
        """
        Checks if a path exists from (0,0) to (n-1, n-1) such that 
        all cells in the path have a distance to the nearest thief >= threshold.
        """
        # If the start cell itself is within the forbidden danger zone.
        if dist_matrix[0][0] < threshold:
            return False
            
        queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while queue:
            curr_r, curr_c = queue.popleft()
            
            # Target reached while respecting the safety threshold.
            if curr_r == n - 1 and curr_c == n - 1:
                return True
                
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = curr_r + dr, curr_c + dc
                
                # Check boundaries, visited status, and the safety constraint.
                if (0 <= nr < n and 0 <= nc < n and not visited[nr][nc] 
                    and dist_matrix[nr][nc] >= threshold):
                    
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    
        return False


# Java Code 
"""
import java.util.*;

class Solution {
    public int maximumSafenessFactor(int[][] grid) {
        int n = grid.length;
        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

        // First find the minimum distance of each cell from any of the thieves using multisource bfs
        Map<String, Integer> calMinimumDist() {
            Queue<int[]> q = new LinkedList<>();
            Map<String, Integer> min_dist = new HashMap<>();
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (grid[r][c] == 1) {
                        q.offer(new int[]{r, c, 0}); // [i, j, distance_from_any_thieves]
                        min_dist.put(r + "," + c, 0);
                    }
                }
            }
            while (!q.isEmpty()) {
                int[] cur = q.poll();
                int r = cur[0], c = cur[1], dist = cur[2];
                for (int[] dir : directions) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    String key = nr + "," + nc;
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && !min_dist.containsKey(key)) {
                        min_dist.put(key, dist + 1);
                        q.offer(new int[]{nr, nc, dist + 1});
                    }
                }
            }
            return min_dist;
        }

        Map<String, Integer> min_dist = calMinimumDist();

        // Now find the minimum distance to go from (0, 0) to (n - 1, n - 1)
        // Just similar as : "778. Swim in Rising Water".
        // Only difference here while adding we will take the minimum and 
        // out of all those minimum we will take maximum. so we will use maxHeap instead of minHeap.

        // in "778. Swim in Rising Water", while adding we were taking maximum and out of all those
        // maximum, we will take minimum for ans. so we wil use 'minHeap'

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>( (a,b) -> Integer.compare(b[0], a[0]) );
        Set<String> visited = new HashSet<>();
        String startKey = "0,0";
        visited.add(startKey);
        maxHeap.offer(new int[]{min_dist.getOrDefault(startKey, 0), 0, 0});

        while (!maxHeap.isEmpty()) {
            int[] cur = maxHeap.poll();
            int dist = cur[0], r = cur[1], c = cur[2];
            if (r == n - 1 && c == n - 1) {
                return dist;
            }
            for (int[] dir : directions) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                String key = nr + "," + nc;
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited.contains(key)) {
                    int min_distance_to_reach_grid = Math.min(dist, min_dist.getOrDefault(key, Integer.MAX_VALUE));
                    maxHeap.offer(new int[]{min_distance_to_reach_grid, nr, nc});
                    visited.add(key);
                }
            }
        }

        return -1;  // if no path found
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = (int)grid.size();
        vector<vector<int>> directions{{0, -1}, {0, 1}, {-1, 0}, {1, 0}};

        // First find the minimum distance of each cell from any of the thieves using multisource bfs
        auto calMinimumDist = [&]() {
            queue<tuple<int,int,int>> q; // r,c,dist
            unordered_map<int, unordered_map<int,int>> min_dist;
            for (int r = 0; r < n; r++) {
                for (int c = 0; c < n; c++) {
                    if (grid[r][c] == 1) {
                        q.emplace(r, c, 0);  // [i, j, distance_from_any_thieves]
                        min_dist[r][c] = 0;
                    }
                }
            }
            while (!q.empty()) {
                auto [r, c, dist] = q.front();
                q.pop();
                for (auto& dir : directions) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];
                    if (nr >= 0 && nr < n && nc >= 0 && nc < n && min_dist[nr].find(nc) == min_dist[nr].end()) {
                        min_dist[nr][nc] = dist + 1;
                        q.emplace(nr, nc, dist + 1);
                    }
                }
            }
            return min_dist;
        };

        auto min_dist = calMinimumDist();

        // Now find the minimum distance to go from (0, 0) to (n - 1, n - 1)
        // Just similar as : "778. Swim in Rising Water".
        // Only difference here while adding we will take the minimum and 
        // out of all those minimum we will take maximum. so we will use maxHeap instead of minHeap.

        // in "778. Swim in Rising Water", while adding we were taking maximum and out of all those
        // maximum, we will take minimum for ans. so we wil use 'minHeap'

        using T = tuple<int,int,int>; // dist, r, c
        auto cmp = [](const T& a, const T& b) { return get<0>(a) < get<0>(b); };
        priority_queue<T, vector<T>, decltype(cmp)> maxHeap(cmp);

        unordered_set<int> visited;  // encode (r,c) as r * n + c
        visited.insert(0 * n + 0);
        maxHeap.emplace(min_dist[0][0], 0, 0);

        while (!maxHeap.empty()) {
            auto [dist, r, c] = maxHeap.top();
            maxHeap.pop();

            if (r == n-1 && c == n-1) {
                return dist;
            }
            for (auto& dir : directions) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                int encoded = nr * n + nc;
                if (nr >= 0 && nr < n && nc >= 0 && nc < n && visited.find(encoded) == visited.end()) {
                    int min_distance_to_reach_grid = min(dist, min_dist[nr][nc]);
                    maxHeap.emplace(min_distance_to_reach_grid, nr, nc);
                    visited.insert(encoded);
                }
            }
        }

        return -1;  // if no path found
    }
};

"""
