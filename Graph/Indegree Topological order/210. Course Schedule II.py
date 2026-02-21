# just print the order of topological sort
# method 1: By  Bfs

"""
Time Complexity: O(V + E)
Where V is numCourses and E is the number of prerequisites.

Space Complexity: O(V + E)
Adjacency List: Stores all V nodes and E edges: O(V + E)
Indegree array : O(V)
Queue & anwer = O(V)
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        AdjList = defaultdict(list)
        indegree = [0]*n
        # first convert into adjacency list(edges) for directed graph and calculate indegree
        for second,first in prerequisites:
            AdjList[first].append(second)
            indegree[second] += 1
        
        count, ans = 0, []
        Q = collections.deque()
        # now applying the BFS to get the topological order
        # find the node with indegree '0' as this node will come 1st in the topological order
        # i.e it will be the source node and after that apply the BFS
        for i in range(n):
            if indegree[i] == 0: 
                Q.append(i)
    
        while Q:
            count += 1  
            u = Q.popleft()
            ans.append(u)
            # after poping decrease the indegree of all node adjacent to 'u'
            for j in AdjList[u]:
                indegree[j] -= 1
                if indegree[j] == 0:  # after decreasing if any node has indegree == 0 then put in the Q
                    Q.append(j)

        if count != n:  # means cycle so no order is possible 
            return []
        return ans

# Java
"""
import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int n = numCourses;
        List<List<Integer>> adjList = new ArrayList<>();
        int[] indegree = new int[n];

        // Initialize adjacency list
        for (int i = 0; i < n; i++) {
            adjList.add(new ArrayList<>());
        }

        // Build graph and compute indegrees
        for (int[] pre : prerequisites) {
            int second = pre[0];
            int first = pre[1];
            adjList.get(first).add(second);
            indegree[second]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        List<Integer> result = new ArrayList<>();

        // Start with nodes having 0 indegree
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        // BFS (Kahn's Algorithm)
        while (!queue.isEmpty()) {
            int u = queue.poll();
            result.add(u);

            for (int v : adjList.get(u)) {
                indegree[v]--;
                if (indegree[v] == 0) {
                    queue.offer(v);
                }
            }
        }

        // If not all nodes were visited, a cycle exists
        if (result.size() != n) {
            return new int[0];
        }

        // Convert list to array
        int[] order = new int[n];
        for (int i = 0; i < n; i++) {
            order[i] = result.get(i);
        }

        return order;
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

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int n = numCourses;
        unordered_map<int, vector<int>> AdjList;
        vector<int> indegree(n, 0);
        // first convert into adjacency list(edges) for directed graph and calculate indegree
        for (auto& pre : prerequisites) {
            int second = pre[0], first = pre[1];
            AdjList[first].push_back(second);
            indegree[second] += 1;
        }

        int count = 0;
        vector<int> ans;
        queue<int> Q;
        // now applying the BFS to get the topological order
        // find the node with indegree '0' as this node will come 1st in the topological order
        // i.e it will be the source node and after that apply the BFS
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 0) {
                Q.push(i);
            }
        }

        while (!Q.empty()) {
            count += 1;
            int u = Q.front(); Q.pop();
            ans.push_back(u);
            // after poping decrease the indegree of all node adjacent to 'u'
            for (int j : AdjList[u]) {
                indegree[j] -= 1;
                if (indegree[j] == 0) {  // after decreasing if any node has indegree == 0 then put in the Q
                    Q.push(j);
                }
            }
        }

        if (count != n) {  // means cycle so no order is possible 
            return {};
        }
        return ans;
    }
};

