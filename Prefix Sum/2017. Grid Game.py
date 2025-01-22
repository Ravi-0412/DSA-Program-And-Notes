# logic:
"""
1) Please note that robot 1 and robot 2 can only move down once.
2)There are total n possible paths(take down at any column) of Robot 1. Each possible path of Robot 1, Robot 2 can only get one of following total points:
topSum: If robot 2 moves on the top row.
bottomSum: If robot 2 moves on the bottom row.
3) It means, total points that Robot 2 can get = max(topSum, bottomSum).
4) Finally, we need to choose one path among n paths of Robot 1 so that it can minimize total points of Robot 2.

Note: See below link for visualisation
Link: https://leetcode.com/problems/grid-game/solutions/1486340/c-java-python-robot1-minimize-topsum-and-bottomsum-of-robot-2-picture-explained/?envType=daily-question&envId=2025-01-22 

Note: Using DP, we can find the maximum points of Robot1 taking care of sum of values of two paths(from bottom right) i.e right and down.
But there is we can find minimum points for Robot2 after making all those cells '0' that was taken by Robot1.

Note: Robot2 should get less points than Robot1.

Time: O(n), space: O(1)
"""

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = math.inf
        topSum = sum(grid[0])
        bottomSum = 0

        for i in range(n):
            topSum -= grid[0][i]
            ans = min(ans, max(topSum, bottomSum))
            bottomSum += grid[1][i]

        return ans

  # Java
  """
  import java.util.*;

class Solution {
    public int gridGame(int[][] grid) {
        int n = grid[0].length;
        int ans = Integer.MAX_VALUE;
        int topSum = 0;
        int bottomSum = 0;

        // Calculate the total sum of the top row
        for (int i = 0; i < n; i++) {
            topSum += grid[0][i];
        }

        for (int i = 0; i < n; i++) {
            topSum -= grid[0][i]; // Reduce the current cell from the top row sum
            ans = Math.min(ans, Math.max(topSum, bottomSum));
            bottomSum += grid[1][i]; // Add the current cell to the bottom row sum
        }

        return ans;
    }
}
  """
