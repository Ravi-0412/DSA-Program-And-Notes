# Methiod 1: 

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

i) time: O(4*n) = O(n)
ii) Space Complexity: O(n + e)
adj stores all edges: O(n + e)
color array of size n + 1: O(n)
Recursion stack: up to O(n) in the worst case

"""

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

class Solution {
    Map<Integer, List<Integer>> adj = new HashMap<>();
    int[] color;
    int n;

    public int[] gardenNoAdj(int n, int[][] paths) {
        this.n = n;
        color = new int[n + 1];  // 1-based indexing

        // Build adjacency list
        for (int i = 1; i <= n; i++) {
            adj.put(i, new ArrayList<>());
        }
        for (int[] path : paths) {
            adj.get(path[0]).add(path[1]);
            adj.get(path[1]).add(path[0]);
        }

        // Start backtracking from garden 1
        isPlantingPossible(1);
        return Arrays.copyOfRange(color, 1, n + 1);  // Skip index 0 for 1-based result
    }

    // Check if the current flower color is safe for the garden
    private boolean isSafe(int node, int nodeColor) {
        for (int neighbor : adj.get(node)) {
            if (color[neighbor] == nodeColor) return false;
        }
        return true;
    }

    // Try assigning colors recursively to each garden
    private boolean isPlantingPossible(int node) {
        if (node == n + 1) return true;

        for (int i = 1; i <= 4; i++) {  // Try flower types 1 to 4
            if (isSafe(node, i)) {
                color[node] = i;
                if (isPlantingPossible(node + 1)) return true;
                // Backtracking step not needed since problem guarantees a solution
            }
        }
        return false;
    }
}
"""


# C++
"""
class Solution {
public:
    vector<vector<int>> adj;
    vector<int> color;
    int n;

    vector<int> gardenNoAdj(int n, vector<vector<int>>& paths) {
        this->n = n;
        color.resize(n + 1, -1);  // 1-based indexing
        adj.resize(n + 1);

        // Build adjacency list
        for (auto& path : paths) {
            adj[path[0]].push_back(path[1]);
            adj[path[1]].push_back(path[0]);
        }

        // Start backtracking from garden 1
        isPlantingPossible(1);
        vector<int> result(color.begin() + 1, color.end());  // Skip index 0
        return result;
    }

    // Check if the current flower color is safe for the garden
    bool isSafe(int node, int nodeColor) {
        for (int nei : adj[node]) {
            if (color[nei] == nodeColor) return false;
        }
        return true;
    }

    // Try assigning colors recursively to each garden
    bool isPlantingPossible(int node) {
        if (node == n + 1) return true;

        for (int i = 1; i <= 4; i++) {  // Try flower types 1 to 4
            if (isSafe(node, i)) {
                color[node] = i;
                if (isPlantingPossible(node + 1)) return true;
                // Backtracking step not needed since problem guarantees a solution
            }
        }
        return false;
    }
};
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

i) time: O(4*n) = O(n)
ii) Space Complexity: O(n + e)
adj stores all edges: O(n + e)
color array of size n + 1: O(n)
Recursion stack: up to O(n) in the worst case

"""


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

class Solution {
    public int[] gardenNoAdj(int n, int[][] paths) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] path : paths) {
            adj.get(path[0] - 1).add(path[1] - 1);
            adj.get(path[1] - 1).add(path[0] - 1);
        }

        int[] res = new int[n];  // for each flower, we have to return the color

        // color each node with available color
        for (int i = 0; i < n; i++) {
            boolean[] usedColors = new boolean[5];  // will store the used colors by the nei of node 'i'

            // check whatever color has been used by its neighbor.
            for (int nei : adj.get(i)) {
                usedColors[res[nei]] = true;  // mark used
            }

            // check which color has not been used till now by its nei.
            for (int color = 1; color <= 4; color++) {
                if (!usedColors[color]) {
                    // if not used then color the current node with current 'color'
                    res[i] = color;
                    break;
                }
            }
        }

        return res;
    }
}
"""


# C++
"""
class Solution {
public:
    vector<int> gardenNoAdj(int n, vector<vector<int>>& paths) {
        vector<vector<int>> adj(n);
        for (auto& path : paths) {
            adj[path[0] - 1].push_back(path[1] - 1);
            adj[path[1] - 1].push_back(path[0] - 1);
        }

        vector<int> res(n, 0);  // for each flower, we have to return the color

        // color each node with available color
        for (int i = 0; i < n; i++) {
            vector<bool> usedColors(5, false);  // will store the used colors by the nei of node 'i'

            // check whatever color has been used by its neighbor
            for (int nei : adj[i]) {
                usedColors[res[nei]] = true;  // mark used
            }

            // check which color has not been used till now by its nei.
            for (int color = 1; color <= 4; color++) {
                if (!usedColors[color]) {
                    // if not used then color the current node with current 'color'
                    res[i] = color;
                    break;
                }
            }
        }

        return res;
    }
};
"""