import collections
from typing import List

class DSU:
    """
    Disjoint Set Union (Union-Find) with Path Compression and Union by Size.
    Optimizes edge connectivity checks to nearly O(1) time.
    """
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]   
    
    def findParent(self, n):   
        # Path compression: flattens the structure for faster future lookups
        if n == self.parent[n]:   
            return n
        self.parent[n] = self.findParent(self.parent[n])   
        return self.parent[n]
    
    def union(self, n1, n2):  
        # Union by size: attaches smaller tree under the larger tree
        p1, p2 = self.findParent(n1), self.findParent(n2)
        if p1 == p2:   
            return False
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2  
            self.size[p2] += self.size[p1]   
        else:
            self.parent[p2] = p1   
            self.size[p1] += self.size[p2]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """
        1. Critical: Must be in all MSTs. Deleting it increases MST weight or breaks connectivity.
        2. Pseudo-Critical: Part of some MST but not all. Forcing it into the MST maintains min weight.
        """
        # Preserving original indices before sorting for the final answer
        for i, edge in enumerate(edges):
            edge.append(i)  # Format: [u, v, weight, original_index]
        
        # Kruskal's requires edges sorted by weight
        edges.sort(key=lambda e: e[2])
        
        # Step 1: Find the baseline weight of the standard MST
        base_mst_weight = self.get_mst_weight(n, edges)
        
        critical, pseudo = [], []

        # Step 2: Test each edge individually
        for u_curr, v_curr, w_curr, edge_idx in edges:
            
            # --- CRITICAL CHECK ---
            # Try to build an MST without this edge.
            # If weight increases or we can't connect all nodes, it's critical.
            weight_without = self.get_mst_weight(n, edges, exclude_idx=edge_idx)
            if weight_without > base_mst_weight:
                critical.append(edge_idx)
                continue # If it's critical, it cannot be pseudo-critical by definition
            
            # --- PSEUDO-CRITICAL CHECK ---
            # Try to build an MST by forcing this edge into the solution first.
            # If the resulting total weight still equals the baseline, it's pseudo-critical.
            weight_with = self.get_mst_weight(n, edges, include_edge=[u_curr, v_curr, w_curr])
            if weight_with == base_mst_weight:
                pseudo.append(edge_idx)

        return [critical, pseudo]

    def get_mst_weight(self, n, edges, exclude_idx=-1, include_edge=None):
        """
        Kruskal's Algorithm helper.
        Calculates MST weight with options to skip an edge or force one in.
        """
        uf = DSU(n)
        weight_sum = 0
        edges_count = 0
        
        # Scenario: Force Include (used for pseudo-critical check)
        # We start the MST by taking this edge regardless of weight order
        if include_edge:
            u, v, w = include_edge
            if uf.union(u, v):
                weight_sum += w
                edges_count += 1
            
        # Scenario: Standard Kruskal's (with optional exclusion)
        for u, v, w, i in edges:
            if i == exclude_idx:
                continue # Skip the edge we are testing for criticality
            
            if uf.union(u, v):
                weight_sum += w
                edges_count += 1
        
        # A valid MST must contain exactly n-1 edges
        # If it's disconnected, return infinity so the weight comparison fails
        return weight_sum if edges_count == n - 1 else float('inf')
