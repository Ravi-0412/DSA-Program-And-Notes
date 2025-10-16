"""
Theory:
1) It has capacity to detect whether a graph has negative weight cycle or not.
But Dijkastra can't do this.
Note: It can only detect negative weight cycle but can't give ans for negative weight cycle.

working:
Note: If we have 'n' nodes then, the shortest path in the graph will never contain more than 'n-1' edges.
1) Relax every edge 'n-1' times.
Relaxing means: Relaxing edge one time means we are finding the length of the shortest path
where each path has maximum one edge and so on seeing the previos iteration distance result.

2) Stop after 'n-1'th relaxation because length of the shortest path won't contain more than 'n-1' edge.
3) For checking 'negative' weight cycle , again one more time relax edge after 'n-1'th relaxation
and compare distance of any node. if there is better value then it means there is a negative weight cycle.

time- O(N*E) as each edge will get relaxed 'n' times, E= no of edges, N= no of vertices.

Note: Where to use this
1) When you have to find the minimum distance between all nodes from a source after 'k' iteration/stop etc.
e.g: 787. Cheapest Flights Within K Stops
"""

def BellmanFord(src,edges,n):
    distance= [999999]*n
    distance[src] = 0
    # to get the optimal ans if there is no negative weight cycle
    for i in range(n-1):
        tempDistance= distance.copy()
        for s,d,w in edges:
            if distance[s]==999999:  # first check if we have reached the source till now or not
                continue
            if tempDistance[d]> distance[s] +w:
                # if we can more optimise distance of 'd' using the calculation till now.
                tempDistance[d]= distance[s] + w
        distance= tempDistance.copy()   # will tell what is the minimum distance to all nodes from source
                                        # after 'i'th iteration.
    
    # now to check the negative cycle
    for s,d,w in edges:
        if distance[s]!= 999999 and distance[d] > distance[s] + w:  # first check if we have reached the source & getting more better ans
            print("negative weight cycle is there")
            return
    print(distance)
            
# let directed graph
edges= [[0, 1, -1],[0, 2, 4],[1,2,3],[1, 4, 2],[3, 2, 5],[3, 1, 1],[4, 3, -3]]
BellmanFord(0,edges,5)

# Java
"""
import java.util.*;

public class Solution {

    public void bellmanFord(int src, int[][] edges, int n) {
        int[] distance = new int[n];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[src] = 0;

        // Relax all edges (n - 1) times
        for (int i = 0; i < n - 1; i++) {
            int[] tempDistance = Arrays.copyOf(distance, n);

            for (int[] edge : edges) {
                int u = edge[0], v = edge[1], w = edge[2];

                if (distance[u] == Integer.MAX_VALUE) continue;

                if (tempDistance[v] > distance[u] + w) {
                    tempDistance[v] = distance[u] + w;
                }
            }

            distance = Arrays.copyOf(tempDistance, n);  // update distance after each pass
        }

        // Check for negative weight cycle
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];

            if (distance[u] != Integer.MAX_VALUE && distance[v] > distance[u] + w) {
                System.out.println("Negative weight cycle is there");
                return;
            }
        }

        // Print final distances
        System.out.println("Shortest distances from source " + src + ":");
        for (int i = 0; i < n; i++) {
            System.out.println("Node " + i + " --> " + (distance[i] == Integer.MAX_VALUE ? "INF" : distance[i]));
        }
    }
}
"""

