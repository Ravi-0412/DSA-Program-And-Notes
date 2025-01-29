
# using Disjoint Set union.
# This Q was based on this logic only.
# logic: 
"""
all edges connected together should not lead to cycle, so
whenver we find any two node for which union is not possible then return those node & that will be our ans.

Also we need to return the answer that occurs last in the input, If there are multiple answers.
And this will get handled automatically
"""

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

# Java
import java.util.*;

class DSU {
    int[] parent;
    int[] size;
    
    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }
    
    public int findUPar(int n) {
        if (n == parent[n]) {
            return n;
        }
        parent[n] = findUPar(parent[n]);  // Path compression
        return parent[n];
    }
    
    public boolean unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);
        
        if (p1 == p2) {
            return false;  // Already in the same set
        }
        
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
        
        return true;
    }
}

public class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        DSU dsu = new DSU(n + 1);  // n + 1 for 1-based indexing
        
        for (int[] edge : edges) {
            int n1 = edge[0];
            int n2 = edge[1];
            
            if (!dsu.unionBySize(n1, n2)) {
                return edge;  // Return the redundant edge
            }
        }
        
        return new int[] {};  // In case there's no redundant connection
    }
}



