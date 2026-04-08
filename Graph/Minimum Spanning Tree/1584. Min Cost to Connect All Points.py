# exactly same as Prim's algo
# logic: 1st make adjacency list
# after that it is totally same as prim's algo.

# for adjacency list we will have to take distance between every pair of node,
# and all node will be adjacnet to each other  => O(n^2)

# Time: o(n^2 * logn^2) + O(n^2) = O(N^2 * logN)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj= defaultdict(list)
        for i in range(len(points)):
            x1,y1= points[i]
            for j in range(i+1, len(points)):
                x2,y2= points[j]
                distance= abs(x1-x2) + abs(y1-y2)
                adj[i].append((j,distance))
                adj[j].append((i,distance))

        # after this totally prim's algo
        visited= set()
        min_mst= 0
        min_heap= [(0,0)]  # (weight, node)
        while len(visited) < len(points):
            w1,n1= heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add(n1)
            min_mst+= w1
            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap,(w2, n2))
        return min_mst


# my mistake: i was creating adjacency list like this
for i in range(len(points)//2 +1):  # if you do like this then you will miss all the edges after mid to the remaining nodes
    x1,y1= points[i]
    for j in range(i+1,len(points)):
        if i==j:
            continue
        x2,y2= points[j]
        distance= abs(x1-x2) + abs(y1-y2)
        adj[i].append((j,distance))
        adj[j].append((i, distance))

# method 2:
# Time  : same as above
import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        Optimal Prim's Algorithm for a Complete Graph.
        Time: O(N^2 log N) | Space: O(N)
        """
        n = len(points)
        min_mst_cost = 0
        visited = set()
        
        # min_heap stores: (cost_to_reach_node, node_index)
        # We start with node 0. The cost to include the first node is always 0.
        min_heap = [(0, 0)]
        
        while len(visited) < n:
            cost, u = heapq.heappop(min_heap)
            
            # If the node is already part of our MST, skip it
            if u in visited:
                continue
            
            # 1. Add node to MST
            visited.add(u)
            min_mst_cost += cost
            
            # 2. Explore all neighbors (all other points)
            # In a complete graph, every other point is a neighbor.
            for v in range(n):
                if v not in visited:
                    # Calculate Manhattan distance on the fly to save O(N^2) space
                    dist = abs(points[u][0] - points[v][0]) + \
                           abs(points[u][1] - points[v][1])
                    
                    heapq.heappush(min_heap, (dist, v))
                    
        return min_mst_cost

# Java Code 
"""
import java.util.*;

public class Solution {
    public int minCostConnectPoints(int[][] points) {
        int n = points.length;
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        // Build adjacency list (graph) with Manhattan distances
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                int distance = Math.abs(x1 - x2) + Math.abs(y1 - y2);
                adj.get(i).add(new int[]{j, distance});
                adj.get(j).add(new int[]{i, distance});
            }
        }

        Set<Integer> visited = new HashSet<>();
        int min_mst = 0;
        PriorityQueue<int[]> min_heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        // min_heap stores int[]{weight, node}
        min_heap.offer(new int[]{0, 0}); // start from node 0 with weight 0

        while (visited.size() < n) {
            int[] top = min_heap.poll();
            int w1 = top[0], n1 = top[1];
            if (visited.contains(n1)) continue;
            visited.add(n1);
            min_mst += w1;
            for (int[] neighbor : adj.get(n1)) {
                int n2 = neighbor[0], w2 = neighbor[1];
                if (!visited.contains(n2)) {
                    min_heap.offer(new int[]{w2, n2});
                }
            }
        }
        return min_mst;
    }
}

"""

# C++ Code 
"""
#include <vector>
#include <queue>
#include <cmath>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        vector<vector<pair<int,int>>> adj(n);

        // Build adjacency list (graph) with Manhattan distances
        for (int i = 0; i < n; i++) {
            int x1 = points[i][0], y1 = points[i][1];
            for (int j = i + 1; j < n; j++) {
                int x2 = points[j][0], y2 = points[j][1];
                int distance = abs(x1 - x2) + abs(y1 - y2);
                adj[i].emplace_back(j, distance);
                adj[j].emplace_back(i, distance);
            }
        }

        unordered_set<int> visited;
        int min_mst = 0;
        // min_heap stores pairs (weight, node)
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> min_heap;
        min_heap.push({0, 0}); // start from node 0 with weight 0

        while ((int)visited.size() < n) {
            auto [w1, n1] = min_heap.top();
            min_heap.pop();
            if (visited.count(n1))
                continue;
            visited.insert(n1);
            min_mst += w1;
            for (auto& [n2, w2] : adj[n1]) {
                if (!visited.count(n2)) {
                    min_heap.push({w2, n2});
                }
            }
        }
        return min_mst;
    }
};

"""
