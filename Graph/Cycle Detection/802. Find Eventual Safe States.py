"""
Note: Terminal nodes has no outgoing vertices so these can't be part of a cycle.
And safe nodes will have all its edges to terminal nodes only so this also can't be part of any cycle.

Except these nodes i.e terminal and safe all nodes will be part of cycle .

logic of above: since terminal will be the nodes having no adjacent node and 
safe nodes are those nodes which have only terminal or safe node as adjacent node.
i.e if any node reaches to any terminal or safe node then it will not go back. so will not form a cycle.

vvi: So basically we have to find the 'nodes which doesn't belong to any of cycle formed'.

One thing to keep in mind:
Also we do not have to include those nodes which is directly not included in cycle but is a part of cycle i.e 
it is directly connected to any node which is directly included in the cycle.

how to solve: just try to find the cycle and if you don't encounter a cycle 
then all nodes from starting to where call ended(will end only at any terminal node)
will be safe only since they are not part of any cycle.

exactly same code as cycle detction in directed graph using dfs.
only one extra line added to include the node in the ans that's it.

Note: All terminal node is a safe node since all paths from terminal node go to same terminal node.
"""

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n= len(graph)
        visited= set()
        path_visited= set()   # making this as local variable for each dfs call will give error
        ans= []

        def dfs(node):   #checking cycle
            visited.add(node)
            path_visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei)== True:   # means we have found a cycle. so simply return we don't have to include any node as safe.
                        return True
                elif nei in path_visited:   # means cycle so simply return, because all nodes part of this cycle will not be in our ans.
                    return True
            # if neither of nei is part of a cycle means that is a safe node.
            ans.append(node)    # only extra line than cycle detection.
            path_visited.remove(node)
            return False

        for i in range(n):
            if i not in visited:
                dfs(i)     # we have to call for each component. we don't have to return 
        ans.sort()
        return ans

# Java
"""
import java.util.*;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        boolean[] visited = new boolean[n];
        boolean[] pathVisited = new boolean[n];
        boolean[] isSafe = new boolean[n];
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i, graph, visited, pathVisited, isSafe);
            }
        }

        for (int i = 0; i < n; i++) {
            if (isSafe[i]) {
                result.add(i);
            }
        }

        return result;
    }

    private boolean dfs(int node, int[][] graph, boolean[] visited, boolean[] pathVisited, boolean[] isSafe) {
        visited[node] = true;
        pathVisited[node] = true;

        for (int nei : graph[node]) {
            if (!visited[nei]) {
                if (dfs(nei, graph, visited, pathVisited, isSafe)) {
                    return true; // Found cycle
                }
            } else if (pathVisited[nei]) {
                return true; // Found cycle
            }
        }

        isSafe[node] = true; // No cycle found from this node
        pathVisited[node] = false;
        return false;
    }
}
"""

# Method 2: Kahn's Algo only
"""
Nodes that do not lead to a cycle are called "eventual safe nodes".
If we reverse the graph, then terminal nodes (no outgoing edges) become sources.
Using Kahn’s algorithm (topological sort) on the reversed graph, we can find all nodes
that eventually lead to terminal nodes (i.e., safe nodes) by following paths backwards.
Any node that can reach a terminal node without hitting a cycle is marked safe.
"""
from collections import deque, defaultdict
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        reverse_graph = defaultdict(list)
        indegree = [0] * n

        # Build reverse graph and count original outdegrees
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
                indegree[u] += 1

        # Start with terminal nodes (outdegree 0)
        queue = deque([i for i in range(n) if indegree[i] == 0])
        safe = [False] * n

        # Kahn's algorithm to find safe nodes
        while queue:
            node = queue.popleft()
            safe[node] = True
            for prev in reverse_graph[node]:
                indegree[prev] -= 1
                if indegree[prev] == 0:
                    queue.append(prev)

        # Collect and return safe nodes
        return sorted(i for i, val in enumerate(safe) if val)

# Java
"""
import java.util.*;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        List<List<Integer>> reverseGraph = new ArrayList<>();
        int[] indegree = new int[n];

        // Step 1: Create reverse graph
        for (int i = 0; i < n; i++) {
            reverseGraph.add(new ArrayList<>());
        }

        for (int u = 0; u < n; u++) {
            for (int v : graph[u]) {
                reverseGraph.get(v).add(u); // Reverse the edge u -> v to v -> u
                indegree[u]++; // Original node u has an outgoing edge, count for indegree
            }
        }

        // Step 2: Topological sort using Kahn's algorithm
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i); // Terminal nodes in original graph
            }
        }

        boolean[] isSafe = new boolean[n];

        while (!queue.isEmpty()) {
            int node = queue.poll();
            isSafe[node] = true;

            for (int prev : reverseGraph.get(node)) {
                indegree[prev]--;
                if (indegree[prev] == 0) {
                    queue.offer(prev);
                }
            }
        }

        // Step 3: Collect safe nodes and sort
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (isSafe[i]) {
                result.add(i);
            }
        }

        Collections.sort(result);
        return result;
    }
}
"""
