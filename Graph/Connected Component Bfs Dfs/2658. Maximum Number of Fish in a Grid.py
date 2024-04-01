# Fisher can only start at water cell and can only move to water cell i.e having grid value is not equal to '0'.

# This Q you can reduce to "Find max sum among all connected components having grid value not equal to zero".
# more generalise , it is exactly just same as "695. Max Area of Island". 

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        def bfs(r, c):
            sum= 0
            q= collections.deque()
            visited.add((r, c))
            q.append((r, c))
            while q:
                r1, c1= q.popleft()
                sum+= grid[r1][c1]
                directions= [[r1, c1 -1], [r1, c1+ 1], [r1+1, c1],[r1-1, c1]]
                for nr, nc in directions:
                    if 0<= nr < m and 0<= nc < n and (nr, nc) not in visited and grid[nr][nc]:
                        q.append((nr, nc))
                        visited.add((nr, nc))
            return sum       
        
        m, n= len(grid), len(grid[0])
        visited= set()
        ans= 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:  # if water cell and not in visited
                    ans= max(ans, bfs(i, j))
        return ans