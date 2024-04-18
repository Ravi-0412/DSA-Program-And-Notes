# Method 1: 
# Every land max can contribute to '4' unit of perimeter.
# If it is surrounded by land then it's contribution will decrease.
# like if any land cell is surrounded by '2' land then it's contribution will be '4-2 = 2' and son on.

# So for every land cell, count the neighbour land cell in all four directions.
# say count of such neighbour = 'k'  then cur land cell will contribute '4-k' to the ans.
# Add for all land cell for final ans.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        ans = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    cnt = 0
                    for dr, dc in directions:
                        if 0 <= (r + dr) < m and 0 <= (c + dc) < n and grid[r + dr][c + dc] == 1:
                            cnt += 1
                    ans += 4 - cnt
        return ans


# Method 2:
# Just reverse of above
# Logic: Count the no of water cell for every land cell.
# if any land cell has 'k' water cell on its four directions then it will contribute 'k' unit of parameter to ans.

# class Solution {
#     public int islandPerimeter(int[][] grid) {
#         int rows = grid.length;
#         int cols = grid[0].length;
    
#         int num = 0;
#         for (int i = 0; i < rows; i++) {
#             for (int j = 0; j < cols; j++) {
#                 if (grid[i][j] == 1) {
#                     if (i == 0 || grid[i - 1][j] == 0) num++; // UP
#                     if (j == 0 || grid[i][j - 1] == 0) num++; // LEFT
#                     if (i == rows -1 || grid[i + 1][j] == 0) num++; // DOWN
#                     if (j == cols -1 || grid[i][j + 1] == 0) num++; // RIGHT
#                 }
#             }
#         }
#         return num;
#     }
# }