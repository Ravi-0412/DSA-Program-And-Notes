# logic: just find one connected component and store those cell say visited set.
# Now run bfs to check for any '1' of other component.
# time: O(n^2)

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n= len(grid)
        
        visited= set()
        directions= [[0, -1], [0, 1], [-1, 0], [1, 0]]
        def dfs(r, c):
            if 0 <= r < n and 0 <= c < n and (r, c) not in visited and grid[r][c] == 1:
                visited.add((r, c))
                for dr, dc in directions:
                    dfs(r + dr, c + dc)

        # multisource source bfs to just find the nearest '1' any of the node in 1st connected component
        def bfs():
            ans= 0
            q= collections.deque(visited)   # automaticaly got converted to list.
            while q:
                for i in range(len(q)):
                    r,c= q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                            if grid[nr][nc]== 1:
                                return ans   # my mistake: ans + 1
                            q.append((nr, nc))
                            visited.add((nr, nc))
                ans+= 1

        # store one connected component into visited set.
        for i in range(n):
            for j in range(n):
                if grid[i][j]== 1:
                    dfs(i, j)
                    return bfs()   # after finding one of component, run bfs to find to any '1' of other component.



# My mistake and learning

# After seeing '1' i was doing break then was calling bfs separately but 'break' statement in 2-D array work differently.
# for x in range(4):
#     for y in range(4):
#         if x == 1:
#             break
#     print(x, y)


# to get the desired result
# method 1: use any varible and after each internal loop check value of that variable
# force_break_loop = False
# for x in range(4):
#     for y in range(4):
#         if x == 1:
#             force_break_loop = True
#             break
#     if force_break_loop:
#         break
#     print(x, y)
    

# method 2: Break Statement Twice
for x in range(4):
    for y in range(4):
        if x == 1:
            break
    if x == 1:
        break
    print(x, y)

