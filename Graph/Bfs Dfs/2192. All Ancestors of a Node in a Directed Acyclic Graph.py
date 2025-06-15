# Logic: Perform a DFS from each node to identify all nodes that can reach the current node. 
# During this traversal, mark nodes as visited to avoid cycles and repeated work.
# While performing the DFS, if we reach a node, we add the starting node (ancestor) 
# to the list of ancestors for the reached node.

# Time; O(n*(n + m) + n*k logk), k = average number of ancestors per node, n  nodes, m = edges

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