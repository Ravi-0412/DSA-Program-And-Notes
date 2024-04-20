# Very good problem. Not much hard. Medium level
# Just need to think a little.

# little similar way of doing as :"2699. Modify Graph Edge Weights".

# 1) critical: Edge that must be in all of the mst.
# How to find? 
# If deleting the edge and re-calculating the mst again makes mst increase 
# (or can't form mst),then the edge goes into critical list.

# Note: if any edge is critical then that can't be pseudo because pseudo may or may not be in all mst.

# 2) pseudo: edge that is part of some mst but not.
# i.e if no matter we use or do not use this edge, we can always find an MST with the min cost.

# Note vvi: If any edge is critical then no need to check for 'pseudo' else check for pseudo.

# How to check?
# Ans: If after including the edge we get mst value = original mst then it is 'pseudo'.
# Because it is  not critical(not part of all MST) but part of one of the MST.

# Note: Pseudo we will only get when edge weight will repeat , in case of unique edge weight there is no chance of pseudo edge.

# Note: some edge may not belong to either 'critical' or 'pseudo'
# The larger weight edge remaining after mst.

# Time: O(E^2)

class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   
    
    def findParent(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findParent(self.parent[n])   
        return self.parent[n]
    
    def union(self, n1, n2):  
        p1, p2= self.findParent(n1), self.findParent(n2)
        if p1== p2:   
            return False
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # we will find the MST using 'Kruskal' so sorting is needed but we also need to preserve the 
        # edge index to get the edge number for ans. for this appending the index at last in each edge.
        for i, edge in enumerate(edges):
            edge.append(i)   #[v1, v2, weight, index]
        
        # sort the edges based on weight
        edges.sort(key = lambda e :e[2])
        mst = 0
        uf = DSU(n)
        # find the mst with all edges.
        for u, v, w, i in edges:
            if uf.union(u, v):
                mst += w
        # Now find the critical and pseudo critical
        critical , pseudo = [], []
        # Traverse each edge once more
        for n1, n2, weight, j in edges:
            # check for critical
            # Find the mst without this edge
            mst_excluding = 0
            uf1 = DSU(n)
            # find the mst with all edges.
            for u, v, w, i in edges:
                if i == j:
                    # we have to exclude the above edge
                    continue
                if uf1.union(u, v):
                    mst_excluding += w
            
            # add if critical
            # if we are not able to form mst without the above edge(any of parent size is not 'n') 
            # or value of mst is greater then it is critical edge
            if max(uf1.size) != n or mst_excluding > mst:
                critical.append(j)
                continue  # because if any edge in critical then that can't be 'pseudo critical'
                          # so no need to check for psedu critical
            
            # Now check for pseudo critical
            # means the current edge is not critical so it may or not be part of MST
            # But after including the cur edge if we get the same mst value as original then
            # it means cur edge is part of any of the MST and since not critical(not part of all MST)
            # Therefore it will be 'pseudo critical'.

            # Find Mst including cur edge
            mst_including = weight
            uf2 = DSU(n)
            uf2.union(n1, n2)   # We have to include this edges first
            # find the mst with all edges.
            for u, v, w, i in edges:
                if uf2.union(u, v):  # no need to check (i = j) as already added so union will return False automatically
                    mst_including += w

            # Add if 'pseudo' . Here no need to check for mst formation
            # As it will form mst for sure since we are including 
            if mst_including == mst:
                pseudo.append(j)

        return [critical ,pseudo]

