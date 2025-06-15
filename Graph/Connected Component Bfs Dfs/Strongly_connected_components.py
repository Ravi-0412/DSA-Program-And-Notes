# Method 1: 

"""
# (Kosaraju Algorithm)

logic steps: 1) sort all nodes in order of largest finishing time using Topo Sort logic, time: O(n + E)
2) Transpose the graph .time: O(n + E)
transposing the graph means changing the direrction of the path . 
Reason for transposing: Nodes having path one way betwen them , we will not able to reach other if we start from one node in order of last finising time.
we will only reach the nodes which was connected bidirectionally after transposing( and when we will start from largest finishing time).
3) Call DFS acc to the largest finishing time got in step 1 on the transposed graph.
Note: 
top of the stack will store the  ele with largest finishing time to 
verify direction from both sides.
Note: element from which we had started will have largest finishing time because while backtrack we are putting
element in stack so first visited will be visited last also.
# So when we run dfs again on transpose matrix then it checks whether from this node we can still reach other nodes
If we can reach then it means they are strongly connected to each other.

time: O(n +E)
Space : O(n)
"""

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.visited_reverse= [False]*n  # when we call the DFS on the transpose
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)

    def DFS(self, adj,src, stack):
        self.visited[src]= True
        for u in adj[src]:
            if not self.visited[u]:
                self.DFS(adj, u, stack)  
        
        stack.append(src) # will contain node with largest finishing time at the top

    def PrintScc(self, transpose1, src):   # just the DFS only on tranpose matrix
        self.visited_reverse[src]= True
        print(src, end=" ")
        for v in transpose1[src]:
            if not self.visited_reverse[v]:
                self.PrintScc(transpose1, v)

    # start reading from here
    def KosaRaju(self, adj, n):
        stack= []
        for i in range(n):
            if self.visited[i]== False:
                self.DFS(adj,i, stack)
        
        # now transpose the graph
        transpose= defaultdict(list)
        for i  in range(n):
            for j in adj[i]:
                transpose[j].append(i)
        
        print("Element according to largest finishing time: ", stack)
        print("the strongly connected components are: ")
        while stack:
            u= stack.pop()
            if self.visited_reverse[u]== False:
                print()
                self.PrintScc(transpose, u)

g= Graph(5)
g.addEdge(1,0)
g.addEdge(2,1)
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(3,4)
g.KosaRaju(g.AdjList, 5)


# java
"""
import java.util.*;

class Graph {
    int V;
    boolean[] visited;
    boolean[] visited_reverse;
    HashMap<Integer, List<Integer>> AdjList;

    Graph(int n) {
        V = n;
        visited = new boolean[n];
        visited_reverse = new boolean[n];
        AdjList = new HashMap<>();
        for (int i = 0; i < n; i++) {
            AdjList.put(i, new ArrayList<>());
        }
    }

    void addEdge(int u, int v) {
        AdjList.get(u).add(v);
    }

    void DFS(HashMap<Integer, List<Integer>> adj, int src, Stack<Integer> stack) {
        visited[src] = true;
        for (int u : adj.get(src)) {
            if (!visited[u]) {
                DFS(adj, u, stack);
            }
        }
        // will contain node with largest finishing time at the top
        stack.push(src);
    }

    void PrintScc(HashMap<Integer, List<Integer>> transpose, int src) {
        visited_reverse[src] = true;
        System.out.print(src + " ");
        for (int v : transpose.get(src)) {
            if (!visited_reverse[v]) {
                PrintScc(transpose, v);
            }
        }
    }

    void KosaRaju(HashMap<Integer, List<Integer>> adj, int n) {
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                DFS(adj, i, stack);
            }
        }

        // now transpose the graph
        HashMap<Integer, List<Integer>> transpose = new HashMap<>();
        for (int i = 0; i < n; i++) {
            transpose.put(i, new ArrayList<>());
        }

        for (int i = 0; i < n; i++) {
            for (int j : adj.get(i)) {
                transpose.get(j).add(i);
            }
        }

        System.out.println("Element according to largest finishing time: " + stack);
        System.out.println("The strongly connected components are:");

        while (!stack.isEmpty()) {
            int u = stack.pop();
            if (!visited_reverse[u]) {
                System.out.println();
                PrintScc(transpose, u);
            }
        }
    }

    public static void main(String[] args) {
        Graph g = new Graph(5);
        g.addEdge(1, 0);
        g.addEdge(2, 1);
        g.addEdge(0, 2);
        g.addEdge(0, 3);
        g.addEdge(3, 4);
        g.KosaRaju(g.AdjList, 5);
    }
}

"""


# C++ Code 
"""
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

class Graph {
public:
    int V;
    vector<bool> visited;
    vector<bool> visited_reverse;
    unordered_map<int, vector<int>> AdjList;

    Graph(int n) {
        V = n;
        visited.assign(n, false);
        visited_reverse.assign(n, false);
        for (int i = 0; i < n; i++) {
            AdjList[i] = vector<int>();
        }
    }

    void addEdge(int u, int v) {
        AdjList[u].push_back(v);
    }

    void DFS(unordered_map<int, vector<int>>& adj, int src, stack<int>& stk) {
        visited[src] = true;
        for (int u : adj[src]) {
            if (!visited[u]) {
                DFS(adj, u, stk);
            }
        }
        // will contain node with largest finishing time at the top
        stk.push(src);
    }

    void PrintScc(unordered_map<int, vector<int>>& transpose, int src) {
        visited_reverse[src] = true;
        cout << src << " ";
        for (int v : transpose[src]) {
            if (!visited_reverse[v]) {
                PrintScc(transpose, v);
            }
        }
    }

    void KosaRaju(unordered_map<int, vector<int>>& adj, int n) {
        stack<int> stk;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                DFS(adj, i, stk);
            }
        }

        // now transpose the graph
        unordered_map<int, vector<int>> transpose;
        for (int i = 0; i < n; i++) {
            transpose[i] = vector<int>();
        }

        for (int i = 0; i < n; i++) {
            for (int j : adj[i]) {
                transpose[j].push_back(i);
            }
        }

        cout << "Element according to largest finishing time: ";
        stack<int> tempStack = stk;  // Copy to print without destroying original stack
        vector<int> order;
        while (!tempStack.empty()) {
            order.push_back(tempStack.top());
            tempStack.pop();
        }
        for (int i = (int)order.size() - 1; i >= 0; i--) {
            cout << order[i] << " ";
        }
        cout << "\nThe strongly connected components are:\n";

        while (!stk.empty()) {
            int u = stk.top();
            stk.pop();
            if (!visited_reverse[u]) {
                cout << "\n";
                PrintScc(transpose, u);
            }
        }
    }
};

int main() {
    Graph g(5);
    g.addEdge(1, 0);
    g.addEdge(2, 1);
    g.addEdge(0, 2);
    g.addEdge(0, 3);
    g.addEdge(3, 4);
    g.KosaRaju(g.AdjList, 5);
    return 0;
}

"""

Related Question
# 1) 1520. Maximum Number of Non-Overlapping Substrings