# Method 1: 

# logic: just we have to connect all the village with water.
# for this there are two ways: 1) either buliding wells at the village or 2) connecting by pipes through already connected village.

# since we have to connect all village with minimum cost then minimum spanning tree should come into mind.

# how to do?
# Ans: First we have to build well at any of the village then only we can connect other villages through it 
# otherwise we will build the wells at other villages also.

# Note: We don't know digging well at which village will give optimal ans, we can get starting from any village.
# so put cost of all building wells at all villages into heap and then after that totally same as mst.

import collections
import heapq

def supplyWater(n, k, wells, pipes):
	adj= collections.defaultdict(list)
	for s,d,c in pipes:
		adj[s].append((d, c))
		adj[d].append((s, c))
	minHeap= []
	for i in range(n):
		heapq.heappush(minHeap, (wells[i], i+1))
	visited= set()
	minCost= 0
	while minHeap:
		w1, n1= heapq.heappop(minHeap)
		if n1 in visited:
			continue
		visited.add(n1)
		minCost += w1
		if len(visited)== n:
			return minCost
		for n2,w2 in adj[n1]:
			if n2 not in visited:
				heapq.heappush(minHeap, (w2, n2))
	

# Java
"""
import java.util.*;

public class Solution {
    public int supplyWater(int n, int k, int[] wells, int[][] pipes) {
        Map<Integer, List<int[]>> adj = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            adj.put(i, new ArrayList<>());
        }

        for (int[] pipe : pipes) {
            int s = pipe[0], d = pipe[1], c = pipe[2];
            adj.get(s).add(new int[]{d, c});
            adj.get(d).add(new int[]{s, c});
        }

        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        for (int i = 0; i < n; i++) {
            minHeap.offer(new int[]{wells[i], i + 1});
        }

        Set<Integer> visited = new HashSet<>();
        int minCost = 0;

        while (!minHeap.isEmpty()) {
            int[] top = minHeap.poll();
            int w1 = top[0], n1 = top[1];
            if (visited.contains(n1)) continue;

            visited.add(n1);
            minCost += w1;

            if (visited.size() == n) return minCost;

            for (int[] neighbor : adj.get(n1)) {
                int n2 = neighbor[0], w2 = neighbor[1];
                if (!visited.contains(n2)) {
                    minHeap.offer(new int[]{w2, n2});
                }
            }
        }
        return minCost;
    }
}


"""


# C++
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int supplyWater(int n, int k, vector<int>& wells, vector<vector<int>>& pipes) {
        unordered_map<int, vector<pair<int, int>>> adj;
        for (auto& pipe : pipes) {
            int s = pipe[0], d = pipe[1], c = pipe[2];
            adj[s].push_back({d, c});
            adj[d].push_back({s, c});
        }

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;
        for (int i = 0; i < n; ++i) {
            minHeap.push({wells[i], i + 1});
        }

        unordered_set<int> visited;
        int minCost = 0;

        while (!minHeap.empty()) {
            auto [w1, n1] = minHeap.top(); minHeap.pop();
            if (visited.count(n1)) continue;

            visited.insert(n1);
            minCost += w1;

            if (visited.size() == n) return minCost;

            for (auto& [n2, w2] : adj[n1]) {
                if (!visited.count(n2)) {
                    minHeap.push({w2, n2});
                }
            }
        }
        return minCost;
    }
};


"""