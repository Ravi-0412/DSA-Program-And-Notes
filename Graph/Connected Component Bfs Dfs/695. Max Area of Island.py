# just same logic as number of island 
# the same program will give the no of island also.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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
                    if 0 <= r < row and 0 <= c < col and  grid[r][c] == 1 and (r,c) not in visited:
                        visited.add((r,c))
                        Q.append((r,c))
            return count
                        
        # code starts from here
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    island += 1
                    visited.add((r,c))
                    maxArea = max(maxArea, BFS(r,c))
        return maxArea

# method2: Using DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col= len(grid), len(grid[0])
        island= 0
        maxArea= 0
        
        def DFS(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
                return 0
            area = 1
            grid[r][c]= "visited"  # put any special symbol
            directions= [[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in directions:
                r1,c1 = r+dr, c+dc
                area += DFS(r1,c1)
            return area
                        
        # code starts from here
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 : 
                    island += 1
                    maxArea = max(maxArea, DFS(r,c))
        return maxArea

# Method 1: java
"""
import java.util.*;

public class Solution {
    // Direction vectors for up, down, left, right
    private static final int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int maxAreaOfIsland(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        Set<String> visited = new HashSet<>();
        int maxArea = 0;

        // Perform BFS for each unvisited land cell
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == 1 && !visited.contains(r + "," + c)) {
                    int area = BFS(r, c, grid, visited, row, col);
                    maxArea = Math.max(maxArea, area);
                }
            }
        }
        return maxArea;
    }

    private int BFS(int r, int c, int[][] grid, Set<String> visited, int row, int col) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{r, c});
        visited.add(r + "," + c);
        int count = 0;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r1 = curr[0], c1 = curr[1];
            count++;

            for (int[] direction : directions) {
                int nr = r1 + direction[0], nc = c1 + direction[1];

                // Check boundaries and if it's land
                if (nr >= 0 && nr < row && nc >= 0 && nc < col &&
                    grid[nr][nc] == 1 && !visited.contains(nr + "," + nc)) {
                    visited.add(nr + "," + nc);
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
        return count;
    }
}
"""

# method 2: java
"""
import java.util.*;

public class Solution {
    
    // Direction vectors for up, down, left, right
    private static final int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int maxAreaOfIsland(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int maxArea = 0;
        
        // Iterate through the grid and perform DFS
        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == 1) {  // Found an unvisited land
                    maxArea = Math.max(maxArea, DFS(r, c, grid, row, col));
                }
            }
        }
        
        return maxArea;
    }

    private int DFS(int r, int c, int[][] grid, int row, int col) {
        // Boundary check and check if it's land (1)
        if (r < 0 || r >= row || c < 0 || c >= col || grid[r][c] != 1) {
            return 0;
        }
        
        // Mark the cell as visited (can also be marked as 0 or another value)
        grid[r][c] = -1;  // Use -1 to mark visited cells
        
        int area = 1;  // The area starts with 1 as we are visiting this cell
        for (int[] direction : directions) {
            int nr = r + direction[0];
            int nc = c + direction[1];
            area += DFS(nr, nc, grid, row, col);  // Explore all directions
        }
        
        return area;
    }
}
"""

# Related q:
1) 2658. Maximum Number of Fish in a Grid 
