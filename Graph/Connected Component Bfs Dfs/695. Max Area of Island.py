# just same logic as number of island 
# the same program will give the no of island also.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col= len(grid), len(grid[0])
        visited= set()
        island= 0
        maxArea = 0 
        
        directions= [[-1,0],[1,0],[0,-1],[0,1]] # writing all possible allowed directions i.e up,down,left,right in form of matrix

        def BFS(r,c):
            Q= collections.deque()
            Q.append((r,c))
            count= 0
            while Q:
                r1, c1= Q.popleft()
                count+= 1
                for dr,dc in directions:
                    r,c= r1+dr, c1+dc
                    if 0 <= r < row and 0 <= c < col and  grid[r][c] == 1 and (r,c) not in visited:
                        visited.add((r,c))
                        Q.append((r,c))
            return count
                        
        # code starts from here
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    island += 1
                    visited.add((r,c))
                    maxArea = max(maxArea, BFS(r,c))
        return maxArea


# method2: Using DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col= len(grid), len(grid[0])
        island= 0
        maxArea= 0
        
        def DFS(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
                return 0
            area = 1
            grid[r][c]= "visited"  # put any special symbol
            directions= [[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in directions:
                r1,c1 = r+dr, c+dc
                area += DFS(r1,c1)
            return area
                        
        # code starts from here
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 : 
                    island += 1
                    maxArea = max(maxArea, DFS(r,c))
        return maxArea
