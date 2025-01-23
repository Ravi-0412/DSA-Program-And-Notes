# logic:
"""
1) Count no of one in each row and column
2) Then check if each server if they can communicate with any other server in same row or column or not.
For this , no of server in either row or column >= 2.
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        serverCountRow, serverCountCol = [0]*m , [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    serverCountRow[i] += 1
                    serverCountCol[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (serverCountRow[i] >=2 or serverCountCol[j] >= 2):
                    ans += 1
        return ans
# java
"""
class Solution {
    public int countServers(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[] serverCountRow = new int[m];
        int[] serverCountCol = new int[n];

        // Count servers in each row and column
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    serverCountRow[i]++;
                    serverCountCol[j]++;
                }
            }
        }

        int ans = 0;

        // Check if a server can communicate with another
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && (serverCountRow[i] > 1 || serverCountCol[j] > 1)) {
                    ans++;
                }
            }
        }

        return ans;
    }
}

"""
