# logic: we have to take the minimum edge first and include this in mst if after adding this edge, it doesn't form a cycle
# for take the minimum one always, we can either sort or use the minHeap and 
# for checking whether adding an edge will lead to a cycle or not, then only thing come into mind is 'union-find' and 'path compression' method

# submitted on gfg
import heapq

class DisJointSet:
    def __init__(self,n):
        self.parent= [i for i in range(n)]
        self.rank= [0]*n
    
    def find(self,n1):
        p= self.parent[n1]
        while p!= self.parent[p]:
            self.parent[p]= self.parent[self.parent[p]]
            p= self.parent[p]
        return p
    
    def union(self,n1,n2):
        p1,p2= self.find(n1), self.find(n2)
        if p1== p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2]= p1
        else:
            self.parent[p1]= p2
            if self.rank[p1]== self.rank[p2]:
                self.rank[p2]+= 1
        # print(n1,n2)
        return True
        
# code starts from here    
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        edges= []
        mst= 0
        # first converting into the form [(cost,src,dest)] as we have to sort the edges acc to their cost
        for s in range(V):  # s: source
            adj_to_s= adj[s]  
            for d,c in adj[s]:       # d: destination, c= cost
                edges.append((c,s,d))
    
        # heapify the edges so that minimum weight edge come at first index
        heapq.heapify(edges)
        remaining_node= V-1     # as for connecting 'v' node we have to add only 'v-1' vertex
        djs= DisJointSet(V)
        # now take the edge one by one from min heap and add it to the mst if doesn't form a cycle
        while edges and remaining_node!= 0 :
            c,s,d = heapq.heappop(edges)
            if djs.union(s,d):
                # print(mst)
                mst+= c
                remaining_node-= 1
        return mst

