# just you have to find the no of distinct connected components containing consecutive one's

# simple and concise way of writing the above code
# using Bfs

# Same code will give ans for Q: 695. maxArea of island

# Note: Make 'directions' array as global in all questions to avoiding creating again and again every time.

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

# for saving the space which is going in O(n*m), just make the changes just after visiting any grid like we had done in 'IsGraphBipartite'
# no need of extra visited set
# always remember for counting q, in base case there will one condition of returning '0' and one in general
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