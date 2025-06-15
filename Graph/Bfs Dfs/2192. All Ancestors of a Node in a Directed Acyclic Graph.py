# Method 1:

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
# Space Complexity: O(N^2) . Storing the ancestors: in the worst case if every node is an ancestor of every other node.
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
class Solution {
    List<Integer>[] adj;
    List<Integer>[] ans;

    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        adj = new ArrayList[n];
        ans = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
            ans[i] = new ArrayList<>();
        }

        // build the adjacency list
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            adj[u].add(v);
        }

        // call DFS for each node
        for (int i = 0; i < n; i++) {
            dfs(i, i, new boolean[n]);
        }

        // sort the ancestor lists
        for (int i = 0; i < n; i++) {
            Collections.sort(ans[i]);
        }

        return Arrays.asList(ans);
    }

    private void dfs(int parent, int curr, boolean[] visited) {
        visited[curr] = true;
        for (int neighbor : adj[curr]) {
            if (!visited[neighbor]) {
                ans[neighbor].add(parent); // add ancestor
                dfs(parent, neighbor, visited);
            }
        }
    }
}

"""

# C++
"""
class Solution {
public:
    vector<vector<int>> adj;
    vector<vector<int>> ans;

    vector<vector<int>> getAncestors(int n, vector<vector<int>>& edges) {
        adj.resize(n);
        ans.resize(n);

        // build the adjacency list
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            adj[u].push_back(v);
        }

        // call DFS for each node
        for (int i = 0; i < n; i++) {
            vector<bool> visited(n, false);
            dfs(i, i, visited);
        }

        // sort the ancestor lists
        for (int i = 0; i < n; i++) {
            sort(ans[i].begin(), ans[i].end());
        }

        return ans;
    }

    void dfs(int parent, int curr, vector<bool>& visited) {
        visited[curr] = true;
        for (int neighbor : adj[curr]) {
            if (!visited[neighbor]) {
                ans[neighbor].push_back(parent); // add ancestor
                dfs(parent, neighbor, visited);
            }
        }
    }
};
"""