# Method 1: 
"""
BFS (Breadth-First Search)
Use an adjacency list to represent the graph.
For every unvisited node, start a BFS traversal to visit all nodes in its connected component.
Count how many times you initiate BFS — that gives the number of components.

Time : O(n + e) — where n = number of nodes, e = number of edges
O(n + e) for adjacency list

Space: O(n) for visited set and queue in worst case
"""

from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        components = 0

        def bfs(node):
            q = deque([node])
            while q:
                curr = q.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                bfs(node)
                components += 1

        return components


# Method 2:
"""
DFS (Depth-First Search)
i) Build an adjacency list for the graph.
ii) Use DFS recursively to visit all nodes in a connected component.
iii)Each DFS initiation from an unvisited node counts as one component.

Time & space: Same as BFS
"""

from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        components = 0

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                visited.add(node)
                dfs(node)
                components += 1

        return components
