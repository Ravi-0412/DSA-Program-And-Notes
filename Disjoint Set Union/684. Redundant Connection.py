
# using Disjoint Set union.
# This Q was based on this logic only.
# logic: all edges connected together should not lead to cycle, so
# whenver we find any two node for which union is not possible then return those node & that will be our ans.

# time for union: O(4 alpha) nearly = O(1), space: O(n)
# time for find Parent= O(4* alpha)
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
            return False
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n= len(edges)
        dsu= DSU(n +1)  # indexing in input start from '1' so passed 'n+1'.
        for n1,n2 in edges:
            if dsu.unionBySize(n1,n2)== False:   # if you find any edge for which we can't do umio simply return that.
                return [n1,n2]



