

#Note: DFS you can't apply here 
# and bfs you will have to store all the rotten oranges at once in the queue, next all adjacent rotten oranges at once and so on .
# and also you need to call BFS only once time as all the oranges that can got rotten(connected one) will also become rotten
# as we are pushing all the rotten oranges at once that time.
# simple way: just find the oranges that can got rotten in time=1 , time=2 and so on

# Note: All fresh oranges that is not connected to any of the rotten oranges directly or indirectly thwy won't get rotten.
# So we need to call bfs only for one time, if fresh one is connected directly or indirectly they will got rotten else not.

# also you can think like that : fresh oranges that are at level 1 from any of the rotten oranges will got rotten in one unit of time, 
# and oranges at level 2 will got rotten in two unit of time and so on .

# Use multisource bfs

# time: O(m*n)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,col= len(grid), len(grid[0])
        q= collections.deque()
        time, fresh= 0, 0
        
        # Add all rotten oranges in queue and count the no of fresh orange.
        for r in range(row):
            for c in range(col):
                if grid[r][c]== 2:
                    q.append((r,c))
                if grid[r][c]== 1:
                    fresh+= 1

        while q and fresh:
            time+= 1 
            # oranges that will get rotten in one unit time will depend on the no of adjacent oranges with the ele present in the Queue 
            for i in range(len(q)):  # we are poping and pushing but it this loop will run till the pre length only
                # pop one ele and make all the oranges adjacent to this ele as rotten and append that in Q for next cycle
                r1,c1= q.popleft()
                # writing all possible allowed directions i.e up,down,left,right in form of matrix
                directions= [[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    r,c= r1+dr, c1+dc
                    if 0<=r<row and 0<=c<col and  grid[r][c]==1:
                        grid[r][c]= 2
                        fresh-= 1
                        q.append((r,c))  # now from this cell we have to check next time.

        return time if fresh == 0 else -1  # if no fresh oranges is left


# Note: if you will writw : "while q" only and at last you return 'time -1' then it will give wrong ans
# when there is no rotten oranges or no fresh oranges. 
# so checking fresh also with 'queue'.