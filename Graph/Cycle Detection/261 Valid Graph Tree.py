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
// Method 1:
public class Solution {
    private int find(int node, int[] parent) {
        if (parent[node] != node) {
            parent[node] = find(parent[node], parent);
        }
        return parent[node];
    }

    private boolean union(int node1, int node2, int[] parent, int[] rank) {
        int root1 = find(node1, parent);
        int root2 = find(node2, parent);

        if (root1 == root2) {
            return false;
        }

        if (rank[root1] > rank[root2]) {
            parent[root2] = root1;
        } else if (rank[root1] < rank[root2]) {
            parent[root1] = root2;
        } else {
            parent[root2] = root1;
            rank[root1]++;
        }
        return true;
    }

    public boolean validTree(int n, int[][] edges) {
        int[] parent = new int[n];
        int[] rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        for (int[] edge : edges) {
            if (!union(edge[0], edge[1], parent, rank)) {
                return false;
            }
        }

        return edges.length == n - 1;
    }
}

// method 2:
public class Solution {
    public boolean validTree(int n, int[][] edges) {
        // initialize n isolated islands
        int[] nums = new int[n];
        Arrays.fill(nums, -1);
        
        // perform union find
        for (int i = 0; i < edges.length; i++) {
            int x = find(nums, edges[i][0]);
            int y = find(nums, edges[i][1]);
            
            // if two vertices happen to be in the same set
            // then there's a cycle
            if (x == y) return false;
            
            // union
            nums[x] = y;
        }
        
        return edges.length == n - 1;
    }
    
    int find(int nums[], int i) {
        if (nums[i] == -1) return i;
        return find(nums, nums[i]);
    }
}

// Method 3:
public class Solution {
    private Map<Integer, List<Integer>> graph;
    private Set<Integer> visited;

    public boolean validTree(int n, int[][] edges) {
        // Convert into adjacency list
        graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        visited = new HashSet<>();

        // Check for cycle
        if (isCycle(0, -1)) {
            return false;
        }

        // Check if all nodes are connected
        return visited.size() == n;
    }

    // Function to check cycle using DFS
    private boolean isCycle(int src, int parent) {
        visited.add(src);
        for (int neighbor : graph.get(src)) {
            if (!visited.contains(neighbor)) {
                if (isCycle(neighbor, src)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true; // Cycle detected
            }
        }
        return false;
    }
}

"""