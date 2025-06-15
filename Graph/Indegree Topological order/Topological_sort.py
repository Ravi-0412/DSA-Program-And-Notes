# method 1: using DFS
"""
Note VVI: whenever you have to find the order of distinct elements, given some relation between them(or dependency)
must think of topological sort.

logic:  just run the DFS and when there is no adjacent node put the node into the stack
At last print the stack in opposite direction.

why came with DFS? 
Ans: as DFS go deeper and deeper and we need to print the node with lesser outorder vertices first
means stop at node with no adjacent node(no outgoing vertices as DAG will must contain,
 at least one vertex with outgoing edge = 0 and incoming edge =0).

i.e we have to print the vertex with no outgoing edge at last and that can be done 
while traversing back in case of DFS.

Note(VVI) for dfs method: here you are putting the node in the ans(stack), while traversing back that's why it's giving correct ans always
but if we put the node at start itself in the ans like when you are calling the dfs for that node then it will not give the corect ans always...
Adding the node at start won't guarantee the correct order.
keep this in mind.. if you do like this graph like test case 2 will not work

Explanation for adding at Last and why not at start.
Why Post-order Works for Topological Sorting ?

i) Dependency Handling: In topological sorting, if there's an edge u -> v, u must appear before v in the ordering. 
When we perform DFS, we explore v before finishing u. By adding v to the order before u (since we add on backtracking),
we ensure that u comes after v in the list. However, since we reverse the list at the end (or use a stack where later additions come first),
u ends up before v in the final order, satisfying u -> v.

ii) Completion Guarantee: Adding a node after all its descendants are processed means that all nodes that depend on it are already in the order 
(and will be placed after it upon reversal), ensuring no dependencies are violated.

Why Pre-order Can Fail?
-> Premature Addition: Adding a node to the order as soon as you start visiting it means you might add u before exploring its descendants. 
If u has a descendant v that should come after u, but due to the order of DFS traversal,
v hasn't been added yet, u might end up after v in the final order, violating the u -> v edge.

if you do by finding the indegree like BFS then that will always give the correct ans as that is the basic of tolopogical sort.

Note: this method will only work if no cycle.. for cycle detecting and then printing see the below method that i submitted in Q "269 Alien dictionary"
or we can also modify in this like we can use two visited array like we did in cycle detection Q.
"""

from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        self.visited= [False]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)

    def FindTopoSort(self, adj,src, stack):
        self.visited[src]= True
        for u in adj[src]:
            if not self.visited[u]:
                self.FindTopoSort(adj, u, stack)  
        # while traversing back put the node into the stack and node with less no of outorder vertices 
        # will be kept first(as it will start traversing back at this node only) so final ans will be the opposite of stack

        #  node with largest visiting time(or minimum finishing time) is pushed first when there is no further adjacent node is there which has not been visited
        stack.append(src)

    def TopoSort(self,n, adj):
        stack= []
        for i in range(n):
            if not self.visited[i]:
                self.FindTopoSort(adj,i,stack)
        while stack:  
            print(stack.pop(), end=" ")

