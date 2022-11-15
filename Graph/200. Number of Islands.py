# METHOD 1: USING bfs
# just you have to find the no of distinct connected components containing consecutive one's
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col= len(grid), len(grid[0])
        visited= set()
        island= 0
        
        def BFS(r,c):
            Q= collections.deque()
            Q.append((r,c))
            while Q:
                r1,c1= Q.popleft()
                # now check for all allowed directions we can visit from that grid 
                # 4 possible direction: up,down,left,right
                if r1 -1 >=0 and (r1-1,c1) not in visited and grid[r1-1][c1]== "1":
                    visited.add((r1-1,c1))
                    Q.append((r1-1,c1))
                if r1 +1 <row and (r1+1,c1) not in visited and grid[r1+1][c1]== "1":
                    visited.add((r1+1,c1))
                    Q.append((r1+1,c1))
                if c1 -1 >=0 and (r1,c1-1) not in visited and grid[r1][c1-1]== "1":
                    visited.add((r1,c1-1))
                    Q.append((r1,c1-1))
                if c1 +1 <col and (r1,c1+1) not in visited and grid[r1][c1+1]== "1":
                    visited.add((r1,c1+1))
                    Q.append((r1,c1+1))             
        
        # start reading from here
        for r in range(row):
            for c in range(col):
                if grid[r][c]== "1" and (r,c) not in visited: 
                    island+= 1
                    visited.add((r,c))
                    BFS(r,c)
        return island



# simple and concise way of writing the above code
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col= len(grid), len(grid[0])
        visited= set()
        island= 0
        
        def BFS(r,c):
            Q= collections.deque()
            Q.append((r,c))
            while Q:
                r1,c1= Q.popleft()
                # writing all possible allowed directions i.e up,down,left,right in form of matrix
                directions= [[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    r,c= r1+dr, c1+dc
                    if 0<=r<row and 0<=c<col and  grid[r][c]=="1" and (r,c) not in visited:
                        visited.add((r,c))
                        Q.append((r,c))
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]== "1" and (r,c) not in visited:
                    island+= 1
                    visited.add((r,c))
                    BFS(r,c)
        return island

# method 2: using DFS

# for saving the space which is going in O(n*m), just make the changes just after visiting any grid like we had done in 'IsGraphBipartite'
# no need of extra visited set
# always remember for counting q, in base case there will one condition of returning '0' and one in general
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col= len(grid), len(grid[0])
        island= 0
        
        def DFS(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]!= "1":  # write all invalid condition together and return '0' in count(if you are adding the ans somewhere) or simply return 
                return 
            grid[r][c]= "visited"  # put any special symbol
            directions= [[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in directions:
                r1,c1= r+dr, c+dc
                DFS(r1,c1)   

        # code starts from here
        for r in range(row):
            for c in range(col):
                if grid[r][c]== "1": 
                    island+= 1
                    DFS(r,c)
        return island





