# logic: keep track of 'no of nodes & no of edges' in each connected components.
# for complete components: no_edge= (no_node * (no_node -1))//2

# so for each component check the relation between no_nodes and no_edge.

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj= collections.defaultdict(list)
        for u, v in edges:  # graph arrow will be from first to second
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(v):
            visited.add(v)
            self.node_count+= 1
            self.edge_count+= len(adj[v])  # add the no of edge from 'v'.
            for nei in adj[v]:
                if nei not in visited:
                    dfs(nei)   

        # code starts from here
        components= 0
        visited= set()
        for v in range(n):
            if v not in visited:
                self.node_count, self.edge_count= 0, 0
                dfs(v)
                if self.edge_count== self.node_count * (self.node_count -1):
                    # one edge will get included two times so not dividing by '2'.
                    components+= 1
        return components


# method 2:  Also try by 'DSU'.


# Method 3: By counting

# All solutions in sheet.