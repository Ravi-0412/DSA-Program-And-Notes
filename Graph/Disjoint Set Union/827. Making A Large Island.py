# logic: first form the sets(connected components) using the given ele when you encounter '1' with its adjacent neighbour.
# in this way parent and size will get updated automatically.

# Now try to fill '0' with ''1' . and try to combine the size of all of parent adjacent cell having value= 1.
# VVI: But the adjacent cell may have same ultimate parent(may adjacent cell connected to each other also) and if we combine their size then,
# we will get the wrong ans.
# so we we need something to check for each whether we have already visited that ultimate parent or not for each available '0'.
# so using visited_parent to check for every node.

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
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n= len(grid), len(grid[0])
        def isValid(r, c):
            if r >= 0 and r < m and c >= 0 and c< m:
                return True
            return False

        dsu= DSU(m*n)

        # form components with available '1'.
        for r in range(m):
            for c in range(n):
                if grid[r][c]== 1:
                    ind= r * n + c
                    # now check in all four directions
                    directions= [[r, c-1], [r, c+1], [r-1, c], [r+1, c]]  # left, right, up, down
                    for dr, dc in directions:
                        ind1= dr * n + dc   # calculating the index number
                        if isValid(dr, dc) and grid[dr][dc]== 1:
                            dsu.unionBySize(ind, ind1)  # forming the union
        
        max_size= max(dsu.size)   # to handle the base case if there is all '1'.
        # now try to replace every '0' with '1'.
        for r in range(m):
            for c in range(n):
                if grid[r][c]== 0:
                    combinedSize= 1   # curr '0' will also contribute to the ans.
                    ind= r * n + c
                    visited_parent= set()  # check the ultimate parent is visited or not.
                    # now check in all four directions
                    directions= [[r, c-1], [r, c+1], [r-1, c], [r+1, c]]  # left, right, up, down
                    for dr, dc in directions:
                        nei_ind= dr * n + dc   # calculating the index number
                        if isValid(dr, dc) and grid[dr][dc]== 1:
                            adj_parent= dsu.findUPar(nei_ind)  #  we have to combine with size of parent not with the cell.
                            if not visited_parent or adj_parent not in visited_parent:   
                                combinedSize+= dsu.size[adj_parent]
                                max_size= max(max_size, combinedSize)
                                visited_parent.add(adj_parent)
        return max_size
