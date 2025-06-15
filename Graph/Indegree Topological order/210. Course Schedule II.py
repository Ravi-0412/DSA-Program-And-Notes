# Method 1: 

# just print the order of topological sort

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
        List<List<Integer>> AdjList = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            AdjList.add(new ArrayList<>());
        }

        int[] indegree = new int[n];
        
        // first convert into adjacency list(edges) for directed graph and calculate indegree
        for (int[] pair : prerequisites) {
            int second = pair[0];
            int first = pair[1];
            AdjList.get(first).add(second);
            indegree[second]++;
        }

        int count = 0;
        List<Integer> ans = new ArrayList<>();
        Queue<Integer> Q = new LinkedList<>();

        // now applying the BFS to get the topological order
        // find the node with indegree '0' as this node will come 1st in the topological order
        // i.e it will be the source node and after that apply the BFS
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
            for (int j : AdjList.get(u)) {
                indegree[j]--;
                if (indegree[j] == 0) {  // after decreasing if any node has indegree == 0 then put in the Q
                    Q.add(j);
                }
            }
        }

        if (count != n) {  // means cycle so no order is possible
            return new int[0];
        }

        // Convert List<Integer> to int[]
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = ans.get(i);
        }
        return res;
    }
}

"""


# C++ Code 
"""
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int n = numCourses;
        vector<vector<int>> AdjList(n);
        vector<int> indegree(n, 0);

        // first convert into adjacency list(edges) for directed graph and calculate indegree
        for (auto& pair : prerequisites) {
            int second = pair[0];
            int first = pair[1];
            AdjList[first].push_back(second);
            indegree[second]++;
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
            count++;
            int u = Q.front();
            Q.pop();
            ans.push_back(u);

            // after poping decrease the indegree of all node adjacent to 'u'
            for (int j : AdjList[u]) {
                indegree[j]--;
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


# Method 2: 
# Using DFS

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
        List<List<Integer>> AdjList = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) {
            AdjList.add(new ArrayList<>());
        }

        // first convert into adjacency list(edges) for directed graph
        for (int[] pair : prerequisites) {
            int second = pair[0];
            int first = pair[1];
            AdjList.get(first).add(second);
        }

        int[] visited = new int[numCourses];
        List<Integer> stack = new ArrayList<>();  // store the course completion in reverse order

        for (int i = 0; i < numCourses; i++) {
            if (!FindTopoSort(AdjList, i, stack, visited)) {
                return new int[0]; // if cycle simply return []
            }
        }

        // reverse stack to get the actual order
        Collections.reverse(stack);
        int[] res = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            res[i] = stack.get(i);
        }
        return res;
    }

    // Returns true if no cycle is found, false if cycle is found
    private boolean FindTopoSort(List<List<Integer>> adj, int src, List<Integer> stack, int[] visited) {
        // base case for checking whether we have visited all the adjacent node.. 
        if (visited[src] == 1)  // been visited and added to the stack(ans). so simply return true
            return true;
        // base case for checking cycle 
        if (visited[src] == -1)  // means cycle as the current node(src) is already visited in current cycle only
            return false;

        // code starts from here
        visited[src] = -1;  // Marking 'cur' node is visited in current cycle
        for (int u : adj.get(src)) {
            if (!FindTopoSort(adj, u, stack, visited))
                return false;
        }

        // while traversing back mark visited[src]= 1 and put the node into the stack
        visited[src] = 1;
        stack.add(src);
        return true;
    }
}


"""


# C++ Code 
"""
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        int n = numCourses;
        vector<vector<int>> AdjList(n);
        // first convert into adjacency list(edges) for directed graph
        for (auto& pair : prerequisites) {
            int second = pair[0];
            int first = pair[1];
            AdjList[first].push_back(second);
        }

        vector<int> visited(n, 0);
        vector<int> stack;  // store the course completion in reverse order

        for (int i = 0; i < n; i++) {
            if (!FindTopoSort(AdjList, i, stack, visited)) {
                return {}; // if cycle simply return []
            }
        }

        reverse(stack.begin(), stack.end());
        return stack;
    }

    // Returns true if no cycle is found, false if cycle is found
    bool FindTopoSort(vector<vector<int>>& adj, int src, vector<int>& stack, vector<int>& visited) {
        // base case for checking whether we have visited all the adjacent node..
        if (visited[src] == 1)  // been visited and added to the stack(ans). so simply return true
            return true;
        // base case for checking cycle 
        if (visited[src] == -1)  // means cycle as the current node(src) is already visited in current cycle only
            return false;

        // code starts from here
        visited[src] = -1;  // Marking 'cur' node is visited in current cycle
        for (int u : adj[src]) {
            if (!FindTopoSort(adj, u, stack, visited))
                return false;
        }

        // while traversing back mark visited[src]= 1 and put the node into the stack
        visited[src] = 1;
        stack.push_back(src);
        return true;
    }
};

"""

