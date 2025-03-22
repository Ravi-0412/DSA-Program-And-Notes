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

# Java
"""
import java.util.*;

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adj.put(i, new ArrayList<>());
        }
        
        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        Set<Integer> visited = new HashSet<>();
        int components = 0;

        for (int v = 0; v < n; v++) {
            if (!visited.contains(v)) {
                int[] count = new int[2]; // count[0] for nodes, count[1] for edges
                dfs(v, adj, visited, count);
                if (count[1] == count[0] * (count[0] - 1)) {
                    components++;
                }
            }
        }

        return components;
    }

    private void dfs(int v, Map<Integer, List<Integer>> adj, Set<Integer> visited, int[] count) {
        visited.add(v);
        count[0]++; // Increment node count
        count[1] += adj.get(v).size(); // Add number of edges (counted twice)
        
        for (int neighbor : adj.get(v)) {
            if (!visited.contains(neighbor)) {
                dfs(neighbor, adj, visited, count);
            }
        }
    }
}
"""

# Method 2: Counting
"""
For Complete Components, each node has an edge to all its adjancent node, e.g., 
if we regard the node itself as an "adjacent node", all those node has the same adjacent node list.
For example, for node 0,1,2,3. If it is an complete component, we have adjancency matrix as:
0 -> 0,1,2,3
1 -> 0,1,2,3
2 -> 0,1,2,3
3 -> 0,1,2,3

We could first find the adjancency matrix, then count the values. 
If the occurance of a value is the same as the length of the adjancency list, it is a complete component.
"""


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

# Java
"""
import java.util.*;

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        Map<Integer, String> adj2 = new HashMap<>();

        for (int i = 0; i < n; i++) {
            adj.put(i, new ArrayList<>());
        }

        for (int[] edge : edges) {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }

        for (int i = 0; i < n; i++) {
            adj.get(i).add(i); // Add the node itself
            Collections.sort(adj.get(i)); // Sort to ensure order consistency
            adj2.put(i, adj.get(i).toString()); // Store as string to use as a key
        }

        Map<String, Integer> freqMap = new HashMap<>();
        for (String value : adj2.values()) {
            freqMap.put(value, freqMap.getOrDefault(value, 0) + 1);
        }

        int res = 0;
        for (Map.Entry<String, Integer> entry : freqMap.entrySet()) {
            if (entry.getKey().split(",").length == entry.getValue()) {
                res++;
            }
        }

        return res;
    }
}
"""

# method 3:  Also try by 'DSU'. Easy only
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))  
        self.edge_count = [0] * n  # Edge count per component
        self.node_count = [1] * n  

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        self.edge_count[root_u] += 1  # Increment edge count (undirected graph) because we are merging 'V' to 'U'

        if root_u != root_v:
            self.parent[root_v] = root_u  # Merge component V into U
            self.edge_count[root_u] += self.edge_count[root_v]  # Merge edge counts
            self.node_count[root_u] += self.node_count[root_v]  # Merge node counts

    def get_node_count(self, node):
        return self.node_count[self.find(node)]

    def get_edge_count(self, node):
        return self.edge_count[self.find(node)]

    def is_root(self, node):
        return self.parent[node] == node


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        ds = DisjointSet(n)
        complete_components = 0

        # Process edges
        for u, v in edges:
            ds.union(u, v)

        # Count complete components
        for i in range(n):
            if ds.is_root(i):  # Check only root nodes
                nodes = ds.get_node_count(i)
                edges_count = ds.get_edge_count(i)

                # A complete component must have exactly (nodes * (nodes - 1)) / 2 edges
                if edges_count == (nodes * (nodes - 1)) // 2:
                    complete_components += 1

        return complete_components
        
# Java
"""
import java.util.*;

class DisjointSet {
    private int[] parent, edgeCount, nodeCount;
    
    public DisjointSet(int n) {
        parent = new int[n];
        edgeCount = new int[n];
        nodeCount = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;  
            nodeCount[i] = 1;
        }
    }

    public int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]); // Path compression
        }
        return parent[node];
    }

    // Union operation: merge two sets and update counts
    public void union(int u, int v) {
        int rootU = find(u);
        int rootV = find(v);

        edgeCount[rootU]++; // Increment edge count (undirected graph) because we are merging 'V' into 'U'

        if (rootU != rootV) {
            parent[rootV] = rootU; // Merge component V into U
            edgeCount[rootU] += edgeCount[rootV]; // Merge edge counts
            nodeCount[rootU] += nodeCount[rootV]; // Merge node counts
        }
    }

    public int getNodeCount(int node) {
        return nodeCount[find(node)];
    }

    public int getEdgeCount(int node) {
        return edgeCount[find(node)];
    }

    public boolean isRoot(int node) {
        return parent[node] == node;
    }
}

class Solution {
    public int countCompleteComponents(int n, int[][] edges) {
        DisjointSet ds = new DisjointSet(n);
        int completeComponents = 0;

        for (int[] edge : edges) {
            ds.union(edge[0], edge[1]);
        }

        // Count complete components
        for (int i = 0; i < n; i++) {
            if (ds.isRoot(i)) { // Check only root nodes
                int nodes = ds.getNodeCount(i);
                int edgesCount = ds.getEdgeCount(i);

                // A complete component must have exactly (nodes * (nodes - 1)) / 2 edges
                if (edgesCount == (nodes * (nodes - 1)) / 2) {
                    completeComponents++;
                }
            }
        }

        return completeComponents;
    }
}

"""
