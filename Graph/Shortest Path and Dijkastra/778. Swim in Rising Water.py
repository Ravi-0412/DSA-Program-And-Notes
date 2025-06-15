# Question language is little tough to understand.

# This is a good and easy problem.
# take the elevation as time and proceed for Q i.e if ele is '3' then you can only cross this cell 
# if current cell ele is more than or equal to '3'
#  i.e you will have to wait for atleast '3' unit time to cross this cell

# Q meaning: you can only cross the adjacent cell if water level(elevation) which is time only  
# it is less than or equal to the current cell elevation(time)
# we can take the minimum one always but for higher ele , we will have to wait for that much time.

# Note: finally you have to find the minimum(max time from all possible path) and in easy way find the shortest time to reach destination.

# Note: since asking for least in a weightage path then Dijkastra should come into mind for a while and
# for undirected bfs should come into mind.

# vvi : Min time in which you can reach any cell (r,c)= grid[r][c] if it's any of the adjacent cell is reachable in this much time.

# Note vvi : Here we are marking visited when we are seeing first time only since when node is getting for 1st time 
# then this will be minium time in which that will get visited. so no need to wait for any other path to minimise it's time.
# Because there can't be any more optimal path possible for (r,c) because we have to include the curr cell value also.

# time: n^2*log(n^2) (Dijkastra Algo)
# minHeap contains at most n^2 elements, pop time complexity each time is is O(logn^2), At most we will pop n^2 times

# Note: At time of pushing we are maximising the value and with the help of heap we are minimising, 
# so automatically we will minimum(max time from all possible path).

# Note: Also you can't reach cell (r, c) in time grid[r][c] if it's any of the neighbour is not able to reach in time grid[r][c].

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        minHeap= [(grid[0][0],(0,0))]      
        visited= set()
        visited.add((0,0))
        # from here bfs logic
        while minHeap:
            time, (r1,c1)= heapq.heappop(minHeap)
            if r1== row-1 and c1== col-1:   # you reached the destination
                return time
            # visited.add((r1, c1))   # marking here will lead to TLE and wrong ans.
            directions= [[-1,0],[1,0],[0,-1],[0,1]] 
            for r2,c2 in directions:
                r, c= r1 +r2, c1+ c2
                if 0<=r<row and 0<=c<col and (r,c) not in visited:
                    visited.add((r,c))  # mark visite here only as there can't be any more optimal path possible for (r,c) because we have to include the curr cell value also.
                    min_till_needed= max(time, grid[r][c])   # put the max val as we can only reach (r,c) with this time only, not in time less than this. 
                    heapq.heappush(minHeap,(min_till_needed,(r,c)))


# since for every cell, we will get the ans when we will see the node for 1st time itself 
# then we can mark visited at that time itself and check for ans at 1st time when we will see any cell.
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row, col= len(grid), len(grid[0])
        if row== 1:
            return 0
        minHeap= [(grid[0][0],(0,0))]      
        visited= set()
        visited.add((0,0))
        while minHeap:
            time, (r1,c1)= heapq.heappop(minHeap)
            directions= [[-1,0],[1,0],[0,-1],[0,1]] 
            for r2,c2 in directions:
                r, c= r1 +r2, c1+ c2
                if 0<=r<row and 0<=c<col and (r,c) not in visited:
                    min_till_needed= max(time, grid[r][c])   # put the max val as we can only reach (r,c) with this time only, not in time less than this.
                    if r== row-1 and c== col-1:
                        return  min_till_needed
                    visited.add((r,c))  # mark visite here only as there can't be any more optimal path possible for (r,c) because we have to include the curr cell value also.
                    heapq.heappush(minHeap,(min_till_needed,(r,c)))

# Related Q:
# 1) 3341. Find Minimum Time to Reach Last Room I
# 2) 3342. Find Minimum Time to Reach Last Room II

# Related Q:
# Note: Analyse these question properly like why in one q we are getting ans on 1st time and why in other getting after poping.
# 1) 2577. Minimum Time to Visit a Cell In a Grid
# 2) 1631. Path With Minimum Effort
