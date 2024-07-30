# Logic: we can't visit same cell once . So after each cell take the maximum of its adjacent and
# that value to current cell.

# If we will try to values from more than one neighbours then we will get wrong ans(more than expected).

# Complexity:

# Time: O(3^k), where k <= 25 is the number of cells that have gold.
# The first cell has up to 4 neighbors to go to, the (k-3) other cells have up to 3 neighbors to go to 
# (since we don't go back to the already visited cell), the second from the last has 1 way to go, the last cell doesn't go anywhere. 
#  And we try to start at k different cells which has gold.
# So there is total k * 4 * 3^(k-3) ~ k * 3^(k-2) ~ 3^k


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            ans = grid[r][c]
            temp = grid[r][c]
            grid[r][c] = 0
            max_nei = 0
            for dr, dc in directions:
                max_nei = max(max_nei, dfs(r + dr , c + dc))
            grid[r][c] = temp
            return ans + max_nei


        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))
        return ans
        