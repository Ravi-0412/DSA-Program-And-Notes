"""
mostly same logic as Dijkastra.
Only difference is 1) when you find optimal weight for any node then add that our ans.
2) While adding add the weight of neigbour instead of total weight till now.

not able to print the exact path(edges). Have to ask someone.

# Note: Whenever you are asked directly or indirectly to find the :
# 1) minimum cost to connect all points/nodes (or anything) given some cost/distance between each point
"""
from collections import defaultdict
import heapq
def Prim(adj, src, n):
    edges= defaultdict(list)
    parent= [-1]*n
    for u,v,w in adj:
        edges[u].append((v,w))
        edges[v].append((u,w))
    visited= set()
    min_mst= 0
    min_heap= [(0,src)]   # you can start with any node this, will not affect the ans 
    while len(visited) < n:
        w1,n1 = heapq.heappop(min_heap)
        print(n1, end="-")
        if n1 in visited:  # this will automatically check whether all nodes get included or not. so no need to check the condition "if len(visited)==n:"
            continue
        visited.add(n1)
        min_mst += w1   # different from Dijkastra.. Adding the weight of edges coming under MST
        for n2,w2 in edges[n1]:
            if n2 not in visited:
                parent[n2]= n1
                heapq.heappush(min_heap,(w2, n2))  # here little change from dijkastra as in this we have to add the weight of all edges which will be come under MST
                                                   # Instead of adding 'w1+w2' like Dijkastra here adding only 'w2'.

    print("cost of minimum spanning tree is:", min_mst)

# adj= [[0,1,28],[0,5,10],[1,0,28],[1,6,14],[1,2,16],[2,1,16],[2,3,12],[3,6,18],[3,2,12],[3,4,22],[4,6,24],[4,5,25],[5,0,10],[4,3,22],[5,4,25],[6,1,14],[6,4,24],[6,3,18]] # ans= 99
adj= [[0,2,3],[1,3,4],[1,2,10],[2,1,10],[2,3,2],[2,4,6],[2,0,3],[3,1,4],[3,2,2],[3,4,1],[4,2,6],[4,3,1]]  # ans= 10
# Prim(adj, 0, 7)
Prim(adj, 0, 5)

# Java:
"""
import java.util.*;

public class PrimMST {

    public static void prim(int[][] adj, int src, int n) {
        Map<Integer, List<int[]>> edges = new HashMap<>();
        for (int i = 0; i < n; i++) {
            edges.put(i, new ArrayList<>());
        }

        for (int[] e : adj) {
            int u = e[0], v = e[1], w = e[2];
            edges.get(u).add(new int[]{v, w});
            edges.get(v).add(new int[]{u, w});
        }

        Set<Integer> visited = new HashSet<>();
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        int min_mst = 0;

        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        minHeap.offer(new int[]{0, src});  // {weight, node}

        while (visited.size() < n) {
            int[] top = minHeap.poll();
            int w1 = top[0], n1 = top[1];

            if (visited.contains(n1)) continue;

            System.out.print(n1 + "-");
            visited.add(n1);
            min_mst += w1;

            for (int[] nei : edges.get(n1)) {
                int n2 = nei[0], w2 = nei[1];
                if (!visited.contains(n2)) {
                    parent[n2] = n1;
                    minHeap.offer(new int[]{w2, n2});
                }
            }
        }

        System.out.println("\nCost of minimum spanning tree is: " + min_mst);
    }
}
"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
#include <unordered_map>
using namespace std;

void Prim(vector<vector<int>>& adj, int src, int n) {
    // edges: adjacency list representation, map node -> list of (neighbor, weight)
    unordered_map<int, vector<pair<int,int>>> edges;
    vector<int> parent(n, -1);
    
    for (auto& edge : adj) {
        int u = edge[0], v = edge[1], w = edge[2];
        edges[u].push_back({v, w});
        edges[v].push_back({u, w});
    }
    
    unordered_set<int> visited;
    int min_mst = 0;
    // you can start with any node this, will not affect the ans 
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> min_heap;
    min_heap.push({0, src});
    
    while ((int)visited.size() < n) {
        auto [w1, n1] = min_heap.top();
        min_heap.pop();
        cout << n1 << "-";
        
        if (visited.count(n1)) {  // this will automatically check whether all nodes get included or not. so no need to check the condition "if len(visited)==n:"
            continue;
        }
        visited.insert(n1);
        min_mst += w1;   // different from Dijkastra.. Adding the weight of edges coming under MST
        
        for (auto& [n2, w2] : edges[n1]) {
            if (!visited.count(n2)) {
                parent[n2] = n1;
                // here little change from dijkastra as in this we have to add the weight of all edges which will be come under MST
                // Instead of adding 'w1+w2' like Dijkastra here adding only 'w2'.
                min_heap.push({w2, n2});
            }
        }
    }
    cout << "\ncost of minimum spanning tree is: " << min_mst << "\n";
}

int main() {
    // adj= [[0,1,28],[0,5,10],[1,0,28],[1,6,14],[1,2,16],[2,1,16],[2,3,12],[3,6,18],[3,2,12],[3,4,22],[4,6,24],[4,5,25],[5,0,10],[4,3,22],[5,4,25],[6,1,14],[6,4,24],[6,3,18]] // ans= 99
    vector<vector<int>> adj = {{0,2,3},{1,3,4},{1,2,10},{2,1,10},{2,3,2},{2,4,6},{2,0,3},{3,1,4},{3,2,2},{3,4,1},{4,2,6},{4,3,1}};  // ans= 10
    Prim(adj, 0, 5);
    return 0;
}

"""
