# Method 1:

# Bridge: A edge in graph is a bridge if after removing this edge our graph becomes disconnected.
# VVI: whether a node can be the bridge(edge between node-->nei) or articulation point  will be decided by it's neighbour (lowest visited time).
# Note: a node->nei be a bridge if there is no other way 'nei' can reach the 'node'(it's parent) and any node before the node so that it 
# can join to nay other component.

# logic: Two node can be a part of a bridge if there is no any other path possible between those except the parent and nei path.
# Agar ek hi rasta(edge) h parent and nei ke beech me and agar usko bhi remove kar de to dono 2 component me split ho jayega.
# steps and logic in comments.

# VVI=> Bridge: if lowest_visited_time[nei] > first_time_visited[node] => means bridge.
# meaning: nei is saying the 'the lowest time' in which i can get visited from my neighbours (since we are updating the lowest time of every node with the lowest time of all its neighbour)
# is even more than the 'time when you were visited first',
# So no way i we can visit each other from any other path. That's why disconnecting this edge will disconnect the graph.

# time: O(V+ E)
# space: O(V + 2E) for making the adjacency list and O(3*n) for other arrays.

from collections import defaultdict 
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # First create the adjacency list
        adj= defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        self.timer= 1  # will tell the visiting time of a node. for first node it will be equal to '1'.
        visited= set()
        first_time_visited=  [0]*n  # will store the first time when a node is visited.
        lowest_visited_time= [0]*n  # will store the lowest time in which we can reach the node from any of its adjacent node except parent.
        ans= []

        def dfs(node, parent):
            visited.add(node)
            # when we are first visiting, update the first and lowest time visited= timer
            first_time_visited[node]= lowest_visited_time[node]= self.timer
            self.timer+= 1    # incr the timer for next call
            # print(self.timer)
            # now check for its adjacent node
            for nei in adj[node]:
                if nei== parent:  # if we only take two cases one for visited and one for not visited then,we will get wrong ans.
                    continue      # as while updating the lowest time, we don't need time of parent and in  case'not' visited parent time will also get included. and we have to update the lowest time in both visited and not visited case.
                # if it is not visited then only chance is that , we may get bridge between node and its neigh while traversing back.
                # Because if already visited then we can reach that node through other path since we are not including parent.
                if nei not in visited:
                    dfs(nei, node)
                    # update the lowest_visited_time for node
                    lowest_visited_time[node]= min(lowest_visited_time[node], lowest_visited_time[nei])
                    # check if node---> nei can be part of bridge.
                    if lowest_visited_time[nei] > first_time_visited[node]:  # there was no other path we can reach (node-->nei) or any other node before its parent(i.e node)
                        ans.append([node, nei])                              # so they will form bridge.
                else:  # if already visited. then update the lowest time of node with the lowest time of 'nei'
                    #  as we have to get the lowest time for node from all its neighbour either already visited or not except parent.
                       # nei should not reach the node as well as nodes before its parent through any other path,
                       # so we have to keep lowest time as minimum as possible .That's why taking the 'lowest time' not the first visited time.
                       # since we want node also not to get visited by nei through any other path.
                    lowest_visited_time[node]= min(lowest_visited_time[node], lowest_visited_time[nei])  
                    

        dfs(0, -1)  # starting from node '0' and parent= -1.
        print(lowest_visited_time, first_time_visited)  
        return ans


# java
"""
import java.util.*;

class Solution {
    private int timer = 1;  // will tell the visiting time of a node. for first node it will be equal to '1'.
    private List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        // First create the adjacency list
        Map<Integer, List<Integer>> adj = new HashMap<>();
        for (int i = 0; i < n; i++) adj.put(i, new ArrayList<>());

        for (List<Integer> conn : connections) {
            int u = conn.get(0), v = conn.get(1);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        Set<Integer> visited = new HashSet<>();
        int[] first_time_visited = new int[n];   // will store the first time when a node is visited.
        int[] lowest_visited_time = new int[n];  // will store the lowest time in which we can reach the node from any of its adjacent node except parent.

        dfs(0, -1, adj, visited, first_time_visited, lowest_visited_time);
        return ans;
    }

    private void dfs(int node, int parent, Map<Integer, List<Integer>> adj, Set<Integer> visited,
                     int[] first_time_visited, int[] lowest_visited_time) {
        visited.add(node);
        // when we are first visiting, update the first and lowest time visited = timer
        first_time_visited[node] = lowest_visited_time[node] = timer++;
        
        // now check for its adjacent node
        for (int nei : adj.get(node)) {
            if (nei == parent) continue;  // skip parent

            if (!visited.contains(nei)) {
                dfs(nei, node, adj, visited, first_time_visited, lowest_visited_time);
                // update the lowest_visited_time for node
                lowest_visited_time[node] = Math.min(lowest_visited_time[node], lowest_visited_time[nei]);

                // check if node--->nei can be part of bridge
                if (lowest_visited_time[nei] > first_time_visited[node]) {
                    ans.add(Arrays.asList(node, nei));  // they will form bridge
                }
            } else {
                // already visited. then update the lowest time of node with the lowest time of 'nei'
                lowest_visited_time[node] = Math.min(lowest_visited_time[node], lowest_visited_time[nei]);
            }
        }
    }
}


"""


# C++
"""
#include <bits/stdc++.h>
using namespace std;

class Solution {
    int timer = 1;  // will tell the visiting time of a node. for first node it will be equal to '1'
    vector<vector<int>> ans;

    void dfs(int node, int parent, vector<vector<int>>& adj, vector<bool>& visited,
             vector<int>& first_time_visited, vector<int>& lowest_visited_time) {
        visited[node] = true;
        // when we are first visiting, update the first and lowest time visited = timer
        first_time_visited[node] = lowest_visited_time[node] = timer++;

        // now check for its adjacent node
        for (int nei : adj[node]) {
            if (nei == parent) continue;  // skip parent

            if (!visited[nei]) {
                dfs(nei, node, adj, visited, first_time_visited, lowest_visited_time);
                // update the lowest_visited_time for node
                lowest_visited_time[node] = min(lowest_visited_time[node], lowest_visited_time[nei]);

                // check if node--->nei can be part of bridge
                if (lowest_visited_time[nei] > first_time_visited[node]) {
                    ans.push_back({node, nei});  // they will form bridge
                }
            } else {
                // already visited. then update the lowest time of node with the lowest time of 'nei'
                lowest_visited_time[node] = min(lowest_visited_time[node], lowest_visited_time[nei]);
            }
        }
    }

public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        // First create the adjacency list
        vector<vector<int>> adj(n);
        for (auto& conn : connections) {
            int u = conn[0], v = conn[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        vector<int> first_time_visited(n, 0);   // will store the first time when a node is visited
        vector<int> lowest_visited_time(n, 0);  // will store the lowest time to reach node from its neighbors
        vector<bool> visited(n, false);

        dfs(0, -1, adj, visited, first_time_visited, lowest_visited_time);
        return ans;
    }
};



"""