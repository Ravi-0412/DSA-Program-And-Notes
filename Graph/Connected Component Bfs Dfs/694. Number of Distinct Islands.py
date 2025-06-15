"""
just similar as '200.No of Island'.
We need to keep track of what all cells we covered, when starting from a cell and to check if that is 
structurally same as other one or not .
For checking this we will make the starting cell as (0, 0) and will add value according to direction in which we will move, into a list.
And after each call add this list into set after converting into tuple for avoiding duplicate.

e.g:  if starting index of island is (2,3) then for this we can take pos= (0, 0) and in direction we move from this starting index, 
we will keep adding them into positin say we moved left i.e [-1, 0] then, we will add this value to the pos like (pos -1, pos +0). 
after that we can add this list value into a set by converting them into tuple.
set can't store list.
"""

from typing import List

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        islands = set()  # we have to return the distinct
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]  # left, right, up, down
        visited = set()
        
        def dfs(r, c, pos):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc] == 1:
                    temp_direction = (pos[0] + dr, pos[1] + dc)  # adding the direction in which we are moving.
                    included_cell.append(temp_direction)
                    dfs(nr, nc, temp_direction)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and (r, c) not in visited:
                    included_cell = [(0, 0)]
                    dfs(r, c, (0, 0))
                    islands.add(tuple(included_cell))
        
        return len(islands)

# Java
"""
import java.util.*;

class Solution {
    public int numDistinctIslands(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;

        Set<String> islands = new HashSet<>();
        boolean[][] visited = new boolean[row][col];

        int[][] directions = {
            {0, -1}, // left
            {0, 1},  // right
            {-1, 0}, // up
            {1, 0}   // down
        };

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                if (grid[r][c] == 1 && !visited[r][c]) {
                    List<String> includedCell = new ArrayList<>();
                    includedCell.add("0:0");
                    dfs(grid, r, c, r, c, visited, includedCell, directions);
                    islands.add(String.join(",", includedCell));
                }
            }
        }

        return islands.size();
    }

    private void dfs(int[][] grid, int r, int c, int baseR, int baseC,
                     boolean[][] visited, List<String> shape, int[][] directions) {
        visited[r][c] = true;

        for (int[] dir : directions) {
            int nr = r + dir[0];
            int nc = c + dir[1];

            if (nr >= 0 && nc >= 0 && nr < grid.length && nc < grid[0].length
                && grid[nr][nc] == 1 && !visited[nr][nc]) {
                int relR = nr - baseR;
                int relC = nc - baseC;
                shape.add(relR + ":" + relC);
                dfs(grid, nr, nc, baseR, baseC, visited, shape, directions);
            }
        }
    }
}
"""


