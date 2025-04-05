from collections import defaultdict
from time import time
class Graph:
    def __init__(self,n):
        self.V= n
        self.colors= ['white']*n
        self.pred= [-1]*n
        self.time= 0
        self.first_time_visited= [0]*n
        self.last_time_visited= [0]*n
        self.graph= defaultdict(list)
    
    # for directed graph
    def add_edge(self,u,v):
        self.graph[u].append(v)

    def DFS(self):
        print("Dfs traversal is: ")
        for u in range(self.V):
            if self.colors[u]== 'white':
                self.DFS_Visit(u)
        print()
        print("first time visit of nodes",self.first_time_visited)
        print("last time visit of nodes ",self.last_time_visited)
    
    def DFS_Visit(self,u):
        self.time+= 1
        self.first_time_visited[u]= self.time
        self.colors[u]= 'gray'
        print(u, end=" ")
        for v in self.graph[u]:
            if self.colors[v]== 'white':
                self.pred[v]= u
                self.DFS_Visit(v)
        self.time+= 1
        self.last_time_visited[u]= self.time
        self.colors[u]= 'black'

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

# Java
"""
import java.util.*;

class Graph {
    private int V;
    private String[] colors;
    private int[] pred;
    private int time;
    private int[] firstTimeVisited;
    private int[] lastTimeVisited;
    private Map<Integer, List<Integer>> graph;

    public Graph(int n) {
        V = n;
        colors = new String[n];
        Arrays.fill(colors, "white");
        pred = new int[n];
        Arrays.fill(pred, -1);
        time = 0;
        firstTimeVisited = new int[n];
        lastTimeVisited = new int[n];
        graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }
    }

    // for directed graph
    public void addEdge(int u, int v) {
        graph.get(u).add(v);
    }

    public void DFS() {
        System.out.println("DFS traversal is: ");
        for (int u = 0; u < V; u++) {
            if (colors[u].equals("white")) {
                DFSVisit(u);
            }
        }
        System.out.println();
        System.out.println("First time visit of nodes: " + Arrays.toString(firstTimeVisited));
        System.out.println("Last time visit of nodes: " + Arrays.toString(lastTimeVisited));
    }

    private void DFSVisit(int u) {
        time++;
        firstTimeVisited[u] = time;
        colors[u] = "gray";
        System.out.print(u + " ");
        for (int v : graph.get(u)) {
            if (colors[v].equals("white")) {
                pred[v] = u;
                DFSVisit(v);
            }
        }
        time++;
        lastTimeVisited[u] = time;
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

        System.out.println(g.graph);
        g.DFS();
    }
}
"""
