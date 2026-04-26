"""
Given an array of strings words where every string is an anagram of every other string, define two strings as similar if:
They are identical, or
Swapping exactly two characters in one string makes it equal to the other
Strings that are similar to a common string are transitively grouped together. Return the total number of such groups.
"""

# Method 1:
"""
Intuition: Treat each string as a node. Draw an edge between every pair that is "similar". Count connected components via BFS/DFS.
How to check if two strings are similar?
Since all strings are anagrams of each other, compare position by position. Count positions where characters differ. It must be exactly 0 or exactly 2 (the two swap positions).

time  : O(n^2 * L)  — compare every pair, each comparison costs O(L)
space : O(n^2)      — adjacency list can store O(n^2) edges in worst case

"""

from collections import deque

class StringClusterBrute:
    def num_similar_groups(self, strs: list[str]) -> int:
        """
        Calculates the number of clusters using a manual BFS expansion.
        """
        if not strs:
            return 0
            
        n = len(strs)
        visited = [False] * n
        cluster_count = 0
        
        for i in range(n):
            # If we haven't processed this string, it's a new cluster
            if not visited[i]:
                cluster_count += 1
                self._expand_cluster(i, strs, visited)
                
        return cluster_count

    def _expand_cluster(self, start_idx: int, strs: list[str], visited: list[bool]) -> None:
        """Helper to find all strings reachable from start_idx using BFS."""
        queue = deque([start_idx])
        visited[start_idx] = True
        
        while queue:
            curr_idx = queue.popleft()
            
            # Scan all nodes to find unvisited neighbors
            for j in range(len(strs)):
                if not visited[j] and self._is_similar(strs[curr_idx], strs[j]):
                    visited[j] = True
                    queue.append(j)

    def _is_similar(self, s1: str, s2: str) -> bool:
        """Hamming distance check: similar if diff is 0 or 2."""
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
            if diff > 2:
                return False
        return diff == 0 or diff == 2

# Sample Test Case
# strs = ["tars","rats","arts","star"]
# Result: 2


# Method 2:
"""
🧠 Thought Process & Logic
1. The Concept: Use a Disjoint Set Union (DSU) to maintain partitions of strings. 
Whenever we find two strings that are "similar," we merge their sets.
2. Transitivity: DSU handles the A -> B -> C logic automatically. 
If A and B are joined, and then B and C are joined, A and C naturally end up with the same "Representative" (Parent).
3. Optimization: We use Path Compression in the find operation and Union by Rank/Size (implied here by decrementing self.count) to keep the tree flat, making operations nearly O(1).

time  : O(n^2 * L * alpha(N))  — compare every pair, each comparison costs O(L)
space : O(n^2)      — adjacency list can store O(n^2) edges in worst case
"""

class UnionFind:
    def __init__(self, n: int):
        # Every element is its own parent initially
        self.parent = list(range(n))
        self.count = n

    def find(self, i: int) -> int:
        """Find with Path Compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        """Union two sets if they are different."""
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.count -= 1

class StringClusterOptimal:
    def num_similar_groups(self, strs: list[str]) -> int:
        """
        Calculates clusters using Union-Find for efficient merging.
        """
        if not strs:
            return 0
            
        n = len(strs)
        uf = UnionFind(n)
        
        # O(N^2) pair-wise check
        for i in range(n):
            for j in range(i + 1, n):
                if self._is_similar(strs[i], strs[j]):
                    uf.union(i, j)
                    
        return uf.count

    def _is_similar(self, s1: str, s2: str) -> bool:
        """Helper to determine if two strings are within one swap."""
        diff = 0
        for char1, char2 in zip(s1, s2):
            if char1 != char2:
                diff += 1
            if diff > 2:
                return False
        return diff == 0 or diff == 2

# Sample Test Case
# strs = ["omv", "ovm"]
# Result: 1

# Follow ups"
"""
1. "What if the number of strings (N) is huge but length (L) is small?
-> "Strategy: Instead of O(N^2), iterate through each string (O(N)) and generate all possible one-swap neighbors (O(L^2)). 
Check if those neighbors exist in a pre-built Hash Map.
Complexity: O(N * M^2) instead of O(N^2 * L).
"""

