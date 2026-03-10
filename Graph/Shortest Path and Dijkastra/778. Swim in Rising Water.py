# Method 1: 
"""
We can start with the brute force approach and explore all the possible paths to reach the end of the grid. 
The path which minimizes the maximum value of some cell in a path will be chosen and that water level - w_lvl will be our answer.

vvi : Min time in which you can reach any cell (r,c)= grid[r][c] if it's any of the adjacent cell is reachable in this much time.

Note vvi : Here we are marking visited when we are seeing first time only since when node is getting for 1st time 
then this will be minium time in which that will get visited. so no need to wait for any other path to minimise it's time.
Because there can't be any more optimal path possible for (r,c) because we have to include the curr cell value also.

Note: At time of pushing we are maximising the value and with the help of heap we are minimising, 
so automatically we will minimum(max time from all possible path).

Note: Also you can't reach cell (r, c) in time grid[r][c] if it's any of the neighbour is not able to reach in time grid[r][c].

Time: n^2*log(n^2) (Dijkastra Algo)
minHeap contains at most n^2 elements, pop time complexity each time is is O(logn^2), At most we will pop n^2 times
"""

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        minHeap= [(grid[0][0],(0,0))]      
        visited= set()
        visited.add((0,0))
        # from here bfs logic
        while minHeap:
            time, (r1,c1)= heapq.heappop(minHeap)
            if r1== row-1 and c1== col-1:   # you reached the destination
                return time
            # visited.add((r1, c1))   # marking here will lead to TLE and wrong ans.
            directions= [[-1,0],[1,0],[0,-1],[0,1]] 
            for r2,c2 in directions:
                r, c= r1 +r2, c1+ c2
                if 0<=r<row and 0<=c<col and (r,c) not in visited:
                    visited.add((r,c))  # mark visite here only as there can't be any more optimal path possible for (r,c) because we have to include the curr cell value also.
                    min_till_needed= max(time, grid[r][c])   # put the max val as we can only reach (r,c) with this time only, not in time less than this. 
                    heapq.heappush(minHeap,(min_till_needed,(r,c)))


# since for every cell, we will get the ans when we will see the node for 1st time itself 
# then we can mark visited at that time itself and check for ans at 1st time when we will see any cell.
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        if row == 1:
            return 0 # or return grid[0][0]
        minHeap= [(grid[0][0],(0,0))]      
        visited= set()
        visited.add((0,0))
        while minHeap:
            time, (r1,c1)= heapq.heappop(minHeap)
            directions= [[-1,0],[1,0],[0,-1],[0,1]] 
            for r2,c2 in directions:
                r, c= r1 +r2, c1+ c2
                if 0<=r<row and 0<=c<col and (r,c) not in visited:
                    min_till_needed= max(time, grid[r][c])   # put the max val as we can only reach (r,c) with this time only, not in time less than this.
                    if r== row-1 and c== col-1:
                        return  min_till_needed
                    visited.add((r,c))  # mark visite here only as there can't be any more optimal path possible for (r,c) because we have to include the curr cell value also.
                    heapq.heappush(minHeap,(min_till_needed,(r,c)))

# Method 2: 
"""
Most Optimised: Using Union-find
Time : O(MN * alpha(MN)) , where alpha is the nearly-constant inverse Ackermann function. 


we can utilise the below constraint:
0 <= grid[i][j] < n2
Each value grid[i][j] is unique.

Logic :
Instead of searching for a path, imagine the water level starting at 0 and rising. As it hits a certain elevation t, the cell at that elevation "activates."
1. Pre-sort the cells: Create a list of all cells (r,c) and sort them by their elevation. 
    Since elevations are unique and range from 0 to N^2−1, you can actually just use an array of size N^2 where index = elevation and value = (r, c). This "sorting" is O(N^2).
2. Activate & Connect: Iterate through elevations t=0,1,2,…,N^2−1.
        At each t, find the cell (r,c) with that elevation.
        Look at its 4 neighbors. If a neighbor has already been "activated" (elevation ≤t), use Union-Find to connect the current cell to that neighbor.
        
        At T=0, only the cell with elevation 0 exists. At T=10, only cells with elevations 0 through 10 "exist" as swimmable nodes.
        By mapping elevation -> (r, c), we know exactly which node is added to our graph at every second.

        When a cell at (r,c) is "unlocked" at time t, we check its four neighbors.
        If a neighbor is already unlocked, we merge the current cell's island with the neighbor's island.
        Why this works: The moment (0,0) and (n−1,n−1) are part of the same island, a path must exist between them. 
        Because we add cells in increasing order of elevation, the time t when they connect is guaranteed to be the minimum possible maximum elevation.

3. Stop: After each union, check if the start (0,0) and end (N−1,N−1) are in the same connected component. The first t at which this happens is your answer.
"""

class UnionFind:
    def __init__(self, size):
        # Each cell is its own parent initially
        self.parent = list(range(size))
        
    def find(self, i):
        # Path compression: makes future lookups nearly O(1)
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Connect one component to the other
            self.parent[root_i] = root_j

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # 1. Map elevation to coordinates (Bucket Sort style)
        # Since elevations are 0 to n^2-1, this is O(n^2) and gives us 
        # a sorted order of which cell "unlocks" at which time.
        pos = [None] * (n * n)
        for r in range(n):
            for c in range(n):
                pos[grid[r][c]] = (r, c)
        
        uf = UnionFind(n * n)
        unlocked = [[False] * n for _ in range(n)]
        
        # 2. Iterate through time t from 0 to n^2-1
        for t in range(n * n):
            r, c = pos[t]
            unlocked[r][c] = True
            
            # Check 4-directional neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                
                # If neighbor is within bounds and already unlocked by the rising water
                if 0 <= nr < n and 0 <= nc < n and unlocked[nr][nc]:
                    # Union the current cell with the neighbor
                    # We map (r, c) to a 1D index: r * n + c
                    uf.union(r * n + c, nr * n + nc)
            
            # 3. Check if the start and end points are now in the same component
            # If find(start) == find(end), it means a path has formed
            if uf.find(0) == uf.find(n * n - 1):
                return t
        
        return -1

# Related Q:
# 1) 3341. Find Minimum Time to Reach Last Room I
# 2) 3342. Find Minimum Time to Reach Last Room II

# Related Q:
# Note: Analyse these question properly like why in one q we are getting ans on 1st time and why in other getting after poping.
# 1) 2577. Minimum Time to Visit a Cell In a Grid
# 2) 1631. Path With Minimum Effort
