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
# Shortcut of above one.
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
// Logic: It should be connected into a single component with no cycle.
class Solution {
    int[] parent;
    int[] rank;

    public int find(int n) {
        int p = parent[n];
        while (p != parent[p]) {
            parent[p] = parent[parent[p]]; // Path compression
            p = parent[p];
        }
        return p;
    }

    public boolean union(int n1, int n2) {
        int p1 = find(n1);
        int p2 = find(n2);
        if (p1 == p2) return false; // Cycle detected

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
        rank = new int[n]; // Initially, rank of all will be 0 (single node)
        for (int i = 0; i < n; i++) parent[i] = i;

        for (int[] edge : edges) {
            if (!union(edge[0], edge[1])) return false; // If union returns false, cycle exists
        }

        // If no cycle, then we just need to check if all nodes are connected
        return edges.length == n - 1; // For a tree: n-1 edges
    }
}


// Method 2: Shortcut of above one
class Solution2 {
    int[] nums;

    public int find(int i) {
        if (nums[i] == -1) return i;
        return find(nums[i]);
    }

    public boolean validTree(int n, int[][] edges) {
        nums = new int[n];
        Arrays.fill(nums, -1); // Initialize n isolated islands

        for (int[] edge : edges) {
            int x = find(edge[0]);
            int y = find(edge[1]);

            if (x == y) return false; // Cycle found

            nums[x] = y; // Union
        }

        return edges.length == n - 1; // Must have n-1 edges to be a valid tree
    }
}


// Method 3: Using DFS
class Solution3 {
    Map<Integer, List<Integer>> graph = new HashMap<>();
    Set<Integer> visited = new HashSet<>();

    // This will check cycle or not using DFS
    public boolean isCycle(int src, int parent) {
        visited.add(src);
        for (int u : graph.getOrDefault(src, new ArrayList<>())) {
            if (!visited.contains(u)) {
                if (isCycle(u, src)) return true;
            } else if (u != parent) {
                return true; // Means cycle
            }
        }
        return false;
    }

    public boolean validTree(int n, int[][] edges) {
        // First convert into adjacency list
        for (int[] edge : edges) {
            graph.computeIfAbsent(edge[0], k -> new ArrayList<>()).add(edge[1]);
            graph.computeIfAbsent(edge[1], k -> new ArrayList<>()).add(edge[0]);
        }

        // For tree it should be connected and should not have a cycle
        // So we only need to call dfs once; if connected all nodes will be visited
        if (isCycle(0, -1)) return false; // Means cycle, so not a tree

        return visited.size() == n; // Check connected component
    }
}

"""

# C++ Code 
"""
// Method 1: Union-Find
// Logic: It should be connected into a single component with no cycle.
class Solution {
public:
    vector<int> parent, rank;

    int find(int n) {
        int p = parent[n];
        while (p != parent[p]) {
            parent[p] = parent[parent[p]]; // Path compression
            p = parent[p];
        }
        return p;
    }

    bool unionSet(int n1, int n2) {
        int p1 = find(n1), p2 = find(n2);
        if (p1 == p2) return false; // Cycle detected

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
        rank.resize(n, 0); // Initially, rank of all will be 0 (single node)
        for (int i = 0; i < n; ++i) parent[i] = i;

        for (auto& e : edges) {
            if (!unionSet(e[0], e[1])) return false; // If union returns false, cycle exists
        }

        // If no cycle, then we just need to check if all nodes are connected
        return edges.size() == n - 1; // For a tree: n-1 edges
    }
};


// Method 2: Shortcut of above one
class Solution2 {
public:
    vector<int> nums;

    int find(int i) {
        if (nums[i] == -1) return i;
        return find(nums[i]);
    }

    bool validTree(int n, vector<vector<int>>& edges) {
        nums.resize(n, -1); // Initialize n isolated islands

        for (auto& edge : edges) {
            int x = find(edge[0]);
            int y = find(edge[1]);

            if (x == y) return false; // Cycle found

            nums[x] = y; // Union
        }

        return edges.size() == n - 1; // Must have n-1 edges to be a valid tree
    }
};


// Method 3: Using DFS
class Solution3 {
public:
    unordered_map<int, vector<int>> graph;
    unordered_set<int> visited;

    // This will check cycle or not using DFS
    bool isCycle(int src, int parent) {
        visited.insert(src);
        for (int u : graph[src]) {
            if (visited.find(u) == visited.end()) {
                if (isCycle(u, src)) return true;
            } else if (u != parent) {
                return true; // Means cycle
            }
        }
        return false;
    }

    bool validTree(int n, vector<vector<int>>& edges) {
        // First convert into adjacency list
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }

        // For tree it should be connected and should not have a cycle
        // So we only need to call dfs once; if connected all nodes will be visited
        if (isCycle(0, -1)) return false; // Means cycle, so not a tree

        return visited.size() == n; // Check connected component
    }
};

"""