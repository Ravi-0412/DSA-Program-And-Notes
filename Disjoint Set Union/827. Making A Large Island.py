# Method 1: 

# logic: first form the sets(connected components) using the given ele when you encounter '1' with its adjacent neighbour.
# in this way parent and size will get updated automatically.

# Now try to fill '0' with ''1' . and try to combine the size of all of parent adjacent cell having value= 1.
# VVI: But the adjacent cell may have same ultimate parent(may adjacent cell connected to each other also) and if we combine their size then,
# we will get the wrong ans.
# so we we need something to check for each whether we have already visited that ultimate parent or not for each available '0'.
# so using visited_parent to check for every node.

class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]   
    
    def findUPar(self, n):   
        if n== self.parent[n]:   
            return n
        self.parent[n]= self.findUPar(self.parent[n])   
        return self.parent[n]
    
    def unionBySize(self, n1, n2):
        p1, p2= self.findUPar(n1), self.findUPar(n2)
        if p1== p2:   # we can't do union since they belong to the same component.
            return
        if self.size[p1] < self.size[p2]:
            self.parent[p1]= p2  
            self.size[p2]+= self.size[p1]   
        else :   # rank[p1]>= rank[p2]
            self.parent[p2]= p1   
            self.size[p1]+= self.size[p2]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n= len(grid), len(grid[0])
        def isValid(r, c):
            if r >= 0 and r < m and c >= 0 and c< m:
                return True
            return False

        dsu= DSU(m*n)

        # form components with available '1'.
        for r in range(m):
            for c in range(n):
                if grid[r][c]== 1:
                    ind= r * n + c
                    # now check in all four directions
                    directions= [[r, c-1], [r, c+1], [r-1, c], [r+1, c]]  # left, right, up, down
                    for dr, dc in directions:
                        ind1= dr * n + dc   # calculating the index number
                        if isValid(dr, dc) and grid[dr][dc]== 1:
                            dsu.unionBySize(ind, ind1)  # forming the union
        
        max_size= max(dsu.size)   # to handle the base case if there is all '1'.
        # now try to replace every '0' with '1'.
        for r in range(m):
            for c in range(n):
                if grid[r][c]== 0:
                    combinedSize= 1   # curr '0' will also contribute to the ans.
                    ind= r * n + c
                    visited_parent= set()  # check the ultimate parent is visited or not.
                    # now check in all four directions
                    directions= [[r, c-1], [r, c+1], [r-1, c], [r+1, c]]  # left, right, up, down
                    for dr, dc in directions:
                        nei_ind= dr * n + dc   # calculating the index number
                        if isValid(dr, dc) and grid[dr][dc]== 1:
                            adj_parent= dsu.findUPar(nei_ind)  #  we have to combine with size of parent not with the cell.
                            if not visited_parent or adj_parent not in visited_parent:   
                                combinedSize+= dsu.size[adj_parent]
                                max_size= max(max_size, combinedSize)
                                visited_parent.add(adj_parent)
        return max_size


# Java
"""
import java.util.*;

class DSU {
    int[] parent;
    int[] size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int findUPar(int n) {
        if (n == parent[n]) return n;
        return parent[n] = findUPar(parent[n]); // path compression
    }

    public void unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);
        if (p1 == p2) return; // we can't do union since they belong to the same component.

        // wherever we are assigning the parent means we are directly connecting those two nodes.
        if (size[p1] < size[p2]) {
            parent[p1] = p2;  // attaching ultimate parent of 'n1' to ultimate parent of 'n2'.
            size[p2] += size[p1]; // increase the size of p2 by size of p1.
        } else {
            parent[p2] = p1;  // attaching ultimate parent of 'n2' to ultimate parent of 'n1'.
            size[p1] += size[p2];
        }
    }
}

class Solution {
    public int largestIsland(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        DSU dsu = new DSU(m * n);

        // form components with available '1'.
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    int ind = r * n + c;
                    int[][] directions = {{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}}; // left, right, up, down
                    for (int[] dir : directions) {
                        int dr = dir[0], dc = dir[1];
                        if (isValid(dr, dc, m, n) && grid[dr][dc] == 1) {
                            int ind1 = dr * n + dc;
                            dsu.unionBySize(ind, ind1); // forming the union
                        }
                    }
                }
            }
        }

        int max_size = 0;
        for (int val : dsu.size) {
            max_size = Math.max(max_size, val); // to handle the base case if all are '1'
        }

        // now try to replace every '0' with '1'.
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 0) {
                    int combinedSize = 1; // current '0' will also contribute to the answer
                    Set<Integer> visited_parent = new HashSet<>();
                    int[][] directions = {{r, c - 1}, {r, c + 1}, {r - 1, c}, {r + 1, c}}; // left, right, up, down

                    for (int[] dir : directions) {
                        int dr = dir[0], dc = dir[1];
                        if (isValid(dr, dc, m, n) && grid[dr][dc] == 1) {
                            int nei_ind = d_

"""


# c++
"""
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class DSU {
public:
    vector<int> parent, size;

    DSU(int n) {
        parent.resize(n);
        size.resize(n, 1);
        for(int i = 0; i < n; i++) parent[i] = i;
    }

    int findUPar(int n) {
        if(n == parent[n]) return n;
        return parent[n] = findUPar(parent[n]); // path compression
    }

    void unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);
        if(p1 == p2) return; // we can't do union since they belong to the same component.

        // wherever we are assigning the parent means we are directly connecting those two nodes.
        if(size[p1] < size[p2]) {
            parent[p1] = p2; // attaching ultimate parent of 'n1' to ultimate parent of 'n2'.
            size[p2] += size[p1]; // increase the size of p2 by size of p1.
        } else {
            parent[p2] = p1; // attaching ultimate parent of 'n2' to ultimate parent of 'n1'.
            size[p1] += size[p2];
        }
    }
};

class Solution {
public:
    int largestIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        DSU dsu(m * n);

        auto isValid = [&](int r, int c) {
            return r >= 0 && r < m && c >= 0 && c < n;
        };

        // form components with available '1'.
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(grid[r][c] == 1) {
                    int ind = r * n + c;
                    vector<pair<int,int>> directions = {{r, c-1}, {r, c+1}, {r-1, c}, {r+1, c}};
                    for(auto& [dr, dc] : directions) {
                        if(isValid(dr, dc) && grid[dr][dc] == 1) {
                            int ind1 = dr * n + dc; // calculating the index number
                            dsu.unionBySize(ind, ind1); // forming the union
                        }
                    }
                }
            }
        }

        int max_size = *max_element(dsu.size.begin(), dsu.size.end()); // to handle base case if all are '1'

        // now try to replace every '0' with '1'.
        for(int r = 0; r < m; ++r) {
            for(int c = 0; c < n; ++c) {
                if(grid[r][c] == 0) {
                    int combinedSize = 1; // current '0' will also contribute to the answer
                    int ind = r * n + c;
                    unordered_set<int> visited_parent;
                    vector<pair<int,int>> directions = {{r, c-1}, {r, c+1}, {r-1, c}, {r+1, c}};
                    for(auto& [dr, dc] : directions) {
                        if(isValid(dr, dc) && grid[dr][dc] == 1) {
                            int nei_ind = dr * n + dc;
                            int adj_parent = dsu.findUPar(nei_ind); // combine with size of parent not cell
                            if(visited_parent.find(adj_parent) == visited_parent.end()) {
                                combinedSize += dsu.size[adj_parent];
                                visited_parent.insert(adj_parent);
                            }
                        }
                    }
                    max_size = max(max_size, combinedSize);
                }
            }
        }

        return max_size;
    }
};

"""