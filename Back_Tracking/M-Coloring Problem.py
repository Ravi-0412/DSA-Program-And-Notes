# Method 1: 

# try to color the node one by one with every possible color

# time: O(m^n): 
# Reason: Every node has 'm' possibility i.e we can color it with any of the 'm' color.

# space: O(n). Recursive depth

def graphColoring(graph, k, V):
    # first create  a adjacency list
    adj= {i:[] for i in range(V)}   # adj= collections.defaultdict(list)
    for i in range(V):
        for j in range(V):
            if graph[i][j]==1:
                adj[i].append(j)
    
    color= [0]*V   # using number 1,2,3....M for 'm' colors.                       
    return isColoringPossible(adj,color,k,V,0)

def isSafe(adj,color,node,node_col):
    for nei in adj[node]:
        if color[nei]== node_col:  # if adjacent node has same color then you can't color with chosen color
            return False
    return True


def isColoringPossible(adj,color,k,n,node):
    # try to color the given node with all possible color
    if node==n:   # means we have colored all the nodes
        return True
        
    for i in range(1,k+1):  
        # check if we can color 'node' with color 'i' safely.
        if isSafe(adj,color,node,i):
            color[node]= i
            # call the function to color the next node safely
            if isColoringPossible(adj,color,k,n,node+1):  
                # if we are able to color the current and next node(all nodes) safely then simply return.
                return True
            # if not possible to color all the nodes with chosen color then backtrack i.e try with different color
            color[node]= 0
    
    # if not possible to color any of the nodes with any of the color then it means not possible to color
    return False

# Java Code 
"""
import java.util.ArrayList;
import java.util.List;

public class GraphColoring {

    static boolean isSafe(List<List<Integer>> adj, int[] color, int node, int node_col) {
        for (int nei : adj.get(node)) {
            if (color[nei] == node_col) { // if adjacent node has same color then you can't color with chosen color
                return false;
            }
        }
        return true;
    }

    static boolean isColoringPossible(List<List<Integer>> adj, int[] color, int k, int n, int node) {
        // try to color the given node with all possible colors
        if (node == n) { // means we have colored all the nodes
            return true;
        }

        for (int i = 1; i <= k; i++) {
            // check if we can color 'node' with color 'i' safely.
            if (isSafe(adj, color, node, i)) {
                color[node] = i;
                // call the function to color the next node safely
                if (isColoringPossible(adj, color, k, n, node + 1)) {
                    // if we are able to color the current and next node(all nodes) safely then simply return.
                    return true;
                }
                // if not possible to color all the nodes with chosen color then backtrack i.e try with different color
                color[node] = 0;
            }
        }

        // if not possible to color any of the nodes with any of the colors then it means not possible to color
        return false;
    }

    static boolean graphColoring(int[][] graph, int k, int V) {
        // first create an adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                if (graph[i][j] == 1) {
                    adj.get(i).add(j);
                }
            }
        }

        int[] color = new int[V]; // using number 1,2,3....M for 'm' colors.
        return isColoringPossible(adj, color, k, V, 0);
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>

using namespace std;

bool isSafe(vector<vector<int>> &adj, vector<int> &color, int node, int node_col) {
    for (int nei : adj[node]) {
        if (color[nei] == node_col) { // if adjacent node has same color then you can't color with chosen color
            return false;
        }
    }
    return true;
}

bool isColoringPossible(vector<vector<int>> &adj, vector<int> &color, int k, int n, int node) {
    // try to color the given node with all possible color
    if (node == n) { // means we have colored all the nodes
        return true;
    }

    for (int i = 1; i <= k; i++) {
        // check if we can color 'node' with color 'i' safely.
        if (isSafe(adj, color, node, i)) {
            color[node] = i;
            // call the function to color the next node safely
            if (isColoringPossible(adj, color, k, n, node + 1)) {
                // if we are able to color the current and next node(all nodes) safely then simply return.
                return true;
            }
            // if not possible to color all the nodes with chosen color then backtrack i.e try with different color
            color[node] = 0;
        }
    }

    // if not possible to color any of the nodes with any of the color then it means not possible to color
    return false;
}

bool graphColoring(vector<vector<int>> &graph, int k, int V) {
    // first create an adjacency list
    vector<vector<int>> adj(V);
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            if (graph[i][j] == 1) {
                adj[i].push_back(j);
            }
        }
    }

    vector<int> color(V, 0); // using number 1,2,3....M for 'm' colors.
    return isColoringPossible(adj, color, k, V, 0);
}
"""