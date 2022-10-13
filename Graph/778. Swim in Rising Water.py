# my mistake: i didn't understand the Q and left totally but it is good and easy problem
# take the elevation as time and proceed for Q i.e if ele is '3' then you can only cross this cell if current cell ele is more than '3'
#  i.e you will have to wait for atleast '3' unit time to cross this cell

# Q meaning: you can only cross the adjacent cell if water level(elevation) which is time only  is less than or equal to the current cell elevation(time)
# we can takew the minium one always but for higher ele , we will have to wait for that much time 
# finally: you have to find the minimum(max time from all possibel path)

# since asking for least in  then Dijkastra should come into mind for a while
# and this instead of putting the elevation in minHeap with coordinates, we will put the max(elevation till now)
#  i.e max(pre poped and current_cell elevation)


# time: n^2*logn (Dijkastra Algo)
# minHeap contains at most n^2 elements, pop time complexity each time is is O(logn^2) = O(2*logn), At most we will pop n^2 times

# # no need to run a nested loop since already connected and we don't have to mark anything also
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
            directions= [[-1,0],[1,0],[0,-1],[0,1]]  #up,down,left,right
            for r2,c2 in directions:
                r, c= r1 +r2, c1+ c2
                if 0<=r<row and 0<=c<col and (r,c) not in visited:
                    visited.add((r,c))
                    max_for_curr_path= max(time, grid[r][c])
                    heapq.heappush(minHeap,(max_for_curr_path,(r,c)))

    