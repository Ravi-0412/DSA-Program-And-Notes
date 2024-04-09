# logic: we have to take the minimum edge first and include this in mst if after adding this edge, it doesn't form a cycle.
# for take the minimum one always, we can either sort or use the minHeap and 
# for checking whether adding an edge will lead to a cycle or not, then only thing come into mind is 'union-find' and 'path compression' method

# submitted on gfg
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

import heapq
class Solution:
    def spanningTree(self, V, adj):
        edges= []
        mst= 0
        # first converting into the form [(cost,src,dest)] as we have to sort the edges acc to their cost
        for s in range(V):  # s: source
            for d,c in adj[s]:       # d: destination, c= cost
                edges.append((c,s,d))
    
        # heapify the edges so that minimum weight edge come at first index or sort the edge
        heapq.heapify(edges)
        remaining_edge= V-1     # as for connecting 'v' node we have to add only 'v-1' edges
        dsu = DSU(V)
        # now take the edge one by one from min heap and add it to the mst if doesn't form a cycle
        while edges and remaining_edge!= 0 :
            c,s,d = heapq.heappop(edges)
            if dsu.unionBySize(s,d):
                mst+= c
                remaining_edge-= 1
        return mst

