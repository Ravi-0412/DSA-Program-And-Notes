"""
logic: Every bipartite graph should be coloured with exactly two colors.
use the concept of graph coloring and try to color with two color.
no need of visited array in this because color array can work like visited also.

Note: just similar logic as we detect cycle in undirected graph.

Logic: if any node is not visited, then color it with different color than its parent and 
if already visited then check it's color with the color of its neighbour. if same return False.

Note: xor of any number with 0 will give the same no  and  xor with '1' give the different number.
so to color the adjacent node with different color, we will take 1^color[parent].
And since we are only using '0' and '1' so number will be always : 0 or 1.

Note: Complete graph can never be bipartite.

Note: It can done also by 'm-coloring' problem using backtracking.
Just replace 'm' -> 2.
"""

# method 1: using BFS

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # graph is already given as adjacency list.
        n= len(graph)
        color= [-1]*n  # will tell node has been visited or not.
        for i in range(n):
            if color[i]== -1:  # means not visited till now
                # if any of components return False, return False
                if self.BfsCheck(graph,i,color)== False:
                    return False
        # otherwise graph is bipartite.
        return True
    
    def BfsCheck(self, graph,src,color):
        Q= collections.deque()
        Q.append(src)
        color[src] = 1   # for starting node of each component color it with either '0' or '1'.
        while Q:
            curr= Q.popleft()
            for nei in graph[curr]:
                if color[nei] == -1:  # if not visited
                    color[nei]= 1^color[curr]  # used xor operation with 1(to get the diff one). it will also mark node as visited.
                    Q.append(nei)  # in DFS instead of this line we call the DFS gain and everything is same only
                elif color[nei]== color[curr]: # if colored and have same color then not bipartite 
                    return False
        # return True  # no need of this

# Java Code
"""
import java.util.*;

class Solution {
    // method 1: using BFS
    public boolean isBipartite(int[][] graph) {
        // graph is already given as adjacency list.
        int n = graph.length;
        int[] color = new int[n];  // will tell node has been visited or not.
        Arrays.fill(color, -1);

        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {  // means not visited till now
                // if any of components return False, return False
                if (BfsCheck(graph, i, color) == false) {
                    return false;
                }
            }
        }

        // otherwise graph is bipartite.
        return true;
    }

    public boolean BfsCheck(int[][] graph, int src, int[] color) {
        Queue<Integer> Q = new LinkedList<>();
        Q.offer(src);
        color[src] = 1;  // for starting node of each component color it with either '0' or '1'.

        while (!Q.isEmpty()) {
            int curr = Q.poll();

            for (int nei : graph[curr]) {
                if (color[nei] == -1) {  // if not visited
                    color[nei] = 1 ^ color[curr];  // used xor operation with 1(to get the diff one). it will also mark node as visited.
                    Q.offer(nei);  // in DFS instead of this line we call the DFS again and everything is same only
                } else if (color[nei] == color[curr]) { // if colored and have same color then not bipartite 
                    return false;
                }
            }
        }

        // return True  // no need of this
        return true;
    }
}


"""

# C++ Code 
"""
class Solution {
public:
    // method 1: using BFS
    bool isBipartite(vector<vector<int>>& graph) {
        // graph is already given as adjacency list.
        int n = graph.size();
        vector<int> color(n, -1);  // will tell node has been visited or not.
        
        for (int i = 0; i < n; i++) {
            if (color[i] == -1) {  // means not visited till now
                // if any of components return False, return False
                if (BfsCheck(graph, i, color) == false) {
                    return false;
                }
            }
        }

        // otherwise graph is bipartite.
        return true;
    }

    bool BfsCheck(vector<vector<int>>& graph, int src, vector<int>& color) {
        queue<int> Q;
        Q.push(src);
        color[src] = 1;  // for starting node of each component color it with either '0' or '1'.

        while (!Q.empty()) {
            int curr = Q.front();
            Q.pop();

            for (int nei : graph[curr]) {
                if (color[nei] == -1) {  // if not visited
                    color[nei] = 1 ^ color[curr];  // used xor operation with 1 (to get the diff one). it will also mark node as visited.
                    Q.push(nei);  // in DFS instead of this line we call the DFS again and everything is same only
                }
                else if (color[nei] == color[curr]) {  // if colored and have same color then not bipartite
                    return false;
                }
            }
        }

        // return True  // no need of this
        return true;
    }
};

"""
# method 2: By using DFS
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n= len(graph)
        color= [-1]*n
        for v in range(n):
            if color[v]== -1:
                color[v]= 1
                if  self.DfsCheck(graph,v,color)== False:
                    return False
        return True

    def DfsCheck(self, graph, src, color):
        for u in graph[src]:
            if color[u] == -1:  # means not visited
                color[u] = 1^color[src]
                if self.DfsCheck(graph,u,color) == False:
                    return False
            elif color[u]== color[src]:
                return False
        # return True # no need of this 



