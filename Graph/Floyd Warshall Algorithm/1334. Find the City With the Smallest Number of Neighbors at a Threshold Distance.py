# Q: have to find the city from which we can reach the smallest no of nodes within the threshold.
# since we have to find the optimal for each city then only Algo comes into mind is 'Floyd Warshall Algo'.

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # first make the adjacency matrix
        adjMat= [[float('inf') for j in range(n)] for i in range(n)]
        for s, d, w in edges:
            adjMat[s][d]= w
            adjMat[d][s]= w
        # put '0' for i== j.
        for i in range(n):
            adjMat[i][i]= 0
        # now apply the Floyd warshall Algo.
        for via in range(n):
	        for i in range(n):
	            for j in range(n):
	                adjMat[i][j]= min(adjMat[i][j], (adjMat[i][via] + adjMat[via][j])) 
        # now for each vertex find the no of city that we can visit within the given threshold.
        MinCity= n +1  # will store the min count of reachable city for a node till now. initialisng with any number we can't visit.
        ans= -1   # will give the city number we are finding
        for i in range(n):
            count= 0  
            for j in range(n):
                if adjMat[i][j] <= distanceThreshold:
                    count+= 1
            if count < MinCity:
                MinCity= count 
                ans= i
            elif count== MinCity:
                ans= i
        return ans

# for finding the count of city(smallest reachable ) just subtract '-1' from the minCity as we were also including the same city while calculating.