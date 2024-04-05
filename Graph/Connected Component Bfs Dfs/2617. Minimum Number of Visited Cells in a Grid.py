# Just normal BFS.

# logic: add (steps, r, c) in deque
# Adding in visited at 1st time when we see the cell because:
#  1st time when we will see any cell that will be the minimum no of steps required to reach that cell.

# after that apply normal bfs as we do i.e traverse all the possible paths as we do normally.
# before adding any node in 'q' check if it is destination.

# at last return -1 means we can't reach the destination.

# time: O(m*n)  , ask someone

# space: O(m*n)


# note: This is similar to "45. Jump Game II" i.e 
# we can take any cell in same row with col in range (c+1,grid[r][c] + c ) (rightward) and same for downward.
# More concisely, you can take further 'grid[r][c]' steps in rightward and downward after reaching (r, c).

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n= len(grid), len(grid[0])
        if m== n==1:  # corner case
            return 1 
        q= collections.deque([])
        visited= set()
        q.append((1, 0, 0))  # [steps, r, c]
        visited.add((0, 0))  # [r, c]
        while q:
            steps, r, c= q.popleft()
            # traversing all the possible paths in rightward.
            for nc in range(c+1, grid[r][c] + c + 1):
                if nc < n and (r, nc) not in visited:
                    if r== m-1 and nc== n-1:  # if destination
                        return steps + 1 
                    q.append((steps + 1, r, nc))
                    visited.add((r, nc))
            # traversing all the possible paths in downward.
            for nr in range(r+1, grid[r][c] + r + 1):
                if nr < m and (nr, c) not in visited:
                    if nr== m-1 and c== n-1:  # if destination
                        return steps + 1 
                    q.append((steps + 1, nr, c))
                    visited.add((nr, c))
        return -1
    

# Note: we can also apply 'multisource bfs' i.e in step 1 we can visit this much cells, in step 2 we can visit this much cells etc.
