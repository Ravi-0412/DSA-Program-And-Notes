# Method 1: Already done using BFS and DFS before.

# method 2: using union-find.
# m= rows, n= cols
# What differences from 'No of provinces'?
# Ans: Here there can be more than 'm'(rows) island, infact there can be max nearly (m*n)//2 island.(nearly half of all cell).
# so here we will make parent and size array of size (m*n) itself.
# Also in that Q. we have to combine cities (i,j) into one so was passing (i, j) in union function.
# But here we have to combine all cell so we have to the pass the cell index in terms of 'i' and 'j'. 
# But we can't do because for finding parent we have to pass as a integer only. So converted all cell into an integer.

# So first we will convert all cell into an integer like 0,1,2,3.......
# to find and do the union.

# logic: wherever there is '1', treat them all as independent island initially.
# and later if we can combine those with its neighbour and keep reducing the count by '1'.

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
            return 0  # means we can't decrease the component since we can't combine
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]
        return 1   # we can decrease the component by '1' since we can combine them.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n= len(grid), len(grid[0])
        dsu= DSU(m*n)

        count= 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]== "1":
                    count+= 1  # initially first incr the count.
                    x1= i*n + j  # number of curr cell 
                    # now try to bring the adjacent cell to this curr cell into one .
                    # we only need to go down and right. no need to go in all four directions since those cell will be already checked before.

                    # going down (i+1, j)
                    if i + 1<= m-1 and grid[i+1][j]== "1":
                        x2= x1 + n  # no of this cell
                        count-= dsu.unionBySize(x1, x2)
                    # going right (i, j+1)
                    if j + 1<= n-1 and grid[i][j +1]== "1":
                        x2= x1 + 1  # no of this cell
                        count-= dsu.unionBySize(x1, x2)
        return count


# Method 2: counting the distinct parent .
# But here we will try to find the distinct parent not from parent array itself(like "Q: no of provinces") then it will give the incorrect ans.
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

        for i in range(m):
            for j in range(n):
                if grid[i][j]== "1":
                    x1= i*n + j  # number of curr cell 
                    # now try to bring the adjacent cell to this curr cell into one .
                    # we only need to go down and right. no need to go in all four directions since those cell will be already checked before.

                    # going down (i+1, j)
                    if i + 1<= m-1 and grid[i+1][j]== "1":
                        x2= x1 + n  # no of this cell
                        dsu.unionBySize(x1, x2)
                    # going right (i, j+1)
                    if j + 1<= n-1 and grid[i][j +1]== "1":
                        x2= x1 + 1  # no of this cell
                        dsu.unionBySize(x1, x2)
        
        # Now count the no of cell which is the parent of itself.
        # That will give the no of ultimate parent and that will be our ans.
        count= 0

        # Directly counting will give the error.,
        # total_cell= m*n
        # for p in range(total_cell):
        #     if p== dsu.parent[p]:
        #         count+= 1
        # return count

        for i in range(m):
            for j in range(n):
                x1= i*n + j  # number of curr cell.
                if grid[i][j]== "1" and x1== dsu.parent[x1]:
                    count+= 1
        return count



