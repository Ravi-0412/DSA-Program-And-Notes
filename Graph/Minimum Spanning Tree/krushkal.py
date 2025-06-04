"""
logic: we have to take the minimum edge first and include this in mst if after adding this edge, it doesn't form a cycle.
i) for taking the minimum one always, we can either sort or use the minHeap and 
ii) for checking whether adding an edge will lead to a cycle or not, then only thing come into mind is 'union-find' and 'path compression' method

submitted on gfg
"""
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

# java
"""
import java.util.*;

class DSU {
    int[] parent, size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int findUPar(int node) {
        if (node == parent[node]) return node;
        parent[node] = findUPar(parent[node]);  // Path compression
        return parent[node];
    }

    public boolean unionBySize(int u, int v) {
        int pu = findUPar(u);
        int pv = findUPar(v);
        if (pu == pv) return false;

        if (size[pu] < size[pv]) {
            parent[pu] = pv;
            size[pv] += size[pu];
        } else {
            parent[pv] = pu;
            size[pu] += size[pv];
        }
        return true;
    }
}

class Solution {
    public int spanningTree(int V, List<List<List<Integer>>> adj) {
        List<int[]> edges = new ArrayList<>();

        // Convert adjacency list to edge list with (cost, src, dest)
        for (int i = 0; i < V; i++) {
            for (List<Integer> edge : adj.get(i)) {
                int v = edge.get(0);
                int w = edge.get(1);
                edges.add(new int[]{w, i, v});
            }
        }

        // Sort edges by weight
        edges.sort(Comparator.comparingInt(a -> a[0]));

        DSU dsu = new DSU(V);
        int mst = 0;
        int remaining_edges = V - 1;

        for (int[] edge : edges) {
            int w = edge[0], u = edge[1], v = edge[2];
            if (dsu.unionBySize(u, v)) {
                mst += w;
                remaining_edges--;
                if (remaining_edges == 0) break;
            }
        }

        return mst;
    }
}

"""

# C++ Code
"""
#include <vector>
#include <queue>
using namespace std;

class DSU {
public:
    vector<int> parent, size;
    DSU(int n) {
        parent.resize(n);
        size.resize(n, 1);
        for (int i = 0; i < n; i++) parent[i] = i;
    }
    
    int findUPar(int n) {
        if (n == parent[n]) return n;
        return parent[n] = findUPar(parent[n]);
    }
    
    bool unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);
        if (p1 == p2) return false;  // they belong to same component
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
        return true;
    }
};

class Solution {
public:
    int spanningTree(int V, vector<vector<pair<int,int>>>& adj) {
        vector<tuple<int,int,int>> edges; // (cost, src, dest)
        int mst = 0;
        
        // convert adjacency list into edge list with costs
        for (int s = 0; s < V; s++) {
            for (auto& [d, c] : adj[s]) {
                edges.emplace_back(c, s, d);
            }
        }
        
        // min heap for edges by cost
        priority_queue<tuple<int,int,int>, vector<tuple<int,int,int>>, greater<tuple<int,int,int>>> pq;
        for (auto& e : edges) pq.push(e);
        
        int remaining_edge = V - 1; // edges needed for MST
        DSU dsu(V);
        
        while (!pq.empty() && remaining_edge != 0) {
            auto [c, s, d] = pq.top();
            pq.pop();
            if (dsu.unionBySize(s, d)) {
                mst += c;
                remaining_edge--;
            }
        }
        return mst;
    }
};

"""