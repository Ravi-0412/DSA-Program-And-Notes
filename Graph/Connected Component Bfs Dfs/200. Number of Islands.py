# Method 1:

"""
just you have to find the no of distinct connected components containing consecutive one's
Same code will give ans for Q: 695. maxArea of island
Note: Make 'directions' array as global in all questions to avoiding creating again and again every time.
"""
# 1st Method: Using Bfs

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col= len(grid), len(grid[0])
        visited= set()
        island= 0
        maxArea = 0 
        
        directions= [[-1,0],[1,0],[0,-1],[0,1]] # writing all possible allowed directions i.e up,down,left,right in form of matrix

        def BFS(r,c):
            Q= collections.deque()
            Q.append((r,c))
            count= 0
            while Q:
                r1, c1= Q.popleft()
                count+= 1
                for dr,dc in directions:
                    r,c= r1+dr, c1+dc
                    if 0 <= r < row and 0 <= c < col and  grid[r][c] == "1" and (r,c) not in visited:
                        visited.add((r,c))
                        Q.append((r,c))
            return count
                        
        # code starts from here
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island += 1
                    visited.add((r,c))
                    maxArea = max(maxArea, BFS(r,c))
        return island
        

# method 2: using DFS
"""
for saving the space which is going in O(n*m), just make the changes just after visiting any grid like we had done in 'IsGraphBipartite'
no need of extra visited set
Note: always remember for counting q, in base case there will one condition of returning '0' and one in general.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col= len(grid), len(grid[0])
        island= 0
        
        def DFS(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]!= "1":  # write all invalid condition together and return '0' in count(if you are adding the ans somewhere) or simply return 
                return 
            grid[r][c]= "visited"  # put any special symbol
            directions= [[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in directions:
                r1,c1= r+dr, c+dc
                DFS(r1,c1)   

        # code starts from here
        for r in range(row):
            for c in range(col):
                if grid[r][c]== "1": 
                    island+= 1
                    DFS(r,c)
        return island


# Java
"""
// Method 1:

public class Solution {
    private int row, col;
    private boolean[][] visited;
    private int maxArea = 0;
    private int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // up, down, left, right

    public int numIslands(char[][] grid) {
        row = grid.length;
        col = grid[0].length;
        visited = new boolean[row][col];
        int islandCount = 0;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    islandCount++;
                    maxArea = Math.max(maxArea, bfs(grid, r, c));
                }
            }
        }
        // If you want to return the maximum area as well, you can modify the method to return a Pair or another data structure.
        // For now, this only returns the number of islands.
        return islandCount;
    }

    private int bfs(char[][] grid, int r, int c) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{r, c});
        visited[r][c] = true;
        int area = 0;

        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r1 = cell[0], c1 = cell[1];
            area++;
            for (int[] direction : directions) {
                int newRow = r1 + direction[0], newCol = c1 + direction[1];
                if (newRow >= 0 && newRow < row && newCol >= 0 && newCol < col && grid[newRow][newCol] == '1' && !visited[newRow][newCol]) {
                    queue.offer(new int[]{newRow, newCol});
                    visited[newRow][newCol] = true;
                }
            }
        }
        return area;
    }
}

// Method 2:
public class Solution {
    private int row, col;
    private char[][] grid;

    public int numIslands(char[][] grid) {
        this.row = grid.length;
        this.col = grid[0].length;
        this.grid = grid;
        int islandCount = 0;

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == '1') {
                    islandCount++;
                    dfs(r, c);
                }
            }
        }
        return islandCount;
    }

    private void dfs(int r, int c) {
        if (r < 0 || r >= row || c < 0 || c >= col || grid[r][c] != '1') {
            return;
        }

        grid[r][c] = 'v'; // mark as visited
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}}; // up, down, left, right

        for (int[] direction : directions) {
            int newRow = r + direction[0];
            int newCol = c + direction[1];
            dfs(newRow, newCol);
        }
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
    // BFS Method
    int numIslandsBFS(vector<vector<char>>& grid) {
        int row = grid.size(), col = grid[0].size();
        vector<vector<bool>> visited(row, vector<bool>(col, false));
        int islands = 0;
        
        vector<vector<int>> directions = {{-1,0},{1,0},{0,-1},{0,1}};

        auto BFS = [&](int r, int c) {
            queue<pair<int,int>> Q;
            Q.push({r,c});
            visited[r][c] = true;
            int count = 0;
            while(!Q.empty()) {
                auto [r1,c1] = Q.front(); Q.pop();
                count++;
                for (auto& d : directions) {
                    int nr = r1 + d[0], nc = c1 + d[1];
                    if (nr >=0 && nr < row && nc >=0 && nc < col && 
                        grid[nr][nc] == '1' && !visited[nr][nc]) {
                        visited[nr][nc] = true;
                        Q.push({nr,nc});
                    }
                }
            }
            return count;
        };

        int maxArea = 0;
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    islands++;
                    int area = BFS(r,c);
                    maxArea = max(maxArea, area);
                }
            }
        }
        return islands;
    }

    // DFS Method
    void DFS(int r, int c, vector<vector<char>>& grid) {
        int row = grid.size(), col = grid[0].size();
        if (r < 0 || r >= row || c < 0 || c >= col || grid[r][c] != '1')
            return;
        grid[r][c] = 'v';  // mark visited
        vector<vector<int>> directions = {{-1,0},{1,0},{0,-1},{0,1}};
        for (auto& d : directions) {
            DFS(r + d[0], c + d[1], grid);
        }
    }

    int numIslandsDFS(vector<vector<char>>& grid) {
        int row = grid.size(), col = grid[0].size();
        int islands = 0;
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == '1') {
                    islands++;
                    DFS(r, c, grid);
                }
            }
        }
        return islands;
    }
};

