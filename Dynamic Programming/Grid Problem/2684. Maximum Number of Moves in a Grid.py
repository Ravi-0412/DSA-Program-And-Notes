# method 1: using bfs
# TLE: Because we are reaching the same cell many time.
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])

        def bfs(i, j):
            # print(i,j,"start")
            count= 0
            q= collections.deque()
            q.append((0, i, j))
            while q:
                move, r, c= q.popleft()
                count= max(count, move)
                directions= [[r-1, c + 1], [r, c+ 1],[r+1, c+1]]
                for nr, nc in directions:
                    if 0 <= nr < row and 0<= nc < col and grid[nr][nc] > grid[r][c]:
                        q.append((move + 1, nr, nc))
            return count

        ans= 0
        for i in range(row):
            ans= max(ans, bfs(i, 0))
        return ans

# Note => My mistake:  If we do return like  
"""
Add '1' to maximum of all its three choice then it will give wrong ans.
Will give more than expected.

Reason: Because you are atleast returning '1 from each cell but this cell may not combine with previous
(if value has less than or equal to previous).

How to do?
-> Just while calling function, check the condition and take maximum after adding '1' with each of its neighbours.
Did in next method
"""
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])

        def dfs(r, c):
            move = 0
            directions= [[r-1, c + 1], [r, c+ 1],[r+1, c+1]]
            for nr, nc in directions:
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] > grid[r][c]:
                    move = max(move, dfs(nr, nc))
            return 1 + move

        ans= 0
        for i in range(row):
            ans= max(ans, dfs(i, 0))
        return ans

# method 2: using recursion
# TLE
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])

        def dfs(r, c):
            move= 0
            directions= [[r-1, c + 1], [r, c+ 1],[r+1, c+1]]
            for nr, nc in directions:
                if 0 <= nr < row and 0<= nc < col and grid[nr][nc] > grid[r][c]:
                    move = max(move, 1 + dfs(nr, nc))
            return move

        ans= 0
        for i in range(row):
            ans= max(ans, dfs(i, 0))
        return ans

# Method 3: memoisation
# time= space= O(m*n)

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[-1 for _ in range(col)] for _ in range(row)]

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            
            move = 0
            directions = [[r-1, c+1], [r, c+1], [r+1, c+1]]
            for nr, nc in directions:
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] > grid[r][c]:
                    move = max(move, 1 + dfs(nr, nc))
            dp[r][c] = move
            return dp[r][c]

        ans = 0
        for i in range(row):
            ans = max(ans, dfs(i, 0))
        return ans

# Java
"""
class Solution {
    public int maxMoves(int[][] grid) {
        int row = grid.length;
        int col = grid[0].length;
        int[][] dp = new int[row][col];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                dp[i][j] = -1;
            }
        }

        int ans = 0;
        for (int i = 0; i < row; i++) {
            ans = Math.max(ans, dfs(i, 0, grid, dp));
        }
        return ans;
    }

    private int dfs(int r, int c, int[][] grid, int[][] dp) {
        if (dp[r][c] != -1) {
            return dp[r][c];
        }

        int row = grid.length;
        int col = grid[0].length;
        int move = 0;

        int[][] directions = {{r - 1, c + 1}, {r, c + 1}, {r + 1, c + 1}};
        for (int[] dir : directions) {
            int nr = dir[0];
            int nc = dir[1];
            if (nr >= 0 && nr < row && nc >= 0 && nc < col && grid[nr][nc] > grid[r][c]) {
                move = Math.max(move, 1 + dfs(nr, nc, grid, dp));
            }
        }
        
        dp[r][c] = move;
        return move;
    }
}
"""


# try to do by bfs also (optimised one)
