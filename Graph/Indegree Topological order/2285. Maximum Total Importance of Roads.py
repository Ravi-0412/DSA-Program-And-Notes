# logic: 
# For the maximum result, we assign the highest value to a city with the largest degree (number of roads).

# We compute the degree of each node, and then sort them. 
# Finally, we assing increasing values starting from the smallest degree.

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree = [0] * n
        for u, v in roads:
            indegree[u] += 1
            indegree[v] += 1
        indegree.sort()
        ans = 0
        for i in range(n):
            ans += indegree[i] * (i + 1)   # (i +1 ) = value assigned , 
                                           # no of times 'i'th node value will be included in ans = indegree[i]
        return ans


# Java
"""
import java.util.Arrays;

class Solution {
    public long maximumImportance(int n, int[][] roads) {
        int[] indegree = new int[n];
        
        // Calculate the indegree of each node
        for (int[] road : roads) {
            indegree[road[0]]++;
            indegree[road[1]]++;
        }
        
        // Sort the indegree array
        Arrays.sort(indegree);
        
        long ans = 0;
        
        // Calculate the total importance
        for (int i = 0; i < n; i++) {
            ans += (long) (i + 1) * indegree[i];
        }
        
        return ans;
    }
}

"""