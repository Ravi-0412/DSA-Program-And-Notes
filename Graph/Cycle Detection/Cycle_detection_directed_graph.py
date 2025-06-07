# method 1: By DFS
"""
Use two arrays:
  - `visited[]`: marks if a node was ever visited.
  - `dfsVisited[]`: marks if it's in the current DFS path.
- If during DFS, a neighbor is already in `dfsVisited`, it means a cycle exists.

Why Not Just One Array?
- In directed graphs, a node can be visited from different paths.
- Only if it’s visited in the same DFS path, it forms a cycle.

Time Complexity: same as DFS traversal.

"""

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.dfs_visited= [False]*n   # will check whether that node has been visited in current cycle or not
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)

    def DFS_Visit(self, adj,src):
        self.visited[src]= True
        self.dfs_visited[src]= True
        for u in adj[src]:
            if not self.visited[u]:
                if self.DFS_Visit(adj, u):  # if for any component there is a cycle
                    return True
            # if adjacent node is visited then check if that is visited in current cycle or not
            elif self.dfs_visited[u]==True:
                return True
        # while traversing back(i.e curr node has no adjacent node) make dfs_visited of current node= False 
        # to check again in next DFS call or next component
        self.dfs_visited[src]= False
        # return False   # no need of this line 

    def isCycle(self,n, adj):
        for i in range(n):
            if not self.visited[i]:
                if self.DFS_Visit(adj,i):
                    return True
        # if no component has cycle then return False
        return False


g= Graph(9)
# test case 1: only one component
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(2,5)
# g.addEdge(4,2)
g.addEdge(5,4)
g.addEdge(6,1)
g.addEdge(6,7)
g.addEdge(7,8)
# g.addEdge(8,6)

# test case 2: more than one component
print(g.AdjList)
print(g.isCycle(9,g.AdjList))

# Java
"""
import java.util.*;

class Graph {
    private int V;
    private boolean[] visited;
    private boolean[] dfsVisited;
    private Map<Integer, List<Integer>> adjList;

    public Graph(int n) {
        V = n;
        visited = new boolean[n];
        dfsVisited = new boolean[n];
        adjList = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adjList.put(i, new ArrayList<>());
        }
    }

    public void addEdge(int u, int v) {
        adjList.get(u).add(v);
    }

    private boolean DFS_Visit(Map<Integer, List<Integer>> adj, int src) {
        visited[src] = true;
        dfsVisited[src] = true;

        for (int u : adj.get(src)) {
            if (!visited[u]) {
                if (DFS_Visit(adj, u)) {
                    return true; // Cycle detected
                }
            } else if (dfsVisited[u]) {
                return true; // Cycle detected
            }
        }

        dfsVisited[src] = false; // Unmark the node after backtracking
        return false; // No cycle detected in this path
    }

    public boolean isCycle(int n) {
        Arrays.fill(visited, false); // Reset visited array

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (DFS_Visit(adjList, i)) {
                    return true; // Cycle detected
                }
            }
        }
        return false; // No cycle detected
    }
}
"""
# C++ Code 
"""
#include <bits/stdc++.h>
using namespace std;

class Graph {
private:
    int V;  // Number of vertices
    vector<bool> visited;
    vector<bool> dfsVisited;
    unordered_map<int, vector<int>> adjList;

public:
    // Constructor to initialize graph
    Graph(int n) {
        V = n;
        visited.resize(n, false);
        dfsVisited.resize(n, false);
        for (int i = 0; i < n; ++i) {
            adjList[i] = vector<int>();
        }
    }

    // Function to add a directed edge from u -> v
    void addEdge(int u, int v) {
        adjList[u].push_back(v);
    }

    // Helper function for DFS traversal to detect cycle
    bool DFS_Visit(int src) {
        visited[src] = true;
        dfsVisited[src] = true;

        for (int neighbor : adjList[src]) {
            if (!visited[neighbor]) {
                if (DFS_Visit(neighbor)) {
                    return true; // Cycle detected
                }
            } else if (dfsVisited[neighbor]) {
                return true; // Cycle detected
            }
        }

        dfsVisited[src] = false; // Unmark the node after backtracking
        return false; // No cycle detected in this path
    }

    // Function to detect cycle in the entire graph
    bool isCycle() {
        fill(visited.begin(), visited.end(), false);
        fill(dfsVisited.begin(), dfsVisited.end(), false);

        for (int i = 0; i < V; ++i) {
            if (!visited[i]) {
                if (DFS_Visit(i)) {
                    return true; // Cycle detected
                }
            }
        }
        return false; // No cycle detected
    }
};

"""


