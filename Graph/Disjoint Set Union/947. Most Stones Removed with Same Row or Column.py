# logic: we can remove any stone if it has either same row or same col with remaining stone.
# Reducing: So we can combine all stones having same row or same col into components.
# After that we can delete all stones from the all components except 1 i.e 
# for each component (distinct parent or node is parent of itself), find the size of the node and if size is greater than >1
# delete all stones equal to 'size-1'. 

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
    def removeStones(self, stones: List[List[int]]) -> int:
        n= len(stones)
        dsu= DSU(n)    # passing 'n' only as we have to check only 'n' stones. so no need to take dimension and all.
        # first form components from stone.
        for i in range(n):
            x1, y1= stones[i]
            for j in range(n):
                x2, y2= stones[j]
                if x1== x2 or y1== y2 :
                    dsu.unionBySize(i, j)
        # Now delete stones from component.
        count= 0
        for p in range(n):
            if p== dsu.parent[p] and dsu.size[p] > 1:
                count+= dsu.size[p] - 1
        return count
