# Method 1:

# exactly same as Prim's algo
# logic: 1st make adjacency list
# after that it is totally same as prim's algo.

# for adjacency list we will have to take distance between every pair of node,
# and all node will be adjacnet to each other  => O(n^2)

# Time: o(E*logV) + O(n^2)


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


# correct solution

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