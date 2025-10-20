# Logic: Exact same as method 2 of Question: 87. Cheapest Flights Within K Stops

"""
Time : 

At most, each city can be visited with discounts from 0 → discounts, so:
Maximum states = n × (discounts + 1)
For each state, you explore all neighbors → average degree ~ m / n (but worst-case up to n)

Overall Time = O( (n × discounts) × log(n × discounts) + m × log(n × discounts) ) = O(m × log(n × discounts))

Space : (n × discounts) , Priority Queue (heap)
"""

import heapq
from collections import defaultdict

class Solution:
    def minimumCost(self, n: int, highways: list[list[int]], discounts: int) -> int:
        edges = defaultdict(list)    # Build adjacency list
        for u, v, toll in highways:
            edges[u].append((v, toll))
            edges[v].append((u, toll))  # Because roads are two-way

        # (total_cost, current_city, discounts_used)
        minHeap = [(0, 0, 0)]

        # Keep track of minimum discounts used to reach a city
        visited = dict()

        while minHeap:
            cost, city, used = heapq.heappop(minHeap)

            # If we reach destination, return cost
            if city == n - 1:
                return cost

            # If this city was already reached with fewer or equal discounts used → skip
            if city in visited and visited[city] <= used:
                continue
            visited[city] = used

            # Explore neighbors
            for nei, toll in edges[city]:
                # 1) Without using discount on this road
                heapq.heappush(minHeap, (cost + toll, nei, used))

                # 2) Use discount if available (toll // 2)
                if used < discounts:
                    heapq.heappush(minHeap, (cost + toll // 2, nei, used + 1))

        # If destination cannot be reached
        return -1


# Java
"""
import java.util.*;

class Solution {
    public int minimumCost(int n, int[][] highways, int discounts) {
        // Build adjacency list
        Map<Integer, List<int[]>> edges = new HashMap<>();
        for (int i = 0; i < n; i++) {
            edges.put(i, new ArrayList<>());
        }
        for (int[] h : highways) {
            int u = h[0], v = h[1], toll = h[2];
            edges.get(u).add(new int[]{v, toll});
            edges.get(v).add(new int[]{u, toll}); // roads are two-way
        }

        // (cost, city, discounts_used) -> Min-Heap based on cost
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        minHeap.offer(new int[]{0, 0, 0});

        // Keep track of minimum discounts used to reach a city
        Map<Integer, Integer> visited = new HashMap<>();

        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int cost = top[0], city = top[1], used = top[2];

            // If destination reached
            if (city == n - 1) {
                return cost;
            }

            // If already visited with fewer or equal discounts, skip
            if (visited.containsKey(city) && visited.get(city) <= used) {
                continue;
            }
            visited.put(city, used);

            // Explore neighbors
            for (int[] nxt : edges.get(city)) {
                int nei = nxt[0], toll = nxt[1];

                // 1) Without discount
                minHeap.offer(new int[]{cost + toll, nei, used});

                // 2) Use discount if available
                if (used < discounts) {
                    minHeap.offer(new int[]{cost + toll / 2, nei, used + 1});
                }
            }
        }
        return -1; // If no path exists
    }
}
"""


# C++
"""
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <limits>
#include <iostream>
using namespace std;

class Solution {
public:
    int minimumCost(int n, vector<vector<int>>& highways, int discounts) {
        // Build adjacency list
        vector<vector<pair<int, int>>> edges(n);
        for (auto& h : highways) {
            int u = h[0], v = h[1], toll = h[2];
            edges[u].push_back({v, toll});
            edges[v].push_back({u, toll}); // roads are two-way
        }

        // Min-heap of (cost, city, discounts_used)
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> minHeap;
        minHeap.push({0, 0, 0});

        // Keep track of minimum discounts used to reach a city
        unordered_map<int, int> visited;

        while (!minHeap.empty()) {
            auto top = minHeap.top();
            minHeap.pop();
            int cost = top[0], city = top[1], used = top[2];

            // If destination reached
            if (city == n - 1) {
                return cost;
            }

            // If city already visited with fewer or equal discounts, skip
            if (visited.count(city) && visited[city] <= used) {
                continue;
            }
            visited[city] = used;

            // Explore neighbors
            for (auto& nxt : edges[city]) {
                int nei = nxt.first;
                int toll = nxt.second;

                // 1) Without using discount
                minHeap.push({cost + toll, nei, used});

                // 2) Use discount if available
                if (used < discounts) {
                    minHeap.push({cost + toll / 2, nei, used + 1});
                }
            }
        }
        return -1; // If destination cannot be reached
    }
};
"""
