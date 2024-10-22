# Q: Simply asking: "Make connections acyclic by removing the edges that are leading to cycle' and then 
# connect required no of edges to make all nodes connected into a single component.

# logic: we exactly need 'n-1' edges to connect 'n' nodes into one component with no cycle.
# There can be extra cable than the required one 'n-1'.
# so first calculate the extra_cable=> extra_cable= len(connections) - (n-1)
# then calculate the no of cable we have to remove to make connections acyclic.

# But here is the twist. we may not require all removed cable to connect the remaining node.
# we only need 'n-1' cable in total i.e 'no of cables in connection after removing' + cables required to connect remaining.

# so to get the ans subtract 'extra_cable from removed_cables' and finally 
# ans will be equal to: ans= removed_cables - extra cable.

class DSU:
    def __init__(self, n):
        self.v= n
        self.parent=  [i for i in range(n)]     # here '0' based indexing is used in Q.
        self.size=    [1 for i in range(n)]   # will give thesize of each parent component.
            # initially size of all be '1'(node itself).
    
    def findUPar(self, n):   # finding the ultimate parent
        if n== self.parent[n]:   # Root parent will be the parent of itself. so continue till we find that.
            return n
        # return self.parent[n]= self.findUPar(self.parent[n])    # this will assign the root parent of every node coming in that ultimate root.
                                                #    This is called path compression.
        self.parent[n]= self.findUPar(self.parent[n])   # writing above in same link is giving error
        return self.parent[n]
        # return self.findUPar(self.parent[n])   # This will only give the parent node, will not assign.
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return False
        # wherever we are assigning the parent means we are directly connecting those two nodes.
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2   # attaching ultimate parent of 'n1' i.e p1 to ultimate parent of 'n2' i.e p2.
            self.size[p2]+= self.size[p1]   # increase the size of p2 by size of p1.
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   # attaching ultimate parent of 'n2' i.e p2 to ultimate parent of 'n1' i.e p1.
            self.size[p1]+= self.size[p2]
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:  # we need at atleast 'n-1' edges to connect 'n' nodes into one single component.
            return -1
        extra_cable= len(connections) - (n-1)
        # print(extra_cable)
        dsu= DSU(n)
        to_remove= 0
        for n1, n2 in connections:
            if dsu.unionBySize(n1, n2)== False:
                # print(n1, n2)
                to_remove+= 1
        # print(to_remove, "remove")
        to_add= to_remove - extra_cable
        return to_add


# Method 2: very simple , concise and good logic.
# just find the no of components say 'k' then, to connect all these components together we need exactly 'k-1' edge.
# 'k-1' will be our ans as we have to connect all these components together only.
# so no need to worry about from how we will get these edges.
class DSU:
    def __init__(self, n):
        self.v= n
        self.parent=  [i for i in range(n)]     # here '0' based indexing is used in Q.
        self.size=    [1 for i in range(n)]   # will give thesize of each parent component.
            # initially size of all be '1'(node itself).
    
    def findUPar(self, n):   # finding the ultimate parent
        if n== self.parent[n]:   # Root parent will be the parent of itself. so continue till we find that.
            return n
        # return self.parent[n]= self.findUPar(self.parent[n])    # this will assign the root parent of every node coming in that ultimate root.
                                                #    This is called path compression.
        self.parent[n]= self.findUPar(self.parent[n])   # writing above in same link is giving error
        return self.parent[n]
        # return self.findUPar(self.parent[n])   # This will only give the parent node, will not assign.
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return 
        # wherever we are assigning the parent means we are directly connecting those two nodes.
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2   # attaching ultimate parent of 'n1' i.e p1 to ultimate parent of 'n2' i.e p2.
            self.size[p2]+= self.size[p1]   # increase the size of p2 by size of p1.
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   # attaching ultimate parent of 'n2' i.e p2 to ultimate parent of 'n1' i.e p1.
            self.size[p1]+= self.size[p2]
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        dsu= DSU(n)
        component= 0
        for n1, n2 in connections:
            dsu.unionBySize(n1, n2)
        
        component= 0
        for p in range(n):  
            if p== dsu.parent[p]:
                component+= 1
        return component -1

# Java
"""
class DSU {
    private int[] parent;
    private int[] size;

    // Constructor to initialize DSU
    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i; // Each node is its own parent initially
            size[i] = 1;   // Size of each component is initially 1
        }
    }

    // Method to find the ultimate parent (with path compression)
    public int findUPar(int n) {
        if (n == parent[n]) {
            return n; // If the node is its own parent, return it
        }
        // Path compression
        parent[n] = findUPar(parent[n]);
        return parent[n];
    }

    // Method to perform union by size
    public void unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);
        
        if (p1 == p2) {
            return; // They are already in the same component
        }
        
        // Union by size
        if (size[p1] < size[p2]) {
            parent[p1] = p2; // Attach p1's tree to p2's tree
            size[p2] += size[p1]; // Update size
        } else {
            parent[p2] = p1; // Attach p2's tree to p1's tree
            size[p1] += size[p2]; // Update size
        }
    }
}

class Solution {
    public int makeConnected(int n, int[][] connections) {
        // Step 1: Check if we have enough connections
        if (connections.length < n - 1) {
            return -1; // Not enough connections to connect all computers
        }

        // Step 2: Initialize DSU
        DSU dsu = new DSU(n);
        
        // Step 3: Union each connection
        for (int[] connection : connections) {
            dsu.unionBySize(connection[0], connection[1]);
        }

        // Step 4: Count how many unique components there are
        int componentCount = 0;
        for (int i = 0; i < n; i++) {
            if (i == dsu.findUPar(i)) {
                componentCount++; // Increment for each root parent
            }
        }

        // To connect all components, we need (components - 1) connections
        return componentCount - 1; 
    }
}

"""
