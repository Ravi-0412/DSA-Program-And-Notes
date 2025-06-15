# Logic an dexplanation in notes, page: 15 & 16

class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]
        self.count = 0
    
    def findParent(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findParent(self.parent[n])   
        return self.parent[n]
    
    def union(self, n1, n2):  
        p1, p2 = self.findParent(n1), self.findParent(n2)
        if p1== p2:
            # Means new cycle so number of component will increase
            self.count += 1
            return 
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # size[p1]>= size[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]
    
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        dots = (n + 1) *(n + 1)
        dsu = DSU(dots *dots)
        # 1st connect boundary with (0, 0)
        for i in range(dots):
            for j in range(dots):
                if i == 0 or i == n or j == 0 or j == n:
                    # find the cell number(index) in 1D for this (i, j)
                    index = i * dots + j
                    dsu.union(0, index)

        # Traverse grid and join based on slashes
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    index1 = i * dots + (j + 1)   # dot1
                    index2 = (i + 1) * dots + j  # dot2
                    dsu.union(index1, index2)
                elif grid[i][j] == '\\':
                    index1 = i * dots + j              # dot1
                    index2 = (i + 1) * dots + (j + 1)  # dot2
                    dsu.union(index1, index2)
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