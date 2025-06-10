"""
Breadth-First Search (BFS) in Graphs

🔍 Theory:
BFS is a traversal algorithm used for graphs and trees. It explores all vertices at the current level before moving to the next.

📌 Key Points:
- Uses a queue (FIFO).
- Suitable for finding **shortest path** in unweighted graphs.

📚 Applications:
- Shortest path in unweighted graphs
- Peer-to-peer networks
- Web crawlers
- GPS systems
- Social network friend suggestions

----------------------------
Example Graph:
----------------------------
Let’s say we have this undirected graph:

    0 -- 1 -- 2 -- 3
                  |
                  4 -- 7
                  |  /
                  5
                  |
                  6

Nodes: 0 through 7
Edges: (0-1), (1-2), (2-3), (3-4), (3-5), (4-5), (4-7), (5-6), (5-7), (6-7)

We’ll represent this graph using an **Adjacency Matrix**, and apply BFS starting from node `2`.
"""

==========================
Python Code
==========================

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.size= n
        self.distance= [0]*n
        self.colors= ['white']*n
        self.pred= [-1]*n
        self.adjMatrix= []
        for i in range(n):
            self.adjMatrix.append([0 for i in range(n)])  # intilaise all ele with '0' and creating a matrix
    # add the add
    def addEdge(self,v1,v2):
        if v1==v2:
            print("both the vertices are same")
        else:
            self.adjMatrix[v1][v2]= 1
            self.adjMatrix[v2][v1]= 1  # since making for undirected graph
                                      # so it will be symmetric
    # function to print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)
        print()

    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2]==0:
            print("no edge exist bw these vertices")
        else:
            self.adjMatrix[v1][v2]= 0
            self.adjMatrix[v2][v1]= 0

# use deque as poping starting ele from q when using as list will be take O(n) for eacch element

    def BFS(self,s):   # s: starting vertex
        # first store adjacent of all vertices into a dictionary
        graph= defaultdict(list)  # will contain the vertices mapped with their adjacent vertices
                                  # values(adjacent vertices) will be in the list
        for i in range(self.size):
            for j in range(self.size):
                if self.adjMatrix[i][j]== 1:
                    graph[i].append(j)
        print(graph)
        # for key,val in graph.items():
        #     print(val)
        
        # now apply BFS on the graph
        self.colors[s] ='gray'
        self.distance[s]= 0
        self.pred[s]= -1
        Q= []   # queue to store vertices
        # add source into the Q
        Q.append(s)
        # now run a loop till 'Q' becomes empty
        print("bfs traversal of following graph is: ")
        while Q:
            # pop the first ele from 'Q' 
            curr= Q.pop(0)
            print(curr, end=" ")
            # now push all the adjacent vertices of poped ele into the 'Q'
            # if that has not been seen yet
            for i in range(len(graph[curr])):
                # check whether seen or not
                if self.colors[graph[curr][i]]== 'white': # if seeing for 1st time then push into the Q
                    self.colors[graph[curr][i]]= 'gray'
                    self.distance[graph[curr][i]]= self.distance[curr] +1
                    self.pred[graph[curr][i]]= curr
                    Q.append(graph[curr][i])
            # now you have visited all the nodes ajacent to 1st ele of Q(poped one)
            # so make its colour as 'black'
            # print("queue is ", Q)
            self.colors[curr]= 'black'
        print("distance of all vertices from source",self.distance)
            # print(Q)

g= Graph(8)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(4,7)
g.addEdge(5,6)
g.addEdge(5,7)
g.addEdge(6,7)
g.print_matrix()
g.BFS(2)


==========================
Java Code
==========================
"""
import java.util.*;

class Graph {
    private int size;
    private int[] distance;
    private String[] colors;
    private int[] pred;
    private int[][] adjMatrix;

    public Graph(int n) {
        size = n;
        distance = new int[n];
        colors = new String[n];
        Arrays.fill(colors, "white");
        pred = new int[n];
        Arrays.fill(pred, -1);
        adjMatrix = new int[n][n];
    }

    public void addEdge(int v1, int v2) {
        if (v1 != v2) {
            adjMatrix[v1][v2] = 1;
            adjMatrix[v2][v1] = 1;
        }
    }

    public void BFS(int s) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < size; i++) {
            graph.put(i, new ArrayList<>());
            for (int j = 0; j < size; j++) {
                if (adjMatrix[i][j] == 1) {
                    graph.get(i).add(j);
                }
            }
        }

        colors[s] = "gray";
        distance[s] = 0;
        pred[s] = -1;

        Queue<Integer> q = new LinkedList<>();
        q.add(s);

        while (!q.isEmpty()) {
            int curr = q.poll();
            System.out.print(curr + " ");

            for (int neighbor : graph.get(curr)) {
                if (colors[neighbor].equals("white")) {
                    colors[neighbor] = "gray";
                    distance[neighbor] = distance[curr] + 1;
                    pred[neighbor] = curr;
                    q.add(neighbor);
                }
            }
            colors[curr] = "black";
        }

        System.out.println(Arrays.toString(distance));
    }

    public static void main(String[] args) {
        Graph g = new Graph(8);
        int[][] edges = {{0,1},{1,2},{2,3},{3,4},{3,5},{4,5},{4,7},{5,6},{5,7},{6,7}};
        for (int[] edge : edges) g.addEdge(edge[0], edge[1]);
        g.BFS(2);
    }
}
"""


==========================
 C++ Code
==========================

"""
#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

class Graph {
    int size;
    vector<vector<int>> adjMatrix;
    vector<string> colors;
    vector<int> distance;
    vector<int> pred;

public:
    Graph(int n) {
        size = n;
        adjMatrix.resize(n, vector<int>(n, 0));
        colors.resize(n, "white");
        distance.resize(n, 0);
        pred.resize(n, -1);
    }

    void addEdge(int v1, int v2) {
        if (v1 != v2) {
            adjMatrix[v1][v2] = 1;
            adjMatrix[v2][v1] = 1;
        }
    }

    void BFS(int s) {
        colors[s] = "gray";
        distance[s] = 0;
        pred[s] = -1;

        queue<int> q;
        q.push(s);

        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            cout << curr << " ";

            for (int i = 0; i < size; ++i) {
                if (adjMatrix[curr][i] == 1 && colors[i] == "white") {
                    colors[i] = "gray";
                    distance[i] = distance[curr] + 1;
                    pred[i] = curr;
                    q.push(i);
                }
            }
            colors[curr] = "black";
        }

        cout << "\nDistance from source:\n";
        for (int d : distance) cout << d << " ";
        cout << endl;
    }
};

int main() {
    Graph g(8);
    vector<pair<int, int>> edges = {{0,1},{1,2},{2,3},{3,4},{3,5},{4,5},{4,7},{5,6},{5,7},{6,7}};
    for (auto e : edges) g.addEdge(e.first, e.second);
    g.BFS(2);
}
"""
