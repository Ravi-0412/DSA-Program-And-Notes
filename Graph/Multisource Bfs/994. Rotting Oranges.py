"""
Logic
- Use BFS, not DFS.
- Start with all rotten oranges in the queue.
- Each level of BFS = 1 minute.
- Rot all adjacent fresh oranges.
- Continue until no more fresh oranges can rot.

Key Points
- Fresh oranges at level 1 rot in 1 min, level 2 in 2 min, and so on.
- Only one BFS call is needed.
- If any fresh orange remains after BFS → return `-1`.

Time Complexity: O(m * n) — each cell processed once.

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col= len(grid), len(grid[0])
        q= collections.deque()
        time, fresh= 0, 0
        
        # Add all rotten oranges in queue and count the no of fresh orange.
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 2:
                    q.append((r,c))
                if grid[r][c]== 1:
                    fresh+= 1

        while q and fresh:
            time+= 1 
            # oranges that will get rotten in one unit time will depend on the no of adjacent oranges with the ele present in the Queue 
            for i in range(len(q)):  # we are poping and pushing but it this loop will run till the pre length only
                # pop one ele and make all the oranges adjacent to this ele as rotten and append that in Q for next cycle
                r1,c1= q.popleft()
                # writing all possible allowed directions i.e up,down,left,right in form of matrix
                directions= [[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    r,c= r1+dr, c1+dc
                    if 0<=r<row and 0<=c<col and  grid[r][c]==1:
                        grid[r][c]= 2
                        fresh-= 1
                        q.append((r,c))  # now from this cell we have to check next time.

        return time if fresh == 0 else -1  # if no fresh oranges is left

# Java
"""
import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        Queue<int[]> queue = new LinkedList<>();
        int time = 0, fresh = 0;

        // Add all rotten oranges to the queue and count the fresh ones
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 2) {
                    queue.offer(new int[]{r, c});
                }
                if (grid[r][c] == 1) {
                    fresh++;
                }
            }
        }

        // Directions: up, down, left, right
        int[][] directions = {{-1,0},{1,0},{0,-1},{0,1}};

        while (!queue.isEmpty() && fresh > 0) {
            time++;

            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] pos = queue.poll();
                int r1 = pos[0], c1 = pos[1];

                for (int[] dir : directions) {
                    int r = r1 + dir[0], c = c1 + dir[1];

                    if (r >= 0 && r < rows && c >= 0 && c < cols && grid[r][c] == 1) {
                        grid[r][c] = 2;
                        fresh--;
                        queue.offer(new int[]{r, c});
                    }
                }
            }
        }

        return fresh == 0 ? time : -1;
    }
}
"""

