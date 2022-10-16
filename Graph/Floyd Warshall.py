# logic: go via every node one by one
# in this algo, we store the graph in adjacency matrix rather than adjacency list
# submitted on gfg
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
	    for via in range(n):
	        for i in range(n):
	            for j in range(n):
	                matrix[i][j]= min(matrix[i][j], (matrix[i][via] + matrix[via][j]))
		
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



