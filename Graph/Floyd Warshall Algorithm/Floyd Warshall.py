"""
what does it give?
it gives shortest path between all pairs of vertices.
Also it can detect negative weight cycle but won't give ans for negative weight cycle.

Brute force
Apply Dijkastra one by one for each node(V).
Time: V*(ElogV)
a) for sparse graph, E = O(V),   time: O(V^2*logV)
b) for dense graph, E = O(V^2),  time: O(V^3*logV)


Optimised one using Flyodd Warshall Algo
Graph + DP.

logic: go via every node one by one
in this algo, we store the graph in adjacency matrix rather than adjacency list.
Like if we want to find shortest distance between (i, j) then we can take any node 'k' in between.

For each intermediate vertex k (from 0 to n-1), update the shortest distance between every pair (i, j):
matrix[i][j]= min(matrix[i][j],matrix[i][k]+matrix[k][j])  => If going from i to j via k is shorter than the current known path, update it.

for detecting negative weight cycle, check the distance of any node from itself, if negative it means 'negative weight cycle' exist.
since it should be always zero only but it has decreased and becomes negative.

Time: O(n^3)

Note: See the logic and theory in GATE notes page no: 142-144

# Submitted on gfg
"""

class Solution:
    def shortest_distance(self, matrix):
	    n= len(matrix)
	    # for simplicity change the weight of (i,i)= 0 and and if not edge then to 'inf'
	    for i in range(n):
	        for j in range(n):
	            if matrix[i][j]== -1:
	                matrix[i][j]= float('inf')
	            if i== j:
	                matrix[i][j]= 0
		
	# now apply the algorithm
	# Distance of shortest path between i -> j with {0, 1, 2,...k} as internal vertices.
	    for k in range(n):
	        for i in range(n):
	            for j in range(n):
	                matrix[i][j]= min(matrix[i][j], (matrix[i][k] + matrix[k][j]))
		
		# Note: If you will change the order of 'i', 'j' and 'k' then it won't work.
		
	    # for detecting the negative weight cycle
	    for i in range(n):
	        if matrix[i][i] <0:
	            print("there is negative weight cycle")
	            return
		            
	    # change while returning, change what we have changed at start
	    for i in range(n):
	        for j in range(n):
	            if matrix[i][j]== float('inf'):
	                matrix[i][j]= -1
	            if i== j:
	                matrix[i][j]= 0

# java
"""
import java.util.*;

public class Solution {
    public void shortest_distance(int[][] matrix) {
        int n = matrix.length;

        // Step 1: Replace -1 with INF and set matrix[i][i] = 0
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == -1)
                    matrix[i][j] = Integer.MAX_VALUE;
                if (i == j)
                    matrix[i][j] = 0;
            }
        }

        // Step 2: Apply Floyd-Warshall algorithm
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (matrix[i][k] != Integer.MAX_VALUE && matrix[k][j] != Integer.MAX_VALUE) {
                        matrix[i][j] = Math.min(matrix[i][j], matrix[i][k] + matrix[k][j]);
                    }
                }
            }
        }

        // Step 3: Detect negative weight cycles
        for (int i = 0; i < n; i++) {
            if (matrix[i][i] < 0) {
                System.out.println("There is a negative weight cycle");
                return;
            }
        }

        // Step 4: Replace INF back to -1 for output formatting
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == Integer.MAX_VALUE)
                    matrix[i][j] = -1;
                if (i == j)
                    matrix[i][j] = 0;
            }
        }

        // Optional: Print the matrix
        System.out.println("Shortest distance matrix:");
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
"""
