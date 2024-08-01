""""
if we view each start_i and end_i as nodes in a graph, elements in pairs as (directed) edges in the graph then,
the problem ask us to use up all edges, so we are basically asked to find a Eulerian Path, 
which is a path that walks through each edge exactly once.

Some Properties of Eulerian Path

#  in[i] (and out[i]) to denote the in (and out) degree of a node i.
Existence:
# A graph has an Eulerian Path if and only if
1) we have out[i] == in[i] for each node i. Or
ii) we have out[i] == in[i] for all nodes i except exactly two nodes x and y, with out[x] = in[x] + 1, out[y] = in[y] - 1.
In the first case (out[i] == in[i] for each node i), all Eulerian Paths are also Eulerian Circuits 
(Eulerian Path with starting point == ending point).
Note: a node with out[i] == in[i] + 1 must be the starting point of an Eulerian Path (if there exists one).

# Note: this problem guarantees that an Eulerian Path exists. So we don't need to check for its existence here.

Algorithm

find the starting point of an Eulerian Path.
if we have out[i] == in[i] for all i, we can start at an arbitrary node.
perform postorder DFS on the graph, as we "walk" through an edge, we erase (or mark it visited) the walked edge.
we may reach the same node many times, but we have to pass each edge exactly once.
I use stack in my code for erasing edges.

"""

from collections import defaultdict, Counter
from typing import List

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)  # graph
        in_degree, out_degree = Counter(), Counter()  # in-degree, out-degree
        
        for u, v in pairs:
            g[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1

        start = pairs[0][0]  # Start anywhere if it's an Eulerian cycle.
        for p in out_degree:
            if out_degree[p] - in_degree[p] == 1:  # It's an Eulerian trail. Have to start here
                start = p
                break
        
        # Hierholzer's Algorithm:
        route = []
        stack = [start]
        while stack:
            while g[stack[-1]]:
                next_node = g[stack[-1]].pop()
                stack.append(next_node)
            route.append(stack.pop())
        
        route.reverse()
        # Now get all the edges and return in a list
        return [[route[i], route[i + 1]] for i in range(len(route) - 1)]


# java
"""
import java.util.*;

public class Solution {
    public int[][] validArrangement(int[][] pairs) {
        Map<Integer, List<Integer>> g = new HashMap<>();
        Map<Integer, Integer> inDegree = new HashMap<>();
        Map<Integer, Integer> outDegree = new HashMap<>();

        // Building the graph and calculating in-degrees and out-degrees
        for (int[] pair : pairs) {
            g.putIfAbsent(pair[0], new ArrayList<>());
            g.get(pair[0]).add(pair[1]);
            outDegree.put(pair[0], outDegree.getOrDefault(pair[0], 0) + 1);
            inDegree.put(pair[1], inDegree.getOrDefault(pair[1], 0) + 1);
        }

        // Determine the start node for Hierholzer's algorithm
        int start = pairs[0][0];
        for (int node : outDegree.keySet()) {
            if (outDegree.get(node) - inDegree.getOrDefault(node, 0) == 1) {
                start = node;
                break;
            }
        }

        // Hierholzer's Algorithm to find Eulerian path or cycle
        List<Integer> route = new ArrayList<>();
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(start);
        
        while (!stack.isEmpty()) {
            while (g.containsKey(stack.peek()) && !g.get(stack.peek()).isEmpty()) {
                stack.push(g.get(stack.peek()).remove(g.get(stack.peek()).size() - 1));
            }
            route.add(stack.pop());
        }

        Collections.reverse(route);

        // Convert the route into the list of pairs
        int[][] result = new int[route.size() - 1][2];
        for (int i = 0; i < route.size() - 1; i++) {
            result[i][0] = route.get(i);
            result[i][1] = route.get(i + 1);
        }

        return result;
    }
}
"""

# Other method 
from collections import defaultdict, deque

class Solution:
    def validArrangement(self, pairs):
        m = len(pairs)
        # Initialize the graph and degree counts
        adj = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        # Populate the graph and degree counts
        for u, v in pairs:
            out_degree[u] += 1
            in_degree[v] += 1
            adj[u].append(v)
        
        # Find the starting node
        start = -1
        for node in adj:
            if out_degree[node] - in_degree[node] == 1:
                start = node
                break
        
        if start == -1:
            # Eulerian Circuit -> start at any node
            start = next(iter(adj))
        
        ans = []
        self.euler(adj, ans, start)
        ans.reverse()
        return ans
    
    def euler(self, adj, ans, curr):
        stack = adj[curr]
        while stack:
            nei = stack.popleft()
            self.euler(adj, ans, nei)
            ans.append([curr, nei])

# java
""""


import java.util.*;

public class Solution {
    public int[][] validArrangement(int[][] pairs) {
        int m = pairs.length;
        // Initialize the graph and degree counts
        Map<Integer, Deque<Integer>> adj = new HashMap<>();
        Map<Integer, Integer> inDegree = new HashMap<>();
        Map<Integer, Integer> outDegree = new HashMap<>();
        
        // Populate the graph and degree counts
        for (int[] pair : pairs) {
            int u = pair[0], v = pair[1];
            adj.putIfAbsent(u, new ArrayDeque<>());
            adj.get(u).add(v);
            outDegree.put(u, outDegree.getOrDefault(u, 0) + 1);
            inDegree.put(v, inDegree.getOrDefault(v, 0) + 1);
        }
        
        // Find the starting node
        int start = -1;
        for (int node : adj.keySet()) {
            if (outDegree.getOrDefault(node, 0) - inDegree.getOrDefault(node, 0) == 1) {
                start = node;
                break;
            }
        }
        
        if (start == -1) {
            // Eulerian Circuit -> start at any node
            start = adj.keySet().iterator().next();
        }
        
        List<int[]> ans = new ArrayList<>();
        euler(adj, ans, start);
        Collections.reverse(ans);
        
        // Convert List<int[]> to int[][]
        int[][] result = new int[ans.size()][2];
        for (int i = 0; i < ans.size(); i++) {
            result[i] = ans.get(i);
        }
        
        return result;
    }
    
    private void euler(Map<Integer, Deque<Integer>> adj, List<int[]> ans, int curr) {
        Deque<Integer> stack = adj.get(curr);
        while (stack != null && !stack.isEmpty()) {
            int nei = stack.pollFirst();
            euler(adj, ans, nei);
            ans.add(new int[] { curr, nei });
        }
    }
}

"""