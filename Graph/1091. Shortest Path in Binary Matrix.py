# just the multisource bfs.
# whenever you are asked to find the shortest path in a matrix or between any nodes having same weight think of bfs or multisource bfs.
# And when given different weight think of 'Dijkastra Algo'.
# if directly not able to apply multisource bfs, try to reduce in that format.

# time: O(m*n)

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m= len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[n-1][m-1]!= 0:
            return -1
        q= collections.deque()
        visited= set()
        visited.add((0,0))
        q.append((0,0, 1))   # source(any source given in Q), path_lenth
        while q:
            for i in range(len(q)):
                r,c, path_length= q.popleft()
                if r== n-1 and c== m-1 :   # here you can check for any general destination
                    return path_length
                directions= [[r, c +1], [r+1, c], [r+1, c+1], [r+1, c-1], [r-1, c], [r, c-1],[r-1, c-1],[r-1, c+ 1]]  # right, down, down_right, down_left,, up, left, up_left, up_right
                for nr, nc in directions:
                    if 0<= nr < n and 0<= nc < m and (nr, nc) not in visited and grid[nr][nc]== 0:
                        q.append((nr, nc, path_length + 1))
                        visited.add((nr, nc))
        return -1   # means in between there is no way we can reach the destination