# Method 1:
"""
Breadth-First Search (BFS) is a simple and important algorithm used to explore graphs or trees.

How it works:
i) BFS starts from a chosen starting node.
ii) It explores all the nearby (neighboring) nodes first, before going deeper.
iii) It uses a queue (a line where the first in is the first out) to keep track of which node to visit next.
iv) It makes sure not to visit the same node more than once.

Simple Example:
Imagine you’re trying to find your friend in a network of people.
BFS checks all your direct friends first, then friends of friends, and so on.

Some use case:
i) Finding the shortest path in a maze or map (if all steps cost the same).
ii) Level-order traversal in trees.
iii) Checking if all nodes in a graph are connected.

Time Complexity:
O(V + E) where V is the number of nodes (vertices), and E is the number of edges (connections).
Space Complexity: O(V) — where V is the number of vertices (nodes) in the graph.
"""

# Python Code


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



# Java Code

"""
import java.util.*;

class Graph {
    int size;
    int[] distance;
    String[] colors;
    int[] pred;
    int[][] adjMatrix;

    public Graph(int n) {
        size = n;
        distance = new int[n];
        colors = new String[n];
        pred = new int[n];
        adjMatrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            colors[i] = "white";
            Arrays.fill(adjMatrix[i], 0);  // initialize all elements with '0'
        }
    }

    // add the edge
    public void addEdge(int v1, int v2) {
        if (v1 == v2) {
            System.out.println("both the vertices are same");
        } else {
            adjMatrix[v1][v2] = 1;
            adjMatrix[v2][v1] = 1;  // since making for undirected graph
                                    // so it will be symmetric
        }
    }

    // function to print the matrix
    public void print_matrix() {
        for (int[] row : adjMatrix) {
            System.out.println(Arrays.toString(row));
        }
        System.out.println();
    }

    public void remove_edge(int v1, int v2) {
        if (adjMatrix[v1][v2] == 0) {
            System.out.println("no edge exist bw these vertices");
        } else {
            adjMatrix[v1][v2] = 0;
            adjMatrix[v2][v1] = 0;
        }
    }

    public void BFS(int s) {  // s: starting vertex
        // first store adjacent of all vertices into a map
        Map<Integer, List<Integer>> graph = new HashMap<>();
        // will contain the vertices mapped with their adjacent vertices
        // values (adjacent vertices) will be in the list
        for (int i = 0; i < size; i++) {
            graph.put(i, new ArrayList<>());
            for (int j = 0; j < size; j++) {
                if (adjMatrix[i][j] == 1) {
                    graph.get(i).add(j);
                }
            }
        }
        System.out.println(graph);

        // now apply BFS on the graph
        colors[s] = "gray";
        distance[s] = 0;
        pred[s] = -1;
        Queue<Integer> Q = new LinkedList<>();  // queue to store vertices
        Q.add(s);  // add source into the Q

        // now run a loop till 'Q' becomes empty
        System.out.println("bfs traversal of following graph is: ");
        while (!Q.isEmpty()) {
            // pop the first ele from 'Q'
            int curr = Q.poll();
            System.out.print(curr + " ");
            // now push all the adjacent vertices of popped ele into the 'Q'
            // if that has not been seen yet
            for (int i = 0; i < graph.get(curr).size(); i++) {
                if (colors[graph.get(curr).get(i)].equals("white")) {  // if seeing for 1st time then push into the Q
                    colors[graph.get(curr).get(i)] = "gray";
                    distance[graph.get(curr).get(i)] = distance[curr] + 1;
                    pred[graph.get(curr).get(i)] = curr;
                    Q.add(graph.get(curr).get(i));
                }
            }
            // now you have visited all the nodes adjacent to 1st ele of Q (popped one)
            // so make its colour as 'black'
            colors[curr] = "black";
        }

        System.out.println("\ndistance of all vertices from source " + Arrays.toString(distance));
    }

    public static void main(String[] args) {
        Graph g = new Graph(8);
        g.addEdge(0, 1);
        g.addEdge(1, 2);
        g.addEdge(2, 3);
        g.addEdge(3, 4);
        g.addEdge(3, 5);
        g.addEdge(4, 5);
        g.addEdge(4, 7);
        g.addEdge(5, 6);
        g.addEdge(5, 7);
        g.addEdge(6, 7);
        g.print_matrix();
        g.BFS(2);
    }
}
"""


# C++

"""
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <list>
using namespace std;

class Graph {
public:
    int size;
    vector<int> distance;
    vector<string> colors;
    vector<int> pred;
    vector<vector<int>> adjMatrix;

    Graph(int n) {
        size = n;
        distance.resize(n, 0);
        colors.resize(n, "white");
        pred.resize(n, -1);
        adjMatrix.resize(n, vector<int>(n, 0));  // initialize all elements with '0' and creating a matrix
    }

    // add the edge
    void addEdge(int v1, int v2) {
        if (v1 == v2) {
            cout << "both the vertices are same" << endl;
        } else {
            adjMatrix[v1][v2] = 1;
            adjMatrix[v2][v1] = 1;  // since making for undirected graph
                                    // so it will be symmetric
        }
    }

    // function to print the matrix
    void print_matrix() {
        for (auto& row : adjMatrix) {
            for (int val : row)
                cout << val << " ";
            cout << endl;
        }
        cout << endl;
    }

    void remove_edge(int v1, int v2) {
        if (adjMatrix[v1][v2] == 0) {
            cout << "no edge exist bw these vertices" << endl;
        } else {
            adjMatrix[v1][v2] = 0;
            adjMatrix[v2][v1] = 0;
        }
    }

    void BFS(int s) {  // s: starting vertex
        // first store adjacent of all vertices into a map
        unordered_map<int, list<int>> graph;
        // will contain the vertices mapped with their adjacent vertices
        // values (adjacent vertices) will be in the list
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (adjMatrix[i][j] == 1) {
                    graph[i].push_back(j);
                }
            }
        }

        // now apply BFS on the graph
        colors[s] = "gray";
        distance[s] = 0;
        pred[s] = -1;
        queue<int> Q;  // queue to store vertices
        Q.push(s);  // add source into the Q

        // now run a loop till 'Q' becomes empty
        cout << "bfs traversal of following graph is: " << endl;
        while (!Q.empty()) {
            // pop the first ele from 'Q'
            int curr = Q.front();
            Q.pop();
            cout << curr << " ";
            // now push all the adjacent vertices of popped ele into the 'Q'
            // if that has not been seen yet
            for (int adj : graph[curr]) {
                if (colors[adj] == "white") {  // if seeing for 1st time then push into the Q
                    colors[adj] = "gray";
                    distance[adj] = distance[curr] + 1;
                    pred[adj] = curr;
                    Q.push(adj);
                }
            }
            // now you have visited all the nodes adjacent to 1st ele of Q (popped one)
            // so make its colour as 'black'
            colors[curr] = "black";
        }

        cout << "\ndistance of all vertices from source: ";
        for (int d : distance)
            cout << d << " ";
        cout << endl;
    }
};

int main() {
    Graph g(8);
    g.addEdge(0, 1);
    g.addEdge(1, 2);
    g.addEdge(2, 3);
    g.addEdge(3, 4);
    g.addEdge(3, 5);
    g.addEdge(4, 5);
    g.addEdge(4, 7);
    g.addEdge(5, 6);
    g.addEdge(5, 7);
    g.addEdge(6, 7);
    g.print_matrix();
    g.BFS(2);

    return 0;
}
"""
