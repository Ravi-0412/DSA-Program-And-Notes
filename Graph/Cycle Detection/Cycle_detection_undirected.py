"""
Can detect cycle even graph is given as component

method 1 : using BFS
Time complexity Same as BFS traversal:  
  `O(V + E)` where  
  `V` = number of vertices (nodes)  
  `E` = number of edges

logic: 
- We want to detect if the graph has a cycle and also find how many connected parts (components) it has.
- For each node:
  - If it is not visited, start a BFS from that node.
  - While doing BFS, check each neighbor:
    - If the neighbor is already visited **and is not the parent** of the current node, it means **there is a cycle**.
    - This happens because you found another way to reach the neighbor, forming a loop.
- Every time you start a BFS on an unvisited node, you found a new connected component.


"""


from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)
        self.AdjList[v].append(u)
    
    def BFS(self, adj, src):
        Q= deque()
        # while adding vertex to Q, add its parent node also
        Q.append((src, -1))
        while Q:
            (curr, parent)= Q.popleft()
            # print(curr, parent)
            for u in self.AdjList[curr]:
                if self.visited[u]== False:
                    self.visited[u]= True
                    Q.append((u,curr))
                elif u!= parent:  # u is visited as well as not parent means cycle so return true
                    return True
        # return False   # no need of this line

    def isCycle(self,n, adj):
        for i in range(n):
            if self.visited[i]== False:
                self.visited[i]= True  
                if self.BFS(adj,i):
                    return True
        # if no component has cycle then return False     
        return False   

    
g= Graph(11)
g.addEdge(0,1)
g.addEdge(1,3)
g.addEdge(2,4)
g.addEdge(4,9)
g.addEdge(4,5)
g.addEdge(5,6)
# g.addEdge(5,8)
g.addEdge(9,8)
g.addEdge(8,7)
g.addEdge(6,7)
g.addEdge(7,10)
print(g.AdjList)
print(g.isCycle(11,g.AdjList))
print(g.visited)

# Java
"""
import java.util.*;

class Graph {
    private int V;
    private boolean[] visited;
    private Map<Integer, List<Integer>> adjList;

    public Graph(int n) {
        V = n;
        visited = new boolean[n];
        adjList = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adjList.put(i, new ArrayList<>());
        }
    }

    public void addEdge(int u, int v) {
        adjList.get(u).add(v);
        adjList.get(v).add(u);
    }

    public boolean BFS(int src) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{src, -1});

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int curr = current[0];
            int parent = current[1];

            for (int neighbor : adjList.get(curr)) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.offer(new int[]{neighbor, curr});
                } else if (neighbor != parent) {
                    return true; // Found a cycle
                }
            }
        }
        return false; // No cycle found
    }

    public boolean isCycle() {
        Arrays.fill(visited, false); // Reset visited array

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                visited[i] = true;
                if (BFS(i)) {
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
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

class Graph {
public:
    int V;
    vector<bool> visited;
    unordered_map<int, vector<int>> AdjList;

    Graph(int n) {
        V = n;
        visited.resize(n, false);
    }

    void addEdge(int u, int v) {
        AdjList[u].push_back(v);
        AdjList[v].push_back(u);
    }

    bool BFS(int src) {
        queue<pair<int, int>> Q;
        Q.push({src, -1});

        while (!Q.empty()) {
            auto [curr, parent] = Q.front();
            Q.pop();

            for (int u : AdjList[curr]) {
                if (!visited[u]) {
                    visited[u] = true;
                    Q.push({u, curr});
                } else if (u != parent) {
                    // Visited and not parent means a cycle
                    return true;
                }
            }
        }
        return false;
    }

    bool isCycle(int n) {
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                visited[i] = true;
                if (BFS(i)) {
                    return true;
                }
            }
        }
        return false;
    }
};

"""

"""
METHOD 2 : DFS Traversal
The logic is the same as BFS, just using DFS instead.
- For each node:
  - If it is not visited, start a DFS from that node.
  - While exploring neighbors:
    - If the neighbor is already visited and is not the parent, it means there is a cycle.
    - This means the neighbor was visited from a different path, forming a loop.
- Every time you start a DFS from an unvisited node, it means you found a new connected component.
Time complexity : Same as dfs traversal

"""

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)
        self.AdjList[v].append(u)

    def DFS_Visit(self, adj,src,parent):
        self.visited[src]= True
        for u in adj[src]:
            if not self.visited[u]:
                if self.DFS_Visit(adj, u, src):
                    return True
            elif u != parent:
                return True

    def isCycle(self,n, adj):
        for i in range(n):
            if not self.visited[i]:    
                if self.DFS_Visit(adj,i, -1):
                    return True       
        return False


# g= Graph(11)
# g.addEdge(0,1)
# g.addEdge(1,3)
# g.addEdge(2,4)
# g.addEdge(4,9)
# g.addEdge(4,5)
# g.addEdge(5,6)
# # g.addEdge(5,8)
# g.addEdge(9,8)
# g.addEdge(8,7)
# # g.addEdge(6,7)
# g.addEdge(7,10)
# # print(g.AdjList)
# print(g.isCycle(11,g.AdjList))

# Java
"""
import java.util.*;

class Graph {
    private int V;
    private boolean[] visited;
    private Map<Integer, List<Integer>> adjList;

    public Graph(int n) {
        V = n;
        visited = new boolean[n];
        adjList = new HashMap<>();
        for (int i = 0; i < n; i++) {
            adjList.put(i, new ArrayList<>());
        }
    }

    public void addEdge(int u, int v) {
        adjList.get(u).add(v);
        adjList.get(v).add(u);
    }

    private boolean DFS_Visit(Map<Integer, List<Integer>> adj, int src, int parent) {
        visited[src] = true;
        for (int u : adj.get(src)) {
            if (!visited[u]) {
                if (DFS_Visit(adj, u, src)) {
                    return true;
                }
            } else if (u != parent) {
                return true; // Found a cycle
            }
        }
        return false;
    }

    public boolean isCycle(int n) {
        Arrays.fill(visited, false); // Reset visited array

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                if (DFS_Visit(adjList, i, -1)) {
                    return true; // Cycle detected
                }
            }
        }
        return false; // No cycle detected
    }

    public static void main(String[] args) {
        Graph g = new Graph(6);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.addEdge(3, 4);
        g.addEdge(4, 5);

        if (g.isCycle(6)) {
            System.out.println("Graph contains a cycle.");
        } else {
            System.out.println("Graph does not contain a cycle.");
        }
    }
}
"""
# C++ Code 
"""
// Method 2: Using DFS
// Logic is exactly same as BFS
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Graph {
public:
    int V;
    vector<bool> visited;
    unordered_map<int, vector<int>> AdjList;

    Graph(int n) {
        V = n;
        visited.resize(n, false);
        // initialize adjacency list
    }

    void addEdge(int u, int v) {
        AdjList[u].push_back(v);
        AdjList[v].push_back(u);
    }

    // DFS method to detect cycle
    bool DFS_Visit(unordered_map<int, vector<int>>& adj, int src, int parent) {
        visited[src] = true;
        for (int u : adj[src]) {
            if (!visited[u]) {
                if (DFS_Visit(adj, u, src)) {
                    return true; // Cycle found
                }
            } else if (u != parent) {
                return true; // If visited and not parent, cycle
            }
        }
        return false;
    }

    bool isCycle(int n, unordered_map<int, vector<int>>& adj) {
        for (int i = 0; i < n; ++i) {
            if (!visited[i]) {
                if (DFS_Visit(adj, i, -1)) {
                    return true;
                }
            }
        }
        return false;
    }
};
"""
