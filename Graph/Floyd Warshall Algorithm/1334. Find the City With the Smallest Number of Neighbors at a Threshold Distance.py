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

# Java Code 
"""
class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        // first make the adjacency matrix
        int INF = (int)1e9;
        int[][] adjMat = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(adjMat[i], INF);
        }
        for (int[] edge : edges) {
            int s = edge[0], d = edge[1], w = edge[2];
            adjMat[s][d] = w;
            adjMat[d][s] = w;
        }
        // put '0' for i == j.
        for (int i = 0; i < n; i++) {
            adjMat[i][i] = 0;
        }
        // now apply the Floyd warshall Algo.
        for (int via = 0; via < n; via++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (adjMat[i][via] == INF || adjMat[via][j] == INF) continue;
                    adjMat[i][j] = Math.min(adjMat[i][j], adjMat[i][via] + adjMat[via][j]);
                }
            }
        }
        // now for each vertex find the no of city that we can visit within the given threshold.
        int MinCity = n + 1;  // will store the min count of reachable city for a node till now. initializing with any number we can't visit.
        int ans = -1;         // will give the city number we are finding
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (adjMat[i][j] <= distanceThreshold) {
                    count++;
                }
            }
            if (count < MinCity) {
                MinCity = count;
                ans = i;
            } else if (count == MinCity) {
                ans = i;
            }
        }
        return ans;
    }
}

"""

# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findTheCity(int n, vector<vector<int>>& edges, int distanceThreshold) {
        // first make the adjacency matrix
        vector<vector<int>> adjMat(n, vector<int>(n, INT_MAX));
        for (auto &edge : edges) {
            int s = edge[0], d = edge[1], w = edge[2];
            adjMat[s][d] = w;
            adjMat[d][s] = w;
        }
        // put '0' for i == j.
        for (int i = 0; i < n; i++) {
            adjMat[i][i] = 0;
        }
        // now apply the Floyd warshall Algo.
        for (int via = 0; via < n; via++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (adjMat[i][via] == INT_MAX || adjMat[via][j] == INT_MAX) continue;
                    adjMat[i][j] = min(adjMat[i][j], adjMat[i][via] + adjMat[via][j]);
                }
            }
        }
        // now for each vertex find the no of city that we can visit within the given threshold.
        int MinCity = n + 1;  // will store the min count of reachable city for a node till now. initializing with any number we can't visit.
        int ans = -1;         // will give the city number we are finding
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (adjMat[i][j] <= distanceThreshold) {
                    count++;
                }
            }
            if (count < MinCity) {
                MinCity = count;
                ans = i;
            } else if (count == MinCity) {
                ans = i;
            }
        }
        return ans;
    }
};

"""