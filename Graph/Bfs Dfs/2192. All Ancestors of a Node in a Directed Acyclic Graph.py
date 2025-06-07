"""
Logic: 
1. Perform a DFS from every node in the graph.
2. During each DFS traversal:
   - Keep track of visited nodes to avoid cycles and unnecessary rework.
   - If you reach a node `child` during DFS from a node `parent`, then:
     - Add `parent` to the list of ancestors of `child`.
3. Repeat this for all nodes.
4. Finally, sort the list of ancestors for each node if needed.

Why DFS?
- DFS helps us explore all paths from a given starting node.
- It naturally allows us to track which nodes are reachable, and hence, identify ancestors.
- We avoid repeated work by using a visited array during traversal.

# Time; O(n*(n + m) + n*k logk), k = average number of ancestors per node, n  nodes, m = edges
"""
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        def dfs(parent, cur, visited):
            visited.add(cur)
            for nei in adj[cur]:
                if nei not in visited:
                    ans[nei].append(parent)
                    dfs(parent, nei, visited)

        ans = [[] for i in range(n)]
        for i in range(n):
            dfs(i, i, set())
        for i in range(n):
            ans[i].sort()
        return ans


# in java
"""
import java.util.*;

class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        Map<Integer, List<Integer>> adj = new HashMap<>();
        
        // Build adjacency list
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if (!adj.containsKey(u)) {
                adj.put(u, new ArrayList<>());
            }
            adj.get(u).add(v);
        }
        
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            ans.add(new ArrayList<>());
        }
        
        // DFS function
        for (int i = 0; i < n; i++) {
            Set<Integer> visited = new HashSet<>();
            dfs(i, i, visited, adj, ans);
        }
        
        // Sort the ancestor lists
        for (List<Integer> list : ans) {
            Collections.sort(list);
        }
        
        return ans;
    }
    
    private void dfs(int parent, int cur, Set<Integer> visited, Map<Integer, List<Integer>> adj, List<List<Integer>> ans) {
        visited.add(cur);
        
        if (!adj.containsKey(cur)) return;  // have to check this in java otherwise will get exception
        
        for (int nei : adj.get(cur)) {
            if (!visited.contains(nei)) {
                ans.get(nei).add(parent);
                dfs(parent, nei, visited, adj, ans);
            }
        }
    }
}

"""

Cpp code
"""
class Solution {
public:
    void dfs(int parent, int cur, vector<vector<int>>& adj, vector<vector<int>>& ans, vector<bool>& visited) {
        visited[cur] = true;
        for (int nei : adj[cur]) {
            if (!visited[nei]) {
                ans[nei].push_back(parent);
                dfs(parent, nei, adj, ans, visited);
            }
        }
    }

    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adj(n);
        vector<vector<int>> ans(n);
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
        }

        for (int i = 0; i < n; ++i) {
            vector<bool> visited(n, false);
            dfs(i, i, adj, ans, visited);
        }
        for (int i = 0; i < n; ++i) {
            sort(ans[i].begin(), ans[i].end());
        }

        return ans;
    }
};
"""
