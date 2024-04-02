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

# Method 2: Counting
# Logic:
# For Complete Components, each node has an edge to all its adjancent node, e.g., 
# if we regard the node itself as an "adjancent node", all those node has the same adjancent node list.
# For example, for node 0,1,2,3. If it is an complete component, we have adjancency matrix as:
# 0 -> 0,1,2,3
# 1 -> 0,1,2,3
# 2 -> 0,1,2,3
# 3 -> 0,1,2,3

# We could first find the adjancency matrix, then count the values. 
# If the occurance of a value is the same as the length of the adjancency list, it is a complete component.

from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        adj2 = {}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)
        for i in range(n):
            # add the node itself
            adj[i].append(i)
            adj[i].sort()  # so that when we will apply count then order come same
            adj2[i] = tuple(adj[i])
        res = 0
        
        # count = collections.defaultdict(int)
        # for v in adj2.values():
        #     count[v] += 1
        # for k, v in count.items():
        #     res += 1 if len(k) == v else 0
        
        # Shortcut of above two for loop.
        # Counter(adj2.values()).items(): It will just count the frequency of values of adj2 and after that 
        # it will make a hashmap where k = value of adj2 and v = their frequency
        for k, v in Counter(adj2.values()).items():
            res += 1 if len(k) == v else 0
        
        return res

# method 3:  Also try by 'DSU'.