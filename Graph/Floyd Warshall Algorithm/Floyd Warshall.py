# what does it give?
# it gives shortest path between all pairs of vertices.
# Also it can detect negative weight cycle but won't give ans for negative weight cycle.

# Brute force
# Apply Dijkastra one by one for each node(V).
# Time: V*(ElogV)
# a) for sparse graph, E = O(V),   time: O(V^2*logV)
# b) for dense graph, E = O(V^2),  time: O(V^3*logV)


# Optimised one using Flyodd Warshall Algo
# Graph + DP.

# logic: go via every node one by one
# in this algo, we store the graph in adjacency matrix rather than adjacency list.

# for detecting negative weight cycle, check the distance of any node from itself, if negative it means 'negative weight cycle' exist.
# since it should be always zero only but it has decreased and becomes negative.

# Time: O(n^3)

# Note: See the logic and theory in GATE notes page no: 142-144

# Submitted on gfg

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



