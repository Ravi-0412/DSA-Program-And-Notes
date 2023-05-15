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


# method 2: using recursion
# TLE
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])

        # @lru_cache(None)
        def dfs(r, c):
            move= 0
            directions= [[r-1, c + 1], [r, c+ 1],[r+1, c+1]]
            for nr, nc in directions:
                if 0 <= nr < row and 0<= nc < col and grid[nr][nc] > grid[r][c]:
                    move= max(move, 1 + dfs(nr, nc))
            return move

        ans= 0
        for i in range(row):
            visited= {}
            ans= max(ans, dfs(i, 0))
        return ans


# Method 3: memoisation
# time= space= O(m*n)

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        visited= {}

        def dfs(r, c):
            if (r, c) in visited:
                return visited[(r, c)]
            move= 0
            directions= [[r-1, c + 1], [r, c+ 1],[r+1, c+1]]
            for nr, nc in directions:
                if 0 <= nr < row and 0<= nc < col and grid[nr][nc] > grid[r][c]:
                    move= max(move, 1 + dfs(nr, nc))
            visited[(r, c)]= move
            return move

        ans= 0
        for i in range(row):
            ans= max(ans, dfs(i, 0))
        return ans


# try to do by bfs also (optimised one)