# test case 1:
g= Graph(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(4,0)
g.addEdge(4,1)
print(g.AdjList)
g.TopoSort(6,g.AdjList)

# test case 2:
g= Graph(3)
g.addEdge(0,2)
g.addEdge(0,1)
g.addEdge(1,2)

# Java
"""
import java.util.*;

public class Graph {
    int V;
    boolean[] visited;
    Map<Integer, List<Integer>> AdjList;

    public Graph(int n) {
        V = n;
        visited = new boolean[n];
        AdjList = new HashMap<>();
    }

    public void addEdge(int u, int v) {
        AdjList.computeIfAbsent(u, k -> new ArrayList<>()).add(v);
    }

    public void FindTopoSort(Map<Integer, List<Integer>> adj, int src, Deque<Integer> stack) {
        visited[src] = true;
        if (adj.containsKey(src)) {
            for (int u : adj.get(src)) {
                if (!visited[u]) {
                    FindTopoSort(adj, u, stack);
                }
            }
        }
        // while traversing back put the node into the stack and node with less no of outorder vertices 
        // will be kept first(as it will start traversing back at this node only) so final ans will be the opposite of stack

        // node with largest visiting time(or minimum finishing time) is pushed first when there is no further adjacent node is there which has not been visited
        stack.push(src);
    }

    public void TopoSort(int n, Map<Integer, List<Integer>> adj) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                FindTopoSort(adj, i, stack);
            }
        }
        while (!stack.isEmpty()) {
            System.out.print(stack.pop() + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // test case 1:
        Graph g1 = new Graph(6);
        g1.addEdge(5, 2);
        g1.addEdge(5, 0);
        g1.addEdge(2, 3);
        g1.addEdge(3, 1);
        g1.addEdge(4, 0);
        g1.addEdge(4, 1);
        g1.TopoSort(6, g1.AdjList);

        // test case 2:
        Graph g2 = new Graph(3);
        g2.addEdge(0, 2);
        g2.addEdge(0, 1);
        g2.addEdge(1, 2);
        g2.TopoSort(3, g2.AdjList);
    }
}

"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_map>
#include <stack>
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
    }

    void FindTopoSort(unordered_map<int, vector<int>>& adj, int src, stack<int>& st) {
        visited[src] = true;
        for (int u : adj[src]) {
            if (!visited[u]) {
                FindTopoSort(adj, u, st);
            }
        }
        // while traversing back put the node into the stack and node with less no of outorder vertices 
        // will be kept first(as it will start traversing back at this node only) so final ans will be the opposite of stack

        // node with largest visiting time(or minimum finishing time) is pushed first when there is no further adjacent node is there which has not been visited
        st.push(src);
    }

    void TopoSort(int n, unordered_map<int, vector<int>>& adj) {
        stack<int> st;
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                FindTopoSort(adj, i, st);
            }
        }
        while (!st.empty()) {
            cout << st.top() << " ";
            st.pop();
        }
        cout << endl;
    }
};

// test case 1:
int main() {
    Graph g1(6);
    g1.addEdge(5, 2);
    g1.addEdge(5, 0);
    g1.addEdge(2, 3);
    g1.addEdge(3, 1);
    g1.addEdge(4, 0);
    g1.addEdge(4, 1);
    g1.TopoSort(6, g1.AdjList);

    // test case 2:
    Graph g2(3);
    g2.addEdge(0, 2);
    g2.addEdge(0, 1);
    g2.addEdge(1, 2);
    g2.TopoSort(3, g2.AdjList);

    return 0;
}

"""


# method 2 using BFS: Kahn's Algorithm
"""
logic: use the concept of indegree as the node with indegree 0 will come at first and
node with more indegree will come later and so

This method can also be used to detect cycle in directed graph.
just count the no of nodes added in the Q, if there will be cycle then count <n because  at some point,
there will not be any node whose indegree will be equal to '0' to put into the Q or call the bfs function.
here no need of visited set since we are adding only the node with 'indegree==0'.

Note: You can go level wise i.e Node with indegree '0' come at first then node with indegree = '1' and so on.
This will useful in Q: 1136. Parallel Courses
"""
from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.V= n
        # self.visited= [False]*n  # here no need of this as we are pushing on ele in Q and doing the operation on that
        self.indegree= [0]*n
        self.AdjList= defaultdict(list)
    
    def addEdge(self,u,v):
        self.AdjList[u].append(v)
    
    # calculate the indegree of all node
    def Indegree_count(self):
        for i in range(self.V):
            for k in self.AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                self.indegree[k]+= 1

    def FindTopoSort(self):
        Q, ans= [], []      # Note: Replace 'Q' -> deque

        # find the node with indegree '0' as this node will come 1st in the topological order
        # i.e it will be the source node and after that apply the BFS
        for i in range(self.V):   # will also work for more than one component
            if self.indegree[i]==0:  # this will put node with indegree '0' of all component into the 'Q' and will check for each component
                Q.append(i)

        count= 0  # will count the no of times node is added in the ans
        while Q:
            count+= 1  
            u= Q.pop(0)
            ans.append(u)
            # after poping decrease the indegree of all node adjacent to 'u'
            for j in self.AdjList[u]:
                self.indegree[j]-= 1
                if self.indegree[j]== 0:  # after decreasing if any node has indegree == 0 then put in the Q
                    Q.append(j)
        # note: count will be less than 'V'.
        if count!= self.V:  # for checking the cycle in directed graph using BFS .. 
            print("there exist a cycle in the graph")
        else:
            print(ans)


# test case 1
# g= Graph(6)
# g.addEdge(5,2)
# g.addEdge(5,0)
# g.addEdge(2,3)
# g.addEdge(3,1)
# g.addEdge(4,0)
# g.addEdge(4,1)

# test case 2
# g= Graph(3)
# g.addEdge(0,1)
# g.addEdge(1,2)
# g.addEdge(2,0)
# g.Indegree_count()
# g.FindTopoSort()

# test case 3
g= Graph(3)
g.addEdge(0,2)
g.addEdge(0,1)
g.addEdge(1,2)
print(g.AdjList)
g.Indegree_count()
g.FindTopoSort()


# Java
"""
import java.util.*;

class Graph {
    private int V;
    private int[] indegree;
    private List<List<Integer>> AdjList;

    public Graph(int n) {
        this.V = n;
        indegree = new int[n];
        AdjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            AdjList.add(new ArrayList<>());
        }
    }

    public void addEdge(int u, int v) {
        AdjList.get(u).add(v);
    }

    // calculate the indegree of all node
    public void Indegree_count() {
        for (int i = 0; i < V; i++) {
            for (int k : AdjList.get(i)) {  // if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]++;
            }
        }
    }

    public void FindTopoSort() {
        Queue<Integer> Q = new LinkedList<>();
        List<Integer> ans = new ArrayList<>();

        // find the node with indegree '0' as this node will come 1st in the topological order
        // i.e it will be the source node and after that apply the BFS
        for (int i = 0; i < V; i++) {
            if (indegree[i] == 0) {  // this will put node with indegree '0' of all component into the 'Q'
                Q.add(i);
            }
        }

        int count = 0;  // will count the no of times node is added in the ans
        while (!Q.isEmpty()) {
            int u = Q.poll();
            count++;
            ans.add(u);

            // after poping decrease the indegree of all node adjacent to 'u'
            for (int j : AdjList.get(u)) {
                indegree[j]--;
                if (indegree[j] == 0) {
                    Q.add(j);
                }
            }
        }

        // note: count will be less than 'V' if there is a cycle
        if (count != V) {
            System.out.println("there exist a cycle in the graph");
        } else {
            System.out.println(ans);
        }
    }
}


"""

# C++ Code 
"""
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Graph {
    int V;
    vector<int> indegree;
    vector<vector<int>> AdjList;

public:
    Graph(int n) {
        V = n;
        indegree.assign(n, 0);
        AdjList.resize(n);
    }

    void addEdge(int u, int v) {
        AdjList[u].push_back(v);
    }

    // calculate the indegree of all node
    void Indegree_count() {
        for (int i = 0; i < V; ++i) {
            for (int k : AdjList[i]) {  // if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]++;
            }
        }
    }

    void FindTopoSort() {
        queue<int> Q;
        vector<int> ans;

        // find the node with indegree '0' as this node will come 1st in the topological order
        // i.e it will be the source node and after that apply the BFS
        for (int i = 0; i < V; ++i) {
            if (indegree[i] == 0) {  // this will put node with indegree '0' of all component into the 'Q'
                Q.push(i);
            }
        }

        int count = 0;  // will count the no of times node is added in the ans
        while (!Q.empty()) {
            int u = Q.front();
            Q.pop();
            count++;
            ans.push_back(u);

            // after poping decrease the indegree of all node adjacent to 'u'
            for (int j : AdjList[u]) {
                indegree[j]--;
                if (indegree[j] == 0) {
                    Q.push(j);
                }
            }
        }

        // note: count will be less than 'V' if there is a cycle
        if (count != V) {
            cout << "there exist a cycle in the graph" << endl;
        } else {
            for (int node : ans) cout << node << " ";
            cout << endl;
        }
    }
};

"""

# 1) Dfs template
    
# method 2: bfs template
from collections import defaultdict
import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        for first,second in prerequisites:
            AdjList[second].append(first)  # phle 2nd wala course karenge tb hi first kar sakte h.
        
        n = numCourses
        indegree= [0]*n
        
        # finding the indegree of each vertices
        for i in range(n):
            for k in AdjList[i]:  # if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]+= 1
        
        # now applying the BFS to get the topological order
        count, ans = 0, []
        Q  = collections.deque()
        for i in range(n):
            if indegree[i]==0: 
                Q.append(i)
    
        while Q:
            count+= 1  
            u= Q.popleft()
            ans.append(u)
            # after poping decrease the indegree of all node adjacent to 'u'
            for j in AdjList[u]:
                indegree[j] -= 1   
                if indegree[j]== 0: 
                    Q.append(j)

        if count!= n: 
            return False
        return True

# Java Code 
"""
import java.util.*;

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> AdjList = new HashMap<>();
        // first convert into adjacency list(edges) for directed graph
        for (int[] pre : prerequisites) {
            int first = pre[0];
            int second = pre[1];
            AdjList.computeIfAbsent(second, k -> new ArrayList<>()).add(first);  // phle 2nd wala course karenge tb hi first kar sakte h.
        }

        int n = numCourses;
        int[] indegree = new int[n];

        // finding the indegree of each vertices
        for (int i = 0; i < n; i++) {
            if (AdjList.containsKey(i)) {
                for (int k : AdjList.get(i)) {  // if k is adj to 'i' means there is one indegree edge to 'k'
                    indegree[k]++;
                }
            }
        }

        // now applying the BFS to get the topological order
        int count = 0;
        List<Integer> ans = new ArrayList<>();
        Queue<Integer> Q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                Q.add(i);
            }
        }

        while (!Q.isEmpty()) {
            count++;
            int u = Q.poll();
            ans.add(u);
            // after poping decrease the indegree of all node adjacent to 'u'
            if (AdjList.containsKey(u)) {
                for (int j : AdjList.get(u)) {
                    indegree[j]--;
                    if (indegree[j] == 0) {
                        Q.add(j);
                    }
                }
            }
        }

        if (count != n) {
            return false;
        }
        return true;
    }
}
"""


# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> AdjList;
        // first convert into adjacency list(edges) for directed graph
        for (auto& pre : prerequisites) {
            int first = pre[0];
            int second = pre[1];
            AdjList[second].push_back(first);  // phle 2nd wala course karenge tb hi first kar sakte h.
        }

        int n = numCourses;
        vector<int> indegree(n, 0);

        // finding the indegree of each vertices
        for (int i = 0; i < n; i++) {
            for (int k : AdjList[i]) {  // if k is adj to 'i' means there is one indegree edge to 'k'
                indegree[k]++;
            }
        }

        // now applying the BFS to get the topological order
        int count = 0;
        vector<int> ans;
        queue<int> Q;
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                Q.push(i);
            }
        }

        while (!Q.empty()) {
            count++;
            int u = Q.front();
            Q.pop();
            ans.push_back(u);
            // after poping decrease the indegree of all node adjacent to 'u'
            for (int j : AdjList[u]) {
                indegree[j]--;
                if (indegree[j] == 0) {
                    Q.push(j);
                }
            }
        }

        if (count != n) {
            return false;
        }
        return true;
    }
};

"""