"""
DFS (Depth-First Search) ?
DFS is a graph (or tree) traversal algorithm that explores as far as possible down one path before backtracking.

How it works ?
i) Start from a node.
ii) Go to one of its neighbors.
iii)Then go to that neighbor's neighbor, and so on...
iv) If you reach a dead end (no unvisited neighbors), go back (backtrack) and try other paths.

DFS can be done recursively or using a stack.

Usecase:
i) cycle detection in a graph.
ii) Pathfinding in a maze (to explore all paths).
iii) Topological sorting in DAGs.
iv) Finding connected components in a graph.
v) Solving puzzles (like Sudoku, word search).

Time Complexity: O(V + E), sapce: O(V)
- V = number of vertices (nodes)
- E = number of edges (connections)

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


# Java Version

"""
import java.util.*;

class Graph {
    int V;
    String[] colors;
    int[] pred;
    int time;
    int[] first_time_visited;
    int[] last_time_visited;
    Map<Integer, List<Integer>> graph;

    // Step 1: Define a Graph class
    public Graph(int n) {
        V = n;
        colors = new String[n];  // Track status: white (unvisited), gray (visiting), black (visited)
        Arrays.fill(colors, "white");
        pred = new int[n];       // To store the parent (for path tracking)
        Arrays.fill(pred, -1);
        time = 0;                // To track discovery and finish time
        first_time_visited = new int[n];
        last_time_visited = new int[n];
        graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }
    }

    // Step 2: Add a directed edge from u to v
    public void add_edge(int u, int v) {
        graph.get(u).add(v);
    }

    // Step 3: Start DFS for all unvisited nodes
    public void DFS() {
        System.out.println("📌 DFS Traversal Order:");
        for (int u = 0; u < V; u++) {
            if (colors[u].equals("white")) {
                DFS_Visit(u);
            }
        }
        System.out.println();
        System.out.println(" First visit time of each node: " + Arrays.toString(first_time_visited));
        System.out.println(" Last visit time of each node:  " + Arrays.toString(last_time_visited));
    }

    // Step 4: Recursive DFS function
    public void DFS_Visit(int u) {
        time += 1;
        first_time_visited[u] = time;
        colors[u] = "gray";
        System.out.print(u + " ");  // Visit this node

        for (int v : graph.get(u)) {  // Visit all neighbors
            if (colors[v].equals("white")) {
                pred[v] = u;
                DFS_Visit(v);
            }
        }

        time += 1;
        last_time_visited[u] = time;
        colors[u] = "black";  // Mark as done
    }

    public static void main(String[] args) {
        //  Example: Create a graph and run DFS
        Graph g = new Graph(6);
        g.add_edge(0, 1);
        g.add_edge(0, 2);
        g.add_edge(1, 2);
        g.add_edge(2, 3);
        g.add_edge(3, 1);
        g.add_edge(4, 3);
        g.add_edge(4, 5);
        g.add_edge(5, 5);

        System.out.println(g.graph);
        g.DFS();
    }
}
"""

# C++ Version

"""
#include <iostream>
#include <vector>
#include <unordered_map>
#include <list>
#include <string>
using namespace std;

class Graph {
public:
    int V;
    vector<string> colors;               // Track status: white (unvisited), gray (visiting), black (visited)
    vector<int> pred;                    // To store the parent (for path tracking)
    int time;                            // To track discovery and finish time
    vector<int> first_time_visited;
    vector<int> last_time_visited;
    unordered_map<int, list<int>> graph;  // Adjacency list

    // Step 1: Define a Graph class
    Graph(int n) {
        V = n;
        colors.resize(n, "white");
        pred.resize(n, -1);
        time = 0;
        first_time_visited.resize(n, 0);
        last_time_visited.resize(n, 0);
    }

    // Step 2: Add a directed edge from u to v
    void add_edge(int u, int v) {
        graph[u].push_back(v);
    }

    // Step 3: Start DFS for all unvisited nodes
    void DFS() {
        cout << " DFS Traversal Order:\n";
        for (int u = 0; u < V; ++u) {
            if (colors[u] == "white") {
                DFS_Visit(u);
            }
        }
        cout << "\n First visit time of each node: ";
        for (int t : first_time_visited) cout << t << " ";
        cout << "\n Last visit time of each node:  ";
        for (int t : last_time_visited) cout << t << " ";
        cout << endl;
    }

    // Step 4: Recursive DFS function
    void DFS_Visit(int u) {
        time += 1;
        first_time_visited[u] = time;
        colors[u] = "gray";
        cout << u << " ";  // Visit this node

        for (int v : graph[u]) {  // Visit all neighbors
            if (colors[v] == "white") {
                pred[v] = u;
                DFS_Visit(v);
            }
        }

        time += 1;
        last_time_visited[u] = time;
        colors[u] = "black";  // Mark as done
    }
};

int main() {
    // Example: Create a graph and run DFS
    Graph g(6);
    g.add_edge(0, 1);
    g.add_edge(0, 2);
    g.add_edge(1, 2);
    g.add_edge(2, 3);
    g.add_edge(3, 1);
    g.add_edge(4, 3);
    g.add_edge(4, 5);
    g.add_edge(5, 5);

    g.DFS();

    return 0;
}

"""
