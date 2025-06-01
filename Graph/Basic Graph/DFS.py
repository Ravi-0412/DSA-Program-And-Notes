"""
📘 What is DFS (Depth First Search)?

DFS is a way to explore or traverse a graph. In DFS, we start from one node and 
go as deep as we can along each path before coming back (backtracking).

✅ DFS is like exploring a maze – you go forward until there's no way, 
then come back and try another way.

🕒 Time Complexity: O(V + E)
- V = number of vertices (nodes)
- E = number of edges (connections)

👀 Useful for:
- Finding paths
- Detecting cycles
- Topological sorting
- Maze solving
"""

from collections import defaultdict
from time import time
# Step 1: Define a Graph class
class Graph:
    def __init__(self, n):
        self.V = n  # Number of vertices
        self.colors = ['white'] * n  # Track status: white (unvisited), gray (visiting), black (visited)
        self.pred = [-1] * n         # To store the parent (for path tracking)
        self.time = 0                # To track discovery and finish time
        self.first_time_visited = [0] * n
        self.last_time_visited = [0] * n
        self.graph = defaultdict(list)  # Adjacency list

    # Step 2: Add a directed edge from u to v
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Step 3: Start DFS for all unvisited nodes
    def DFS(self):
        print("📌 DFS Traversal Order:")
        for u in range(self.V):
            if self.colors[u] == 'white':
                self.DFS_Visit(u)
        print()
        print("🕓 First visit time of each node:", self.first_time_visited)
        print("🕓 Last visit time of each node: ", self.last_time_visited)

    # Step 4: Recursive DFS function
    def DFS_Visit(self, u):
        self.time += 1
        self.first_time_visited[u] = self.time
        self.colors[u] = 'gray'
        print(u, end=" ")  # Visit this node

        for v in self.graph[u]:  # Visit all neighbors
            if self.colors[v] == 'white':
                self.pred[v] = u
                self.DFS_Visit(v)

        self.time += 1
        self.last_time_visited[u] = self.time
        self.colors[u] = 'black'  # Mark as done

# -----------------------------------------
# 🔁 Example: Create a graph and run DFS
# -----------------------------------------
g= Graph(6)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(4,3)
g.add_edge(4,5)
g.add_edge(5,5)

print(g.graph)
g.DFS()

# -----------------------------------------
Java Version
-----------------------------------------

"""
import java.util.*;

class Graph {
    int V;
    String[] colors;
    int[] pred;
    int[] firstTime, lastTime;
    int time;
    Map<Integer, List<Integer>> graph;

    Graph(int n) {
        V = n;
        colors = new String[n];
        Arrays.fill(colors, "white");
        pred = new int[n];
        Arrays.fill(pred, -1);
        firstTime = new int[n];
        lastTime = new int[n];
        graph = new HashMap<>();
        for (int i = 0; i < n; i++)
            graph.put(i, new ArrayList<>());
    }

    void addEdge(int u, int v) {
        graph.get(u).add(v);
    }

    void DFS() {
        System.out.println("DFS traversal:");
        for (int i = 0; i < V; i++) {
            if (colors[i].equals("white")) {
                DFSVisit(i);
            }
        }
    }

    void DFSVisit(int u) {
        time++;
        firstTime[u] = time;
        colors[u] = "gray";
        System.out.print(u + " ");
        for (int v : graph.get(u)) {
            if (colors[v].equals("white")) {
                pred[v] = u;
                DFSVisit(v);
            }
        }
        time++;
        lastTime[u] = time;
        colors[u] = "black";
    }

    public static void main(String[] args) {
        Graph g = new Graph(6);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.addEdge(3, 1);
        g.addEdge(4, 3);
        g.addEdge(4, 5);
        g.addEdge(5, 5);
        g.DFS();
    }
}
"""

-----------------------------------------
C++ Version
-----------------------------------------
"""

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Graph {
    int V;
    vector<string> colors;
    vector<int> pred, firstTime, lastTime;
    int time;
    unordered_map<int, vector<int>> graph;

public:
    Graph(int n) : V(n), colors(n, "white"), pred(n, -1), firstTime(n, 0), lastTime(n, 0), time(0) {}

    void addEdge(int u, int v) {
        graph[u].push_back(v);
    }

    void DFS() {
        cout << "DFS traversal: ";
        for (int u = 0; u < V; ++u) {
            if (colors[u] == "white") {
                DFSVisit(u);
            }
        }
        cout << endl;
    }

    void DFSVisit(int u) {
        time++;
        firstTime[u] = time;
        colors[u] = "gray";
        cout << u << " ";
        for (int v : graph[u]) {
            if (colors[v] == "white") {
                pred[v] = u;
                DFSVisit(v);
            }
        }
        time++;
        lastTime[u] = time;
        colors[u] = "black";
    }
};

int main() {
    Graph g(6);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
    g.addEdge(4, 3);
    g.addEdge(4, 5);
    g.addEdge(5, 5);
    g.DFS();
    return 0;
}
"""
