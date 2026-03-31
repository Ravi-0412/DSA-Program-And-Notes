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
class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int n = graph.length;
        Set<Integer> visited = new HashSet<>();
        Set<Integer> path_visited = new HashSet<>();  // making this as local variable for each dfs call will give error
        List<Integer> ans = new ArrayList<>();

        // checking cycle
        boolean dfs(int node, int[][] graph, Set<Integer> visited, Set<Integer> path_visited, List<Integer> ans) {
            visited.add(node);
            path_visited.add(node);
            for (int nei : graph[node]) {
                if (!visited.contains(nei)) {
                    if (dfs(nei, graph, visited, path_visited, ans)) {
                        return true;  // means we have found a cycle. so simply return
                    }
                } else if (path_visited.contains(nei)) {
                    return true;  // means cycle so simply return
                }
            }
            // if neither of nei is part of a cycle means that is a safe node.
            ans.add(node);  // only extra line than cycle detection.
            path_visited.remove(node);
            return false;
        }

        for (int i = 0; i < n; i++) {
            if (!visited.contains(i)) {
                dfs(i, graph, visited, path_visited, ans);  // we have to call for each component. we don't have to return
            }
        }

        Collections.sort(ans);
        return ans;
    }

    private boolean dfs(int node, int[][] graph, Set<Integer> visited, Set<Integer> path_visited, List<Integer> ans) {
        visited.add(node);
        path_visited.add(node);
        for (int nei : graph[node]) {
            if (!visited.contains(nei)) {
                if (dfs(nei, graph, visited, path_visited, ans)) {
                    return true;
                }
            } else if (path_visited.contains(nei)) {
                return true;
            }
        }
        ans.add(node);
        path_visited.remove(node);
        return false;
    }
}

"""
# C++ Code 
"""
class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        unordered_set<int> visited;
        unordered_set<int> path_visited;  // making this as local variable for each dfs call will give error
        vector<int> ans;

        function<bool(int)> dfs = [&](int node) {
            visited.insert(node);
            path_visited.insert(node);
            for (int nei : graph[node]) {
                if (!visited.count(nei)) {
                    if (dfs(nei) == true) {  // means we have found a cycle. so simply return
                        return true;
                    }
                } else if (path_visited.count(nei)) {  // means cycle so simply return
                    return true;
                }
            }
            // if neither of nei is part of a cycle means that is a safe node.
            ans.push_back(node);  // only extra line than cycle detection.
            path_visited.erase(node);
            return false;
        };

        for (int i = 0; i < n; i++) {
            if (!visited.count(i)) {
                dfs(i);  // we have to call for each component. we don't have to return
            }
        }

        sort(ans.begin(), ans.end());
        return ans;
    }
};

"""

# Method 2: Kahn's Algo only
"""
Safe: Nodes that do not lead to a cycle are called "eventual safe nodes".
Terminal Nodes: These are the "ultimate" safe nodes (outdegree = 0).
If we reverse the graph, then terminal nodes (no outgoing edges) become sources.
Using Kahn’s algorithm (topological sort) on the reversed graph, we can find all nodes
that eventually lead to terminal nodes (i.e., safe nodes) by following paths backwards.

By reversing the edges, the original terminal nodes (outdegree 0) now have an indegree of 0 in the reversed graph.
Now, we can perform a standard Topological Sort starting from these terminal nodes.
If a node's outdegree becomes 0, it means all of its original outgoing edges now point to 
nodes that have been confirmed as "safe." Therefore, this node is now safe too! Add it to the queue.
Any node that was added to the queue is safe.

Time = sapce : O(V + E)
"""
from collections import deque, defaultdict
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        # reverse_graph[v] will store all nodes 'u' such that there is an edge u -> v
        reverse_graph = defaultdict(list)
        
        # In this reversed context, 'outdegree' of the original graph 
        # acts like 'indegree' for our Kahn's algorithm.
        outdegree = [0] * n

        # Step 1: Build the reversed graph and calculate original outdegrees
        for u in range(n):
            for v in graph[u]:
                # Original: u -> v | Reversed: v -> u
                reverse_graph[v].append(u)
                # Count how many outgoing edges node 'u' has
                outdegree[u] += 1

        # Step 2: Initialize queue with Terminal Nodes
        # A terminal node has an outdegree of 0 (no outgoing edges).
        queue = deque([i for i in range(n) if outdegree[i] == 0])
        
        # safe[i] will be True if node i is an eventual safe state
        is_safe = [False] * n

        # Step 3: Kahn's Algorithm (Topological Sort on reversed graph)
        while queue:
            curr = queue.popleft()
            is_safe[curr] = True
            
            # Look at all nodes 'prev' that point to the current 'safe' node
            for prev in reverse_graph[curr]:
                # Since 'curr' is safe, 'prev' has one less 'potentially unsafe' path
                outdegree[prev] -= 1
                
                # If outdegree becomes 0, ALL paths from 'prev' lead to safe nodes
                if outdegree[prev] == 0:
                    queue.append(prev)

        # Step 4: Collect all nodes marked as safe
        # We iterate from 0 to n-1 to ensure the result is sorted as required
        return [i for i in range(n) if is_safe[i]]

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
# C++ Code 
"""
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        unordered_map<int, vector<int>> reverse_graph;
        vector<int> indegree(n, 0);

        // Build reverse graph and count original outdegrees
        for (int u = 0; u < n; ++u) {
            for (int v : graph[u]) {
                reverse_graph[v].push_back(u);
                indegree[u]++;
            }
        }

        // Start with terminal nodes (outdegree 0)
        queue<int> q;
        for (int i = 0; i < n; ++i) {
            if (indegree[i] == 0) q.push(i);
        }

        vector<bool> safe(n, false);

        // Kahn's algorithm to find safe nodes
        while (!q.empty()) {
            int node = q.front(); q.pop();
            safe[node] = true;
            for (int prev : reverse_graph[node]) {
                indegree[prev]--;
                if (indegree[prev] == 0) {
                    q.push(prev);
                }
            }
        }

        // Collect and return safe nodes
        vector<int> result;
        for (int i = 0; i < n; ++i) {
            if (safe[i]) result.push_back(i);
        }
        sort(result.begin(), result.end());
        return result;
    }
};

"""
