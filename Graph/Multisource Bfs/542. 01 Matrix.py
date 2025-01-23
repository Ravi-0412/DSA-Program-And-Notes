# just same as "Rotten Oranges".
# only one extra we added here, the visited to check whether we have already visited the cell with value== 1 before or not.
# since the same cell can be visited again(in next cycle) and then time for that cell will increase.

# Note: First time we will see any '1' that will be shortest distance.

# Here we haveto find shortest distance of '1' from any of the '0' 
# so append all '0' into queue and apply multisource bfs.

# time= O(m*n)
# Space = o(m*n) , because of visited set

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row, col= len(mat), len(mat[0])
        visited= set()
        de= collections.deque([])
        time= 0
        count_1= 0
        for r in range(row):
            for c in range(col):
                if mat[r][c]== 0 :  # put all '0' into the Q
                    de.append((r, c))
                if mat[r][c]== 1:
                    count_1+= 1
        
        while de and count_1:
            time+= 1
            for i in range(len(de)):
                r, c= de.popleft()
                directions= [[r, c-1], [r, c+1], [r-1, c], [r+1, c]]  # left right, up, down
                for r1, c1 in directions:
                    if 0<= r1 < row and 0<= c1 < col and (r1, c1) not in visited and mat[r1][c1]== 1:
                        mat[r1][c1]= time
                        visited.add((r1, c1))
                        de.append((r1, c1))
                        count_1-= 1'
        return mat

# Method 2: Better one (Space optimised to O(1))
from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
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

# Method 3: Using DP, space: O(1)
# logic:
"""
1) For convinience, let's call the cell with value 0 as zero-cell, the cell has with value 1 as one-cell, the distance of the nearest 0 of a cell as distance.
2)Firstly, we can see that the distance of all zero-cells are 0, so we skip zero-cells, we process one-cells only.
3) In DP, we can only use prevous values if they're already computed.
4) In this problem, a cell has at most 4 neighbors that are left, top, right, bottom. 
If we use dynamic programming to compute the distance of the current cell based on 4 neighbors simultaneously, 
it's impossible because we are not sure if distance of neighboring cells is already computed or not.
5)That's why, we need to compute the distance one by one:
5.1) Firstly, for a cell, we restrict it to only 2 directions which are left and top. 
Then we iterate cells from top to bottom, and from left to right, we calculate the distance of a cell based on its left and top neighbors.
5.2) Secondly, for a cell, we restrict it only have 2 directions which are right and bottom. 
Then we iterate cells from bottom to top, and from right to left, we update the distance of a cell based on its right and bottom neighbors.

"""
class Solution: 
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat

# Method 1: Java
"""
import java.util.*;

class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        boolean[][] visited = new boolean[rows][cols];
        Queue<int[]> queue = new LinkedList<>();
        int countOnes = 0;
        
        // Initialize the queue with all '0' cells and count '1' cells
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (mat[r][c] == 0) {
                    queue.offer(new int[] {r, c});
                    visited[r][c] = true;
                } else {
                    countOnes++;
                }
            }
        }

        int[][] directions = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
        int time = 0;

        // Perform BFS to update the matrix
        while (!queue.isEmpty() && countOnes > 0) {
            time++;
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                int row = cell[0];
                int col = cell[1];

                for (int[] dir : directions) {
                    int newRow = row + dir[0];
                    int newCol = col + dir[1];

                    if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols 
                        && !visited[newRow][newCol] && mat[newRow][newCol] == 1) {
                        
                        mat[newRow][newCol] = time;
                        visited[newRow][newCol] = true;
                        queue.offer(new int[] {newRow, newCol});
                        countOnes--;
                    }
                }
            }
        }

        return mat;
    }
}
"""

# Java: Method 3
"""
class Solution { // 5 ms, faster than 99.66%
    public int[][] updateMatrix(int[][] mat) {
        int m = mat.length, n = mat[0].length, INF = m + n; // The distance of cells is up to (M+N)
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (mat[r][c] == 0) continue;
                int top = INF, left = INF;
                if (r - 1 >= 0) top = mat[r - 1][c];
                if (c - 1 >= 0) left = mat[r][c - 1];
                mat[r][c] = Math.min(top, left) + 1;
            }
        }
        for (int r = m - 1; r >= 0; r--) {
            for (int c = n - 1; c >= 0; c--) {
                if (mat[r][c] == 0) continue;
                int bottom = INF, right = INF;
                if (r + 1 < m) bottom = mat[r + 1][c];
                if (c + 1 < n) right = mat[r][c + 1];
                mat[r][c] = Math.min(mat[r][c], Math.min(bottom, right) + 1);
            }
        }
        return mat;
    }
}
"""

# similar questions:
1) 1765. Map of Highest Peak 