"""
# another way using dfs: this submitted in Q "269 Alien dictionary"
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        AdjList= defaultdict(list)
        # first convert into adjacency list(edges) for directed graph
        for second,first in prerequisites:
            AdjList[first].append(second)
        visited= [0]*numCourses
        stack= []   # store the course completion in reverse order
        for i in range(numCourses):
            if not self.FindTopoSort(AdjList,i,stack,visited):    # if cycle simply return False, else continue checking for another node
                return []
        return stack[::-1]
        

    def FindTopoSort(self, adj,src, stack,visited):
        # base case for checking whether we have visited all the adjacent node.. if visited then check on another node
        if visited[src]== 1:   # been visited and added to the stack(ans). so simply return true so that it can check for next node without repeating the work
            return True         # returning False will give wrong ans as when it will see 'False' funtion will return from there only.
        # base case for checking cycle 
        if visited[src]== -1:   # means cycle as the current node(src) is already visited in current cycle only
            return False        # if not '0' means the this has been visited(not) and if = '-1' then visited in current cycle , means there is cycle.

        # code starts from here
        visited[src]= -1   # Marking 'cur' node is visited in current cycle. Also it means till now we have only visited the 'src' not its adjacent node.
        for u in adj[src]:
            if not self.FindTopoSort(adj, u, stack, visited):
                return False
                
        # while traversing back make visited[src]= 1 and  put the node into the stack
        visited[src]= 1   # means we have visited the 'src' as well as its neighbour and added to the ans(stack)
        stack.append(src)
        return True   # means we have visited the current node as well as its neighbour successfully

# Java
"""
import java.util.*;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int[] pre : prerequisites) {
            int second = pre[0], first = pre[1];
            adjList.get(first).add(second);
        }

        int[] visited = new int[numCourses]; // 0 = unvisited, -1 = visiting, 1 = visited
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, adjList, visited, stack)) {
                return new int[0]; // cycle detected
            }
        }

        int[] result = new int[numCourses];
        for (int i = numCourses - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }
        return result;
    }

    private boolean dfs(int node, List<List<Integer>> adj, int[] visited, Stack<Integer> stack) {
        if (visited[node] == -1) return false; // cycle
        if (visited[node] == 1) return true;   // already processed

        visited[node] = -1; // mark as visiting
        for (int neighbor : adj.get(node)) {
            if (!dfs(neighbor, adj, visited, stack)) {
                return false;
            }
        }

        visited[node] = 1; // mark as processed
        stack.push(node);
        return true;
    }
}
"""
# C++ Code 
"""
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> AdjList;
        // first convert into adjacency list(edges) for directed graph
        for (auto& pre : prerequisites) {
            int second = pre[0], first = pre[1];
            AdjList[first].push_back(second);
        }

        vector<int> visited(numCourses, 0);
        vector<int> stack;   // store the course completion in reverse order

        for (int i = 0; i < numCourses; i++) {
            if (!FindTopoSort(AdjList, i, stack, visited)) {    // if cycle simply return False, else continue checking for another node
                return {};
            }
        }

        reverse(stack.begin(), stack.end());
        return stack;
    }

    bool FindTopoSort(unordered_map<int, vector<int>>& adj, int src, vector<int>& stack, vector<int>& visited) {
        // base case for checking whether we have visited all the adjacent node.. if visited then check on another node
        if (visited[src] == 1)   // been visited and added to the stack(ans). so simply return true so that it can check for next node without repeating the work
            return true;         // returning False will give wrong ans as when it will see 'False' funtion will return from there only.
        // base case for checking cycle 
        if (visited[src] == -1)   // means cycle as the current node(src) is already visited in current cycle only
            return false;        // if not '0' means the this has been visited(not) and if = '-1' then visited in current cycle , means there is cycle.

        // code starts from here
        visited[src] = -1;   // Marking 'cur' node is visited in current cycle. Also it means till now we have only visited the 'src' not its adjacent node.
        for (int u : adj[src]) {
            if (!FindTopoSort(adj, u, stack, visited)) {
                return false;
            }
        }

        // while traversing back make visited[src]= 1 and  put the node into the stack
        visited[src] = 1;   // means we have visited the 'src' as well as its neighbour and added to the ans(stack)
        stack.push_back(src);
        return true;   // means we have visited the current node as well as its neighbour successfully
    }
};

"""