# my mistakes
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n= len(graph)
        visited= [False]*n
        color= [-1]*n
        for v in range(n):
            if not visited[v]:
                print(v)
                color[v]= 0
                visited[v]= True
                if self.DFSVisit(graph,v, visited, color)== False:
                    return False
        return True
    
    def DFSVisit(self, graph, src, visited, color):
        # color[v]= 0   # writing here this one will give 'False' always as for every node it will set(update) the color as '0'
                            # But will work properly in case of 'BFS' as there is no recursive call
        for u in graph[src]:
            if not visited[u]:
                visited[u]= True
                # color[u]= 0^color[src]  # here i was making mistake , xor with 0 will give the same no i.e same color so was getting false for all inputs
                color[u]= 1^color[src]   # xor with '1' give the different number. So color first node with '1' only to write code like this.
                if self.DFSVisit(graph,u,visited, color)== False:
                    return False
            elif color[u]== color[src]:
                return False
        # return True   # no need of this


# Java
"""
import java.util.*;

class Solution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        boolean[] visited = new boolean[n];
        int[] color = new int[n];
        Arrays.fill(color, -1);

        for (int v = 0; v < n; v++) {
            if (!visited[v]) {
                color[v] = 0;
                visited[v] = true;
                if (!DFSVisit(graph, v, visited, color)) {
                    return false;
                }
            }
        }
        return true;
    }

    public boolean DFSVisit(int[][] graph, int src, boolean[] visited, int[] color) {
        // color[v] = 0   // writing here this one will give 'False' always as for every node it will set(update) the color as '0'
                          // But will work properly in case of 'BFS' as there is no recursive call
        for (int u : graph[src]) {
            if (!visited[u]) {
                visited[u] = true;
                // color[u] = 0 ^ color[src];  // xor with 0 will give the same no i.e same color so was getting false for all inputs
                color[u] = 1 ^ color[src];    // xor with '1' gives a different number. So color first node with '1' only to write code like this.
                if (!DFSVisit(graph, u, visited, color)) {
                    return false;
                }
            } else if (color[u] == color[src]) {
                return false;
            }
        }
        // return true;   // no need of this
        return true;
    }
}

"""

# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<bool> visited(n, false);
        vector<int> color(n, -1);

        for (int v = 0; v < n; ++v) {
            if (!visited[v]) {
                // color[v] = 0;
                // visited[v] = true;
                color[v] = 0;
                visited[v] = true;
                if (!DFSVisit(graph, v, visited, color)) {
                    return false;
                }
            }
        }
        return true;
    }

    bool DFSVisit(vector<vector<int>>& graph, int src, vector<bool>& visited, vector<int>& color) {
        // color[v]= 0   // writing here this one will give 'False' always as for every node it will set(update) the color as '0'
                         // But will work properly in case of 'BFS' as there is no recursive call
        for (int u : graph[src]) {
            if (!visited[u]) {
                visited[u] = true;
                // color[u] = 0 ^ color[src];  // xor with 0 will give the same no i.e same color so was getting false for all inputs
                color[u] = 1 ^ color[src];     // xor with '1' gives a different number. So color first node with '1' only to write code like this.
                if (!DFSVisit(graph, u, visited, color)) {
                    return false;
                }
            } else if (color[u] == color[src]) {
                return false;
            }
        }
        // return true;   // no need of this
        return true;
    }
};

"""

# Related Q: 
# 1042. Flower Planting With No Adjacent
