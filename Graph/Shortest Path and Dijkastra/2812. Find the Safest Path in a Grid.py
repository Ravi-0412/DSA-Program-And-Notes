# Logic: Have to find path as far as from any of the thieves.

# Combination of: "286 walls and gates " + "778. Swim in Rising Water".

# 1) find the minimum distance of all grid from any of the thieves using multisource bfs.
# 2) find the minimum distance using similar approach as "778. Swim in Rising Water".

# understand and visualise properly.
# Try by other approaches also later.

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