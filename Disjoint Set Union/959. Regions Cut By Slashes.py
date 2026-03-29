"""
First understand the question properly.
1. What do the Variables Represent?
n: The size of the grid. If grid = [" /", "/ "], then n = 2. This means you have a 2 * 2 total area.
grid[i]: This represents one row of the grid.
grid[i][j]: This represents a single 1 * 1 square at row i and column j.
Note : n = len(grid) = len(grid[i]) because of square.

1. Thought Process:
Imagine a grid of size n * n. To draw this grid, you actually need (n+1) * (n+1) dots.
    The Boundary: Initially, all the dots on the outer boundary of the n * n square are already connected. They form one single big loop (the outer frame).
    The Slashes as Edges: Every '/' or '\\' is essentially an edge connecting two dots. 
        A forward slash '/' in cell (i, j) connects the dot at (i, j+1) to the dot at (i+1, j).
        A backslash '\\' in cell (i, j) connects the dot at (i, j) to the dot at (i+1, j+1).
        Note : only see square from right side from point (i, j)
    Creating Regions: In a graph where the boundary is already connected, every time you connect two dots that are already part of the same component, you have closed a cycle.
    The Result: Every closed cycle creates exactly one new enclosed region.

2. The Logic: Why dsu.count works
a) Initial State: We connect all boundary dots (top edge, bottom edge, left edge, right edge) to a single representative (dot 0). 
This forms our first "cycle" (the outer boundary). We set count = 1.
b) Adding Slashes: For every slash, we check if the two dots it connects are already in the same set using findParent.
c) Cycle Detection: If findParent(dot1) == findParent(dot2), it means there is already a path between them. 
Adding this slash completes a new loop. Thus, count += 1.

Note : Make diagram on paper for better visualisation.

Q) Why use (n+1) * (n+1)?
A single square (1x1) has vertices at:(0,0), (0,1)(1,0), (1,1)
To represent a grid of $n$ squares, you need $n+1$ points in each direction. If n=3, you have points 0, 1, 2, 3.

Time : O(n^2 * alpha(n^2)) 
space : O(n^2) 
"""

class DSU:
    def __init__(self, n):
        # parent[i] stores the parent of node i
        self.parent = [i for i in range(n)]
        # size[i] used for Union by Size optimization
        self.size = [1 for i in range(n)]
        # count starts at 1 because the outer boundary itself forms the first region
        self.count = 1
    
    def findParent(self, n):   
        if n == self.parent[n]:   
            return n
        # Path Compression: making the tree flat for O(alpha(N)) lookups
        self.parent[n] = self.findParent(self.parent[n])   
        return self.parent[n]
    
    def union(self, n1, n2):  
        p1, p2 = self.findParent(n1), self.findParent(n2)
        
        # If both dots already share the same parent, a cycle is formed
        if p1 == p2:
            self.count += 1
            return 
        
        # Union by Size: attach the smaller tree to the larger tree
        if self.size[p1] < self.size[p2]:
            self.parent[p1] = p2  
            self.size[p2] += self.size[p1]   
        else:
            self.parent[p2] = p1   
            self.size[p1] += self.size[p2]

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        # An n x n grid has (n+1) x (n+1) vertices (dots)
        dots_per_side = n + 1
        total_dots = dots_per_side * dots_per_side
        
        dsu = DSU(total_dots)
        
        # Step 1: Connect all dots on the boundary to each other.
        # This forms the initial single region (the outer frame).
        for i in range(dots_per_side):
            for j in range(dots_per_side):
                if i == 0 or i == n or j == 0 or j == n:
                    current_dot_idx = i * dots_per_side + j
                    # We union all boundary dots with dot 0
                    dsu.union(0, current_dot_idx)
        
        # Step 2: Manually reset count to 1 after boundary initialization
        # Because our union logic increments count for cycles, and the 
        # boundary initialization will trigger that logic.
        # (Alternatively, you could start count at 0 and let the boundary union set it to 1)
        
        # Step 3: Iterate through each cell and add edges based on slashes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    # '/' connects top-right dot to bottom-left dot
                    # Top-right dot coords: (i, j+1)
                    # Bottom-left dot coords: (i+1, j)
                    dot1 = i * dots_per_side + (j + 1)
                    dot2 = (i + 1) * dots_per_side + j
                    dsu.union(dot1, dot2)
                    
                elif grid[i][j] == '\\':
                    # '\' connects top-left dot to bottom-right dot
                    # Top-left dot coords: (i, j)
                    # Bottom-right dot coords: (i+1, j+1)
                    dot1 = i * dots_per_side + j
                    dot2 = (i + 1) * dots_per_side + (j + 1)
                    dsu.union(dot1, dot2)
                    
        return dsu.count

# Java
"""
class DSU {
    private int[] parent;
    private int[] size;
    private int count;
    
    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        count = 0;
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }
    
    public int findParent(int n) {
        if (n == parent[n]) {
            return n;
        }
        parent[n] = findParent(parent[n]); // Path compression
        return parent[n];
    }
    
    public void union(int n1, int n2) {
        int p1 = findParent(n1);
        int p2 = findParent(n2);
        if (p1 == p2) {
            count++;
            return;
        }
        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
    }
    
    public int getCount() {
        return count;
    }
}

class Solution {
    public int regionsBySlashes(String[] grid) {
        int n = grid.length;
        int dots = (n + 1) * (n + 1);
        DSU dsu = new DSU(dots * dots);
        
        // 1st connect boundary with (0, 0)
        for (int i = 0; i <= n; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || i == n || j == 0 || j == n) {
                    int index = i * (n + 1) + j;
                    dsu.union(0, index);
                }
            }
        }
        
        // Traverse grid and join based on slashes
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i].charAt(j) == '/') {
                    int index1 = i * (n + 1) + (j + 1);
                    int index2 = (i + 1) * (n + 1) + j;
                    dsu.union(index1, index2);
                } else if (grid[i].charAt(j) == '\\') {
                    int index1 = i * (n + 1) + j;
                    int index2 = (i + 1) * (n + 1) + (j + 1);
                    dsu.union(index1, index2);
                }
            }
        }
        
        return dsu.getCount();
    }
}
"""