"""


# method 3: 
"""
# using union-find.

m= rows, n= cols
What differences from 'No of provinces'?
Ans: Here there can be more than 'm'(rows) island, infact there can be max nearly (m*n)//2 island.(nearly half of all cell).
so here we will make parent and size array of size (m*n) itself. But there was only 'n' city.
Also in that Q. we have to combine cities (i,j) into one so was passing (i, j) in union function.
But here we have to combine all cell so we have to the pass the cell index in terms of 'i' and 'j'. 
But we can't do because for finding parent we have to pass as a integer only. So converted all cell into an integer.

So first we will convert all cell into an integer like 0,1,2,3.......
to find and do the union.

Method 1: counting the distinct parent .
But here we will try to find the distinct parent not from parent array itself(like "Q: no of provinces") 
then it will give the incorrect ans.
As where there will be "0" in grid that will be the parent of itself and that also be get counted in the ans.

only that will be part of ans who is parent of himself and value at that grid cell== "1".
"""

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
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n= len(grid), len(grid[0])
        dsu= DSU(m*n)
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # up, down, left, right
        for i in range(m):
            for j in range(n):
                if grid[i][j]== "1":
                    x1 = i*n + j  # number of curr cell 
                    # now try to bring the adjacent cell to this curr cell into one .
                    for dr, dc in directions:
                        nr, nc = i + dr , j + dc
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                            x2 = nr * n + nc
                            dsu.unionBySize(x1, x2)
        
        # Now count the no of cell which is the parent of itself when grid[i][j] == "1"
        # That will give the no of ultimate parent and that will be our ans.
        count= 0
        for i in range(m):
            for j in range(n):
                x1= i*n + j  # number of curr cell.
                if grid[i][j]== "1" and x1== dsu.parent[x1]:
                    count+= 1
        return count
    

# Java
"""
class DSU {
    int[] parent, size;

    public DSU(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    public int findUPar(int n) {
        if (n == parent[n])
            return n;
        return parent[n] = findUPar(parent[n]);
    }

    public void unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);
        if (p1 == p2) return; // same component

        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
    }
}

class Solution {
    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        DSU dsu = new DSU(m * n);
        int[][] directions = {{-1,0}, {1,0}, {0,-1}, {0,1}}; // up, down, left, right

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    int x1 = i * n + j; // number of curr cell
                    // now try to bring the adjacent cell to this curr cell into one
                    for (int[] dir : directions) {
                        int nr = i + dir[0];
                        int nc = j + dir[1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1') {
                            int x2 = nr * n + nc;
                            dsu.unionBySize(x1, x2);
                        }
                    }
                }
            }
        }

        // Count the number of ultimate parents among '1' cells
        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int x1 = i * n + j;
                if (grid[i][j] == '1' && x1 == dsu.findUPar(x1)) {
                    count++;
                }
            }
        }
        return count;
    }
}


"""


# C++
"""
#include <vector>
using namespace std;

class DSU {
public:
    vector<int> parent, size;

    DSU(int n) {
        parent.resize(n);
        size.resize(n, 1);
        for (int i = 0; i < n; ++i)
            parent[i] = i;
    }

    int findUPar(int n) {
        if (n == parent[n])
            return n;
        return parent[n] = findUPar(parent[n]);
    }

    void unionBySize(int n1, int n2) {
        int p1 = findUPar(n1);
        int p2 = findUPar(n2);
        if (p1 == p2) return; // same component

        if (size[p1] < size[p2]) {
            parent[p1] = p2;
            size[p2] += size[p1];
        } else {
            parent[p2] = p1;
            size[p1] += size[p2];
        }
    }
};

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size(), n = grid[0].size();
        DSU dsu(m * n);
        vector<vector<int>> directions = {{-1,0}, {1,0}, {0,-1}, {0,1}}; // up, down, left, right

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    int x1 = i * n + j; // number of curr cell
                    // now try to bring the adjacent cell to this curr cell into one
                    for (auto& dir : directions) {
                        int nr = i + dir[0];
                        int nc = j + dir[1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1') {
                            int x2 = nr * n + nc;
                            dsu.unionBySize(x1, x2);
                        }
                    }
                }
            }
        }

        // Count the number of ultimate parents among '1' cells
        int count = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int x1 = i * n + j;
                if (grid[i][j] == '1' && x1 == dsu.findUPar(x1)) {
                    count++;
                }
            }
        }
        return count;
    }
};


"""


# Extension

# Note: Here if we will try to solve by method of '959. Regions Cut By Slashes'
# i.e taking 'count' as member of DSU and incrementing count when we will find any cycle then it will give wrong ans
# Will give very high number than expected.

"""
class DSU:
    def __init__(self, n):
        self.parent=  [i for i in range(n)]
        self.size=    [1 for i in range(n)]
        self.count = 0
"""

# Reason: Because here comparing with 4 adjacent cell and not a single point like '959. Regions Cut By Slashes'
# so there will be lot of repeating in this.

# That's why easiest way to find ans is by counting number of distinct parents.
