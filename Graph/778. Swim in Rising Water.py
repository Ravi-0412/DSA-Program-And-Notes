# my mistake: i didn't understand the Q and left totally but it is good and easy problem
# take the elevation as time and proceed for Q i.e if ele is '3' then you can only cross this cell if current cell ele is more than or equal to '3'
#  i.e you will have to wait for atleast '3' unit time to cross this cell

# Q meaning: you can only cross the adjacent cell if water level(elevation) which is time only  is less than or equal to the current cell elevation(time)
# we can take the minimum one always but for higher ele , we will have to wait for that much time 
# finally: you have to find the minimum(max time from all possibel path)

# since asking for least in a weightage path   then Dijkastra should come into mind for a while and for undirected bfs should come into mind
# and this instead of putting the elevation in minHeap with coordinates, we will put the max(elevation till now)
#  i.e max(pre poped and current_cell elevation)

# this q is simply asking to return minimum of all the paths possible i.e (min(max of all possible paths))

# time: n^2*logn (Dijkastra Algo)
# minHeap contains at most n^2 elements, pop time complexity each time is is O(logn^2) = O(2*logn), At most we will pop n^2 times

# # no need to run a nested loop since already connected 
# so better start with (0,0) and you will get your ans when it will reach the bottom right end
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
            directions= [[-1,0],[1,0],[0,-1],[0,1]] 
            for r2,c2 in directions:
                r, c= r1 +r2, c1+ c2
                if 0<=r<row and 0<=c<col and (r,c) not in visited:
                    visited.add((r,c))  # mark visite here only as there can't be any more optimal path possible for (r,c)
                    max_till_now= max(time, grid[r][c])   # put the max val as we can only reach (r,c) with this time only, not in time less than this
                    heapq.heappush(minHeap,(max_till_now,(r,c)))

