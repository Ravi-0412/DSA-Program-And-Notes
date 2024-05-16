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