"""
another way using dfs: this submitted in Q "269 Alien dictionary" understand the logic properly and do here 

Method 2: Using BFS (Kahn’s Algorithm)

- Count in-degrees of each node.
- Add nodes with in-degree `0` to the queue.
- Remove them one by one, reducing in-degrees of neighbors.
- If not all nodes are processed → cycle exists.

This is Topological Sort using BFS.

Dfs template to use in other Q
Just code of: 207. Course Schedule
"""
Python code
from collections import defaultdict
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        # According to the meaning of the Q.
        for second,first in prerequisites:
            AdjList[first].append(second)

        def checkCycle(src):
            visited.add(src)
            path_visited.add(src)
            for u in AdjList[src]:
                if u not in visited:
                    if checkCycle(u):
                        return True
                elif u in path_visited:
                    return True
            path_visited.remove(src)
            return False

        visited= set()
        path_visited= set()
        for i in range(numCourses):
            if i not in visited and checkCycle(i):    # if cycle simply return False, else continue checking for another node
                return False
        return True

# Java Code 
"""
import java.util.*;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> AdjList = new HashMap<>();
        for (int[] pre : prerequisites) {
            int second = pre[0], first = pre[1];
            AdjList.computeIfAbsent(first, k -> new ArrayList<>()).add(second);
        }

        Set<Integer> visited = new HashSet<>();
        Set<Integer> pathVisited = new HashSet<>();

        // DFS function to check for cycle
        boolean checkCycle(int src, Map<Integer, List<Integer>> graph, Set<Integer> visited, Set<Integer> pathVisited) {
            visited.add(src);
            pathVisited.add(src);

            for (int u : graph.getOrDefault(src, new ArrayList<>())) {
                if (!visited.contains(u)) {
                    if (checkCycle(u, graph, visited, pathVisited)) {
                        return true;
                    }
                } else if (pathVisited.contains(u)) {
                    return true;
                }
            }

            pathVisited.remove(src);
            return false;
        }

        for (int i = 0; i < numCourses; i++) {
            if (!visited.contains(i)) {
                if (checkCycle(i, AdjList, visited, pathVisited)) {
                    return false;
                }
            }
        }

        return true;
    }
}

"""

# C++ Code
"""
// C++ version of Leetcode 207: Course Schedule using DFS Cycle Detection
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> AdjList;
        for (auto& pre : prerequisites) {
            int second = pre[0], first = pre[1];
            AdjList[first].push_back(second); // Directed graph
        }

        unordered_set<int> visited;
        unordered_set<int> pathVisited;

        function<bool(int)> checkCycle = [&](int src) {
            visited.insert(src);
            pathVisited.insert(src);
            for (int u : AdjList[src]) {
                if (visited.find(u) == visited.end()) {
                    if (checkCycle(u)) return true;
                } else if (pathVisited.find(u) != pathVisited.end()) {
                    return true; // Cycle detected
                }
            }
            pathVisited.erase(src);
            return false;
        };

        for (int i = 0; i < numCourses; ++i) {
            if (visited.find(i) == visited.end()) {
                if (checkCycle(i)) return false;
            }
        }
        return true;
    }
};

"""
