# Logic: All '1' which are directly or indirectly connected to the corner '1' can reach to to the end.
# so put all corner '1' in the 'Q' and apply mutisource bfs.
# single source bfs will also work but 'multisource is far better if applicable anywhere'.

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row,col= len(grid), len(grid[0])
        de= collections.deque()
        visited= set()  # so that same cell having '1' doesn't get added to Q.
        corner_1, middle_1= 0, 0 
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 1:
                    if r== 0 or r== row-1 or c==0 or c== col -1:  # if it is corner 1
                        de.append((r,c))
                        visited.add((r, c))   # 
                        corner_1 += 1
                    else:
                        middle_1 += 1
                   
        while de and middle_1:
            for i in range(len(de)):
                r, c= de.popleft()
                directions= [[r, c-1], [r, c+1], [r-1, c], [r+1, c]]  # left right, up, down
                for r1, c1 in directions:
                    if 0<= r1 < row and 0<= c1 < col and (r1, c1) not in visited and grid[r1][c1]== 1:
                        visited.add((r1, c1))
                        de.append((r1, c1))
                        middle_1 -= 1
        return middle_1   # count of '1' in middle which can't reach end.

