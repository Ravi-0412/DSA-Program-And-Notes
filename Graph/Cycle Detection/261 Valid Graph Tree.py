# Method 1: Union-find

# Logic: It should be connected into single coponent with no cycle.

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent= [i for i in range(n)]  
        rank= [0] *(n)  # initally rank of all will be '0' since all are at height '0' (single node)
        
        # finding the root parent and the 1st level parent
        # for root level parent, compress the path till parent[p]!= p as root will parent as root only
        def find(n):
            p= parent[n]
            while p!= parent[p]:
                parent[p]= parent[parent[p]]  
                p= parent[p]
            return p
        
        def union(n1,n2):
            p1,p2= find(n1), find(n2)
            if p1== p2:            
                return False  
            
            if rank[p1]> rank[p2]:
                parent[p2]= p1
                
            else:
                parent[p1]= p2
                if rank[p2]== rank[p1]:
                    rank[p2]+= 1
        
        # code starts from here
        for n1,n2 in edges:
            if union(n1,n2)== False:
                return False
        # Means there is no cycle so only thing need to check is that they are conencted into a single component.
        # Fo this no of edges should = n -1
        return len(edges) == n - 1

# Method 2:
# Shortcut of Method 1.

class Solution:
    def validTree(self, n, edges):
        # initialize n isolated islands
        nums = [-1] * n
        
        # perform union find
        for edge in edges:
            x = self.find(nums, edge[0])
            y = self.find(nums, edge[1])
            
            # if two vertices happen to be in the same set
            # then there's a cycle
            if x == y:
                return False
            
            # union
            nums[x] = y
        
        return len(edges) == n - 1
    
    def find(self, nums, i):
        if nums[i] == -1:
            return i
        return self.find(nums, nums[i])


# method 3: using DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # first convert into adjacency list say 'graph'
        graph= collections.defaultdict(list)
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)

        visited= set()
        # this will check cycle or not using DFS
        def isCycle(src,parent):
            visited.add(src)
            for u in graph[src]:
                if u not in visited:
                    if isCycle(u,src):
                        return True
                elif u != parent:  # means cycle
                    return True

        # code starts from here
        # for tree it shoule be connected and should not have a cycle
        # so we only need to call dfs once, if conneceted all node will get visited 
        if isCycle(0,-1):   # means cycle  so it can't be a tree
            return False
        # to check connected or not. Either you do this or call Dfs in a for loop and count the no of times dfs is called..
        #  if called more than one time then it means has more than one component
        if len(visited) == n:  
            return True
        return False


# Java
""""
// Method 1: Union-Find
import java.util.*;

public class Solution {
    int[] parent;
    int[] rank;

    // Finds the root parent with path compression
    private int find(int n) {
        int p = parent[n];
        while (p != parent[p]) {
            parent[p] = parent[parent[p]];  // Path compression
            p = parent[p];
        }
        return p;
    }

    // Unions two nodes; returns false if they are already connected (cycle detected)
    private boolean union(int n1, int n2) {
        int p1 = find(n1), p2 = find(n2);
        if (p1 == p2) {
            return false;  // A cycle is detected
        }

        if (rank[p1] > rank[p2]) {
            parent[p2] = p1;
        } else {
            parent[p1] = p2;
            if (rank[p2] == rank[p1]) {
                rank[p2]++;
            }
        }
        return true;
    }

    public boolean validTree(int n, int[][] edges) {
        parent = new int[n];
        rank = new int[n];

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        // Main logic starts here
        for (int[] edge : edges) {
            if (!union(edge[0], edge[1])) {
                return false;
            }
        }

        // If there are no cycles, we still need to check that the graph is fully connected
        // A valid tree must have exactly n - 1 edges
        return edges.length == n - 1;
    }
}



// Method 2: Shortcut of above one
public class Solution {
    // this will check cycle or not using union-find
    public boolean validTree(int n, int[][] edges) {
        // initialize n isolated islands
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = -1;

        // perform union find
        for (int[] edge : edges) {
            int x = find(nums, edge[0]);
            int y = find(nums, edge[1]);

            // if two vertices happen to be in the same set
            // then there's a cycle
            if (x == y) {
                return false;
            }

            // union
            nums[x] = y;
        }

        return edges.length == n - 1;
    }

    public int find(int[] nums, int i) {
        if (nums[i] == -1) return i;
        return find(nums, nums[i]);
    }
}



// Method 3: Using DFS
import java.util.*;

public class Solution {
    Map<Integer, List<Integer>> graph = new HashMap<>();
    Set<Integer> visited = new HashSet<>();

    public boolean validTree(int n, int[][] edges) {
        // first convert into adjacency list say 'graph'
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(edge[1]);
            graph.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(edge[0]);
        }

        // code starts from here
        // for tree it should be connected and should not have a cycle
        // so we only need to call dfs once, if connected all nodes will get visited 
        if (isCycle(0, -1)) {   // means cycle so it can't be a tree
            return false;
        }

        // to check connected or not. Either you do this or call DFS in a for loop and count the number of times DFS is called.
        // if called more than one time then it means has more than one component
        return visited.size() == n;
    }

    // this will check cycle or not using DFS
    public boolean isCycle(int src, int parent) {
        visited.add(src);
        for (int neighbor : graph.getOrDefault(src, new ArrayList<>())) {
            if (!visited.contains(neighbor)) {
                if (isCycle(neighbor, src)) {
                    return true;
                }
            } else if (neighbor != parent) {  // means cycle
                return true;
            }
        }
        return false;
    }
}



"""

