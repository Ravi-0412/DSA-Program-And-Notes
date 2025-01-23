# Logic:
"""
1) start to fill water cells with height = 0, from lowest height
2) We need to take care that 'any two adjacent cells must have an absolute height difference of at most 1', 
for this we must assign all adjacent cell same value(+1 bigger than current cell) asn so on.
So this question reduces to : "542. 01 Matrix". Exactly same as this one only.
"""
# time: O(m*n), space: o(1)
class Solution:
    def highestPeak(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    q.append((r, c))
                    mat[r][c] = 0
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()
            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: 
                    continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat

# java
"""
import java.util.*;

class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int m = isWater.length, n = isWater[0].length;
        int[][] result = new int[m][n];
        int[][] directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        Queue<int[]> queue = new LinkedList<>();
        
        // Initialize the queue and set water cells to 0, others to -1
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (isWater[r][c] == 1) {
                    queue.offer(new int[]{r, c});
                    result[r][c] = 0; // Water cells are height 0
                } else {
                    result[r][c] = -1; // Land cells are unprocessed
                }
            }
        }
        
        // Perform BFS to calculate the heights
        while (!queue.isEmpty()) {
            int[] cell = queue.poll();
            int r = cell[0], c = cell[1];
            for (int[] dir : directions) {
                int nr = r + dir[0], nc = c + dir[1];
                // Skip invalid or already processed cells
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || result[nr][nc] != -1) {
                    continue;
                }
                result[nr][nc] = result[r][c] + 1;
                queue.offer(new int[]{nr, nc});
            }
        }
        
        return result;
    }
}
"""
