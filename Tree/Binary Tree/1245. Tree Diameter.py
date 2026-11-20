"""
Question link: https://algo.monster/liteproblems/1245
"""

"""
DFS Logic — Thought Process
Step	Observation / Reasoning	Decision
1	The tree is undirected, so every edge is stored in both directions.	A child can also see its parent as a neighbour.
2	If DFS moves back to its parent, it can repeatedly traverse the same edge.	Skip the parent using if child == parent.
3	We start DFS from node 0, which has no parent.	Pass -1 as the initial parent.
4	A leaf node has no neighbours other than its parent.	The loop doesn't execute, so best = 0 is returned.
5	Each child returns its longest downward distance.	Add 1 to include the edge connecting the current node to that child.
6	A longest path through the current node can use two different branches.	Maintain the best and second-best distances and 
update the diameter using their sum.
7	The parent can extend the current path through only one branch.	Return only best.

Key takeaway: DFS returns the longest downward path, while best + second_best represents the longest path passing through the current node.
"""


from typing import List

class Solution:

    def treeDiameter(self, edges: List[List[int]]) -> int:

        n = len(edges) + 1
        adj = [[] for _ in range(n)]

        # Build adjacency list for the undirected tree
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.diameter = 0

        def dfs(node, parent):

            best = 0
            second_best = 0

            # Explore all children except the parent
            for child in adj[node]:

                if child == parent:
                    continue

                # Include the edge connecting the current node to its child
                current_path = 1 + dfs(child, node)

                # Maintain the two longest downward paths
                if current_path > best:
                    second_best = best
                    best = current_path

                elif current_path > second_best:
                    second_best = current_path

            # Longest path passing through this node
            self.diameter = max(
                self.diameter,
                best + second_best
            )

            # Return only the longest branch to the parent
            return best

        dfs(0, -1)

        return self.diameter

# Java
"""

import java.util.*;

class Solution {

    List<Integer>[] adj;
    int diameter;

    public int treeDiameter(int[][] edges) {

        int n = edges.length + 1;

        adj = new ArrayList[n];

        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }

        // Build adjacency list for the undirected tree
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];

            adj[u].add(v);
            adj[v].add(u);
        }

        diameter = 0;

        dfs(0, -1);

        return diameter;
    }

    private int dfs(int node, int parent) {

        int best = 0;
        int secondBest = 0;

        // Explore all children except the parent
        for (int child : adj[node]) {

            if (child == parent) {
                continue;
            }

            // Include the edge connecting the current node to its child
            int currentPath = 1 + dfs(child, node);

            // Maintain the two longest downward paths
            if (currentPath > best) {
                secondBest = best;
                best = currentPath;
            } else if (currentPath > secondBest) {
                secondBest = currentPath;
            }
        }

        // Longest path passing through the current node
        diameter = Math.max(diameter, best + secondBest);

        // Return only the longest branch to the parent
        return best;
    }
}

"""
