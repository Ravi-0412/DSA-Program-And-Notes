# just same as '200.No of Island'.
# here we have to keep track of size also and we have to store different sizes into set for distinct one.
# How we can keep track of size?.
# Ans: we can add all four directions to the start of an island and can store them into one list.
# like if starting index of island is (2,3) then for this we can take pos= (0, 0) and in direction we move from this starting index, 
# we will keep adding them into positin say we moved left i.e [-1, 0] then, we will add this value to the pos like (pos -1, pos +0). 
# after that we can add this list value into a set by converting them into tuple.
# set can't store list.

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        islands= set()   # we have to return the distinct
        directions= [[0, -1], [0, 1], [-1, 0], [1, 0]]  # lft, right, up, down
        visited= set()
        
        def dfs(r, c, pos, island_direction):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc= r + dr, c + dc
                if 0<= nr < row and 0<= nc < col and (nr, nc) not in visited and grid[nr][nc]== 1:
                    temp_direction= (pos[0] + dr, pos[1] +dc)  # adding the direction in which we are moving.
                    island_direction.append((temp_direction))
                    dfs(nr, nc, temp_direction, island_direction)
            return tuple(island_direction)   # we can't store list inside set so converting into tuple
        
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 1 and (r, c) not in visited:
                    islands.add(dfs(r, c, (0,0), [(0, 0)]))
        return len(islands)