# C++ Code 
"""
// Method 1: 
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> parent;
    vector<int> rank;

    // Finds the root parent with path compression
    int find(int n) {
        int p = parent[n];
        while (p != parent[p]) {
            parent[p] = parent[parent[p]];  // Path compression
            p = parent[p];
        }
        return p;
    }

    // Unions two nodes; returns false if they are already connected (cycle detected)
    bool unionSet(int n1, int n2) {
        int p1 = find(n1), p2 = find(n2);
        if (p1 == p2) {
            return false;  // A cycle is detected
        }

        if (rank[p1] > rank[p2]) {
            parent[p2] = p1;
        } else {
            parent[p1] = p2;
            if (rank[p2] == rank[p1]) {
                rank[p2]++;
            }
        }
        return true;
    }

    bool validTree(int n, vector<vector<int>>& edges) {
        parent.resize(n);
        rank.resize(n, 0);

        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        // Main logic starts here
        for (auto& edge : edges) {
            if (!unionSet(edge[0], edge[1])) {
                return false;
            }
        }

        // If there are no cycles, we still need to check that the graph is fully connected
        // A valid tree must have exactly n - 1 edges
        return edges.size() == n - 1;
    }
};



// Method 2: 
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        // initialize n isolated islands
        vector<int> nums(n, -1);

        // perform union find
        for (auto& edge : edges) {
            int x = find(nums, edge[0]);
            int y = find(nums, edge[1]);

            // if two vertices happen to be in the same set
            // then there's a cycle
            if (x == y) {
                return false;
            }

            // union
            nums[x] = y;
        }

        return edges.size() == n - 1;
    }

    int find(vector<int>& nums, int i) {
        if (nums[i] == -1) return i;
        return find(nums, nums[i]);
    }
};



// Method 3: Using DFS
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

class Solution {
public:
    unordered_map<int, vector<int>> graph;
    unordered_set<int> visited;

    bool validTree(int n, vector<vector<int>>& edges) {
        // first convert into adjacency list say 'graph'
        for (auto& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        // code starts from here
        // for tree it should be connected and should not have a cycle
        // so we only need to call dfs once, if connected all nodes will get visited 
        if (isCycle(0, -1)) {   // means cycle so it can't be a tree
            return false;
        }

        // to check connected or not. Either you do this or call DFS in a for loop and count the number of times DFS is called.
        // if called more than one time then it means has more than one component
        return visited.size() == n;
    }

    // this will check cycle or not using DFS
    bool isCycle(int src, int parent) {
        visited.insert(src);
        for (int neighbor : graph[src]) {
            if (!visited.count(neighbor)) {
                if (isCycle(neighbor, src)) {
                    return true;
                }
            } else if (neighbor != parent) {  // means cycle
                return true;
            }
        }
        return false;
    }
};



"""