# Method 1: 
"""
Every land max can contribute to '4' unit of perimeter.
If it is surrounded by land then it's contribution will decrease.
like if any land cell is surrounded by '2' land then it's contribution will be '4-2 = 2' and son on.

So for every land cell, count the neighbour land cell in all four directions.
say count of such neighbour = 'k'  then cur land cell will contribute '4-k' to the ans.
Add for all land cell for final ans.

Time: O(row * col), sapce: O(1)
"""

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

# Java
"""
class Solution {
    public int islandPerimeter(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int ans = 0;
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    int cnt = 0;
                    for (int[] dir : directions) {
                        int nr = r + dir[0];
                        int nc = c + dir[1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                            cnt++;
                        }
                    }
                    ans += 4 - cnt;
                }
            }
        }
        return ans;
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int ans = 0;
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) {
                    int cnt = 0;
                    for (auto& dir : directions) {
                        int dr = dir[0], dc = dir[1];
                        if (0 <= r + dr && r + dr < m && 0 <= c + dc && c + dc < n &&
                            grid[r + dr][c + dc] == 1) {
                            cnt++;
                        }
                    }
                    ans += 4 - cnt;
                }
            }
        }

        return ans;
    }
};

"""

# Method 2:
# Just reverse of above
# Logic: Count the no of water cell for every land cell.
# if any land cell has 'k' water cell on its four directions then it will contribute 'k' unit of parameter to ans.
# Time: O(row * col), sapce: O(1)

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i == 0 or grid[i - 1][j] == 0:  # UP
                        perimeter += 1
                    if j == 0 or grid[i][j - 1] == 0:  # LEFT
                        perimeter += 1
                    if i == rows - 1 or grid[i + 1][j] == 0:  # DOWN
                        perimeter += 1
                    if j == cols - 1 or grid[i][j + 1] == 0:  # RIGHT
                        perimeter += 1
                        
        return perimeter

# Java
"""
class Solution {
    public int islandPerimeter(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
    
        int num = 0;
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) {
                    if (i == 0 || grid[i - 1][j] == 0) num++; // UP
                    if (j == 0 || grid[i][j - 1] == 0) num++; // LEFT
                    if (i == rows -1 || grid[i + 1][j] == 0) num++; // DOWN
                    if (j == cols -1 || grid[i][j + 1] == 0) num++; // RIGHT
                }
            }
        }
        return num;
    }
}
"""
# C++ Code 
"""
#include <vector>
using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int perimeter = 0;

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == 1) {
                    if (i == 0 || grid[i - 1][j] == 0)  // UP
                        perimeter++;
                    if (j == 0 || grid[i][j - 1] == 0)  // LEFT
                        perimeter++;
                    if (i == rows - 1 || grid[i + 1][j] == 0)  // DOWN
                        perimeter++;
                    if (j == cols - 1 || grid[i][j + 1] == 0)  // RIGHT
                        perimeter++;
                }
            }
        }

        return perimeter;
    }
};

"""
