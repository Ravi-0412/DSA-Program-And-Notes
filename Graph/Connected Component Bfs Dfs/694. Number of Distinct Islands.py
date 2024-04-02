# just similar as '200.No of Island'.
# We need to keep track of what all cells we cover when starting from a cell and to check if that is 
# structurally same as other one or not .
# For checking this we wil make the starting cell as (0, 0) and will add value according to direction in which we will move into a list.
# And after each call add this list into set after converting into tuple for avoiding duplicate.

# e.g:  if starting index of island is (2,3) then for this we can take pos= (0, 0) and in direction we move from this starting index, 
# we will keep adding them into positin say we moved left i.e [-1, 0] then, we will add this value to the pos like (pos -1, pos +0). 
# after that we can add this list value into a set by converting them into tuple.
# set can't store list.

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        islands= set()   # we have to return the distinct
        directions= [[0, -1], [0, 1], [-1, 0], [1, 0]]  # lft, right, up, down
        visited= set()
        
        def dfs(r, c, pos):
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc= r + dr, c + dc
                if 0 <= nr < row and 0<= nc < col and (nr, nc) not in visited and grid[nr][nc]== 1:
                    temp_direction= (pos[0] + dr, pos[1] +dc)  # adding the direction in which we are moving.
                    included_cell.append((temp_direction))
                    dfs(nr, nc, temp_direction)
        
        
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 1 and (r, c) not in visited:
                    included_cell = [(0, 0)]
                    dfs(r, c, (0,0))
                    islands.add(tuple(included_cell))
        return len(islands)


