"""
logic: Just exacyly same as 'M-coloring'.
just treat garden as nodes and flowers as color.

" choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers."
This line tells that this is a 'M-coloring' problem only.

Here we have to print one of the possible ans.

Note: This will work for every Q of this type.

Note: there is no node that has more than 3 neighbors, always one possible color to choose.
so There must be one color availabe to color a node anytime.

Note: Due to this reason, this  brute force solution get accepted.
"""

# time: O(4**n)

import collections
from typing import List

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for u, v in paths:
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * (n + 1)  # 1-based indexing

        def isSafe(node, node_color):
            for nei in adj[node]:
                if color[nei] == node_color:
                    return False
            return True

        def isPlantingPossible(node):
            if node == n + 1:
                return True  # successfully assigned colors to all gardens

            for i in range(1, 5):  # Try flower types 1 to 4
                if isSafe(node, i):
                    color[node] = i
                    if isPlantingPossible(node + 1):
                        return True
                    # Backtrack not required explicitly since guaranteed to have a solution
            return False

        isPlantingPossible(1)
        return color[1:]  # Skip index 0 for 1-based result

# Java
"""
import java.util.*;

public class Solution {
    public int[] gardenNoAdj(int n, int[][] paths) {
        List<Integer>[] adj = new ArrayList[n + 1]; // 1-based indexing
        for (int i = 0; i <= n; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int[] edge : paths) {
            int u = edge[0];
            int v = edge[1];
            adj[u].add(v);
            adj[v].add(u);
        }

        int[] color = new int[n + 1]; // index 0 unused, flower types are 1 to 4

        // start from garden 1
        isPlantingPossible(1, n, color, adj);

        // return final answer skipping 0th index
        return Arrays.copyOfRange(color, 1, n + 1);
    }

    // check if it's safe to plant this color
    private boolean isSafe(int node, int nodeColor, int[] color, List<Integer>[] adj) {
        for (int nei : adj[node]) {
            if (color[nei] == nodeColor) return false;
        }
        return true;
    }

    private boolean isPlantingPossible(int node, int n, int[] color, List<Integer>[] adj) {
        if (node == n + 1) return true;

        for (int i = 1; i <= 4; i++) {
            if (isSafe(node, i, color, adj)) {
                color[node] = i;
                if (isPlantingPossible(node + 1, n, color, adj)) {
                    return true;
                }
                // No need to reset color[node] = 0 because a solution is guaranteed
            }
        }

        return false;
    }
}
"""


# method 2: will only work if no of color is > no of adjacent node for any node.
"""
Here no_of_color = 4 and max_no_adjacent_node_for_any_node = 3

logic: There must be one color availabe to color a node.

Note: Due to this reason,above brute force solution get accepted.
Reason: Because there is no node that has more than 3 neighbors, always one possible color to choose.

It says that there are 4 flowers to choose from, but each garden can only have 3 edges. 
This means that there must be a flower to choose from for each garden and 
you don't have to worry about choosing the order of the garden to plant flowers in.

Note: color every node with least value color available(not used by its neighbour).
"""

# time: O(4*n)

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj= collections.defaultdict(list)
        for u, v in paths:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        res= [0]*n  # for each flower, we have to return the color.
        # color each node with available color
        for i in range(n):
            used_colors= set()  # will store the used colors by the nei of node 'i'.
            # check whatever color has been used by its neighbour.
            # Add those into 'used_colors'
            for nei in adj[i]:
                used_colors.add(res[nei])
            # check which color has not been used till now by its nei.
            for color in range(1, 5):
                if color not in used_colors:
                    # if not used then color the cur node with cur 'color'.
                    res[i]= color
        return res

# Java
"""
import java.util.*;

public class Solution {
    public int[] gardenNoAdj(int n, int[][] paths) {
        List<Integer>[] adj = new ArrayList[n];
        
        // Initialize adjacency list
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }

        // Build the adjacency list (0-based indexing)
        for (int[] edge : paths) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            adj[u].add(v);
            adj[v].add(u);
        }

        int[] res = new int[n];  // will store the flower type for each garden (1 to 4)

        for (int i = 0; i < n; i++) {
            boolean[] usedColors = new boolean[5];  // index 1 to 4

            // Check which colors are already used by neighbors
            for (int neighbor : adj[i]) {
                int color = res[neighbor];
                if (color != 0) {
                    usedColors[color] = true;
                }
            }

            // Assign the first available color not used by neighbors
            for (int c = 1; c <= 4; c++) {
                if (!usedColors[c]) {
                    res[i] = c;
                    break;
                }
            }
        }

        return res;
    }
}
"""
