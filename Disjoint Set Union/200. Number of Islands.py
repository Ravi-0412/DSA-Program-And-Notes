# Method 1: Already done using BFS and DFS before.

# method 2: using union-find.
# m= rows, n= cols
# What differences from 'No of provinces'?
# Ans: Here there can be more than 'm'(rows) island, infact there can be max nearly (m*n)//2 island.(nearly half of all cell).
# so here we will make parent and size array of size (m*n) itself. But there was only 'n' city.
# Also in that Q. we have to combine cities (i,j) into one so was passing (i, j) in union function.
# But here we have to combine all cell so we have to the pass the cell index in terms of 'i' and 'j'. 
# But we can't do because for finding parent we have to pass as a integer only. So converted all cell into an integer.

# So first we will convert all cell into an integer like 0,1,2,3.......
# to find and do the union.

# Method 1: counting the distinct parent .
# But here we will try to find the distinct parent not from parent array itself(like "Q: no of provinces") 
# then it will give the incorrect ans.
# As where there will be "0" in grid that will be the parent of itself and that also be get counted in the ans.

# only that will be part of ans who is parent of himself and value at that grid cell== "1".

class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   
    
    def findUPar(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findUPar(self.parent[n])   
        return self.parent[n]
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return 
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n= len(grid), len(grid[0])
        dsu= DSU(m*n)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        for i in range(m):
            for j in range(n):
                if grid[i][j]== "1":
                    x1 = i*n + j  # number of curr cell 
                    # now try to bring the adjacent cell to this curr cell into one .
                    for dr, dc in directions:
                        nr, nc = i + dr , j + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                            x2 = nr * n + nc
                            dsu.unionBySize(x1, x2)
        
        # Now count the no of cell which is the parent of itself when grid[i][j] == "1"
        # That will give the no of ultimate parent and that will be our ans.
        count= 0
        for i in range(m):
            for j in range(n):
                x1= i*n + j  # number of curr cell.
                if grid[i][j]== "1" and x1== dsu.parent[x1]:
                    count+= 1
        return count

# Note: Here if we will try to solve by method of '959. Regions Cut By Slashes'
# i.e taking 'count' as member of DSU and incrementing count when we will find any cycle then it will give wrong ans
# Will give very high number than expected.

"""
class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]
        self.count = 0
"""

# Reason: Because here comparing with 4 adjacent cell and not a single point like '959. Regions Cut By Slashes'
# so there will be lot of repeating in this.

# That's why easiest way to find ans is by counting number of distinct parents.