# Method 1: 

# Logic :
# vvvi: Since each day, the new cell becomes flooded with water, so if on ith day,
# if we can't walk from the top to bottom then all days after ith we also can't walk.

# So we can apply Binary Search to find the last day we can walk in range [1..len(cells)], 
# for each mid = (left + right)/2), we need to check if we can still walk in mid th day.

# How to check if we can walk in dayAt th day?

# Ans: Firstly, we build the grid in the dayAt th day
# Then we use BFS to check if we can reach to the any cells in bottom row by starting from any cells in top row

# Time: O(log(days) * row*col) , days= len(cells)

# Note: indirectly it is asking for "we need to find the moment of time when graph becomes unconnected"

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def canWalkFromTopToBottom(dayAt):
            # create maxtrix at the 'dayAt'th day.
            # we have to make all cell value = 1 till the 'dayAt' th day.
            mat = [[0 for j in range(col)] for i in range(row)]
            for i in range(dayAt):
                r, c= cells[i]
                mat[r - 1][c - 1] = 1
            # Now run bfs to check whether we can run reach top to bottom at the given day.
            q = collections.deque()
            # first push all the cell indices of first col in 'Q' if it is a cell
            # rather than checking one by one.
            for j in range(col):
                if mat[0][j] == 0:
                    q.append((0, j))
                    mat[0][j] = 1    # marking as visited by changing the value.
                                     # Try to mark like this only where we have to chnage the value like here.
            
            # Now run the bfs
            while q:
                r, c = q.popleft()
                if r == row -1:  # we have reached the bottom so return true
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and mat[nr][nc] == 0:
                        # note: checking here for last row may give wrong ans.
                        q.append((nr, nc))
                        mat[nr][nc] = 1  # marking as visited
            return False

        # Just same as we find the last index of an ele in sorted array
        start, end= 1, len(cells)
        while start <= end:
            mid = start + (end - start)//2
            if canWalkFromTopToBottom(mid):
                start = mid + 1
            else:
                end = mid -1
        return end 
