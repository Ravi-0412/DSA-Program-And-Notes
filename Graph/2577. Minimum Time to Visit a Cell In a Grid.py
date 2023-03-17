# method 1: used mutisource bfs.
# TLE : Because we are inserting a single node multiple times and checking it's nei also many time.
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        q= collections.deque([(0,0)])
        time= 0
        while q:
            visited= set()
            print(q, time)
            for i in range(len(q)):
                r, c= q.popleft()
                if r== row-1 and c== col-1:
                    return time
                directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]    # up, down, left, right
                for nr, nc in directions:
                    if 0<= nr < row and 0 <= nc < col and (nr, nc) not in visited and grid[nr][nc]<= time +1:
                        # if nr== row-1 and nc== col-1:
                        #     return time
                        q.append((nr, nc))
                        visited.add((nr, nc))
            time+= 1
        return -1
    

# optimising and using dijskatra
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1 :
            return -1
        row, col= len(grid), len(grid[0])
        minHeap= []
        heapq.heappush(minHeap, (0, 0, 0) )   # [(time, r, c)]
        visited= set()
        while minHeap:
            time, r, c= heapq.heappop(minHeap)
            if r== row- 1 and c== col-1:
                return time
            if (r, c) in visited:    # means we have already relaxed all edges through this. Already poped before
                continue
            visited.add((r, c))    # we are going to relax all edges through this.
            directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]    # up, down, left, right
            for nr, nc in directions:
                    if nr < 0 or nr >= row or nc <0 or nc >= col or (nr, nc) in visited:
                        continue
                    # if we can visit the neigh with current time then add into the heap
                    if grid[nr][nc] <= time +1:
                        heapq.heappush(minHeap, (time+1, nr, nc))
                    # find the time when we can visit the cell (nr, nc) later
                    else:
                        diff= grid[nr][nc] - time
                        if diff & 1: # if difference is odd then we can visit that cell in 'grid[nr][nc]' time during back and forth to other cell in this diff to of time i.e we can come back to (nr, nc) in grid[nr][nc]
                            heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                        else:  # if even then we can visit in time = 'grid[nr][nc] +1' later.
                            heapq.heappush(minHeap, (grid[nr][nc] +1, nr, nc))
        return -1
    

# concise version of above
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1 :
            return -1
        row, col= len(grid), len(grid[0])
        minHeap= []
        heapq.heappush(minHeap, (0, 0, 0) )   # [(time, r, c)]
        visited= set()
        while minHeap:
            time, r, c= heapq.heappop(minHeap)
            if r== row- 1 and c== col-1:
                return time
            if (r, c) in visited:    # means we have already relaxed all edges through this. Already poped before
                continue
            visited.add((r, c))    # we are going to relax all edges through this.
            directions= [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]    # up, down, left, right
            for nr, nc in directions:
                    if nr < 0 or nr >= row or nc <0 or nc >= col or (nr, nc) in visited:
                        continue
                    # if we can visit the neigh with current time then add into the heap
                    if grid[nr][nc] <= time +1:
                        heapq.heappush(minHeap, (time+1, nr, nc))
                    # find the time when we can visit the cell (nr, nc) later
                    else:
                        diff= grid[nr][nc] - time
                        if diff & 1: # if difference is odd then we can visit that cell in 'grid[nr][nc]' time during back and forth to other cell in this diff to of time i.e we can come back to (nr, nc) in grid[nr][nc]
                            heapq.heappush(minHeap, (grid[nr][nc], nr, nc))
                        else:  # if even then we can visit in time = 'grid[nr][nc] +1' later.
                            heapq.heappush(minHeap, (grid[nr][nc] +1, nr, nc))
        return -1

    
